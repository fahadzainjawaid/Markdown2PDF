# md2pdf.py

import argparse
from MarkdownPDFConverter import MarkdownPDFConverter

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown file to PDF")
    parser.add_argument('--filename', required=True, help="Path to the input markdown (.md) file")
    parser.add_argument('--output-file', help="Optional path to the output PDF file")

    args = parser.parse_args()

    converter = MarkdownPDFConverter(input_file=args.filename, output_file=args.output_file)
    converter.convert()

if __name__ == '__main__':
    main()
