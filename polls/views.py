from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Tweet


def index(request, question_id):
    context = {
        'sushi': 'sush1234',
        'hisushi': 1234,
        'id' : question_id,
        'tweets': Tweet.objects.all()
        }
    return render(request, 'polls/poll.html', context)