from django.urls import path

from newsletter_module import component_views


urlpatterns = [
    path('subscribe-newsletter/', component_views.SubscribeView.as_view(), name='subscribe_newsletter'),
]