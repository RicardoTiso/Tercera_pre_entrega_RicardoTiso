from django.urls import path
from AppGymTiso.views import (
    inicio,
    enConstruccion,
    alumnos,
    instructores,
    lista_clases,
    registro_clases,
    desafios,
    masPowerNutricion,
    masPowerRutinas,
    masPowerSeguimiento,     
    clases_Form,
    registro_Form
)

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('enConstruccion/', enConstruccion, name='enConstruccion'),
    path('alumnos/', alumnos, name='Alumnos'),
    path('instructores/', instructores, name='Instructores'),
    path('clases/', lista_clases, name='lista_clases'),
    path('registroClases/', registro_clases, name='registro_clases'),    
    path('desafios/', desafios, name='Desafios'),
    path('MP_Rutinas/', masPowerRutinas, name='masPowerRutinas'),
    path('MP_Nutricion/', masPowerNutricion, name='masPowerNutricion'),
    path('MP_Seguimiento/', masPowerSeguimiento, name='masPowerSeguimiento'),
    path('clases_Form/', clases_Form, name='clasesForm'),
    path('registro_Form/', registro_Form, name='registroForm'),

]