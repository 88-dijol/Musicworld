from django.shortcuts import render

from rest_framework.response import Response

from api.models import Album,Tracks,Review

from api.serializers import AlbumSerializer,TrackSerializer,Registration,ReviewSerializer

from rest_framework import status

from rest_framework import authentication,permissions

from api.permission import OwnerOnly

from rest_framework.decorators import action

from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from rest_framework.generics import RetrieveUpdateDestroyAPIView




class AlbumViewsetView(ModelViewSet):

    queryset=Album.objects.all()
    
    serializer_class=AlbumSerializer


    @action(methods=["post"],detail=True)

    def add_tracks(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance=Album.objects.get(id=id)

        serializer=TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)

            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        
        else:

            return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    

class TrackMixinView(RetrieveUpdateDestroyAPIView):

    queryset=Tracks.objects.all()

    serializer_class=TrackSerializer

# =====================================================reg

class Userregister(APIView):

    def post(self,request,*args,**kwargs):

        serializer=Registration(data=request.data)

        if serializer.is_valid():

            serializer.save()

        return Response(serializer.data)



# review

class addReviewView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance=Album.objects.get(id=id)

        serializer=ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance,user=request.user)

            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        
        else:

            return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)


class ReviewMixinView(RetrieveUpdateDestroyAPIView):

    queryset=Review.objects.all()

    serializer_class=ReviewSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

