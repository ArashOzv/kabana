from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout

from user_module.froms import LoginForm, SignupForm
from user_module.models import CustomUser
# Create your views here.


class SignUpView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_page')
        sign_up_form = SignupForm()
        context = {
            'sign_up_form': sign_up_form,
        }
        
        return render(request, 'signup.html', context)
    
    def post(self, request):
        sign_up_form = SignupForm(request.POST)
        if sign_up_form.is_valid():
            username = sign_up_form.cleaned_data['username']
            password = sign_up_form.cleaned_data['password']
            if CustomUser.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'sign_up_form': sign_up_form, 'error': 'این نام کاربری قبلا ثبت شده است'})
            user = CustomUser.objects.create(
                username=username,
                password=password,
                is_active = False
            )
            user.save()
            #todo:
            # send email
            # send sms
            return redirect('home_page')
        else:
            context = {
                'sign_up_form': sign_up_form,
                'error': 'لطفا فرم را به درستی پر کنید',
            }
            return render(request, 'signup.html', context)



class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home_page')
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }
        
        return render(request, 'login.html', context)


    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = CustomUser.objects.filter(username=username)
            if not user.exists():
                context = {
                    'login_form' : login_form,
                    'error' : 'شماره یا رمز عبور صحیح نمیباشد'
                }
                return render(request, 'login.html', context)
            if user.first().check_password(password):
                login(request, user.first())
                return redirect('home_page')
            else:
                context = {
                    'login_form' : login_form,
                    'error' : 'شماره یا رمز عبور صحیح نمیباشد'
                }
                return render(request, 'login.html', context)
            
        else:
            print('not_valid')
            context = {
                    'login_form' : login_form,
                    'error' : 'شماره یا رمز عبور صحیح نمیباشد'
                }
            return render(request, 'login.html', context)