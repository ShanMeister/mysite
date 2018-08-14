from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_category', 'project_picture', 'project_description', 'project_duration',
                  'project_goal', 'user_name', 'user_email', 'user_phone']
