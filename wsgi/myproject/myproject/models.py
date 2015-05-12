from mongoengine import *
connect('python', username='admin', password='kYD1vRSUspmw')
from mongoengine.django.auth import User
from rest_framework import serializers

from rest_framework_mongoengine.serializers import DocumentSerializer

class Chapterdetails(Document):
    chapter_name = StringField(max_length=200)
    chapter_path = StringField(max_length=500)

class Examdetails(Document):
    exam_name = StringField(max_length= 25000)
    question = StringField(max_length= 25000)
    a = StringField(max_length= 2500)
    b = StringField(max_length= 2500)
    c = StringField(max_length= 2500)
    d = StringField(max_length= 2500)
    correct = StringField(max_length= 250)
