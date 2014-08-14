from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField()

    def send_email(self):
    	# TODO(a.frolovskiy): make and send message
    	print self.cleaned_data
