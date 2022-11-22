from django.urls import path
from .views import IndexView, SubmitView


urlpatterns = [
    path('', IndexView.as_view()),
    path('thanks/', SubmitView.as_view()),
]