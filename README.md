## Number Plate Recognition with Optical Character Recognition

This code is not open source, it is for my personal portfolio. If you want open source, please visit [simple-npr](https://github.com/JosuaLimbu/npr-tesseract)

Number Plate Recognition (NPR), also known as Automatic Number Plate Recognition (ANPR) or License Plate Recognition (LPR), is a technology used to automatically detect and recognize vehicle license plates. The system uses an optical camera and character recognition (OCR) software to capture images of license plates from passing vehicles, then analyzes the images to recognize and extract the text contained within. Upon successful reading using OCR, the extracted license plate data is stored in a MySQL database. This code is integrated into the [U-Park](https://github.com/JosuaLimbu/u-park/) web system.

### Install

**Install on Windows**

Install [Git Bash](https://git-scm.com/downloads), [Python](https://www.python.org/downloads/) and [Tesseract](https://sourceforge.net/projects/tesseract-ocr.mirror/) first

After that, open git bash and follow these commands

```bash
$ git clone https://github.com/JosuaLimbu/npr-tesseract.git
$ cd npr-with-ocr
$ pip install -r requirements.txt
$ python3 detect3.py
```

The end result will be like this.
![Result](img/Result.jpg)
