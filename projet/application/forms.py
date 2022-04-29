from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AvionForm(ModelForm):
    class Meta:
        model = models.Avion
        fields = ('nom', 'fabriquant', 'date_production', 'nombre_avion','resume')
        labels = {
            'nom' : _('Nom'),
            'fabriquant' : _('Fabriquant') ,
            'date_production' : _('date de production'),
            'nombre_avion' : _('nombres avion'),
            'resume' : _('Résumé')
        }
        localized_fields = ('date_parution',)
