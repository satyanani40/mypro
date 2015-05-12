from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.generic import View
from django.shortcuts import  render
import json
from models import *
import os
from settings import *
from django.core.files.base import ContentFile
import datetime
from django.core import serializers
from mongoengine.django.auth import User
from django.core.mail import EmailMultiAlternatives
from bson.json_util import dumps
from bson import json_util
from django.core.serializers.json import DjangoJSONEncoder
#from rest_framework import viewsets
import csv





class All_chapters(View):
    def get(self, request):
        queryset = Chapterdetails.objects.all()
        data = queryset.to_json()
        loop_data = json.loads(data)
        for k in loop_data:
            k['_id'] = k['_id']['$oid']
        return HttpResponse(dumps({'data':loop_data}))

class CreateExam(View):

    def get(self, request):
        queryset = Examdetails.objects.all()
        data = queryset.to_json()
        loop_data = json.loads(data)
        for k in loop_data:
            k['_id'] = k['_id']['$oid']
        return HttpResponse(dumps({'data':loop_data}))

    def post(self, request):
        print request.POST['exam_name']
        print request.FILES['upload']

        folder = 'all_csv_files'
        uploaded_filename = request.FILES['upload'].name
        try:
            os.mkdir(os.path.join(BASE_DIR, folder))
        except:
            pass

        # save the uploaded file inside that folder.
        uploaded_filename = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S_%f_file.csv")
        full_filename = os.path.join(BASE_DIR, folder, uploaded_filename)
        store_path = folder+'/'+uploaded_filename
        fout = open(full_filename, 'wb+')
        file_content = ContentFile(request.FILES['upload'].read())
        try:
            # Iterate through the chunks.
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()

            with open(full_filename, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                counter = 0
                for row in spamreader:
                    print '-------------------------'
                    data =  ', '.join(row)
                    details = data.split(",")

                    if counter > 0:
                        exam_details_insert = Examdetails(exam_name = request.POST['exam_name'])
                        exam_details_insert.question =details[0]
                        exam_details_insert.a = details[1]
                        exam_details_insert.b = details[2]
                        exam_details_insert.c = details[3]
                        exam_details_insert.d = details[4]
                        exam_details_insert.correct = details[5]
                        exam_details_insert.save()
                    counter += 1

            return HttpResponse('hellow')
        except Exception as e:
            return HttpResponse(e)

class LoginCheck(View):

    def get(self, request):
        return render(request, 'chapters.html')
    def post(self, request):
        data = json.loads(request.body)
        username = data['email']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                return HttpResponse("User is valid, active and authenticated")
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
            return HttpResponse("incorrect")
        return HttpResponse('hellow')

class Chapters(View):

    def get(self, request):
        return render(request, 'chapters.html')

    def post(self, request):
        #print request.FILES['upload']
        print request.POST['chaptername']
        folder = 'chapter_pdf'
        uploaded_filename = request.FILES['upload'].name
        try:
            os.mkdir(os.path.join(BASE_DIR, folder))
        except:
            pass

        # save the uploaded file inside that folder.
        uploaded_filename = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S_%f_file.pdf")
        full_filename = os.path.join(BASE_DIR, folder, uploaded_filename)
        print '-------full_filename------------'
        store_path = folder+'/'+uploaded_filename
        print '--------base dir------------', BASE_DIR


        fout = open(full_filename, 'wb+')
        file_content = ContentFile(request.FILES['upload'].read())

        try:
            # Iterate through the chunks.
            for chunk in file_content.chunks():
                fout.write(chunk)
            fout.close()

            data = Chapterdetails(chapter_name = request.POST['chaptername'])
            data.chapter_path = store_path
            data.save()

            html = "<html><body>SAVED</body></html>"
            return HttpResponse(html)
        except Exception as e:
            html = "<html><body>NOT SAVED</body></html>"
            return HttpResponse(html)



class DoRegister(View):
    def get(self, request):
        return render(request, 'chapters.html')

    def post(self, request):
        try:
            status = ''
            data = json.loads(request.body)
            password = data['password'] #request_data['email'
            email    = data['email']      #request_data['email'
            username = data['username']
            isuser_email = is_emailalredyexits(email)
            isusername = is_useravaible(username)

            if not isuser_email and not isusername:
                User_save = User.create_user(username = username, email=email,password=password)
                User_save.is_active = True;
                User_save.save()
                user_email = User_save.email

                subject = 'user account details'
                text_content = 'useremail :'+user_email+'<br/>user password:'+password+'<br/>username:'+username
                from_email = EMAIL_HOST_USER
                to = user_email
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                #msg.attach_alternative(html_content, "text/html")
                msg.send()
                status = ('a details  has been sent to your '+user_email+' please click on the link')
            else:
                status = ('email or username alredy exits')
            return (json.dumps({'status':status}))
        except Exception as e:
            print e
            return HttpResponse({'status':e})

def is_emailalredyexits(email):
    status = 0
    try:
        if email:
            User.objects.get(email=email)
            status = 1
    except Exception as e:
        status = 0
    return status

def is_useravaible(username):
    status = 0
    try:
        if username:
            User.objects.get(username=username)
            status = 1
    except Exception as e:
        status = 0
    return status
