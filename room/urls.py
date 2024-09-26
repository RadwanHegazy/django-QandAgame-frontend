from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:room_number>/', views.GetRoom.as_view(),name='room'),
    path('start/<int:room_number>/', views.StartRoom.as_view(),name='start_room'),

]