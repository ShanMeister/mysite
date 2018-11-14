from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .models import Project, TransactionModel, FeedbackModel
from django.contrib import messages
from .forms import ProjectForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, TransactionModelForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import auth
from .tokens import Token
from django.conf import settings as django_settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import UserPassesTestMixin  # 瀏覽權限
from django.shortcuts import get_object_or_404
import datetime

token_confirm = Token(django_settings.SECRET_KEY.encode())


# Create your views here.

def home(request):
    object_list = Project.objects.all()
    return render(request, 'home2.html', {'object_list': object_list})


def testDeploy(request):
    return render(request, 'testDeploy.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def blockchainTest(request):
    return render(request, 'blockchainTest.html')


class ProjectAdmin(UserPassesTestMixin, ListView):
    model = Project
    template_name = 'project_admin.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 10)

    def get_context_data(self, **kwargs):
        context = super(ProjectAdmin, self).get_context_data(**kwargs)
        context['paginate_by'] = self.get_paginate_by(context['object_list'])
        context['paginate_list'] = [10, 25, 50, 100]

        if context.get('is_paginated', False):
            paginator = context.get('paginator')
            context['num_pages'] = num_pages = paginator.num_pages
            current_page = context.get('page_obj')
            page_no = current_page.number

            if num_pages <= 5:
                pages = [x for x in range(1, num_pages + 1)]
            elif page_no < 3:
                pages = [x for x in range(1, 6)]
            elif page_no > num_pages - 2:
                pages = [x for x in range(num_pages - 5 + 1, num_pages + 1)]
            else:
                pages = [x for x in range(page_no - 2, page_no + 3)]

            context.update({'pages': pages})
        return context


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


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project_display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['percent'] = '{}%'.format(int((self.object.project_gain / self.object.project_goal) * 100))
        except ZeroDivisionError:
            context['percent'] = '0%'
        return context


class ProjectList(ListView):
    model = Project
    template_name = 'project_list.html'


class ProjectCreate(CreateView):
    # first way
    # model = Project
    # fields = fields = ['projec+t_name', 'project_category', 'project_picture', 'project_description', 'project_duration', 'project_goal', 'project_contact']
    template_name = 'project_create.html'
    form_class = ProjectForm

    def form_valid(self, form):
        self.object = form.save()
        # Create Feedback
        moneylist = self.request.POST.getlist('feedback_money')
        descriptionlist = self.request.POST.getlist('feedback_description')

        for money, description in zip(moneylist, descriptionlist):
            feedback = FeedbackModel(feedback_money=money, feedback_description=description, project=self.object)
            feedback.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        print(self.get_form())
        return context

    def get_success_url(self):
        messages.success(self.request, '已新增')
        return reverse('home')


def signup2(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            token = token_confirm.generate_validate_token(user.username)
            url = '/'.join(['127.0.0.1:8000', 'activate', token])

            message = "\n".join(['親愛的 {}，您好：'.format(user.username),
                                 '感謝您註冊MySite會員',
                                 '請點擊下面連結以完成帳號驗證：',
                                 url])
            send_mail('MySite  註冊帳號驗證訊息',
                      message,
                      django_settings.EMAIL_HOST_USER,
                      [user.email])
            messages.success(request, '請登錄到註冊信箱中驗證帳號，有效期為1個小時')
            return redirect('login')
    return render(request, 'signup2.html', {'form': form})


def project_donate(request, pk):
    if request.method == 'POST':
        form = TransactionModelForm(request.POST)
        if form.is_valid():
            form.save()
            # project = form.cleaned_data.get('project')
            # user = form.cleaned_data.get('user')
            # feedback_money = form.cleaned_data.get('feedback_money')
            # feedback_description = form.cleaned_data.get('feedback_description')
            # backer_wallet_address = form.cleaned_data.get('backer_wallet_address')
            # txHash_pledge = form.cleaned_data.get('txHash_pledge')
            messages.success(request, '交易成功!')
            return reverse('home')
        else:
            messages.error(request, form.errors)
            return reverse('home')
    else:
        project = get_object_or_404(Project, pk=pk)
        #thing = project.feedbackmodel_set.all()
        return render(request, 'project_donate.html', {'project': project})


def activate(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        username = token_confirm.remove_validate_token(token)
        users = User.objects.filter(username=username)
        for user in users:
            if not user.is_active:
                user.delete()
        messages.error(request, '對不起，驗證連結已過期，請重新註冊')
        return render(request, 'signup2.html')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, '對不起，您所驗證的帳號不存在，請重新註冊')
        return render(request, 'signup2.html')
    user.is_active = True
    user.save()
    messages.success(request, '驗證成功，請進行登入操作')
    return redirect('login')


def project_update_deploy(request):
    if request.method == "POST":
        pk = request.POST.get('pk')
        txHash_deploy = request.POST.get('txHash_deploy')
        contractaddr_deploy = request.POST.get('contractaddr_deploy')
        project = get_object_or_404(Project, pk=pk)
        project.txHash_deploy = txHash_deploy
        project.Contract_address = contractaddr_deploy
        project.project_passFlag = 'True'
        project.save()
    return redirect('project_admin')


def project_update_drawdown(request):
    if request.method == "POST":
        pk = request.POST.get('pk')
        project = get_object_or_404(Project, pk=pk)
        project.project_completeFlag = 'True'
        project.save()
        messages.success(request, 'drawdown成功!')
    else:
        messages.warning(request, 'drawdown失敗!')
    return redirect('project_admin')