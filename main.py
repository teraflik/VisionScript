import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def VisionScript(indir):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    folders = []
    files = []
    

    print("\nReading Directory \'images\\\'... ", end="")
    for entry in os.scandir(indir):
        if entry.is_dir():
            folders.append(entry.path)
        elif entry.is_file():
            files.append(entry.path)
    print("done\n")
    
    i = 0
    total = len(files)
    output_text = ""

    for image in files:
        i = i+1
        file_name = str(image)
        print("Processing {:d} of {:d} images: {:s}...".format(i, total, file_name), end="")

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        
        response = client.document_text_detection(image=image)
        document = response.full_text_annotation
        
        output_text = output_text + document.text + "\n\n\n"
        
        print("... done!")
    
    f = open('output.txt', 'w', encoding='utf-8')
    f.write(output_text)
    f.close()
    print("\nAll images processed. Output saved to output.txt\n")

if __name__ == "__main__":
    VisionScript('images/')