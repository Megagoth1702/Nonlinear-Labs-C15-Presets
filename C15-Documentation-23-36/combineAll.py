import os

def combine_html_files(input_folder, output_file):
    # List to hold the content of all HTML files
    combined_html_content = []

    # Traverse the directory and subdirectories to find all HTML files
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as html_file:
                    combined_html_content.append(html_file.read())

    # Combine all HTML content into one large HTML string
    combined_html = "\n".join(combined_html_content)

    # Write the combined HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as output_html_file:
        output_html_file.write(combined_html)

    print(f"Combined HTML file created at: {output_file}")

# Specify the input folder containing the HTML files and the output file path
input_folder = r'c:\Users\schmittand\Downloads\C15-Documentation-23-36\HTML-Manual'
output_file = r'c:\Users\schmittand\Downloads\C15-Documentation-23-36\combined.html'

# Call the function to combine HTML files
combine_html_files(input_folder, output_file)