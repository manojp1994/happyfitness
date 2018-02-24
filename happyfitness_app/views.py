from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

# index
def index(request):
	args={}
	return render_to_response("index.html",args)

# gallery
def gallery(request):
	args={}
	return render_to_response("gallery.html",args)

# Special features
def specialfeatures(request):
	args={}
	return render_to_response("specialfeatures.html",args)