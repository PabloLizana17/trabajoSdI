#from Academica.models import Campeones, Items, League, Min, Rol, Sumonerspells, Usuario, league
from django.contrib import admin
from Academica.models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Campeones)
admin.site.register(Items)
admin.site.register(Sumonerspells)
