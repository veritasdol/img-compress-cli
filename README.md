# img-compress-cli

A simple Python CLI tool to compress JPG, JPEG, and PNG images using adjustable quality.

---

## Features

- Compress a single image or all images in a directory
- Automatically saves compressed images to the specified folder
- Daily rotating logs stored in `~/.img-compress/logs/`
- Supports `.jpg`, `.jpeg`, `.png`

---

## Installation

```bash
pip install .
```
> [!IMPORTANT] 
> Make sure you're in the root of the project (img-compress-cli) and have Python 3.8+

---

## Usage

Compress a single image:
```bash
img-compress --file-path ./images/photo.jpg --target-path ./output --quality 80
```
OR

```bash
img-compress -f ./images/photo.jpg -d ./output -q 80
```

Compress all images in a directory:
```bash
img-compress --dir-name ./images --target-path ./output --quality 70
```

OR

```bash
img-compress -d ./images -t ./output -q 70
```

---

## CLI Reference

```bash
img-compress [OPTIONS]
```
| Option          | Short | Required                       | Description                                                                       |
| --------------- | ----- | ------------------------------ | --------------------------------------------------------------------------------- |
| `--file-path`   | `-f`  | ✅ Either this or `--dir-name`  | Path to a single image file to compress.                                          |
| `--dir-name`    | `-d`  | ✅ Either this or `--file-path` | Path to a directory containing images to compress.                                |
| `--target-path` | `-t`  | ❌ Optional                     | Directory where compressed images will be saved. Defaults to the source location. |
| `--quality`     | `-q`  | ❌ Optional                     | Compression quality (1–100). Default is `90`.                                     |
| `--help`        |       | ❌                              | Show help message and exit.                                                       |

---

## Notes

You must provide either --file-path or --dir-name, but not both.

Compressed images are saved with _optimized suffix, e.g., photo_optimized.jpg.

Logs are saved daily to ~/.img-compress/logs/.

---

## Run Tests

```bash
pytest
```

---

## Project Structure

```css
img-compress-cli/
├── src/
│   └── img_compress/
│       ├── main.py
│       ├── utils.py
│       └── __init__.py
├── tests/
│   ├── test_utils.py
│   └── test_compression.py
├── pyproject.toml
├── README.md
```

## License

MIT License — free to use and modify.