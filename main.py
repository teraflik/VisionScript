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
	f = open('output.txt', 'w', encoding='utf-8')
	f2 = open('output_old.txt', 'w', encoding='utf-8')

	for image in files:
		i = i+1
		file_name = str(image)
		print("Processing {:d} of {:d} images: {:s}...".format(i, total, file_name), end="")

		with io.open(file_name, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content=content)
		
		response = client.document_text_detection(image=image)
		document = response.full_text_annotation
		
		original_output = document.text
		
		new_output = original_output.replace("\r", "")
		new_output = new_output.replace("\n", " ")
		output_text = new_output + "\n\n"
		output_text_lb = original_output + "\n\n"

		f.write(output_text)
		f2.write(output_text_lb)
			
		print("... done!")
	
	f.close()
	f2.close()
	print("\nAll images processed. Output saved to output.txt\n")

if __name__ == "__main__":
	VisionScript('images/')
	input("Press Enter to continue...\n")