from django import forms
from .models import Post

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields =('buyer', 'now_price')

class NewPostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields =('author', 'category','image', 'title', 'start_price', 'description', 'end_date')