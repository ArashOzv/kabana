from django.shortcuts import redirect, render
from django.views import View

from newsletter_module.forms import SubscribeForm
from newsletter_module.models import Newsletter




class SubscribeView(View):
    def get(self, request):
        subscribe_form = SubscribeForm()
        context = {
            'subscribe_form': subscribe_form
        }
        return render(request, 'components/subscribe_newsletter.html', context)


    def post(self, request):
        user = request.user
        if user.is_authenticated:
            subscribe_form = SubscribeForm(request.POST)
            if subscribe_form.is_valid():
                email = subscribe_form.cleaned_data['email']
                if not Newsletter.objects.filter(email=email).exists():
                    Newsletter.objects.create(user=user, email=email)
                    ### send email
                    return redirect('home_page')
                else:
                    context = {
                        'subscribe_form': subscribe_form,
                        'error': 'این ایمیل قبلا ثبت شده است.'
                    }
                    return render(request, 'components/subscribe_newsletter.html', context)
            else:
                context = {
                    'subscribe_form': subscribe_form,
                    'error': 'اطلاعات را صحیح پر کنید'
                }
                return render(request, 'components/subscribe_newsletter.html', context)
        else:
            return redirect('login')