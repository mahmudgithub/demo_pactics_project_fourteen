from django.forms import ModelForm
from.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name','email','amount']
        #fields = '__all__'