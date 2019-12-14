#------------------------------------------------------------------------------
# LSTM UI Django Project
# By japoveda10
# forms.py
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from django import forms

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------
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

class SelectRunningCaseForm(forms.Form):
    RUNNING_CASE_1 = 'Running Case 1'
    RUNNING_CASE_2 = 'Running Case 2'
    RUNNING_CASE_3 = 'Running Case 3'
    RUNNING_CASE_4 = 'Running Case 4'
    RUNNING_CASE_CHOICES = (
        (RUNNING_CASE_1, u"Running Case 1"),
        (RUNNING_CASE_2, u"Running Case 2"),
        (RUNNING_CASE_3, u"Running Case 3"),
        (RUNNING_CASE_4, u"Running Case 4"),
    )
    running_case = forms.ChoiceField(choices=RUNNING_CASE_CHOICES)