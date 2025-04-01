# define annotation and get text from annotation rectangles as: first row is title, others are values
#pip install openpyxl #if error
import fitz  # PyMuPDF
import os
import pandas as pd

# Define the folder containing the PDF files
folder_path = 'C:/path/to/your/pdf/files/folder/'
output_folder_path = 'C:/path/to/your/output/folder/'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Define the rectangles coordinates (x0, y0, x1, y1)
rectangles = [
    fitz.Rect(1033, 695, 1103, 714),
    fitz.Rect(820, 754, 968, 773),
    fitz.Rect(820, 774, 1033, 793),
    fitz.Rect(1033, 754, 1160, 783)
]


# Function to extract text from a rectangle
def extract_text_from_rect(page, rect):
    text = page.get_text("text", clip=rect)
    lines = text.split('\n')
    if lines:
        # Filter out empty strings and strings with only '.'
        values = [value for value in lines if value.strip() not in ['', '.']]
        if values:
            title = values[0]  # Take the first value as title
            remaining_values = values[1:]  # Rest are values
            return title, remaining_values
    return None, []


# Create a dictionary to store the extracted data
data = {}

# Loop through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)

        # Open the PDF
        doc = fitz.open(file_path)

        # Select the page (assuming the first page)
        page = doc[0]

        # Extract text from each rectangle and format it
        for rect in rectangles:
            title, values = extract_text_from_rect(page, rect)
            if title:  # Use title as the key
                if title not in data:
                    data[title] = []
                data[title].append(values)

        # Save the annotated file to the output folder
        output_file_path = os.path.join(output_folder_path, filename.replace('.pdf', '_with_annotations.pdf'))
        doc.save(output_file_path)

# Create a DataFrame from the extracted data
df = pd.DataFrame.from_dict(data, orient='index').transpose()

# Save the DataFrame to an Excel file
output_excel_path = 'C:/path/to/your/folder/to/extracted_data.xlsx'
df.to_excel(output_excel_path, index=False)

print(f"Data extraction completed. Excel file saved to: {output_excel_path}")

