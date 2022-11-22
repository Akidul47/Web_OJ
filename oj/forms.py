from django.forms import ModelForm
from .models import CompilerModel


class CompilerModelForm(ModelForm):
    """Form definition for CompilerModel."""

    class Meta:
        """Meta definition for CompilerModelform."""

        model = CompilerModel
        fields = ('code',)
