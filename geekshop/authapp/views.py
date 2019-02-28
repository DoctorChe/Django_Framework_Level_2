from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import auth


from django.core.mail import send_mail
from django.conf import settings

from authapp.models import ShopUser


def user_login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            # next = request.POST['next'] if 'next' in request.POST.keys() else ''
            if user:
                login(request, user)
                if 'next' in request.POST.keys():
                # if 'next' in request.POST.keys() and request.POST['next']:
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main:index'))
    else:
        login_form = ShopUserLoginForm()

    context = {
        'page_title': 'login',
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def user_register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение для подтверждения регистрации отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения для подтверждения регистрации')
                return HttpResponseRedirect(reverse('auth:login'))
            # register_form.save()
            # return HttpResponseRedirect(reverse('main:index'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'page_title': 'registration',
        'register_form': register_form,
    }
    return render(request, 'authapp/register.html', context)


def user_edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {
        'page_title': 'edit',
        'edit_form': edit_form
    }

    return render(request, 'authapp/edit.html', content)


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} \
    на портале {settings.DOMAIN_NAME} перейдите по ссылке: \
    \n{settings.DOMAIN_NAME}{verify_link}'

    print(f'from: {settings.EMAIL_HOST_USER}, to: {user.email}')
    return send_mail(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f'user {user} is activated')
            user.is_active = True
            user.save()
            auth.login(request, user)

            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')

    except Exception as e:
        print(f'error activation user : {e.args}')

    # return HttpResponseRedirect(reverse('main'))
    return HttpResponseRedirect(reverse('main:index'))
