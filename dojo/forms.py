# dojo/forms.py
from django import forms
from .models import Post, GameUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'user_agent']
        widgets= {
            'user_agent': forms.HiddenInput,
        }
    #title = forms.CharField(validators=[min_length_3_validator])
    #content =
    #forms.CharField(widget=forms.Textarea())

    '''
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
    '''

class ServerForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = '__all__'





