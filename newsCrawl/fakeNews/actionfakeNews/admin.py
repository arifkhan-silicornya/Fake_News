from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Fake_NEWS
from .models import Authenticate_NEWS

admin.site.register(Fake_NEWS)
admin.site.register(Authenticate_NEWS)