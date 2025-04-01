# Show Annotation Rectangles on Pictures in every file in a folder

import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
import os

# Define the folder containing the PDF files
folder_path = 'C:/path/to/your/pdf/files/folder/'

# Define the rectangles coordinates (x0, y0, x1, y1)
rectangles = [

    fitz.Rect(1033, 695, 1103, 714),
    fitz.Rect(820, 754, 968, 773),
    fitz.Rect(820, 774, 1033, 793),
    fitz.Rect(1033, 754, 1160, 783)
]

# Loop through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)

        # Open the PDF
        doc = fitz.open(file_path)

        # Select the page (assuming the first page)
        page = doc[0]

        # Render the page to an image
        pix = page.get_pixmap()

        # Convert the image to a NumPy array
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Display the image with the rectangle annotations
        fig, ax = plt.subplots()
        ax.imshow(np.array(img), extent=(0, pix.width, pix.height, 0))

        # Add the rectangle annotations to the plot
        for rect in rectangles:
            rect_patch = patches.Rectangle((rect.x0, rect.y0), rect.width, rect.height, linewidth=1, edgecolor='r',
                                           facecolor='none')
            ax.add_patch(rect_patch)

        plt.show()
