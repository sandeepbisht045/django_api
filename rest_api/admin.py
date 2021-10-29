from django.contrib import admin
from . models import Advisor_details,User,Book_call


# Register your models here.
admin.site.register(Advisor_details)
admin.site.register(User)
admin.site.register(Book_call)

