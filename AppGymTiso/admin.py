from django.contrib import admin
from .models import (
    Clases, 
    ClasesAlumnos,
    RegistroInstructores,
)

admin.site.register(Clases),
admin.site.register(ClasesAlumnos),
admin.site.register(RegistroInstructores),

# Register your models here.
