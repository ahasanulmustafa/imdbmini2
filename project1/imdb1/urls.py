from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('film_list/', views.Film_list, name='film_list'),
    # path('film_list/<int:pk>', views.Film_list, name='film_details'),
    path('filmlist/', views.FilmListCreate.as_view()),
    path('filmlist/<int:pk>', views.FilmRetrieveUpdateDelete.as_view()),
    path('castlist/', views.CastListCreate.as_view()),
    path('castlist/<int:pk>', views.CastRetrieveUpdateDestroy.as_view()),
    path('profilelist/', views.ProfileListCreate.as_view()),
    path('profilelist/<int:pk>', views.ProfileRetrieveUpdateDestroy.as_view()),
    path('castmovie/<int:pk>', views.CastMovieListApi.as_view()),
    path('castupcoming/<int:pk>', views.CastUpcomingMovieApi.as_view()),

]
