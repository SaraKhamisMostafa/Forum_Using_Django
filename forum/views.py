from django.shortcuts import render , redirect
from .models import Question, Answer
from .forums import QuestionForm
# Create your views here.

def questions_list(request):
    data=Question.objects.all()
    return render(request,'forum/list.html',{'data':data})

def question_details(request,id):
    data=Question.objects.get(id=id)
    answers=Answer.objects.filter(question=data)
    return render(request,'forum/detail.html',{'data':data , 'answers':answers})


def add_question(request):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/questions/')
    else:
        form=QuestionForm()  
    return render(request,'forum/add.html',{'form': form})