from django.db import models
import re
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )


    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력해주세요. 최대 100자 내외')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='경도/위도 포맷으로 입력', validators=[lnglat_validator])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add 최초에만
    updated_at = models.DateTimeField(auto_now=True) #auto_now 업데이트할때마다

    class Meta:
        ordering = ['-id'] #필드수는 1~2개만 쓰는게 성능 높이는데 좋음

    def __str__(self): #포스트에 글들이 다 Post object로 나오는데 title로 바꾸기 위함
        return self.title