from django.urls import path
from mysns.views import SampleTemplateView

urlpatterns = [
    path('sample', SampleTemplateView.as_view()),
]