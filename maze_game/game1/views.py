from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def game1(request):
  template= loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def start(request):
  template=loader.get_template('index.html')
  return HttpResponse(template.render())
