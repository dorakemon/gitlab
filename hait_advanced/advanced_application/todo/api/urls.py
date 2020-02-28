from django.urls import path
from todo.api.views import (GroupDetailAPIView, 
                            GroupListAPIView, 
                            ContentDetailAPIView,
                            ContentCreateAPIView,
                            ContentRUDAPIView)

urlpatterns = [
    path("group/", GroupListAPIView.as_view(), name="group-detail"),
    path("group/<int:pk>/", GroupDetailAPIView.as_view(), name="group-detail"),
    path("group/<int:pk>/content/", ContentDetailAPIView.as_view(), name="content-detail"),
    path("content/", ContentCreateAPIView.as_view(), name="content"),
    path("content/<str:uuid>/", ContentRUDAPIView.as_view(), name="content-detail")
]