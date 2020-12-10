from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('athlete/', views.athlete, name="athlete"),
    path('athlete/<int:pk>', views.athlete_detail, name="athlete_detail"),
    path('record/', views.record, name="record"),
    path('record/<int:pk>', views.record_detail, name="record_detail"),
    path('search/', views.search, name="search"),
    path('rank/', views.rank, name="rank"),
    path('search/result/', views.result, name="result"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)