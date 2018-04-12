from django.contrib import admin
from .models import Articulo, Categoria, Comentario
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Comentario)
