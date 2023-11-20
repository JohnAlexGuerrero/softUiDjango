from django import forms
from apps.models import Profile
from django.contrib.auth.models import User

class PerfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','email','link','slug']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3','placeholder':'Enlace'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-3','placeholder':'Slug'}),
            'email': forms.TextInput(attrs={'class': 'form-control mt-3','placeholder':'Email'})
        }
    
class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control mt-3'}),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            raise forms.ValidationError(u'El email ya esta registrado, prueba con otro.')
        return email
    
    def get_form(self, form_class=None):
        form = super(EmailForm, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mt-3', 'placeholder':'Email'})
        return form