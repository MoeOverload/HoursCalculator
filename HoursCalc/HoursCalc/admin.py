from django.contrib import admin
from .models import single_day

@admin.register(single_day)
class SingleDayAdmin(admin.ModelAdmin):
    list_display = ('day_date', 'job_name', 'start_time', 'end_time', 'day_hours')
    list_filter = ('day_date', 'job_name')
    search_fields = ('job_name', 'user_notes')
