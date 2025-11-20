# 📚 電子書籍一括統合ツール | Bulk E-book Integrator

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Package Manager](https://img.shields.io/badge/uv-高速-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**自炊ユーザー、漫画愛好家、Web小説コレクター**のために設計されました。散乱した**PDF、画像フォルダ、CBZ、EPUB**を、単一の完全な電子書籍ファイル (EPUB/PDF/MOBI/AZW3) にスマートに統合する、依存関係ゼロのPythonスクリプトです。

---

## ✨ 主な機能

- **📚 デュアルモード**:
  - **コミックモード (Comic Mode)**: 画像/CBZに最適化。無劣化で統合します。
  - **小説モード (Novel Mode)**: テキストのリフローに最適化。Web小説の章やPDFを統合します。
- **🖼️ スマートカバー**: 最初のページを自動的に表紙として抽出します。カスタムパス指定も可能です。
- **🚀 高パフォーマンス**: マルチスレッド処理により、大量の画像やドキュメントを高速に処理します。
- **🔌 Calibre 連携**: `ebook-convert` エンジンを使用して完璧なレンダリングを実現 (Windowsではポータブル版の自動配備に対応)。
- **🛠️ クイック起動**: `uv` に最適化されており、手動での仮想環境構築は不要です。

---

## ⚡ クイックスタート (uvを使用)

このプロジェクトは **[uv](https://github.com/astral-sh/uv)** パッケージマネージャーの使用を推奨しています。pipで手動インストールする必要はありません。

### 1. uv のインストール
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -lsSf https://astral.sh/uv/install.sh | sh
```

### 2. 即時実行
リポジトリをクローンし、`uv run` を実行するだけです。依存関係 (PyMuPDF, Pillow 等) が自動的に同期され、スクリプトが起動します。

```bash
# インタラクティブモード (ウィザード形式)
uv run 批量电子书整合.py
```

---

## 📖 使用例

### 🖥️ インタラクティブモード
引数なしでスクリプトを実行します。画面の指示に従って、フォルダ、言語、出力形式、表紙設定を選択してください。

```bash
uv run 批量电子书整合.py
```

### 🛠️ コマンドラインモード (自動化)

**漫画フォルダを単一のPDFに統合:**
```bash
uv run 批量电子书整合.py -p "C:\Comics\OnePiece" -f pdf -m comic
```

**小説の章を統合し、表紙を指定:**
```bash
uv run 批量电子书整合.py -p "D:\Novels\Overlord" -f epub -m novel --cover "D:\Images\Cover.jpg"
```

**複数のフォルダを一括でKindle形式に変換:**
```bash
uv run 批量电子书整合.py -p "C:\Book1" "C:\Book2" -f azw3 -m novel
```

---

## 📝 トリビア (古の楽園)

内部コードの変数名は、**『崩壊3rd』の古の楽園 (Elysian Realm)** に登場する十三英傑にちなんで名付けられています：

- **`elysiaFitz`**: 欠点のないドキュメント解析 (PyMuPDF)。
- **`edenImage`**: 芸術的な画像処理 (Pillow)。
- **`kevinConcurrent`**: 圧倒的なマルチスレッド並行処理。
- **`griseoEpub`**: EPUB構造の描画。
- その他、英傑たちがバックグラウンドで変換プロセスを支えています。

---

## 📄 ライセンス
[MIT License](LICENSE)
