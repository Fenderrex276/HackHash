from django.urls import path, include
from .views import *

urlpatterns = [
    path('crack', Crack.as_view()),
    # path('status/',)
]

