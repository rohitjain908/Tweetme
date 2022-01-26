from django.urls import path
from . import views

urlpatterns=[
  path('<int:tweet_id>',views.index),
  path('home',views.home,name="home"),
  path('',views.tweet_view),
  path('create-tweet',views.craete_tweet)
]