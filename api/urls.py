from django.urls import path

from api import views

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('albums',views.AlbumViewsetView,basename='albums')

urlpatterns=[

    path("tracks/<int:pk>/",views.TrackMixinView.as_view()),

    path('register/',views.Userregister.as_view()),

    path("token/",ObtainAuthToken.as_view()),

    path("albums/<int:pk>/review/",views.addReviewView.as_view()),

    path("reviews/<int:pk>/",views.ReviewMixinView.as_view())

]+router.urls