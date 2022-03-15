from django.urls import path
from api.views import FizzBuzzView

app_name = "api"

urlpatterns = [
    path("fizzbuzz", FizzBuzzView.as_view()),
    path("fizzbuzz/<int:pk>", FizzBuzzView.as_view())
]