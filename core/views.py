from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .models import Project
from django.contrib import messages
from .forms import ProjectForm
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
)
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    print(form)
    return render(request, 'signup.html', {'form': form})


class ProjectCreate(CreateView):
    #first way
    #model = Project
    #fields = fields = ['project_name', 'project_category', 'project_picture', 'project_description', 'project_duration', 'project_goal', 'project_contact']
    template_name = 'project_create.html'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        print(self.get_form())
        return context

    def get_success_url(self):
        messages.success(self.request, '已新增')
        return reverse('home')






