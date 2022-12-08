import os
import time
import pytesseract
from PIL import Image
import pyautogui

while True:
    # Take a screenshot
    image = pyautogui.screenshot()
    image.save('screenshot.png')

    # Extract text using OCR
    text = pytesseract.image_to_string(Image.open('screenshot.png'), lang='eng')

    # Replace spaces with new lines
    text = text.replace(' ', '\n')

    # Remove duplicates
    words = set(text.split('\n'))

    # Write the extracted words to a file
    with open('wordlist.txt', 'w') as f:
        for word in words:
            f.write(f"{word}\n")

    # Wait for 15 seconds
    time.sleep(15)
