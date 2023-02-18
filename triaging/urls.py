from django.urls import path

from triaging.views import *

urlpatterns = [
  path('hello', hello, name="hello_world"),
  path('feature-color', triagingView, name="triaging"),

]
