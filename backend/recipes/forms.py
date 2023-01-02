from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Ingridient, Recipe, Tag


class RecipeForm(forms.ModelForm):
    ingridients = forms.ModelMultipleChoiceField(
          queryset=Ingridient.objects.all(),
          required=False,
          widget=FilteredSelectMultiple(
              verbose_name='Ингридиенты',
              is_stacked=False
          )
    )
    tags = forms.ModelMultipleChoiceField(
          queryset=Tag.objects.all(),
          required=False,
          widget=FilteredSelectMultiple(
              verbose_name='Тэги',
              is_stacked=False
          )
    )

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['ingridients'].initial = self.instance.ingridients.all()

    def save(self, commit=True):
        return forms.BaseModelForm.save(self, commit=commit)

    class Meta:
        model = Recipe
        fields = '__all__'

