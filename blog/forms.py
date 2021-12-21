from django import forms

from blog.models import Comment
# from .models import Comment
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm 


class ContactForm(forms.Form):
  first_name = forms.CharField(max_length = 50)
  last_name = forms.CharField(max_length = 50)
  email_address = forms.EmailField(max_length = 150)
  message = forms.CharField(widget = forms.Textarea, max_length = 2000)


# editted

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['name','body']
  