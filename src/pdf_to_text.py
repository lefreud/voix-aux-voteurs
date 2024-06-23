import argparse
from pypdf import PdfReader
import os

def main():
    parser = argparse.ArgumentParser(description='Convert folder of PDFs to a folder of text files.')
    parser.add_argument('--input_folder', type=str, help='Folder containing PDFs to convert.', default='data/projets_lois/')
    parser.add_argument('--output_folder', type=str, help='Folder to save text files to.', default='data/projets_lois_text/')
    args = parser.parse_args()
    os.makedirs(args.output_folder, exist_ok=True)

    for filename in os.listdir(args.input_folder):
        reader = PdfReader(os.path.join(args.input_folder, filename))
        full_text = ''
        for page_idx, page in enumerate(reader.pages):
            page_text = page.extract_text()
            full_text += f'Page {page_idx}:\n{page_text}\n\n'
    
        with open(os.path.join(args.output_folder, filename.replace('.pdf', '.txt').replace('.PDF', '.txt')), 'w', encoding='utf-8') as f:
            f.write(full_text)



if __name__ == '__main__':
    main()
