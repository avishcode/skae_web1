from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, View, UpdateView
from classroom.models import *
from classroom.forms import CreateAgeGroupForm, CreateClassRoomForm, BookDemoForm, CreateRoomForm, CreateTimeSlot, UpdateAgeGroupForm
# Create your views here.


class BookDemoCreateView(CreateView):
    model = BookDemo
    form_class = ""
    template_name = "classroom/admin/add_demo.html"
    success_url = ""


class ClassRoomList(ListView):
    model = ClassRoom
    template_name = "classroom/admin/classroom_list.html"

class ClassRoomCreateView(CreateView):
    model = ClassRoom
    form_class = CreateClassRoomForm
    template_name = "classroom/admin/create_classroom.html"
    success_url = "/classroom-list"


class ClassRoomDetailView(DetailView):
    model = ClassRoom
    template_name = "classroom/admin/classroom_detail.html"



class RoomCreateView(CreateView):
    model = Room
    form_class = CreateRoomForm
    template_name = "classroom/admin/create_room.html"
    success_url = "/classroom-detail"


class TimeSlotCreateView(CreateView):
    model = TimeSlot
    form_class = CreateTimeSlot
    template_name = "classroom/admin/create_time_slot.html"
    success_url = "time-slot-list"

class TimeSlotListView(ListView):
    model = TimeSlot
    template_name = "classroom/admin/time_slot_list.html"
    

class AgeGroupCreateView(CreateView):
    model = AgeGroup
    form_class = CreateAgeGroupForm
    template_name = "classroom/admin/create_age_group.html"
    success_url = "age-group-list"


class AgeGroupListView(ListView):
    model = AgeGroup
    template_name = "classroom/admin/age_group_list.html"


class AgeGroupUpdateView(UpdateView):
    model = AgeGroup
    forms = UpdateAgeGroupForm
    template_name = "classroom/admin/update_age_group.html"
    success_url = "age-group-list"

class ClassRoomTypeCreateView(CreateView):
    model = ClassRoomType
    form_class = ""
    template_name = "classroom/admin/create_classroom_type.html"
    success_url = ""


class ClassRoomAttendanceListView(ListView):
    model = ClassRoomAttendance
    template_name = "classroom/admin/class_attendance_list.html"





class RoomView(View):
    def get(self, request, classroom_slug, room_slug, *args, **kwargs):
        classroom_qs = ClassRoom.objects.filter(slug=classroom_slug)
        if classroom_qs.exists():
            classroom = classroom_qs.first()

        room_qs = classroom.rooms.filter(slug=room_slug)
        if room_qs.exists():
            room = room_qs.first()

        context = {
            'object': room
        }
        return render(request, "classroom/admin/room_detail.html", context)
