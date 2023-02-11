from django.urls import path

from bot.views import VerificationViews

urlpatterns = [

   path('verify', VerificationViews.as_view(), name='bot_verify_partial_update'),

]
