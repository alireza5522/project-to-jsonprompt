# MakeJSON CLI

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/alireza5522/project-to-jsonprompt)

A simple and efficient command-line tool to pack your project's structure and file contents into a single JSON file. This is ideal for providing comprehensive, copy-paste-ready context to Large Language Models (LLMs) and other AI tools.

## Features

-   **Consolidated Output**: Combines all relevant project files into one JSON file.
-   **Intelligent Ignoring**: Uses `.fileignore` to completely skip files and folders (like `.gitignore`).
-   **Content Hiding**: Uses `.contextignore` to include a file's path in the output but omit its content, perfect for large or irrelevant files like `package-lock.json` or CSS files.
-   **CLI-Based**: Easy to integrate into scripts and workflows.
-   **Interactive & Automatic**: Provides helpful prompts but also includes a `-y` flag to run without user interaction.
-   **Easy Setup**: An `init` command generates default ignore files to get you started quickly.

## Installation

You can install the tool directly from this GitHub repository using pip:

```bash
pip install git+https://github.com/alireza5522/project-to-jsonprompt.git
```

This will install the package and make the `makejson` command available in your terminal.

## Usage

Using `makejson` is a simple two-step process.

### 1. Initialize Configuration

Navigate to your project's root directory and run the `init` command. This is optional but highly recommended.

```bash
makejson init
```

This command creates two files in your current directory:
-   `.fileignore`: For files/folders to be completely excluded from the output.
-   `.contextignore`: For files whose content should be omitted, but whose path should be included.

### 2. Generate the JSON

Once your ignore files are configured (or if you choose to proceed without them), run the main command:

```bash
makejson
```

The tool will scan your directory, respect the ignore rules, and save the output to `project_context.json` by default.

### Command Options

-   `-o, --output <FILENAME>`: Specify a custom name for the output JSON file.
    ```bash
    makejson --output my_app_context.json
    ```

-   `-y, --yes`: Skip all confirmation prompts and warnings. This is useful for automated scripts.
    ```bash
    makejson -y
    ```

## How the Ignore Files Work

### `.fileignore`
This file works exactly like a `.gitignore` file. Any files or folders matching the patterns listed here will be **completely excluded** from the final JSON.

Default `.fileignore` template:
```
# Completely ignored files and folders
node_modules/
__pycache__/
.env
.ds_store
```

### `.contextignore`
This file is unique to `makejson`. Any files matching the patterns here will be included in the JSON, but their content will be replaced with the message `[Content Omitted / Hidden by .contextignore]`. This is useful when you want the AI to know a file exists, but its content is too large or not relevant.

Default `.contextignore` template:
```
# Metadata only (Content will be omitted)
package-lock.json
*.css
*.json
```

## Example Output

After running `makejson` on a small project, the resulting `project_context.json` file might look like this:

```json
{
  "makejson.py": "import os\nimport json\nimport click\n...",
  "setup.py": "from setuptools import setup\n\nsetup(\n    name='makejson-cli',\n...",
  "project_context.json": "[Content Omitted / Hidden by .contextignore]"
}