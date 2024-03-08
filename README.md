# MKWii Text Generator (Streamlit)
![Demo](https://github.com/nkfr26/mkwii-text-generator-streamlit/assets/148517866/5a5f10fe-ca4d-4df2-9dd6-f2f4f53d0922)

## URL
https://nokky-mkwii-text-generator.streamlit.app

## Overview
This is the web version of [MKWii Text Generator (Tkinter)](https://github.com/nkfr26/mkwii-text-generator-tkinter/).  
This allows you to create Mario Kart Wii text in different strings.

## Description
The characters that can be used are A-Z 1-9 : . + - /  
The second font is provided for 1-9 - / and can be used by enclosing them in double quotes (").  
Also, the space enclosed in double quotes is a quarter length of the normal space.  
Fine adjustment can be done with <> (> x 5 = " ").  
Right-click to save the image and please use it for thumbnail, etc.  
Theme can be changed via the kebab menu (︙) in the top right corner -> Settings.

## Input Example
```
time 00:00.000
lap " 1"  00:00.000
"km/h" sp<<<<<eed
```

## Requirement
- Windows 11
- Python 3.11.8
- Streamlit 1.31.1
- Pillow 10.2.0
- NumPy 1.26.4

## Usage
```
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
streamlit run src/app.py
```

## Author
[Twitter](https://twitter.com/nkfr26/)

## License
[MIT](https://github.com/nkfr26/mkwii-text-generator-streamlit/blob/main/LICENSE/)
