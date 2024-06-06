from django import forms

class clasesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    fechaDeClase= forms.DateField(
        widget= forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/aaaa',
            }
        ),
        input_formats=['%d/%m/%Y']
    )
    clase= forms.IntegerField()

class registroClasesFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    fechaDeClase= forms.DateField(
        widget= forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/aaaa',
            }
        ),
        input_formats=['%d/%m/%Y']
    )
    clase= forms.IntegerField()
    titulo= forms.CharField()
    reseña = forms.CharField(widget=forms.Textarea)
