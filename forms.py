from django import forms

FAILURES = (
    ('', 'Select...'),
    ('1', '1 years'),
    ('2', '2 years'),
    ('3', '3 years'),
    ('4', '4 years & more'),
    ('5', 'never')
)


SEX = (
    ('', 'Select...'),
    ('0', 'men'),
    ('1', 'women')
)

NIVEAU = (
    ('', 'Select...'),
    ('1', 'Illiterate'),
    ('2', 'Primary'),
    ('3', 'Middle School'),
    ('4', 'High School'),
    ('5', 'Higher Education')
)

FAMILLE = (
    ('', 'Select...'),
    ('1', 'Very Poor'),
    ('2', 'Poor'),
    ('3', 'Fair'),
    ('4', 'Good'),
    ('5', 'Excellent')
)
ABSENCE = (
    ('', 'Select...'),
    ('1', 'Less than 5'),
    ('2', 'Between 6 and 10'),
    ('3', 'Between 11 and 15'),
    ('4', 'More than 16')
)

Age = (
    ('', 'Select...'),
    ('1', 'Less than 15'),
    ('2', 'Between 15 and 16'),
    ('3', 'Between 16 and 17'),
    ('4', 'Between 17 and 18'),
    ('5', 'More than 18')
)

TRAVAIL = (
    ('', 'Select...'),
    ('1', 'Teacher'),
    ('2', 'Healthcare'),
    ('3', 'Public Services'),
    ('4', 'At Home'),
    ('5', 'Other')
)

GOOUT = (
    ('', 'Select...'),
    ('1', 'Very Little'),
    ('2', 'Little'),
    ('3', 'Fair'),
    ('4', 'A Lot'),
    ('5', 'A Great Deal')
)
HEURES = (
    ('', 'Select...'),
    ('0', 'No'),
    ('1', 'Yes')
)
CHOIX = (
    ('', 'Select...'),
    ('1', 'Close to Home'),
    ('2', 'Reputation'),
    ('3', 'Course Quality'),
    ('4', 'Other')
)

SCHOOLSUP = (
    ('', 'Select...'),
    ('0', 'Yes'),
    ('1', 'No')
)

class myForm(forms.Form):
    name = forms.CharField(max_length=100)
    sex = forms.ChoiceField(choices=SEX)
    failure = forms.ChoiceField(choices=FAILURES)
    fedu = forms.ChoiceField(choices=NIVEAU)
    schoolsup = forms.ChoiceField(choices=SCHOOLSUP)
    medu = forms.ChoiceField(choices=NIVEAU)
    goout = forms.ChoiceField(choices=GOOUT)
    freetime = forms.ChoiceField(choices=GOOUT)
    mjob = forms.ChoiceField(choices=TRAVAIL)
    fjob = forms.ChoiceField(choices=TRAVAIL)
    raison = forms.ChoiceField(choices=CHOIX)
    relation_familiale = forms.ChoiceField(choices=FAMILLE)
    absences = forms.ChoiceField(choices=ABSENCE)
    age = forms.ChoiceField(choices=Age)
    consomation_alcool = forms.ChoiceField(choices=GOOUT)
    sante = forms.ChoiceField(choices=FAMILLE)
"""   new_row = {'Medu': [Medu], 'Fedu': [Fedu], 'famrel': [famrel], 'freetime': [freetime], 'goout': [goout],'Walc': [Walc],
               'health': [health], 'Age': [Age],'Absences': [Absences],'Mjob': [Mjob],'Fjob': [Fjob],'reason': [reason]}"""
