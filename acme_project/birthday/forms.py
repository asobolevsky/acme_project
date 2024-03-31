from django import forms
from .models import Birthday
from django.core.exceptions import ValidationError


BEATLES = {'джон леннон', 'пол маккартни', 'джордж харрисон', 'ринго старр'}


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        # Вызов родительского метода clean с констрейтами
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if f'{first_name} {last_name}'.lower() in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
