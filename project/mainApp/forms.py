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
        

class SearchForm(forms.Form):

    FILTER_CHOICES = (
        
        ('pet.veterinary', 'Veterinary'),
        ('pet.shop', 'Pet Shops'),
        ('pet.service', 'Pet Services'),
        ('pet.dog_park', 'Pet Parks'),

    )
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your address"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"city"}))
    state= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"state"}))
    filter_by = forms.ChoiceField(choices = FILTER_CHOICES)

    def __init__(self,*args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'inputBox'
            self.fields[field].label = ""
