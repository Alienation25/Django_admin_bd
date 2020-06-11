from django.db import models
from PIL import Image

class info(models.Model):
    title_info= models.CharField('название ',max_length=200)
    text =models.TextField('Текст1')
    def __str__(self):
        return self.title_info

class comment(models.Model):
    info=models.ForeignKey(info,on_delete = models.CASCADE)
    name= models.CharField('Имя' ,max_length=100)
    coment= models.CharField('коментарий' ,max_length=100)
    def __str__(self):
        return self.name



# Create your models here.
