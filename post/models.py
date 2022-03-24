from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

# Create your models here.

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='posts/')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Активный', default=False)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class Coment(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    comment = models.TextField(verbose_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)




