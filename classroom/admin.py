from django.contrib import admin
from classroom.models import *
# Register your models here.


@admin.register(AgeGroup)
class AgeGroup(admin.ModelAdmin):
    list_display = ('age_group', 'is_active')

# @admin.register(WeekDays)
# class WeekDay(admin.ModelAdmin):
#     list_display = ('day')    
@admin.register(BookDemo)
class BookDemoAdmin(admin.ModelAdmin):
    list_display = ('application_id', 'name', 'phone', 'age_group', 'date', 'time')
@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'is_active')
 
admin.site.register(ClassRoom)
admin.site.register(ClassRoomType)
admin.site.register(Room)


"""
@admin.register(ClassRoomSchedule)    
class ClassRoomScheduleAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'time_slot') 


@admin.register(DemoClassFeedBack)
class DemoClassFeedBackAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'student', 'trainer', 'topic', 'technical', 'expression')


@admin.register(ClassStudentFeedBack)
class ClassStudentFeedBackAdmin(admin.ModelAdmin):
    list_display = ('classroom_id', 'student', 'trainer', 'pronunciation', 'grammar_expression', 'confidence', 'fluency', 'content', 'watch_time', 'notes')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'attendance_date')    

@admin.register(AttendanceReport)    
class AttendanceReport(admin.ModelAdmin):
    list_display = ('student_id', 'attendance_id', 'status')

    
"""


admin.site.register(ClassRoomAttendance)