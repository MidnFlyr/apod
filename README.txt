# NASA APOD Auto Downloader and Wallpaper Setter

This Python project fetches the Astronomy Picture of the Day (APOD) from NASA's public API, downloads the daily image, and sets it as the desktop wallpaper on Windows systems.

A simple automation project using space data and basic scripting.

## Features

- Retrieves daily image and explanation from NASA APOD API
- Downloads the image as `apod.jpg`
- Sets the image as Windows desktop wallpaper
- Prints date, title, and explanation to the console

## Requirements

- Python
- requests library
- Windows OS

Install dependencies:

'''
pip install requests
'''

## API Key Setup

1. Get your NASA API key from https://api.nasa.gov
2. Create a `.env` file in the root directory with the following content:

'''
NASA_API_KEY=your_actual_api_key_here
'''

Note: Do not upload your `.env` file to GitHub. It should be listed in `.gitignore`.

## How to Run

'''
python main.py
'''

The script will:

- Download the astronomy image of the day
- Save it as `apod.jpg`
- Set it as your desktop wallpaper (Windows only)
- Print image metadata to the console


Thank you.