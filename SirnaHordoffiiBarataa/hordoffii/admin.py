from django.contrib import admin
from .models import Kutaa, Barataa, Qabxii, Hafittoo

@admin.register(Barataa)
class BarataaAdmin(admin.ModelAdmin):
    list_display = ('maqaa_guutuu', 'kutaa', 'bilbila_maatii')
    search_fields = ('maqaa_guutuu',)

@admin.register(Qabxii)
class QabxiiAdmin(admin.ModelAdmin):
    list_display = ('barataa', 'gosa_barumsaa', 'qabxii_mid', 'qabxii_final')
    list_filter = ('gosa_barumsaa', 'barataa__kutaa')

@admin.register(Hafittoo)
class HafittooAdmin(admin.ModelAdmin):
    list_display = ('barataa', 'guyyaa', 'jira')
    list_filter = ('guyyaa', 'jira')# hordoffii/admin.py keessatti itti dabali
def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(barataa__maqaa_maatii=request.user)