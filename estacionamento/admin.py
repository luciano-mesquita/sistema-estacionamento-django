from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Rotativo

admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Rotativo)
