from gc import get_objects
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect#, Http404
from .models import Choice, Question
#from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "list" 
  def get_queryset(self):
    return Question.objects.all()

class DetailView(generic.DetailView):
  template_name = "polls/detail.html"
  model = Question

class ResultsView(generic.DetailView):
  template_name = "polls/results.html"
  model = Question

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    select_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    return render(request, "polls/detail.html",
        {
            "question": question,
            "error_message": "você não selecionou nenhuma resposta!",
        },
        )
  else:
    select_choice.votes += 1
    select_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
        
def create_question(request):
  return render(request, "polls/new_question.html")
  
def savequest(request):
  question = Question(question_text=request.POST["question"], pub_date=timezone.now())
  question.save()
  question.choice_set.create(choice_text=request.POST["choice1"], votes=0)
  question.choice_set.create(choice_text=request.POST["choice2"], votes=0)
  return HttpResponseRedirect(reverse("polls:index"))
