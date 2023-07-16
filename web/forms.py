from django import forms

from .models import GetInTouch


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = "__all__"
