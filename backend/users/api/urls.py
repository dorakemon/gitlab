from django.urls import path
from users.api.views import CurrentUserAPIView, PlaceListAPIView, PlaceRetrieveAPIView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    #path("university/", UniversityAPIView.as_view(), name="university-list")
    path("place/", PlaceListAPIView.as_view(), name="place-list"),
    path("place/<str:name>/", PlaceRetrieveAPIView.as_view(), name="place-retrieve")
]