import os
import json
import click
import pathspec

def load_ignore_spec(folder, ignore_filename):
    """Reads ignore files and converts them into matchable path specifications."""
    ignore_file = os.path.join(folder, ignore_filename)
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        return pathspec.PathSpec.from_lines('gitwildmatch', lines)
    return None

def should_skip_completely(rel_path, file_spec, output_filename):
    """Determines whether a file or directory should be completely omitted."""
    if file_spec and file_spec.match_file(rel_path):
        return True
    if rel_path.startswith('.git/') or rel_path == '.git':
        return True
    if rel_path in ['.fileignore', '.contextignore', output_filename]:
        return True
    return False

def should_hide_content(rel_path, context_spec):
    """Determines whether only the filename should be included, omitting its content."""
    if context_spec and context_spec.match_file(rel_path):
        return True
    return False

def create_ignore_templates(cwd):
    """Creates default templates for .fileignore and .contextignore."""
    file_ignore_path = os.path.join(cwd, '.fileignore')
    context_ignore_path = os.path.join(cwd, '.contextignore')
    
    if not os.path.exists(file_ignore_path):
        with open(file_ignore_path, 'w', encoding='utf-8') as f:
            f.write("# Completely ignored files and folders\nnode_modules/\n__pycache__/\n.env\n.ds_store\n")
    if not os.path.exists(context_ignore_path):
        with open(context_ignore_path, 'w', encoding='utf-8') as f:
            f.write("# Metadata only (Content will be omitted)\npackage-lock.json\n*.css\n*.json\n")
    click.echo(click.style("✔ .fileignore and .contextignore templates created successfully.", fg="green"))

# دستور اصلی: پرچم‌ها مستقیماً روی خود makejson سوار شده‌اند
@click.group(invoke_without_command=True)
@click.option('-o', '--output', default='project_context.json', help='Name of the output JSON file.')
@click.option('-y', '--yes', is_flag=True, help='Skip all confirmations and warnings. Proceed automatically.')
@click.pass_context
def cli(ctx, output, yes):
    """CLI tool to pack your project structure and contents into a single JSON for AI Context."""
    # اگر کاربر دستور init را نزده بود، مستقیم کار ساخت فایل جیسان را انجام بده
    if ctx.invoked_subcommand is None:
        if not output.endswith('.json'):
            output += '.json'
        generate_json(output, yes)

@cli.command()
def init():
    """Create default .fileignore and .contextignore files in the current directory."""
    create_ignore_templates(os.getcwd())

def generate_json(output_filename, auto_confirm):
    base_dir = os.getcwd()
    
    # بررسی وجود فایل‌های اگنور
    file_ignore_exists = os.path.exists(os.path.join(base_dir, '.fileignore'))
    context_ignore_exists = os.path.exists(os.path.join(base_dir, '.contextignore'))
    
    # منطق هشدار فایل‌های اگنور: اگر -y زده شده باشد، این بخش کاملاً نادیده گرفته می‌شود
    if not (file_ignore_exists and context_ignore_exists) and not auto_confirm:
        click.echo(click.style("⚠ Warning: .fileignore or .contextignore is missing!", fg="yellow", bold=True))
        choice = click.prompt(
            "Do you want to continue without them? \n[y] Yes, proceed | [n] No, exit | [c] Create templates and exit", 
            type=click.Choice(['y', 'n', 'c'], case_sensitive=False)
        ).lower()
        
        if choice == 'n':
            click.echo(click.style("Operation cancelled.", fg="red"))
            return
        elif choice == 'c':
            create_ignore_templates(base_dir)
            return
            
    # اگر نام فایل تغییر نکرده بود و -y هم نبود، تاییدیه نهایی گرفته می‌شود
    if output_filename == 'project_context.json' and not auto_confirm:
        if not click.confirm("No filename provided. Save to default 'project_context.json'?", default=True):
            click.echo(click.style("Operation cancelled.", fg="red"))
            return

    file_spec = load_ignore_spec(base_dir, '.fileignore')
    context_spec = load_ignore_spec(base_dir, '.contextignore')
    
    project_structure = {}
    click.echo(click.style(f"Scanning directory and generating {output_filename}...", fg="cyan"))

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not should_skip_completely(os.path.relpath(os.path.join(root, d), base_dir), file_spec, output_filename)]

        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            normalized_rel_path = rel_path.replace(os.sep, '/')

            if should_skip_completely(normalized_rel_path, file_spec, output_filename):
                continue
            
            if should_hide_content(normalized_rel_path, context_spec):
                project_structure[normalized_rel_path] = "[Content Omitted / Hidden by .contextignore]"
            else:
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                        project_structure[normalized_rel_path] = f.read()
                except Exception as e:
                    project_structure[normalized_rel_path] = f"[Error reading file: {str(e)}]"

    output_file = os.path.join(base_dir, output_filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(project_structure, f, ensure_ascii=False, indent=2)
        
    click.echo(click.style(f"🎉 Success! Context saved to: {output_file}", fg="green", bold=True))

if __name__ == '__main__':
    cli()