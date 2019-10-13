from django import forms

class SelectLogForm(forms.Form):
    LOG_1 = 'Helpdesk'
    LOG_2 = 'BPI 2012 complete'
    LOG_3 = 'BPI 2012 W sub-process'
    LOG_4 = 'BPI 2013 complete'
    LOG_5 = 'BPI 2015-1'
    LOG_6 = 'BPI 2015-2'
    LOG_7 = 'BPI 2015-3'
    LOG_8 = 'BPI 2015-4'
    LOG_9 = 'BPI 2015-5'
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

class SelectTrainedModelForm(forms.Form):
    TRAINED_MODEL_1 = 'Trained Model 1'
    TRAINED_MODEL_2 = 'Trained Model 2'
    TRAINED_MODEL_CHOICES = (
        (TRAINED_MODEL_1, u"Trained Model 1"),
        (TRAINED_MODEL_2, u"Trained Model 2"),
    )
    trained_model = forms.ChoiceField(choices=TRAINED_MODEL_CHOICES)

class SelectPostProcessingTechniqueForm(forms.Form):
    POSTPROCESSING_TECHNIQUE_1 = 'Arg. Max'
    POSTPROCESSING_TECHNIQUE_2 = 'Random Choice'
    POSTPROCESSING_TECHNIQUE_CHOICES = (
        (POSTPROCESSING_TECHNIQUE_1, u"Arg. Max"),
        (POSTPROCESSING_TECHNIQUE_2, u"Random Choice"),
    )
    post_processing_technique = forms.ChoiceField(choices=POSTPROCESSING_TECHNIQUE_CHOICES)