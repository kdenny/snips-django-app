from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Entity)
admin.site.register(EntityRecord)
admin.site.register(Synonym)
admin.site.register(Intent)
admin.site.register(Utterance)
admin.site.register(EntitySlot)