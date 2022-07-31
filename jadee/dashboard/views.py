from rest_framework.response import Response
from rest_framework import generics
import json
from .models import ProjectRequest , NewsLetterForm ,ContactUs

#this class is for project request
class ProjectRequestSubmit(generics.ListAPIView):

    def post(self,request):
        data = json.loads(request.body)
        ProjectRequest.objects.create(
                                    name = data['name'],
                                    email = data['email'],
                                    message = data['message'])
        return Response("ProjectRequest created successfully")
#this class is for news letter form
class NewsLetterFormSubmit(generics.ListAPIView):
    
    def post(self,request):
        data = json.loads(request.body)
        NewsLetterForm.objects.create(
                                    email = data['email']
                                    )
        return Response("NewLetterForm created successfully")

#This class is for communication with
class ContactUsSubmit(generics.ListAPIView):

    def post(self,request):
        data = json.loads(request.body)
        ContactUs.objects.create(
                                    name = data['name'],
                                    email = data['email'],
                                    phone = data['phone'],
                                    message = data['message'])
        return Response("ContactUs created successfully")