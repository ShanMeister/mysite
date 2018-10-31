from django.contrib import admin
from .models import Project, TransactionModel, FeedbackModel
# Register your models here.
admin.site.register(Project)
admin.site.register(FeedbackModel)
admin.site.register(TransactionModel)