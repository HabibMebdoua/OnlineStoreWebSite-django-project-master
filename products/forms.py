from django import forms
from .models import Order

class OrderingForm(forms.ModelForm):
 
    zip_code = forms.CharField(widget=forms.NumberInput,required=True)
    phone = forms.CharField(widget=forms.NumberInput,required=True)
    email = forms.CharField(widget=forms.EmailInput,required=True)
    class Meta:
        model = Order
        fields = ('full_name','town','city','zip_code', 'all_adress' , 'phone','email', 'comment')