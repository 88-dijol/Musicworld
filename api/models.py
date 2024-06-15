from django.db import models

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator



class Album(models.Model):

    title=models.CharField(max_length=100)
    
    year=models.CharField(max_length=100)

    director=models.CharField(max_length=100)

    options=(
        ('Malayalam',"Malayalam"),
        ('Hindi','Hindi'),
        ('Tamil','Tamil'),
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
    )
     
    Languages=models.CharField(max_length=100,choices=options,default='English')

    
    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    @property
    def tracks_count(self):

        return Tracks.objects.filter(album=self).count()
    
    @property
    def tracks(self):

        return Tracks.objects.filter(album=self)
    
    @property

    def reviews(self):

        return Review.objects.filter(album=self)


    def __str__(self) -> str:
        return self.title
    


class Tracks(models.Model):

    title=models.CharField(max_length=100)

    singers=models.CharField(max_length=100)

    options=(
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('hiphop', 'Hip Hop'),
        ('blues', 'Blues'),
        ('country', 'Country'),
        ('reggae', 'Reggae'),
        ('folk', 'Folk'),
        ('latin', 'Latin'),
        ('metal', 'Metal'),
    )

    genre=models.CharField(max_length=100,choices=options,default="pop")

    duration=models.DurationField()

    track_num=models.CharField(max_length=100)

    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title
    


class Review(models.Model):

    comment=models.CharField(max_length=200)

    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

