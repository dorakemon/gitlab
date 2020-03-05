from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import (UserDisplaySerializer, 
                                    PlaceDislaySerializer,
                                    PlaceDislayRetrieveSerializer,
                                    )

from rest_framework import generics
from users.models import Place

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class PlaceListAPIView(generics.ListAPIView):
    serializer_class = PlaceDislaySerializer
    queryset = Place.objects.all()

class PlaceRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PlaceDislayRetrieveSerializer
    queryset = Place.objects.all()
    lookup_field = 'name'