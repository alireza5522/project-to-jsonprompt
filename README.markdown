# Folder to JSON Converter / تبدیل پوشه به JSON

**English**: This Python script (`folder_to_json.py`) recursively scans a directory, collects the contents of text-based files (e.g., `.py`, `.js`, `.jsx`), and generates a nested JSON file representing the folder structure and file contents. It uses `.gitignore`-style patterns to exclude specified files and directories, ensuring only relevant files are processed.

**فارسی**: این اسکریپت پایتون (`folder_to_json.py`) به صورت بازگشتی یک پوشه را اسکن می‌کند، محتوای فایل‌های متنی (مانند `.py`، `.js`، `.jsx`) را جمع‌آوری می‌کند و یک فایل JSON با ساختار تودرتو تولید می‌کند که نشان‌دهنده ساختار پوشه و محتوای فایل‌هاست. این اسکریپت از الگوهای مشابه `.gitignore` برای حذف فایل‌ها و پوشه‌های مشخص استفاده می‌کند تا فقط فایل‌های مرتبط پردازش شوند.

---

## Features / ویژگی‌ها

**English**:
- Recursively traverses a directory to process text-based files.
- Supports custom file extensions (default: `.py`, `.js`, `.jsx`).
- Ignores files and directories based on `.gitignore`-like patterns using the `pathspec` library.
- Creates a nested JSON structure where keys are relative file paths and values are file contents.
- Outputs the result to `project_prompt.json`.
- Handles file encoding errors gracefully with console warnings.
- Uses UTF-8 encoding for file reading and JSON output.

**فارسی**:
- اسکن بازگشتی پوشه برای پردازش فایل‌های متنی.
- پشتیبانی از پسوندهای فایل سفارشی (به طور پیش‌فرض: `.py`، `.js`، `.jsx`).
- نادیده گرفتن فایل‌ها و پوشه‌ها بر اساس الگوهای مشابه `.gitignore` با استفاده از کتابخانه `pathspec`.
- تولید ساختار JSON تودرتو که کلیدها مسیرهای نسبی فایل‌ها و مقادیر محتوای فایل‌ها هستند.
- ذخیره خروجی در فایل `project_prompt.json`.
- مدیریت خطاهای رمزگذاری فایل با نمایش هشدار در کنسول.
- استفاده از رمزگذاری UTF-8 برای خواندن فایل‌ها و تولید JSON.

---

## Prerequisites / پیش‌نیازها

**English**:
- **Python**: Version 3.6 or higher.
- **Required Package**: `pathspec` (install via `pip`).

Install the required package:
```bash
pip install pathspec
```

**فارسی**:
- **پایتون**: نسخه 3.6 یا بالاتر.
- **بسته مورد نیاز**: کتابخانه `pathspec` (نصب از طریق pip).

برای نصب بسته مورد نیاز:
```bash
pip install pathspec
```

---

## Installation / نصب

**English**:
1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the `pathspec` package:
   ```bash
   pip install pathspec
   ```
3. Place `folder_to_json.py` in the root of the directory you want to process, or specify a custom directory (see [Customization](#customization)).

**فارسی**:
1. این مخزن را کلون کنید یا دانلود کنید:
   ```bash
   git clone <آدرس-مخزن>
   cd <پوشه-مخزن>
   ```
2. بسته `pathspec` را نصب کنید:
   ```bash
   pip install pathspec
   ```
3. فایل `folder_to_json.py` را در پوشه ریشه‌ای که می‌خواهید پردازش کنید قرار دهید یا یک پوشه سفارشی مشخص کنید (به بخش [سفارشی‌سازی](#سفارشی‌سازی) مراجعه کنید).

---

## Usage / نحوه استفاده

**English**:
1. **Prepare Your Directory**: Ensure the directory contains text files with extensions listed in `TEXT_EXTENSIONS` (e.g., `.py`, `.js`, `.jsx`).
2. **Run the Script**:
   - To process the current directory:
     ```bash
     python folder_to_json.py
     ```
   - The script generates `project_prompt.json` in the working directory.
3. **Output Format**: The JSON file contains a nested structure where keys are relative file paths and values are file contents. Example:
   ```json
   {
     "src/main.py": "print('Hello, World!')\n",
     "src/utils/helper.js": "function helper() {\n  return true;\n}\n"
   }
   ```
4. **Error Handling**: Files that cannot be read (e.g., due to permissions or encoding issues) are skipped, with warnings printed to the console.

**فارسی**:
1. **آماده‌سازی پوشه**: مطمئن شوید که پوشه حاوی فایل‌های متنی با پسوندهای مشخص شده در `TEXT_EXTENSIONS` (مانند `.py`، `.js`، `.jsx`) است.
2. **اجرای اسکریپت**:
   - برای پردازش پوشه کنونی:
     ```bash
     python folder_to_json.py
     ```
   - اسکریپت فایل `project_prompt.json` را در پوشه کاری تولید می‌کند.
3. **فرمت خروجی**: فایل JSON شامل ساختاری تودرتو است که کلیدها مسیرهای نسبی فایل‌ها و مقادیر محتوای فایل‌ها هستند. مثال:
   ```json
   {
     "src/main.py": "print('Hello, World!')\n",
     "src/utils/helper.js": "function helper() {\n  return true;\n}\n"
   }
   ```
4. **مدیریت خطاها**: فایل‌هایی که قابل خواندن نیستند (مثلاً به دلیل مشکلات دسترسی یا رمزگذاری) نادیده گرفته می‌شوند و هشدارها در کنسول نمایش داده می‌شوند.

---

## Script Details / جزئیات اسکریپت

**English**:
- **Ignore Patterns** (`IGNORE_TEXT`): Defines patterns to exclude files/directories (e.g., `__pycache__/`, `*.pyc`, `node_modules/`). Uses `pathspec` with `gitwildmatch` syntax.
- **Text File Detection** (`is_probably_text_file`): Identifies text files by checking extensions in `TEXT_EXTENSIONS`. A commented-out binary check can be enabled for stricter filtering.
- **Nested JSON Structure** (`insert_nested`): Constructs a nested dictionary by splitting file paths and inserting file contents.
- **Directory Traversal** (`folder_to_json`): Uses `os.walk` to scan directories recursively, filters files, and builds the JSON structure.

**فارسی**:
- **الگوهای نادیده گرفتن** (`IGNORE_TEXT`): الگوهایی برای حذف فایل‌ها و پوشه‌ها (مانند `__pycache__/`، `*.pyc`، `node_modules/`) تعریف می‌کند. از `pathspec` با سینتکس `gitwildmatch` استفاده می‌کند.
- **تشخیص فایل متنی** (`is_probably_text_file`): فایل‌های متنی را با بررسی پسوندها در `TEXT_EXTENSIONS` شناسایی می‌کند. یک بررسی باینری غیرفعال وجود دارد که می‌تواند برای فیلتر دقیق‌تر فعال شود.
- **ساختار JSON تودرتو** (`insert_nested`): با تقسیم مسیرهای فایل، یک دیکشنری تودرتو می‌سازد و محتوای فایل‌ها را در آن قرار می‌دهد.
- **پیمایش پوشه** (`folder_to_json`): از `os.walk` برای اسکن بازگشتی پوشه‌ها استفاده می‌کند، فایل‌ها را فیلتر کرده و ساختار JSON را می‌سازد.

---

## Customization / سفارشی‌سازی

**English**:
- **Change Directory**: Update `folder_to_json(".")` to process a specific directory:
  ```python
  data = folder_to_json("/path/to/your/directory")
  ```
- **Add File Extensions**: Modify `TEXT_EXTENSIONS`:
  ```python
  TEXT_EXTENSIONS = {".py", ".js", ".jsx", ".txt", ".md"}
  ```
- **Update Ignore Patterns**: Edit `IGNORE_TEXT`:
  ```python
  IGNORE_TEXT = """
  __pycache__/
  *.pyc
  node_modules/
  my_custom_folder/
  """
  ```
- **Change Output File**: Modify the output file name:
  ```python
  with open("custom_output.json", "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
  ```

**فارسی**:
- **تغییر پوشه**: فراخوانی `folder_to_json(".")` را برای پردازش یک پوشه خاص تغییر دهید:
  ```python
  data = folder_to_json("/path/to/your/directory")
  ```
- **افزودن پسوندهای فایل**: مجموعه `TEXT_EXTENSIONS` را ویرایش کنید:
  ```python
  TEXT_EXTENSIONS = {".py", ".js", ".jsx", ".txt", ".md"}
  ```
- **به‌روزرسانی الگوهای نادیده گرفتن**: `IGNORE_TEXT` را تغییر دهید:
  ```python
  IGNORE_TEXT = """
  __pycache__/
  *.pyc
  node_modules/
  my_custom_folder/
  """
  ```
- **تغییر نام فایل خروجی**: نام فایل خروجی را تغییر دهید:
  ```python
  with open("custom_output.json", "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
  ```

---

## Example / مثال

**English**:
Given a directory structure:
```
project/
├── src/
│   ├── main.py
│   └── utils/
│       └── helper.js
├── .gitignore
└── node_modules/
```

With `main.py`:
```python
print("Hello, World!")
```

And `helper.js`:
```javascript
function helper() {
  return true;
}
```

Running `python folder_to_json.py` generates `project_prompt.json`:
```json
{
  "src/main.py": "print(\"Hello, World!\")\n",
  "src/utils/helper.js": "function helper() {\n  return true;\n}\n"
}
```

**فارسی**:
با فرض ساختار پوشه:
```
project/
├── src/
│   ├── main.py
│   └── utils/
│       └── helper.js
├── .gitignore
└── node_modules/
```

محتوای `main.py`:
```python
print("Hello, World!")
```

و `helper.js`:
```javascript
function helper() {
  return true;
}
```

اجرای `python folder_to_json.py` فایل `project_prompt.json` را تولید می‌کند:
```json
{
  "src/main.py": "print(\"Hello, World!\")\n",
  "src/utils/helper.js": "function helper() {\n  return true;\n}\n"
}
```

---

## Limitations / محدودیت‌ها

**English**:
- Assumes UTF-8 encoding; non-UTF-8 files may cause errors (logged and skipped).
- Binary file detection relies on extensions only (enable the commented-out check for stricter filtering).
- Large directories may produce large JSON files, impacting performance.

**فارسی**:
- فرض می‌کند فایل‌ها با رمزگذاری UTF-8 هستند؛ فایل‌های غیر UTF-8 ممکن است خطا ایجاد کنند (خطاها ثبت و نادیده گرفته می‌شوند).
- تشخیص فایل‌های باینری فقط بر اساس پسوند است (بررسی غیرفعال شده را می‌توان برای فیلتر دقیق‌تر فعال کرد).
- پوشه‌های بزرگ ممکن است فایل‌های JSON بزرگی تولید کنند که روی عملکرد تأثیر می‌گذارد.

---

## Troubleshooting / عیب‌یابی

**English**:
- **"ModuleNotFoundError: No module named 'pathspec'"**: Install the `pathspec` package:
  ```bash
  pip install pathspec
  ```
- **"PermissionError" or "UnicodeDecodeError"**: Check console warnings for problematic files. Ensure files are accessible and UTF-8 encoded.
- **No Output File**: Verify the directory contains text files with supported extensions and check write permissions.

**فارسی**:
- **خطای "ModuleNotFoundError: No module named 'pathspec'"**: بسته `pathspec` را نصب کنید:
  ```bash
  pip install pathspec
  ```
- **خطای "PermissionError" یا "UnicodeDecodeError"**: هشدارهای کنسول را بررسی کنید. مطمئن شوید فایل‌ها قابل دسترسی و با رمزگذاری UTF-8 هستند.
- **عدم تولید فایل خروجی**: بررسی کنید که پوشه شامل فایل‌های متنی با پسوندهای پشتیبانی‌شده باشد و مجوز نوشتن وجود داشته باشد.

---

## License / مجوز

**English**: This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**فارسی**: این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.