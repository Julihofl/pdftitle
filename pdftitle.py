from pdfrw import PdfReader, PdfWriter, PdfDict
from tkinter import filedialog
import os

def main():
    paths = filedialog.askopenfilenames(defaultextension='.pdf', filetypes=[('PDF', '*.pdf')], title='Choose PDF file(s)')
    if not paths:
        print("No files selected.")
        return
    
    for path in paths:
        set_metadata(path)
    
def set_metadata(path):
    reader = PdfReader(path)
    metadata = PdfDict(Title=os.path.basename(path))
    reader.Info.update(metadata)
    backup_path = path + '.bak'
    try:
        PdfWriter().write(backup_path, reader)
        PdfWriter().write(path, reader)
        print(f"Metadata updated for: {path}")
    except Exception as e:
        print(f"Failed to update metadata for {path}: {e}")

if __name__ == '__main__':
    main()
