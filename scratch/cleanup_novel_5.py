# -*- coding: utf-8 -*-
import os

def cleanup():
    temp_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_5_temp.json"
    if os.path.exists(temp_path):
        try:
            os.remove(temp_path)
            print(f"Successfully deleted temp file: {temp_path}")
        except Exception as e:
            print(f"Error deleting temp file: {e}")
    else:
        print("Temp file already deleted or does not exist.")

    # List of scratch files to delete
    scratch_files = [
        "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/generate_stage1.py",
        "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/generate_stage2.py",
        "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/generate_stage3.py",
        "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/verify_novel_5.py"
    ]

    for sf in scratch_files:
        if os.path.exists(sf):
            try:
                os.remove(sf)
                print(f"Deleted scratch script: {sf}")
            except Exception as e:
                print(f"Error deleting scratch script {sf}: {e}")

if __name__ == "__main__":
    cleanup()
