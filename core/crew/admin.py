from django.contrib import admin
from . models import Crew, Job, Store, NilaiKriteria

# Register your models here.
admin.site.register(Crew)
admin.site.register(Job)
admin.site.register(Store)
admin.site.register(NilaiKriteria)