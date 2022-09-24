from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
# The methods will correspond to the urls.
# We wrote "request" because each method meets the Http Request request from the user.
def index(request):
    return HttpResponse("Home Page")

def blogs(request):
    return HttpResponse("Blogs")

def blog_details(request, id):
    return HttpResponse("Blog Details: " + str(id))