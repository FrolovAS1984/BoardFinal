from django.shortcuts import render

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.conf import settings
# from django.utils.crypto import get_random_string
# from .forms import UserSignupForm
# from .models import User
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             username = form.cleaned_data['username']
#             verification_code = get_random_string(length=4, allowed_chars="1234567890")
#             user = User.objects.create_user(email=email, password=password, is_verified=False,
#                                             verification_code=verification_code, username=username)
#             subject = 'Подтверждение регистрации'
#             message = f'Ваш код подтверждения: {verification_code}'
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [email, ]
#             send_mail(subject, message, email_from, recipient_list)
#             return redirect('verify_email', email)
#     else:
#         form = UserSignupForm()
#     return render(request, 'signup.html', context={'form': form})
#
#
# def verify_email(request, email):
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         user = None
#     if user and not user.is_verified:
#         if request.method == 'POST':
#             input_code = request.POST.get('verification_code')
#             if input_code == user.verification_code:
#                 user.is_verified = True
#                 user.save()
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 error_message = 'Неверный код подтверждения!'
#                 return render(request, 'verify_email.html', context={'error_message': error_message})
#         else:
#             return render(request, 'verify_email.html')
#     elif user and user.is_verified:
#         error_message = 'Данный аккаунт уже подтверждён!'
#         return render(request, 'verify_email.html', context={'error_message': error_message})
#     else:
#         error_message = 'Неправильный URL или ваш аккаунт не был найден!'
#         return render(request, 'verify_email.html', context={'error_message': error_message})
#
#
# @login_required
# def profile(request):
#     return render(request, 'profile.html')
#_______________________________________________________________________________________________________

