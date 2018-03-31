

from django.contrib import admin
from .models import Complaints,Poll,Lecturer
# Register your models here.
admin.site.register(Complaints)
admin.site.register(Poll)
admin.site.register(Lecturer)