from django.urls import path
from app.views import SampleAPIView, DateTimeView, UserView

urlpatterns = [
    path("sample/", SampleAPIView.as_view(), name="sample"),
    path("datetime/", DateTimeView.as_view(), name="datetime"),
]