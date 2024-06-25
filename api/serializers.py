from rest_framework import serializers

from api.models import Album,Tracks,Review,User


class Registration(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['id','username','email','password','first_name','last_name']

        read_only_fields=['id']
        
    #serializer.save--nn to encrypt the password we use create method with prameters(self,validated dat)---also method overriding is taking place in this create method
    def create(self,validated_data):

        return User.objects.create_user(**validated_data)


class TrackSerializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Tracks

        fields="__all__"

        read_only_fields=["id","album","created_date","update_date","is_active"]

class ReviewSerializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    user=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Review

        fields="__all__"

        read_only_fields=["id","album","user","created_date","update_date","is_active"]


class AlbumSerializer(serializers.ModelSerializer):

    tracks_count=serializers.CharField(read_only=True)

    tracks=TrackSerializer(many=True,read_only=True)

    reviews=ReviewSerializer(many=True,read_only=True)

    class Meta:

        model=Album

        fields="__all__"

        read_only_fields=["id","created_date","update_date","is_active"]


