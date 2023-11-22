from pdfrw import PdfReader, PdfWriter, PdfDict
from tkinter import filedialog

def main():
    paths = filedialog.askopenfilenames(defaultextension='.pdf', filetypes=[('PDF', '*.pdf')], title='Choose PDF file(s)')
    for path in paths:
        set_metadata(path)
    
def set_metadata(path):
    reader = PdfReader(path)
    metadata = PdfDict(Title=path.split('/')[-1])
    reader.Info.update(metadata)
    PdfWriter().write(path, reader)

if __name__ == '__main__':
    main()