'''
Created on 3 нояб. 2015 г.

@author: way
'''

from django.contrib.auth.forms import UserCreationForm


## Стандартная форма регистрации без полей подсказок.
class RussianUserCreationForm(UserCreationForm): 
    def __init__(self, *args, **kwargs):
        super(RussianUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    