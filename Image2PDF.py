import os
from PIL import Image
from natsort import natsorted

def create_pdf_from_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Folder not found '{folder_path}'\n"
              f"エラー：フォルダが見つかりません '{folder_path}'\n"
              f"错误：未找到文件夹 '{folder_path}'")
        return

    abs_folder_path = os.path.abspath(folder_path)
    
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
    files = [f for f in os.listdir(abs_folder_path) if f.lower().endswith(valid_extensions)]

    if not files:
        print("Error: No image files found.\n"
              "エラー：画像ファイルが見つかりません。\n"
              "错误：未找到图片文件。")
        return

    sorted_files = natsorted(files)
    print("-" * 50)
    print(f"Found {len(sorted_files)} images, processing...\n"
          f"{len(sorted_files)} 枚の画像が見つかりました、処理中...\n"
          f"找到 {len(sorted_files)} 张图片，正在处理...")
    print("-" * 50)

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
                
        except Exception as e:
            print(f"Skipping file: {file_name} ({e})\n"
                  f"ファイルをスキップします: {file_name}\n"
                  f"跳过文件: {file_name}")

    if not image_list:
        print("No valid images to merge.\n"
              "結合できる有効な画像がありません。\n"
              "没有有效的图片可以合并。")
        return

    folder_name = os.path.basename(abs_folder_path)
    parent_dir = os.path.dirname(abs_folder_path)
    output_pdf_path = os.path.join(parent_dir, f"{folder_name}.pdf")

    print(f"Saving PDF to: {output_pdf_path}\n"
          f"PDFを保存しています: {output_pdf_path}\n"
          f"正在保存 PDF 至: {output_pdf_path}")
    
    first_image = image_list[0]
    rest_images = image_list[1:]
    
    first_image.save(
        output_pdf_path, 
        "PDF", 
        resolution=100.0, 
        save_all=True, 
        append_images=rest_images
    )
    print(" ")
    print(f"Success! Saved to: {output_pdf_path}\n"
          f"成功！保存先: {output_pdf_path}\n"
          f"成功！已保存至: {output_pdf_path}")
    print(" ")
if __name__ == "__main__":
    print(" ")
    print("Enter image folder path")
    print("画像フォルダのパスを入力してください")
    print("请输入图片文件夹路径")
    print(" ")

    input_path = input(">>> ").strip()
    input_path = input_path.replace('"', '').replace("'", "")
    
    print() 
    create_pdf_from_folder(input_path)