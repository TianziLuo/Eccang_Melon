import os
import shutil
from pathlib import Path
from datetime import datetime

def copy_download():
    # Configs
    download_dir = Path(os.path.expanduser('~')) / 'Downloads'
    target_dir = Path(r"C:\Frank\原始数据\易仓下载")

    # List of keywords to search for in file names
    keywords = ["shipment_order","product_csv","库存查询（库位）","产品库存","sku-relation","product-sku-relation"]

    today_files = []
    today_date = datetime.today().date()  # Today's date (without time)

    # Walk through the download directory
    for root, _, files in os.walk(download_dir):
        for file in files:
        # Check if file ends with '.csv' or '.xls' and contains any of the keywords
            if file.endswith((".csv", ".xls")) and any(k in file for k in keywords):
                full_path = Path(root) / file
                mtime = datetime.fromtimestamp(full_path.stat().st_mtime).date()
                if mtime == today_date:
                    today_files.append(full_path)
                    
    # If matching files are found, copy them to target directory
    if today_files:
        for file_path in today_files:
            dest_path = target_dir / file_path.name
            shutil.copy2(file_path, dest_path)
            print(f"✅ Copied: {file_path.name} to {target_dir}")
    else:
        print(f"⚠️ No files found containing keywords {keywords} modified today")
