from django import forms

class SelectLogForm(forms.Form):
    LOG_1 = 'log_1'
    LOG_2 = 'log_2'
    LOG_3 = 'log_3'
    LOG_4 = 'log_4'
    LOG_5 = 'log_5'
    LOG_6 = 'log_6'
    LOG_7 = 'log_7'
    LOG_8 = 'log_8'
    LOG_9 = 'log_9'
    LOG_CHOICES = (
        (LOG_1, u"Helpdesk"),
        (LOG_2, u"BPI 2012 complete"),
        (LOG_3, u"BPI 2012 W sub-process"),
        (LOG_4, u"BPI 2013 complete"),
        (LOG_5, u"BPI 2015-1"),
        (LOG_6, u"BPI 2015-2"),
        (LOG_7, u"BPI 2015-3"),
        (LOG_8, u"BPI 2015-4"),
        (LOG_9, u"BPI 2015-5"),
    )
    log = forms.ChoiceField(choices=LOG_CHOICES)