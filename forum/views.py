from django.shortcuts import render
from .models import Question, Answer
# Create your views here.

def questions_list(request):
    data=Question.objects.all()
    return render(request,'forum/list.html',{'data':data})

def question_details(request,id):
    data=Question.objects.get(id=id)
    return render(request,'forum/detail.html',{'data':data})
