from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('r1', 'art'),
        ('r2', 'music'),
        ('r3', 'game'),
        ('r4', 'computing'),
    )
    project_category = models.CharField(default='r1', max_length=2, choices=CATEGORY_CHOICES, verbose_name='專案類別')
    project_name = models.CharField(default='my project', max_length=50, verbose_name='專案名稱')
    project_description = models.TextField(default='my project', verbose_name='專案敘述')
    project_picture = models.ImageField(blank=False, null=False, upload_to='photos', verbose_name='專案圖片')
    project_duration = models.DateField(default='2099/12/31', verbose_name='專案期限')
    project_goal = models.IntegerField(default=10000, verbose_name='達標金額')

    project_gain = models.IntegerField(default=5000, verbose_name='目前金額')
    user_name = models.CharField(default='user', max_length=15, verbose_name='使用者名稱')
    user_email = models.EmailField(default='abc@gmail.com', max_length=254, verbose_name='聯絡信箱')
    user_phone = models.CharField(blank=True, null=True, default='0912345678', max_length=20, verbose_name='連絡電話')
    benefactor_wallet_address = models.CharField(max_length=50, verbose_name='集資方錢包位置')
    project_passFlag = models.BooleanField(default=False, verbose_name='專案審核')
    project_completeFlag = models.BooleanField(default=True, verbose_name='專案顯示狀態')  # HOME呈現判斷
    txHash_deploy = models.CharField(blank=True, null=True, max_length=100, verbose_name='部屬合約內容')  # 接收合約txhash
    Contract_address = models.CharField(blank=True, null=True, max_length=100, verbose_name='部屬合約位置')  # 接收合約address
    project_totalpeople = models.IntegerField(blank=True, null=True, default=0, verbose_name='投資人數')


class FeedbackModel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feedback_item = models.CharField(default='my feedback item', max_length=30, verbose_name='回饋項目')
    feedback_money = models.IntegerField(default=0, null=False, verbose_name='回饋金額')
    #feedback_money_unit = models.CharField(default='ether', max_length=6, verbose_name='回饋金額單位')
    feedback_description = models.TextField(default='my feedback description', verbose_name='回饋敘述')


class TransactionModel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_money = models.IntegerField(default=0, null=False, verbose_name='回饋金額')
    feedback_description = models.TextField(default='my feedback description', verbose_name='回饋敘述')
    backer_wallet_address = models.CharField(blank=False, null=False, max_length=100, verbose_name='投資方錢包位置')
    txHash_pledge = models.CharField(blank=False, null=False, max_length=100, verbose_name='投資合約內容')









