from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('projectrequest', views.ProjectRequestSubmit.as_view() , name = 'post_project_request'),
    path('newsletterform', views.NewsLetterFormSubmit.as_view(), name = 'post_news_letter_form'),
    path('contactus', views.ContactUsSubmit.as_view(), name = 'post_contact_us'),
]
