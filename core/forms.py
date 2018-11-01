from django import forms
from .models import Project, TransactionModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class GetHash(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['txHash_deploy']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_category', 'project_picture', 'project_description', 'project_duration',
                  'project_goal', 'user_name', 'user_email', 'user_phone', 'benefactor_wallet_address',
                  'project_passFlag', 'project_completeFlag', 'txHash_deploy', 'Contract_address']


class TransactionModelForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = {'project', 'user', 'feedback_money', 'feedback_description', 'backer_wallet_address', 'txHash_pledge'}


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='請輸入有效的電子信箱，someone@example.com', label='電子信箱')

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

    #def __init__(self, args, *kwargs):
     #   super(SignUpForm, self).__init__(*args, **kwargs)
      #  self.fields['username'].label = '帳號'
       # for field in self.fields.values():
        #    field.widget.attrs['class'] = 'form-control'
         #   if not field.help_text:
          #      field.help_text = '請輸入您的{label}'.format(label=field.label)

    def is_valid(self):
        valid = super(SignupForm, self).is_valid()
        if valid and User.objects.filter(email=self.cleaned_data['email']).exists():
            self._errors[forms.forms.NON_FIELD_ERRORS] = self.error_class(['此信箱已註冊過帳號'])
            valid = False
        return valid
