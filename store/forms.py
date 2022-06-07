from django import forms

from store.models import Supplier, Yard, MatMix, MaterialMixP, MixMaterial, OverheadCost


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    supp_id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'supp_id',
        'data-val': 'true',
        'data-val-required': 'Please enter supplier id',
    }))


class YardForm(forms.ModelForm):
    class Meta:
        model = Yard
        fields = [
            'supplier','name', 'address'
        ]

        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
        }



class OverheadCostForm(forms.ModelForm):
    class Meta:
        model = OverheadCost
        fields = [
            'yard','name', 'cost'
        ]

        widgets = {
            'yard': forms.Select(attrs={
                'class': 'form-control', 'id': 'yard'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'cost': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'cost'
            }),
        }









class MaterialUpdateForm(forms.ModelForm):
	class Meta:
		model = MixMaterial
		fields = [
            'yard','alu', 'zn', 'aluc','ss','pb','pvc','fibre','others1','others2','nm','total'
        ]


class MatMixform(forms.ModelForm):
    class Meta:
        model = MatMix

        fields = [
            'yard','cha', 'oil', 'vp','oh','dep','trans','flux','cusi',
            'extrasi','gst','extracost','total'
        ]

        widgets = {
            'yard': forms.Select(attrs={
                'class': 'form-control', 'id': 'yard'
            }),
            'cha' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'cha'
            }),
            'oil' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'oil'
            }),
            'vp' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'vp'
            }),
            'oh' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'oh'
            }),
            'dep' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'dep'
            }),
            'trans' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'trans'
            }),
            'flux' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'flux'
            }),
            'cusi' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'cusi'
            }),
            'extrasi' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'extrasi'
            }),
            'gst' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'gst'
            }),
            'extracost' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'extracost'
            }),
            'total' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'total'
            })

        }        



class MixMatform(forms.ModelForm):
    class Meta:
        model = MixMaterial

        fields = [
            'yard','alu', 'zn', 'aluc','ss','pb','pvc','fibre','others1','others2','nm','total'
        ]

        widgets = {
            'yard': forms.Select(attrs={
                'class': 'form-control', 'id': 'yard'
            }),
            'alu' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'alu'
            }),
            'zn' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'zn'
            }),
            'aluc' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'alcu'
            }),
            'ss' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'ss'
            }),
            'pb' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'pb'
            }),
            'pvc' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'pvc'
            }),
            'fibre' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'fibre'
            }),
            'others1' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'others1'
            }),
            'others2' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'others2'
            }),
            'nm' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'nm'
            }),
            'total' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'total'
            })

        }      





class MaterialMixformP(forms.ModelForm):
    class Meta:
        model = MaterialMixP

        fields = [
            'yard','alu', 'zn', 'aluc','ss','pb','pvc','fibre','others1','others2','nm','total'
        ]

        widgets = {
            'yard': forms.Select(attrs={
                'class': 'form-control', 'id': 'yard','label':'false'
            }),
            'alu' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'alu', 'label':'FALSE'
            }),
            'zn' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'zn'
            }),
            'aluc' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'alcu'
            }),
            'ss' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'ss'
            }),
            'pb' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'pb'
            }),
            'pvc' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'pvc'
            }),
            'fibre' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'fibre'
            }),
            'others1' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'others1'
            }),
            'others2' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'others2'
            }),
            'nm' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'nm'
            }),
            'total' : forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'total'
            })

        }        

