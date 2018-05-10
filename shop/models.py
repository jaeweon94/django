from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    # related_name = 'shop_post_set'
    # +를 쓰게 되면...
    # user.post_set.all()은 못 씀
    # shop.models.Post.objects.filter(user=user)은 가능
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)