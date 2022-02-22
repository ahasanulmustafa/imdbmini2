from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('film_list/', views.Film_list, name='film_list'),
    # path('film_list/<int:pk>', views.Film_list, name='film_details'),
    path('filmlist/', views.LCFilmApi.as_view()),
    path('filmlist/<int:pk>', views.RUDFilmAPI.as_view()),
    path('castlist/', views.LcCastAPI.as_view()),
    path('castlist/<int:pk>', views.RudCastAPI.as_view()),
    path('profilelist/', views.LcProfileAPI.as_view()),
    path('profilelist/<int:pk>', views.RudProfileAPI.as_view()),
    path('castmovie/<int:pk>', views.CastMovieListApi.as_view()),
    path('castupcoming/<int:pk>', views.CastUpcomingMovieApi),

]
