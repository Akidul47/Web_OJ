from django.contrib import admin
from .models import CompilerModel


class CompilerModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(CompilerModel, CompilerModelAdmin)
