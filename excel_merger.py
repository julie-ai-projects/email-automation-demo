import os
import pandas as pd
from config import SOURCE_FOLDER, OUTPUT_FOLDER

def merge_excels():
    print("📊 Merging Excel files...")
    merged = pd.DataFrame()

    for file in os.listdir(SOURCE_FOLDER):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            df = pd.read_excel(os.path.join(SOURCE_FOLDER, file))
            merged = pd.concat([merged, df], ignore_index=True)
            print(f"Added: {file}")

    output_path = os.path.join(OUTPUT_FOLDER, "merged_report.xlsx")
    merged.to_excel(output_path, index=False)
    print(f"✅ Merged file saved to {output_path}")
