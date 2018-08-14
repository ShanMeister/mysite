from django.db import models


# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('r1', 'art'),
        ('r2', 'music'),
        ('r3', 'game'),
    )
    project_category = models.CharField(default='r1', max_length=2, choices=CATEGORY_CHOICES, verbose_name='專案類別')
    project_name = models.CharField(default='my project', max_length=50, verbose_name='專案名稱')
    project_description = models.TextField(default='my project', verbose_name='專案敘述')
    project_picture = models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='專案圖片')
    project_duration = models.DateField(default='2099-01-01', blank=False, null=False, verbose_name='專案期限')
    project_goal = models.IntegerField(default=10000, blank=False, null=False, verbose_name='達標金額')
    user_name = models.CharField(default='user', max_length=15, verbose_name='使用者名稱')
    user_email = models.EmailField(default='abc@gmail.com', max_length=254, verbose_name='聯絡信箱')
    user_phone = models.CharField(default='0912345678', blank=False, null=False, max_length=20, verbose_name='連絡電話')