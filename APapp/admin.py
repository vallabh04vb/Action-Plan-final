from django.contrib import admin
from . import models
from APapp.models import UserAccount, UserMessage
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(UserAccount)


@admin.register(UserAccount)
class Acc (ImportExportModelAdmin):
  pass

@admin.register(UserMessage)
class Acc (ImportExportModelAdmin):
  pass