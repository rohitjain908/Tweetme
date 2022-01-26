from django import forms
from django import forms

MAX_TWEET_LENGTH=20

from .models import Tweet
class Tweetform(forms.ModelForm):
  class Meta:
    model=Tweet
    fields=['content']

  def clean_content(self):
    content=self.cleaned_data.get("content")
    if len(content)>MAX_TWEET_LENGTH:
      return forms.ValidationError("this tweet is too long")
    return content
