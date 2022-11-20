from django import forms
from .models import User, MercuryAddedProducts, EnergyConsumptionAndFuelProduction, Cement, EnvironmentAndHealth, \
    ASGMining
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class NewRegistration(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True,
                             help_text='Required: 50 characters or fewer')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'Fname', 'Sname',
                  'Mname', 'Organization_name', 'ContactPhone', 'OrganizationPhone',
                  'Alternate_mobile', 'Full_address', 'email', 'Web_page',
                  'gender', 'is_cement', 'is_health', 'is_waste', 'is_asgm', 'is_map', 'is_EandF',)  # 'is_admin'


class MapForm(forms.ModelForm):
    class Meta:
        model = MercuryAddedProducts
        fields = ('mercury_compound', 'item', 'imported', 'consumption_or_production', 'year',)
        labels = {
            'mercury_compound': 'Mercury Compound',
            'item': 'Item',
            'imported': 'Produced/Imported',
            'consumption_or_production': 'Annual Consumption / Production',
            'year': 'Year'
        }
        widgets = {
            'item': forms.TextInput({'placeholder': 'Mercury containing product/item'}),
            'imported': forms.TextInput({'placeholder': 'If imported state the country of import'}),
            'consumption_or_production': forms.TextInput({'placeholder': 't/y'}),
            'year': forms.TextInput({'placeholder': 'yyyy-mm-dd'}),

        }

    def __init__(self, *args, **kwargs):
        super(MapForm, self).__init__(*args, **kwargs)
        self.fields['mercury_compound'].choices = [("", "select category"),
                                                   ] + list(self.fields['mercury_compound'].choices)[0:]
        self.fields['item'].required = True
        self.fields['mercury_compound'].required = True
        self.fields['consumption_or_production'].required = True
        self.fields['year'].required = True


class EnergyFuelForm(forms.ModelForm):
    class Meta:
        model = EnergyConsumptionAndFuelProduction
        fields = ('energy_fuel', 'imported', 'consumption_or_production', 'year',)
        labels = {
            'energy_fuel': 'Energy Consumption/Fuel Production',
            'imported': 'Produced/Imported',
            'consumption_or_production': 'Annual Consumption / Production',
            'year': 'Year'
        }
        widgets = {
            'imported': forms.TextInput({'placeholder': 'If imported state the country of import'}),
            'consumption_or_production': forms.TextInput({'placeholder': 't/y'}),
            'year': forms.TextInput({'placeholder': 'yyyy-mm-dd'}),

        }

    def __init__(self, *args, **kwargs):
        super(EnergyFuelForm, self).__init__(*args, **kwargs)
        self.fields['energy_fuel'].choices = [("", "select category"),
                                              ] + list(self.fields['energy_fuel'].choices)[0:]
        self.fields['energy_fuel'].required = True
        self.fields['consumption_or_production'].required = True
        self.fields['year'].required = True


class CementForm(forms.ModelForm):
    class Meta:
        model = Cement
        fields = ('operation_cover', 'yes', 'consumption_or_production', 'year',)
        labels = {
            'operation_cover': 'Choose Activities Covered By Operations',
            'yes': 'Choose',
            'consumption_or_production': 'Annual Consumption / Production',
            'year': 'Year'
        }
        widgets = {
            'consumption_or_production': forms.TextInput({'placeholder': 't/y'}),
            'year': forms.TextInput({'placeholder': 'yyyy-mm-dd'}),

        }

    def __init__(self, *args, **kwargs):
        super(CementForm, self).__init__(*args, **kwargs)
        self.fields['operation_cover'].choices = [("", "Choose Activities Covered By Operations"),
                                                  ] + list(self.fields['operation_cover'].choices)[0:]
        self.fields['operation_cover'].required = True
        self.fields['yes'].required = True
        self.fields['consumption_or_production'].required = True
        self.fields['year'].required = True


class EnvironmentAndHealthForm(forms.ModelForm):
    class Meta:
        model = EnvironmentAndHealth
        exclude = ('author', 'eAndH_id')
        labels = {
            'submitted': 'submitted'
        }

    def __init__(self, *args, **kwargs):
        super(EnvironmentAndHealthForm, self).__init__(*args, **kwargs)
        self.created_at = None
        self.fields['submitted'].choices = [("", "submitted"),
                                            ] + list(self.fields['submitted'].choices)[1:]
        self.fields['submitted'].required = True

    def __str__(self):
        return self.created_at


class ASGMiningForm(forms.ModelForm):
    class Meta:
        model = ASGMining
        exclude = ('author', 'asgm_id')

        def __init__(self):
            self.created_at = None

        def __str__(self):
            return self.created_at
