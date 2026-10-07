from django.forms import ModelForm
from .models import Contact, Feedback

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('First_Name','Last_Name','Email','Phone_Number','Message')

class FeedbackForm(ModelForm):
    class Meta:

        def __init__(self, user ,*args, **kwargs):
            super(FeedbackForm, self).__init__(*args, **kwargs)
            user_instance = user
            if user_instance:
                self.fields['User'].initial = user_instance.id

        model = Feedback
        fields = ('Rating','Feedback')

