import argparse
import re
import xml.etree.ElementTree as ET
from src.paragraph_splitter import split_paragraphs

def extract_text(input_file):
    output_file = input_file.replace(".ttml", ".txt")
    with open(output_file, 'w') as f:
        tree = ET.parse(input_file)
        root = tree.getroot()
        ns = {'ttml': 'http://www.w3.org/ns/ttml'}
        paragraph = ''
        for p in root.findall('.//ttml:p', ns):
            try:
                text = p.text.strip()
            except:
                print(p.text)    
            paragraph += f'{text} '
        # Remove leading/trailing spaces and newlines
        paragraph = paragraph.strip()
        paragraph = re.sub(r'\n+', '\n', paragraph)
        f.write(split_paragraphs(paragraph))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input TTML file')
    args = parser.parse_args()
    extract_text(args.input_file)
