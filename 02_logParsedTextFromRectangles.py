#Log Parsed text from Annotation Rectangles of every file in a folder

import fitz  # PyMuPDF
import os

# ######## Define the folder containing the PDF files ########
folder_path = 'C:/path/to/your/pdf/files/folder/'

# Define the rectangles coordinates (x0, y0, x1, y1),
# add as many as you like (these values are just example),
# you can see the rectangles by running the first file

rectangles = [
    fitz.Rect(1033, 695, 1103, 714),
    fitz.Rect(820, 754, 968, 773),
    fitz.Rect(820, 774, 1033, 793),
    fitz.Rect(1033, 754, 1160, 783)
]


# Function to extract and clean text from a rectangle
def extract_text_from_rect(page, rect):
    text = page.get_text("text", clip=rect)
    lines = text.split('\n')

    if lines:
        # Filter out empty strings and strings with only dots
        cleaned_values = [line.strip() for line in lines if line.strip() not in ['', '.']]

        if cleaned_values:
            # Use the first value as the title if no explicit title is detected
            title = cleaned_values[0]
            values = cleaned_values[1:]  # Remaining lines as values
            return title, values

    return None, None


# Loop through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)
        print(f"Processing file: {filename}")

        # Open the PDF
        doc = fitz.open(file_path)

        # Select the page (assuming the first page)
        page = doc[0]

        # Process each rectangle
        for idx, rect in enumerate(rectangles):
            title, values = extract_text_from_rect(page, rect)

            # Check if title or values exist
            if title or values:
                print(f"Rectangle {idx + 1}:")
                print(f"  Title: {title}")
                if values:
                    print(f"  Values: {', '.join(values)}")
            else:
                print(f"Rectangle {idx + 1}: No text found.")

        print("=" * 50)  # Separator for each file

