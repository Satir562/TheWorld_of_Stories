from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Story(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    summary = models.CharField(verbose_name='Краткое описание', max_length=250, blank=True)
    content = models.TextField(verbose_name='Текст')
    poster = models.ImageField(upload_to='media/', verbose_name='Постер', null=True, blank=True)
    date_publisher = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    publisher = models.BooleanField(verbose_name='Публикация', default=True)


    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
        ordering = ['-date_publisher']

    def get_absolute_url(self):
        return f'/catalog/{self.id}'

    def __str__(self):
        return self.title


