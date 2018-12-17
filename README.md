
# VisionScript
A Python3 script to convert multiple images of scanned text into a single word document using the Google Vision API and python-docx.

Follow the steps below to download, install, and run this project.

## Dependencies
Install these prerequisites:
- Python: https://www.python.org/downloads/
- Google Cloud Vision API Access: https://cloud.google.com/vision/

## Step 1. Clone the project or download ZIP
`git clone https://github.com/teraflik/VisionScript.git`

## Step 2. Install dependencies
Open PowerShell or Bash and type:
```
$ cd VisionScript
$ pip install -r requirements.txt
```
## Step 3. Set up your Google Cloud API Key:
On Windows go to Environment Variables and add a new key. Set Variable Name to `GOOGLE_APPLICATION_CREDENTIALS` and Variable Value to the path where the your access key is stored.

## Step 4. Store your images and run the script
Copy your images to the `images\` folder alongside `main.py` and execute the script by double-clicking it or typing in console:
```
python main.py
```

## Step 5. Output is stored in Word.docx
