# /// script
# dependencies = [
#   "pillow",
#   "natsort",
#   "requests",
# ]
# ///

import os
import sys
from PIL import Image
from natsort import natsorted

def create_pdf_from_folder(folder_path, output_root=None):
    if not os.path.exists(folder_path):
        return

    abs_folder_path = os.path.abspath(folder_path)
    folder_name = os.path.basename(abs_folder_path)
    
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
    files = [f for f in os.listdir(abs_folder_path) if f.lower().endswith(valid_extensions)]

    if not files:
        return

    sorted_files = natsorted(files)
    print(f"Processing / 处理中 / 処理中: {folder_name} ({len(sorted_files)} images)...")

    image_list = []
    
    for file_name in sorted_files:
        file_path = os.path.join(abs_folder_path, file_name)
        try:
            img = Image.open(file_path)
            
            if img.mode == 'RGBA':
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
                
            image_list.append(img)
        except Exception:
            pass

    if not image_list:
        return

    if output_root:
        if not os.path.exists(output_root):
            os.makedirs(output_root, exist_ok=True)
        output_pdf_path = os.path.join(output_root, f"{folder_name}.pdf")
    else:
        parent_dir = os.path.dirname(abs_folder_path)
        output_pdf_path = os.path.join(parent_dir, f"{folder_name}.pdf")

    try:
        first_image = image_list[0]
        rest_images = image_list[1:]
        
        first_image.save(
            output_pdf_path, 
            "PDF", 
            resolution=100.0, 
            save_all=True, 
            append_images=rest_images
        )
        print(f"  -> Saved / 已保存 / 保存しました: {os.path.basename(output_pdf_path)}")
    except Exception as e:
        print(f"  -> Error saving PDF / 保存错误 / 保存エラー: {e}")

def batch_process_root(root_path):
    if not os.path.exists(root_path):
        print("Root path does not exist. / 路径不存在。 / パスが存在しません。")
        return

    abs_root = os.path.abspath(root_path)
    
    pdf_output_dir = os.path.join(abs_root, "_PDF_Output")
    
    print("-" * 50)
    print(f"Batch Mode / 批量模式 / バッチモード: {os.path.basename(abs_root)}")
    print(f"Output Dir / 输出目录 / 出力先: {pdf_output_dir}")
    print("-" * 50)

    items = os.listdir(abs_root)
    subfolders = []
    for item in items:
        full_path = os.path.join(abs_root, item)
        if os.path.isdir(full_path) and item != "_PDF_Output":
            subfolders.append(full_path)
    
    subfolders = natsorted(subfolders)
    
    if not subfolders:
        print("No subfolders found. Trying single folder mode... / 未发现子文件夹，尝试单文件夹模式... / サブフォルダが見つかりません。単一フォルダモードを試行します...")
        create_pdf_from_folder(abs_root)
        return

    for folder in subfolders:
        create_pdf_from_folder(folder, output_root=pdf_output_dir)
    
    print("-" * 50)
    print("Batch processing complete. / 批量处理完成。 / バッチ処理が完了しました。")
    print("-" * 50)

if __name__ == "__main__":
    print("\nUniversal Image to PDF Converter (Batch Edition)")
    print("通用图片转PDF工具 (批量版)")
    print("ユニバーサル画像PDF変換ツール (バッチ版)")
    print("----------------------------------------------")
    print("Tip: You can pass a parent folder containing multiple chapter subfolders.")
    print("提示: 您可以传入包含多个章节子文件夹的父文件夹。")
    print("ヒント: 複数のチャプターサブフォルダを含む親フォルダを渡すことができます。")
    print("     A '_PDF_Output' folder will be created inside.")
    print("     将在其中创建一个 '_PDF_Output' 文件夹。")
    print("     中に '_PDF_Output' フォルダが作成されます。")
    print("----------------------------------------------\n")

    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        print("Enter folder path / 请输入文件夹路径 / フォルダパスを入力してください:")
        input_path = input(">>> ").strip().replace('"', '').replace("'", "")
    
    if input_path:
        batch_process_root(input_path)

    print("\n" + "-" * 50)
    print("Do you want to merge the generated PDFs into EPUB/AZW3/MOBI? (y/n)")
    print("是否需要合并成EPUB/AZW3/MOBI？(y/n)")
    print("生成されたPDFをEPUB/AZW3/MOBIにマージしますか？ (y/n)")
    
    merge_choice = input(">>> ").strip().lower()
    
    if merge_choice in ('y', 'yes'):
        target_script_name = "批量电子书整合.py"
        script_url = "https://raw.githubusercontent.com/ShadowLoveElysia/Bulk-Ebook-Merger-Converter/main/%E6%89%B9%E9%87%8F%E7%94%B5%E5%AD%90%E4%B9%A6%E6%95%B4%E5%90%88.py"
        
        if not os.path.exists(target_script_name):
            print(f"\nDownloading {target_script_name}...")
            print(f"正在下载 {target_script_name}...")
            print(f"{target_script_name} をダウンロードしています...")
            try:
                import requests
                response = requests.get(script_url)
                response.raise_for_status()
                with open(target_script_name, 'wb') as f:
                    f.write(response.content)
                print("Download complete. / 下载完成。 / ダウンロード完了。")
            except ImportError:
                print("Error: 'requests' library is not installed. Cannot download automatically.")
                print("错误: 未安装 'requests' 库。无法自动下载。")
                print("エラー: 'requests' ライブラリがインストールされていません。自動ダウンロードできません。")
            except Exception as e:
                print(f"Download failed / 下载失败 / 下载失败: {e}")
        
        if os.path.exists(target_script_name):
            print(f"\nRunning {target_script_name} using uv...")
            print(f"正在使用 uv 运行 {target_script_name}...")
            print(f"uv を使用して {target_script_name} を実行しています...")
            
            import subprocess
            try:
                subprocess.run(["uv", "run", target_script_name], shell=True)
            except Exception as e:
                print(f"Failed to run script / 运行脚本失败 / スクリプトの実行に失敗しました: {e}")
        else:
            print(f"Script {target_script_name} not found. Skipping merge.")
            print(f"未找到脚本 {target_script_name}。跳过合并。")
            print(f"スクリプト {target_script_name} が見つかりません。マージをスキップします。")