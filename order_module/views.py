from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from book_module.models import Book
from django.conf import settings
import requests
import json


#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/order/verify/'


# Create your views here.
class CartView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login_page')
        user = request.user
        books_in_cart = user.cart.all()
        context = {
            'user': user,
            'books_in_cart': books_in_cart
        }
        return render(request, 'cart.html', context)
    


def add_to_cart(request, book_id):
    user = request.user
    book = Book.objects.get(id=book_id)
    user.cart.add(book)
    return redirect('cart_page')

def send_request(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response_json = response.json()
            if response_json['Status'] == 100:
                authority = response_json['Authority']
                return redirect(f'https://{sandbox}.zarinpal.com/pg/StartPay/{authority}')
                # return JsonResponse({'status': True, 'url': ZP_API_STARTPAY + str(response_json['Authority']), 'authority': response_json['Authority']})
            else:
                return render(request, 'fail.html')
                # return JsonResponse({'status': False, 'code': str(response_json['Status'])})
        return render(request, 'fail.html')
        # return JsonResponse({'status': False, 'code': 'unexpected_error'})
    
    except requests.exceptions.Timeout:
        return JsonResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return JsonResponse({'status': False, 'code': 'connection_error'})



def verify(request):
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')

    if authority and status == 'OK':
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority": authority,
        }

        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(ZP_API_VERIFY, json=data, headers=headers)
            
            if response.status_code == 200:
                response_json = response.json()
                if response_json['Status'] == 100:
                    return render(request, 'success.html')
                    # return JsonResponse({'status': True, 'RefID': response_json['RefID']})
                else:
                    return render(request, 'fail.html')
                    # return JsonResponse({'status': False, 'code': str(response_json['Status'])})
            return render(request, 'fail.html')
            # return JsonResponse({'status': False, 'code': 'unexpected_error'})
        
        except requests.exceptions.Timeout:
            return JsonResponse({'status': False, 'code': 'timeout'})
        except requests.exceptions.ConnectionError:
            return JsonResponse({'status': False, 'code': 'connection_error'})
    else:
        return render(request, 'fail.html')
        # return JsonResponse({'status': False, 'message': 'Invalid Authority or Status'})
