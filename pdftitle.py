import os
import glob

from pdfrw import PdfReader, PdfWriter, PdfDict
from tkinter import filedialog
from typing import List

def process_files(file_paths: List[str]) -> None:
    for file_path in file_paths:
        if not file_path.lower().endswith('.pdf'):
            continue

        try:
            reader = PdfReader(file_path)
            title: str = ""
            if reader.Info:
                reader.Info.Title = title
            else:
                reader.Info = PdfDict(Title=title)

            PdfWriter().write(file_path, reader)
            print(f"Metadata updated for: {file_path}")

        except PermissionError:
            print(f"Failed to update metadata for {file_path}: Permission denied.")
        except Exception as e:
            print(f"Failed to update metadata for {file_path}: {e}")

def get_all_files(folder_path: str, extension: str = '.pdf') -> List[str]:
    return glob.glob(os.path.join(folder_path, '**', f'*{extension}'), recursive=True)

def main():
    while True:
        choice: str = input("Choose mode:\n1. Process folder\n2. Process individual files\n3. Exit\nEnter choice: ")

        if choice == '1':
            folder_path: str = filedialog.askdirectory(title='Choose folder containing PDF files')
            if folder_path:
                file_paths: List[str] = get_all_files(folder_path)
                process_files(file_paths)
        elif choice == '2':
            file_paths: List[str] = filedialog.askopenfilenames(title='Choose PDF file(s)', defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
            process_files(file_paths)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
