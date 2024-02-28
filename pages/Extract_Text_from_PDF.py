import os
import pdfplumber
from pathlib import Path
from Home import *


class Pdf_to_txt:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def list_pdfs(self):
        pdf_files = list(Path(self.folder_path).rglob("*.pdf"))
        self.pdf_files = pdf_files
        return pdf_files

    def extract_txt(self, pdf_files):
        # Create an empty list or a dictionary to store the text from each PDF file
        texts = []
        # texts = {}
        for path in pdf_files:
            text = []
            st.write(f"Extracting text from: {path}")
            with pdfplumber.open(path) as pdf:
                pages = pdf.pages
                for page in pages:
                    text.append(page.extract_text())
                    # get the file name from the path
                    file_name = os.path.basename(path)
                    # split the file name and the extension
                    file_name, _ = os.path.splitext(file_name)
                    # append the text to the list or the dictionary
            texts.append(text)
                    # texts[file_name] = text
        return texts

    def save(self, pdf_files, texts, out_dir="./cache"):
        # Loop through the pdf_files and the texts
        for path, text in zip(pdf_files, texts):
            # get the file name from the path
            file_name = os.path.basename(path)
            # split the file name and the extension
            file_name, _ = os.path.splitext(file_name)
            # join the output directory, the file name, and the txt extension
            output_path = os.path.join(out_dir, file_name + ".txt")
            with open(output_path, "w", encoding='utf-8') as output:
                for row in text:
                    output.write(str(row) + '\n')
    
# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Pick Pdfs Folder')
st.write('Please select a folder:')

dirname = ""
clicked = st.button('Browse')
if clicked:
    dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
    pdfs_folder = Path(dirname)

extract_bt = st.button("Extract text from pdfs")
if extract_bt:
    # Create an instance of Pdf_to_txt with the folder path
    pdf_converter = Pdf_to_txt(dirname)
	# Call the list_pdfs method on the instance
    pdf_files = pdf_converter.list_pdfs()
	# Call the extract_txt method on the instanc
    texts = pdf_converter.extract_txt(pdf_files)
    # Call the save method on the instance
    pdf_converter.save(pdf_files, texts)
