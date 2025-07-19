# MarkdownPDFConverter.py

from markdown import markdown
from weasyprint import HTML
import os

class MarkdownPDFConverter:
    def __init__(self, input_file, output_file=None):
        self.input_file = input_file
        if output_file:
            self.output_file = output_file
        else:
            base, _ = os.path.splitext(self.input_file)
            self.output_file = base + '.pdf'

    def convert(self):
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file '{self.input_file}' does not exist.")

        with open(self.input_file, 'r', encoding='utf-8') as md_file:
            md_text = md_file.read()

        html_content = markdown(md_text, output_format='html5')
        HTML(string=html_content).write_pdf(self.output_file)
        print(f"✅ PDF generated at: {self.output_file}")
