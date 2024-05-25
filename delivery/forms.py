from django import forms
from delivery.models import Agent, Pick, ProductOwner


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = "__all__"


class PickForm(forms.ModelForm):
    class Meta:
        model = Pick
        fields = "__all__"

class ProdForm(forms.ModelForm):
    class Meta:
        model = ProductOwner
        fields = "__all__"