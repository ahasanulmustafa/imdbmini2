from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from .models import Profile, Film, Cast
from .serializers import ProfileSerializer, FilmSerializer, CastSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


def home(request):
    return HttpResponse("Hello Welcome to the IMDB")


def Film_list(request):
    film = Film.objects.all()
    serializer = FilmSerializer(film, many=True)
    return JsonResponse(serializer.data, safe=False)


def Film_details(request, pk):
    details = Film.objects.get(pk=pk),
    serializer = FilmSerializer(details)
    return JsonResponse(serializer.data, safe=False)


# Profile API

class ProfileListCreate(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class LcProfileAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class RudProfileAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Film API

class FilmListCreate(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView)
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


# class LCFilmApi(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class RUDFilmAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# Cast API

class CastListCreate(ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class CastRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


# class LcCastAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Cast.objects.all()
#     serializer_class = CastSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


@permission_classes((permissions.AllowAny,))
class CastMovieListApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            fil = Film.objects.filter(film__profile__user_id=id)
            serializer = FilmSerializer(fil, many=True)
            return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class CastUpcomingMovieApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            fil = Film.objects.filter(film__profile__user_id=id).filter(is_released=False)
            serializer = FilmSerializer(fil, many=True)
            return Response(serializer.data)


# class RudCastAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Cast.objects.all()
#     serializer_class = CastSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

