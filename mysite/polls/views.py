from gc import get_objects
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect#, Http404
from .models import Choice, Question
#from django.template import loader
from django.urls import reverse

def index(request):
    list_questions = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {
        "list" : list_questions,
    }
    return render(request, "polls/index.html", context)
    #return HttpResponse(template.render(context, request))

def detail(request, question_id):
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)
    choice = Choice.objects.get(id=question_id)
    return render(request, "polls/detail.html", {"question":question, "choice":choice})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",
        {
            "question": question,
            "error_message": "you didn´t select a choice",
        },
        )
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
