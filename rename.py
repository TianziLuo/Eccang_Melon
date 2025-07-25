from pathlib import Path
import shutil

def rename():
    def get_filename():
        downloads = Path.home() / "Downloads"
        prefix = "产品库存"
        matched_files = [
            f for f in downloads.glob("*.zip") if f.name.startswith(prefix)
        ]
        if not matched_files:
            print(f"❌ 没有找到以“{prefix}”开头的 zip 文件")
            return None

        # Find the most recently modified file
        latest = max(matched_files, key=lambda f: f.stat().st_mtime)

        # Remove .zip extension
        name_without_ext = latest.stem

        # Remove the last 3 characters
        trimmed_name = name_without_ext[:-3]

        print(f"✅ 保存的字符串: {trimmed_name}")
        return trimmed_name

    def rename_unzip_file(new_name: str):
        downloads = Path.home() / "Downloads"

        # Match files containing "product_inventory" (any extension)
        matched_files = [
            f for f in downloads.iterdir()
            if f.is_file() and "product_inventory" in f.name
        ]
        if not matched_files:
            print("❌ 未找到包含 'product_inventory' 的文件")
            return

        # Find the most recently modified file
        latest_file = max(matched_files, key=lambda f: f.stat().st_mtime)

        # Construct new filename (preserve original extension)
        new_file = downloads / f"{new_name}{latest_file.suffix}"

        # Perform renaming (overwrite if file exists)
        shutil.move(str(latest_file), str(new_file))
        print(f"✅ 已重命名: {latest_file.name} → {new_file.name}")

    def main():
        filename_str = get_filename()
        if filename_str:
            rename_unzip_file(filename_str)
    
    main()

'''
if __name__ == "__main__":
    rename()
'''
