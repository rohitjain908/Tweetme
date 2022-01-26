from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import random

from tweets.form import Tweetform

# Create your views here.
from .models import Tweet

def index(request,tweet_id):
  #print(tweet_id)
  try:
    tweet=Tweet.objects.get(id=tweet_id)
  except:
    return HttpResponse("Page not exist")

  data={
    'id':tweet.id,
    'content':tweet.content
  }
  #return JsonResponse(data)

  #return HttpResponse(f"Hello world{id}")

  return render(request,'tweets/home.html',{'data':data})

def home(request):
  return render(request,'tweets/home.html')


def tweet_view(request):
  qs=Tweet.objects.all()
  tweet_list=[{'id':obj.id,'content':obj.content,'likes':random.randint(0,22)} for obj in qs]
  data={
    "response":tweet_list
  }
  return JsonResponse(data)

def craete_tweet(request):
  form=Tweetform(request.POST or None)
  if form.is_valid():
    obj=form.save(commit=False)
    obj.save()
    form=Tweetform()
  return render(request,'components/form.html',{'form':form})
