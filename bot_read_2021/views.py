from django.shortcuts import render
from django.http import HttpResponse
import pytesseract
from PIL import Image
from fpdf import FPDF
import os
import pandas as pd
from ast import literal_eval
from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model
from django.http import HttpResponseRedirect


def text_to_pdf(text):  
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 14)
    pdf.multi_cell(0,10,text, border = 0, align = 'J')
    pdf.output("media/pdf/test.pdf")


def ocr(filename):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def handle_uploaded_file(f):
    with open('media/pdf/'+str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    return render(request,'index.html')
def voice_to_text_fun(file):
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    if 'mp3' in str(file): 
        sound = AudioSegment.from_file('media/'+str(file), format='mp3')

        sound.export('output.wav', format='wav')            
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            audio_text = get_large_audio_transcription('./media/output.wav')   
            print(audio_text)       
            return str(audio_text)
        
        except:
            return 'Sorry.. run again...'   



def img_to_text(request):
    title = "Read Bot"
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return render(request,'img_to_text.html', {"msg":'No file selected'})
        file = request.FILES['file']

        handle_uploaded_file(file)
        extracted_text = ocr(file)
        text_to_pdf(extracted_text)
        if request.POST['question']:
            ans_of_q =  qna(request.POST['question'])
            return render(request,'img_to_text.html',
                            {"msg":'Successfully processed',
                            "extracted_text":extracted_text,
                            'ans_of_q0':ans_of_q[0],
                            'ans_of_q1':ans_of_q[1],
                            'ans_of_q2':ans_of_q[2],
                            'ans_of_q3':ans_of_q[3]
                            })
        else:
            return render(request,'img_to_text.html', {"msg":'No query entered'})

    else:
    	return render(request,'img_to_text.html')

def pdf_to_text(request):
    title = "Read Bot"
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return render(request,'pdf_to_text.html', {"msg":'No file selected'})
        file = request.FILES['file']
        handle_uploaded_file(file)
        if request.POST['question']:
            ans_of_q =  qna(request.POST['question'])
            return render(request,'pdf_to_text.html',
                            {"msg":'Successfully processed',
                            'ans_of_q0':ans_of_q[0],
                            'ans_of_q1':ans_of_q[1],
                            'ans_of_q2':ans_of_q[2],
                            'ans_of_q3':ans_of_q[3]
                            })

        else:
            return render(request,'pdf_to_text.html', {"msg":'No query entered'})

    else:
    	return render(request,'pdf_to_text.html')


download_model(model='bert-squad_1.1', dir='./models/')
def qna(query):
    df = pdf_converter(directory_path='./media/pdf')
    df.head()
    cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)
    # Fit Retriever to documents
    cdqa_pipeline.fit_retriever(df=df)
    # INPUT QUESTION
    print("\n\n\\n",query)
    #query = 'when was the second Indian Factory Act passed?'
    prediction = cdqa_pipeline.predict(query)
   # ans = 'query: {}\n \nanswer: {} \ntitle: {} \nparagraph: {}'.format(query,prediction[0],prediction[1],prediction[2])
    ans=[query,prediction[0],prediction[1],prediction[2]]
    return ans


        