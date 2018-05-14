from django.db import models
from django.conf import settings
from django.forms import ValidationError
from django.core.urlresolvers import reverse
import re


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

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력해주세요. 최대 100자 내외')
    content = models.TextField(verbose_name='내용')

    photo = models.ImageField(blank=True)

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='경도/위도 포맷으로 입력', validators=[lnglat_validator])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    tag_set = models.ManyToManyField('Tag', blank=True)
    #문자열로 지정해도 인식됨. Tag가 아래 있으므로 Tag로 못 씀. 'Tag'로 써야함.
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add 최초에만
    updated_at = models.DateTimeField(auto_now=True) #auto_now 업데이트할때마다

    class Meta:
        ordering = ['-id'] #필드수는 1~2개만 쓰는게 성능 높이는데 좋음

    def __str__(self): #포스트에 글들이 다 Post object로 나오는데 title로 바꾸기 위함
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id]) ## /blog/detail/4


class Ask(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self): #str은 모델에다 쓰는 거였군.
        return self.name



