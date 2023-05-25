from django.http import HttpResponse
from img_app.forms import RegForm, RegWorkerForm, AuthForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, WorkerPorfile

def auth(request):
    context = {}
    if request.method == 'POST':
        form = AuthForm(request.POST)
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            context = {'error': 'Неверное имя пользователя или пароль'}
           
    else:
        form = AuthForm()
    print(context)
    context['form'] = form
    return render(
        request,
        'log-in.html',
        context=context
    )

def main(request):
    context = {}

    return render(
        request,
        'index.html',
        context=context
    )

def register(request):
    context = {}
    form = RegForm()
    form_work = RegWorkerForm()
    if request.method == 'POST':
        if 'inn' in request.POST:
            form = RegWorkerForm(request.POST)
        else:
            form = RegForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if isinstance(form, RegWorkerForm):
                instance.inn = form.cleaned_data['inn']
                instance.city = form.cleaned_data['city']
            form.save()
            return redirect('auth')
        else:
            print(form.errors.as_data())
    context['form'] = form
    context['form_work'] = form_work
    return render(request, 'registration.html', context=context)

def logout_user(request):
    logout(request)


# def recovery(request):
#     context = {'title':'Восстановление\nпароля'}
#     form = PasswordResetForm()
#     if request.method == 'POST':    
#         if 'login' in request.POST:
#             form = PasswordResetForm(request.POST)
#             if form.is_valid():
#                 login = form.cleaned_data.get('login')
#                 user = User.objects.get(username=login)
#                 email = user.email
#                 email_to_user = email[:len(email)//2] + len(email)//2 * '*'
#                 context['email'] = f'Мы отправили SMS с кодом на\nпочту <b>{email_to_user}</b>'
#                 context['title'] = 'Код\nподтверждения'
#                 context['title_class'] = 'code-recovery'
#                 form = RecoveryCode()
#                 recovery = RecoveryInfo(login, email)
#                 recovery.recovery_password()
#                 request.session['code'] = recovery.code_recovery
#                 request.session['email'] = f'Мы отправили SMS с кодом на\nпочту <b>{email_to_user}</b>'
#                 request.session['login'] = login
#                 request.session['title'] = 'Код\nподтверждения'
#             else:
#                 pass
#         if 'recovery_code' in request.POST:
#             form = RecoveryCode(request.POST)
#             if form.is_valid():
#                 code = request.session.get('code')
#                 code_user_input = form.cleaned_data.get('recovery_code')
#                 if code == code_user_input:
#                     request.session.pop('email', None)
#                     context['email'] = 0
#                     context['success'] = 1
#                     context.pop('email', None)
#                     form = PasswordConfirm()    
#                 else:
#                     context['email'] = request.session.get('email')
#                     context['title'] = request.session.get('title')
#                     context['error_code'] = 'Неверный код'
        
#         if 'password1' in request.POST:
#             request.session['success'] = 1
#             form = PasswordConfirm(request.POST)
#             if form.is_valid():
#                 user = User.objects.get(username=request.session.get('login'))
#                 user.set_password(form.cleaned_data)
#                 user.save()
#                 return redirect('auth')
#             else:
#                 context['success'] = 1
        
#     context['form'] = form
#     return render(
#         request,
#         'recovery.html',
#         context=context
#     )

# def profile(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     context = {'user_profile': user_profile}
#     return render(request, 'profile.html', context)

# def edit_profile(request):
#     context = {}
#     user_profile = request.user.userprofile
#     parts = str(user_profile.birthday).split('.')
#     new_date_str = '-'.join(reversed(parts))
#     user_profile.birthday = new_date_str
#     form = ProfileEditor(instance=user_profile)
#     if request.method == 'POST':
#         form = ProfileEditor(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             print('Успешно')
#             print(user_profile.avatar)
#         else:
#             print(form.errors)
#     context['user_profile'] = user_profile
#     context['form'] =  form
#     return render(request, 'edit_profile.html', context)
