import os
import pandas as pd
from ast import literal_eval

from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model

# Download model
download_model(model='bert-squad_1.1', dir='./models')


# INPUT PDFs
# Here path is the folder of the PDFs to be used
df = pdf_converter(directory_path='C:/Users/Viswash/Desktop/Work/ChatBot/Research/ Papers/')
df.head()

cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)

# Fit Retriever to documents
cdqa_pipeline.fit_retriever(df=df)


# INPUT QUESTION
query = 'when was the second Indian Factory Act passed?'

prediction = cdqa_pipeline.predict(query)

ans = 'query: {} \nanswer: {} \ntitle: {} \nparagraph: {}'.format(query,prediction[0],prediction[1],prediction[2])
print(ans)
# OUTPUT
# print('query: {}'.format(query))
# print('answer: {}'.format(prediction[0]))
# print('title: {}'.format(prediction[1]))
# print('paragraph: {}'.format(prediction[2]))
