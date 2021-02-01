from django.contrib import admin   

# Register your models here.
from .models import Poll,SimplePoll


admin.site.register(Poll)
admin.site.register(SimplePoll)