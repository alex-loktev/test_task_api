from django.urls import path
from .views import *

urlpatterns = [
    path('', GetFileView.as_view(), name='upload_file'),
]