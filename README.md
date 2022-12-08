# Screenshot and OCR script
This script takes a screenshot of the desktop, extracts the text from the screenshot using OCR, replaces all spaces with new lines, removes duplicates, and writes the unique words to a file called wordlist.txt. It then waits for 15 seconds before repeating the process.

Requirements
```python
Python 3
pytesseract
Pillow
pyautogui
```
Usage
Install the required libraries:
```python
pip install pytesseract Pillow pyautogui
```
Run the script:
```python
python screenshot-ocr.py
```
Note
This script will keep taking screenshots and extracting text indefinitely, so you may want to add a way to stop the script (e.g. by pressing a key or using a command-line flag) depending on your use case.
