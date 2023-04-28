from django.urls import path
from classroom import views

app_name = "classroom"


urlpatterns = [
    path('classroom-list', views.ClassRoomList.as_view(), name="classroom-list"),
    path('add-classroom', views.ClassRoomCreateView.as_view(), name="add-classroom"),
    path('add-room', views.RoomCreateView.as_view(), name="add-room"),
    path('<slug>/', views.ClassRoomDetailView.as_view(), name='classroom-detail'),
    path('<classroom_slug>/<room_slug>', views.RoomView.as_view(), name='room-detail'),
    path('time-slot-list', views.TimeSlotListView.as_view(), name="time-slot-list"),
    path('add-time-slot', views.TimeSlotCreateView.as_view(), name="add-time-slot"),
    path('add-age-group', views.AgeGroupCreateView.as_view(), name="add-age-group"),
    path('age-group-list', views.AgeGroupListView.as_view(), name="age-group-list"),
    path('update/<pk>', views.AgeGroupUpdateView.as_view(), name='update-age-group'),
    path('time-slot-list', views.TimeSlotListView.as_view(), name="time-slot-list"),
    path('add-time-slot', views.TimeSlotCreateView.as_view(), name="add-time-slot"),
    # path('classroom-list', views.classroomlist, name="classroom-list")
]
