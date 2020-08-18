from django.contrib import admin
from mtcnn.mtcnn import MTCNN
# Register your models here.

class FaceApi:
    detector = MTCNN()