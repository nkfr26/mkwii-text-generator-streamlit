# MKWii Text Generator
![Demo](https://github.com/NOKKY726/mkwii-text-generator/assets/117383835/ea2a5e4d-0fe6-4850-b9dd-a04143fd2df6)

## URL
https://nokky-mkwii-text-generator.streamlit.app

## Overview
マリオカートWiiのフォントを使用し、様々な文字列の画像を作成できます。

## Description
使用することができる文字は A～Z 1～9 : . + - / です。
1～9 - / には2つ目のフォントが用意されており、ダブルクォート ("") で囲むことにより使用できます。
また、ダブルクォートで囲んだ空白は、通常の空白の4分の1の長さとなっています。
微調整は <> で行うことができます。(> x 5 = " ")
右クリックから画像を保存し、サムネイル等にご利用ください。

## Requirement
- Windows 11
- Python 3.10.8
- Streamlit 1.22.0
- Pillow 9.5.0

## Usage
```
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
streamlit run src/app.py
```

## Input Example
```
time 00:00.000
lap " 1"  00:00.000
"km/h" sp<<<<<eed
```

## Author
[Twitter](https://twitter.com/nkfrom_mkw/)

## License
[MIT](https://github.com/NOKKY726/mkwii-text-generator/blob/main/LICENSE/)
