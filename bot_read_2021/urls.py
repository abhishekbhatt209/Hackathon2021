from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('img_to_text', views.img_to_text, name='img_to_text'),
    path('pdf_to_text', views.pdf_to_text, name='pdf_to_text'),
]