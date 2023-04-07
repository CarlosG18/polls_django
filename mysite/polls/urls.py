from django.urls import path
#from numpy import result_type

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="details"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("createquest/", views.create_question, name="createquest"),
    path("savequest/", views.savequest, name="savequest"),
]
