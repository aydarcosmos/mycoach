from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название статьи')
    content = models.TextField(verbose_name = 'Статья')
    published = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name = 'Опубликовано')
    sport = models.ForeignKey('Sport', on_delete = models.PROTECT, verbose_name = 'Вид спорта')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published']

class Sport(models.Model):
    name = models.CharField(max_length = 30, verbose_name = 'Вид спорта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'
        ordering = ['name']