from docling.document_converter import DocumentConverter
from pathlib import Path

def convert_to_markdown(input_path):
    # Convert input path to Path object for easier handling
    input_path = Path(input_path)
    
    # Check if input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
        
    # Create converter instance
    converter = DocumentConverter()
    
    # Convert the document
    result = converter.convert(str(input_path))
    
    # Create output path with .md extension in the same directory
    output_path = input_path.with_suffix('.md')
    
    # Write the markdown content to file
    output_path.write_text(result.document.export_to_markdown())
    
    return output_path

# Example usage
if __name__ == "__main__":
    try:
        input_file = "/home/hung/Public/leao/web-development/books/django-by-example/Django 5 By Example.pdf"  # Replace with your input file path
        output_file = convert_to_markdown(input_file)
        print(f"Conversion successful! Markdown file saved at: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")