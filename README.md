
# 📚 Bulk E-book Merger & Converter | 批量电子书整合工具

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Package Manager](https://img.shields.io/badge/uv-lightning--fast-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A blazing fast, single-file script to **merge dispersed folders of files into a single E-book**.  
专为松鼠党设计：零依赖痛点，将散乱的 **PDF, Images, CBZ, EPUB** 智能合并为一本完整的电子书 (EPUB/PDF/MOBI/AZW3)。

---

## ✨ Features (核心功能)

- **📚 Dual Modes**: 
  - **Comic Mode**: Specialized for merging Image folders/CBZs into PDF/EPUB.
  - **Novel Mode**: Intelligent text reflow for merging web novels or chapter files.
- **🖼️ Auto-Cover**: Automatically extracts the first page as the cover, or supports custom cover paths.
- **🚀 High Performance**: Powered by multi-threading for high-speed image/pdf processing.
- **🔌 Calibre Integration**: Uses `ebook-convert` for perfect format rendering (auto-setups on Windows).
- **🛠️ Zero Friction**: Designed to be run directly with `uv` - no manual virtualenv needed.

---

## ⚡ Quick Start with `uv` (推荐)

This project is optimized for **[uv](https://github.com/astral-sh/uv)**. You don't need to manually install pip packages.

### 1. Install uv
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -lsSf https://astral.sh/uv/install.sh | sh
```

### 2. Run Immediately (直接运行)
Clone the repo and run. `uv` will automatically sync all dependencies (PyMuPDF, Pillow, etc.) in an isolated environment instantly.

```bash
# Run in interactive mode (Interactive Wizard)
uv run 批量电子书整合.py
```

---

## 📖 Usage Examples (使用示例)

### 🖥️ Interactive Mode (小白/交互模式)
Simply run the script without arguments. Follow the on-screen guide to select your folder, language (En/Zh/Ja), and target format.

```bash
uv run 批量电子书整合.py
```

### 🛠️ Command Line Mode (高级/命令行模式)

**Merge a Manga folder into a single PDF:**
```bash
uv run 批量电子书整合.py -p "C:\Comics\OnePiece" -f pdf -m comic
```

**Merge Novel chapters with a Custom Cover:**
```bash
uv run 批量电子书整合.py -p "D:\Novels\Overlord" -f epub -m novel --cover "D:\Novels\Cover.jpg"
```

**Batch Process Multiple Folders to Kindle Format:**
```bash
uv run 批量电子书整合.py -p "C:\Book1" "C:\Book2" -f azw3 -m novel
```

---

## 📝 Trivia: The "Elysian" Logic

The internal codebase follows a unique variable naming convention inspired by **Honkai Impact 3rd (Elysian Realm)** to handle specific tasks:

- **`elysiaFitz`**: PDF/Document parsing (PyMuPDF).
- **`edenImage`**: Image processing & art (Pillow).
- **`kevinConcurrent`**: Powerful multi-threaded execution.
- **`griseoEpub`**: Constructing the EPUB structure.
- ...and other Flame-Chasers ensuring a flawless conversion.

---

## 📄 License
[MIT License](LICENSE)