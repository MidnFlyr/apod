'''
    Author: Brayden Rhee
    Date: June 12, 2025
    Program Name: NASA APOD Auto Downloader & Wallpaper Setter
    https://github.com/midnflyr
'''

import requests
import os
import ctypes

API_KEY = "YOUR_API_KEY" 

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
response = requests.get(url)
data = response.json()

print("Date:", data['date'])
print("Title:", data['title'])
print("Description:", data['explanation'])
print("Image URL:", data['url'])

img_url = data['url']
img_data = requests.get(img_url).content
img_path = os.path.join(os.getcwd(), "apod.jpg")

with open(img_path, 'wb') as handler:
    handler.write(img_data)

print(f"Image saved on: {img_path}")

try:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)
    print("Background set!")
except:
    print("This program is for Windows only.")
