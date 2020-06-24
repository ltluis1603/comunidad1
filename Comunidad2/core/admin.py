from django.contrib import admin

from .models import Clasificado

# Register your models here.
class clasificadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Clasificado, clasificadoAdmin)