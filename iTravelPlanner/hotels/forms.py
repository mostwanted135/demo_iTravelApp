from django import forms

INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 6)]

class GetHotelDetails(forms.Form):
    entercity = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input100',
            'onfocus': 'this.placeholder = ''',
            'onblur': "this.placeholder = 'Enter city'",
            'placeholder': "Enter city",
        }
    ))

    checkindate = forms.DateField(widget=forms.TextInput(
        attrs={
            'id': 'datepicker1',
            'placeholder': '08/01/2020',
        }
    ))

    checkoutdate = forms.DateField(widget=forms.TextInput(
        attrs={
            'id': 'datepicker2',
            'placeholder': '08/01/2020',
        }
    ))

    adultcount = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES,
                                                        attrs={
                                                            'name': 'select',
                                                            'id': 'select1'
                                                        }))

    childcount = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES,
                                                        attrs={
                                                            'name': 'select',
                                                            'id': 'select1'
                                                        }))

    roomcount = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES,
                                                        attrs={
                                                            'name': 'select',
                                                            'id': 'select3'
                                                        }))

