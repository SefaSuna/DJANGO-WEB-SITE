from django.db import models
from django.contrib.auth.models import User
from pytz import timezone
from ckeditor.fields import RichTextField


class Data(models.Model):
    # author=models.ForeignKey(User,verbose_name="yazar",on_delete=models.CASCADE)
    title=models.CharField(max_length=80,verbose_name="başlık")
    # sm=models.TextField(max_length=800,verbose_name="özet")
    content=RichTextField(verbose_name="içerik")
    image=models.FileField(blank=True,null=True,verbose_name="fotoğraf ekle")
    date=models.DateField()
    
    def __str__(self):
        return self.title
class comment(models.Model):
    article=models.ForeignKey(Data,verbose_name="article",on_delete=models.CASCADE,related_name="comments")
    ad=models.CharField(max_length=50,verbose_name="ad")
    yorum=models.CharField(max_length=500,verbose_name="yorum")
    date=models.DateField()
    class Meta:
        ordering = ['-date']