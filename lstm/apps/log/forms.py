from django import forms

class SelectLogForm(forms.Form):
    LOG_1 = 'log_1'
    LOG_2 = 'log_2'
    LOG_CHOICES = (
        (LOG_1, u"Log 1"),
        (LOG_2, u"Log 2")
    )
    logs = forms.ChoiceField(choices=LOG_CHOICES)