# BotRead

This project is an effort to make the hefty job of going through tons of books, images, and reference materials in search of our desired answers or references much easier.

Using the CDQA architecture, We can scan through multiple sources at the same time and NLP is used over it to find the most relevant document as well as the most relevant answer to the query asked.

We allow users to upload data in the forms of Images, Text doucments, and PDFs. These are then converted to text. The TF-IDF features based on uni-grams and bi-grams and the cosine similarity is computed between the Query asked and the Documents available in the database to select the most relevant Document. We then use BERT with the paragraphs of the most relevant document selected and the Query provided to find the most relevant part of the paragraph that has the most potential to be our desired answer.


## Packages used

* torch==1.7.1
* django
* cdqa
* transformers==2.0
* pydub
* BERT_Squad1.1 [Model]
* pytesseract
* PIL
* fpdf
* tika
* markdown
* prettytable
* wget

## Installation

NOTE : Tested on Python 3.6.8
```bash
pip install torch==1.7.1
pip install django
pip install cdqa
pip install transformers==2.0
pip install pydub
pip install BERT_Squad1.1 [Model]
pip install pytesseract
pip install PIL
pip install fpdf
pip install tika
pip install markdown
pip install prettytable
pip install wget

git clone https://github.com/abhishekbhatt209/Hackathon2021.git
cd Hackathon2021
```

Additional software: [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe)

## Usage

```bash
python manage.py runserver
```
## References

* [Django](https://docs.djangoproject.com/en/3.1/) - For Django references
* [Unsupervised Question Answering by Cloze Translation](https://arxiv.org/abs/1906.04980)
* [BERT FineTuning](https://medium.com/swlh/fine-tuning-bert-for-text-classification-and-question-answering-using-tensorflow-framework-4d09daeb3330) - Reference article
* [BERT FineTuning](https://medium.com/saarthi-ai/build-a-smart-question-answering-system-with-fine-tuned-bert-b586e4cfa5f5) - Reference article
* [cdQA](https://github.com/cdqa-suite/cdQA) - cdQA Architecture reference
* [GPT3 for Response](https://arxiv.org/ftp/arxiv/papers/2102/2102.03062.pdf) - Understanding Emails and Drafting Responses: An Approach Using GPT-3
* [PyTesseract](https://pypi.org/project/pytesseract/) - For OCR
* [PIL](https://pillow.readthedocs.io/en/stable/) - PIL references
* [Pyfpdf](https://pyfpdf.readthedocs.io/en/latest/) - PDF Generation


## Contributers

👤 **Abhishek Bhatt - Ganpat University - [@abhishekbhatt209](https://github.com/abhishekbhatt209)**

👤 **Kunal Malvi - Ganpat University - [@kunalmalvi18](https://github.com/kunalmalvi18)**

👤 **Anil Prajapati - Ganpat University - [@anilprajapati22](https://github.com/anilprajapati22)**

👤 **Viswash Mehta - Ahmedadad Institute of Technology - [@ViswashMehta](https://github.com/ViswashMehta)**

👤 **Sunny Kushwaha - Ahmedadad Institute of Technology - [@Ares358](https://github.com/Ares358)**


## License
[MIT](https://choosealicense.com/licenses/mit/)
