from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'





#폼자체는 폼을 만들기 위한 것이여. 그리고 이진석 강사님은 이 폼을 쓰면 좋다고 하시는 거고


