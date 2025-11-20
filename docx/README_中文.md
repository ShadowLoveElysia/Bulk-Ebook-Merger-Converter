# 📚 批量电子书整合工具 | Bulk E-book Integrator

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Package Manager](https://img.shields.io/badge/uv-极速-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

专为**松鼠党、漫画迷和网文读者**设计。这是一个单文件、零依赖痛点的 Python 脚本，能将散乱的 **PDF、图片文件夹、CBZ、EPUB 分卷** 智能合并为一本完整的电子书 (EPUB/PDF/MOBI/AZW3)。

---

## ✨ 核心功能

- **📚 双重模式**:
  - **漫画模式 (Comic Mode)**: 针对图片/CBZ优化，无损合并，适合漫画党。
  - **小说模式 (Novel Mode)**: 针对文字重排优化，智能合并网文章节或散乱 PDF。
- **🖼️ 智能封面**: 自动提取第一页作为封面，也支持命令行指定自定义封面路径。
- **🚀 高性能**: 内置多线程处理，飞速处理大量图片和文档。
- **🔌 Calibre 集成**: 调用 `ebook-convert` 引擎确保完美渲染 (Windows 下支持自动部署便携版)。
- **🛠️ 极速启动**: 专为 `uv` 优化，无需手动配置虚拟环境，即开即用。

---

## ⚡ 极速开始 (使用 uv)

本项目推荐使用 **[uv](https://github.com/astral-sh/uv)** 包管理器。你无需手动安装 pip 依赖。

### 1. 安装 uv
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -lsSf https://astral.sh/uv/install.sh | sh
```

### 2. 直接运行
克隆仓库后，直接使用 `uv run`。它会自动在隔离环境中同步所有依赖 (PyMuPDF, Pillow 等) 并启动脚本。

```bash
# 启动交互式向导 (小白推荐)
uv run 批量电子书整合.py
```

---

## 📖 使用示例

### 🖥️ 交互模式
不带参数运行脚本。按照屏幕提示选择文件夹、语言、目标格式和封面设置。

```bash
uv run 批量电子书整合.py
```

### 🛠️ 命令行模式 (批处理)

**将漫画文件夹合并为单一 PDF:**
```bash
uv run 批量电子书整合.py -p "C:\Comics\OnePiece" -f pdf -m comic
```

**合并小说章节并指定封面:**
```bash
uv run 批量电子书整合.py -p "D:\Novels\三体" -f epub -m novel --cover "D:\Images\Cover.jpg"
```

**批量处理多个书籍文件夹到 Kindle 格式:**
```bash
uv run 批量电子书整合.py -p "C:\Book1" "C:\Book2" -f azw3 -m novel
```

---

## 📝 关于代码 (往世乐土)

代码内部变量命名致敬 **《崩坏3》往世乐土 (Elysian Realm)** 的十三英桀，每位英桀负责特定的逻辑职能：

- **`elysiaFitz`**: 负责完美无瑕的文档解析 (PyMuPDF)。
- **`edenImage`**: 负责艺术般的图像处理 (Pillow)。
- **`kevinConcurrent`**: 负责“天火”级别的多线程并发。
- **`griseoEpub`**: 负责绘制 EPUB 结构。
- 以及其他英桀在后台确保转换过程的万无一失。

---

## 📄 许可证
[MIT License](LICENSE)