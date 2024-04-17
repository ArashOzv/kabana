from django.urls import path
from user_module import views
from order_module.views import CartView, add_to_cart
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    # path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('cart/', CartView.as_view(), name='cart_page'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
]