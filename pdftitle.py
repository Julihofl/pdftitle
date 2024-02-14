from pdfrw import PdfReader, PdfWriter, PdfDict
from tkinter import filedialog
import os

def main():
    folder_path = filedialog.askdirectory(title='Choose folder containing PDF files')
    if folder_path:
        process_folder(folder_path)

    file_paths = filedialog.askopenfilenames(title='Choose PDF file(s)', defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
    for file_path in file_paths:
        process_file(file_path)

def process_folder(folder_path):
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"No PDF files found in the selected folder: {folder_path}")
        return
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        process_file(pdf_path)
    exit()

def process_file(file_path):
    if not file_path.lower().endswith('.pdf'):
        print(f"Skipping non-PDF file: {file_path}")
        return
    reader = PdfReader(file_path)
    title = os.path.splitext(os.path.basename(file_path))[0]
    reader.Info.Title = title
    try:
        PdfWriter().write(file_path, reader)
        print(f"Metadata updated for: {file_path}")
    except PermissionError as e:
        print(f"Failed to update metadata for {file_path}: Permission denied.")
    except Exception as e:
        print(f"Failed to update metadata for {file_path}: {e}")

if __name__ == '__main__':
    main()
