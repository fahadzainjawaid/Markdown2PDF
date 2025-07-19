# Markdown to PDF Converter

A simple and efficient Python tool to convert Markdown files to PDF format using WeasyPrint and the Python Markdown library.

## Features

- Convert any Markdown file to PDF with a single command
- Automatic output file naming (same name as input with `.pdf` extension)
- Custom output file path support
- HTML5 output format for better rendering
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites

Before installing the Python dependencies, you need to install system-level packages depending on your operating system:

### Ubuntu/Debian
```bash
sudo apt install libpango-1.0-0 libgdk-pixbuf2.0-0 libffi-dev libcairo
```

### macOS
```bash
brew install cairo pango gdk-pixbuf libffi
```

### Windows
WeasyPrint dependencies are typically handled automatically on Windows, but you may need to install Visual C++ Build Tools if you encounter compilation errors.

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd md2pdf
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Convert a Markdown file to PDF using the command line:

```bash
python md2pdf.py --filename path/to/your/file.md
```

#### Optional Parameters

- `--output-file`: Specify a custom output file path
```bash
python md2pdf.py --filename input.md --output-file custom_output.pdf
```

### Programmatic Usage

You can also use the `MarkdownPDFConverter` class directly in your Python code:

```python
from MarkdownPDFConverter import MarkdownPDFConverter

# Basic usage
converter = MarkdownPDFConverter('example.md')
converter.convert()

# With custom output file
converter = MarkdownPDFConverter('input.md', 'custom_output.pdf')
converter.convert()
```

## Examples

### Basic Conversion
```bash
python md2pdf.py --filename README.md
# Generates: README.pdf
```

### Custom Output Location
```bash
python md2pdf.py --filename docs/guide.md --output-file output/guide.pdf
# Generates: output/guide.pdf
```

## Dependencies

- **markdown**: Python library for parsing Markdown syntax
- **weasyprint**: HTML/CSS to PDF converter

## Project Structure

```
md2pdf/
├── MarkdownPDFConverter.py  # Core converter class
├── md2pdf.py               # Command-line interface
├── requirements.txt        # Python dependencies
├── Prerequisites.txt       # System-level dependencies
└── README.md              # This file
```

## Error Handling

The tool includes basic error handling:
- Checks if input file exists before processing
- Provides clear error messages for missing files
- UTF-8 encoding support for international characters

## Supported Markdown Features

This tool supports standard Markdown syntax including:
- Headers (H1-H6)
- Bold and italic text
- Lists (ordered and unordered)
- Links
- Images
- Code blocks
- Tables
- Blockquotes

## Limitations

- Advanced Markdown extensions may not be fully supported
- PDF styling is basic (no custom CSS support in current version)
- Large files may take some time to process

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source. Please add your preferred license here.

## Troubleshooting

### Common Issues

1. **WeasyPrint installation errors**: Make sure you have installed the system prerequisites for your operating system.

2. **File not found errors**: Ensure the input file path is correct and the file exists.

3. **Permission errors**: Make sure you have write permissions in the output directory.

### Getting Help

If you encounter issues:
1. Check that all prerequisites are installed
2. Verify your Python environment has the required packages
3. Ensure input files are valid Markdown format

## Version History

- **v1.0.0**: Initial release with basic Markdown to PDF conversion functionality
