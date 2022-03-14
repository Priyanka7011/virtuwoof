from django import forms
from django.forms import fields
from mainApp.models import BlogPosts


class BlogForm(forms.ModelForm):

    class Meta:
        model=BlogPosts
        fields=('blog_title','blog_image','blogContent','blog_category')
    
    def __init__(self,*args,**kwargs):
        super(BlogForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'customTextField'
        

        