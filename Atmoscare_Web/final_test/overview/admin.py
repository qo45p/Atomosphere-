from django.contrib import admin

# Register your models here.
from .models import userHealthRecord,weatherPicture,lonLatData,suggestions

admin.site.register(userHealthRecord)
admin.site.register(weatherPicture)
admin.site.register(lonLatData)
admin.site.register(suggestions)