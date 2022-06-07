from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    OverheadCost,
    Supplier,
    Yard,
    MatMix,
    MaterialMixP,
    MixMaterial
)
from .forms import (
    OverheadCostForm,
    SupplierForm,
    YardForm,
    
    MaterialUpdateForm,
    MaterialMixformP,
    MatMixform,
    MixMatform
)

# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            supp_id = forms.cleaned_data['supp_id']

            Supplier.objects.create(name=name, address=address, user_id=supp_id)
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


def create_yard(request):
    forms = YardForm()
    if request.method == 'POST':
        forms = YardForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            Yard.objects.create(
                supplier=supplier,
                name=name,
                address=address,
            )
            return redirect('yard-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_yard.html', context)



def create_overheadCost(request):
    forms = OverheadCostForm()
    if request.method == 'POST':
        forms = OverheadCostForm(request.POST)
        if forms.is_valid():
            yard = forms.cleaned_data['yard']
            name = forms.cleaned_data['name']
            cost = forms.cleaned_data['cost']
            OverheadCost.objects.create(
                yard=yard,
                name=name,
                cost=cost,
            )
            return redirect('cost-list')
    context = {
        'form': forms
    }
    return render(request, 'store/overhead_cost.html', context)


class CostListView(ListView):
    model = OverheadCost
    template_name = 'store/cost_list.html'
    context_object_name = 'cost'



class YardListView(ListView):
    model = Yard
    template_name = 'store/yard_list.html'
    context_object_name = 'yards'



def update_supplier(request, pk):
	queryset = MixMaterial.objects.get(id=pk)
	form = SupplierForm(instance=queryset)
	if request.method == 'POST':
		form = SupplierForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('supplier-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_supplier.html', context)  


def delete_supplier(request, pk):
	queryset = Supplier.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('supplier-list')
	return render(request, 'store/delete_items.html')          



def update_items(request, pk):
	queryset = MixMaterial.objects.get(id=pk)
	form = MaterialUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = MaterialUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('material-list')

	context = {
		'form':form
	}
	return render(request, 'store/create-material-mix.html', context)    


def delete_items(request, pk):
	queryset = MixMaterial.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('material-list')
	return render(request, 'store/delete_items.html')


def create_mixture_material(request):
    forms = MixMatform()
    if request.method == 'POST':
        forms = MixMatform(request.POST)
        if forms.is_valid():
            yard = forms.cleaned_data['yard']
            alu = forms.cleaned_data['alu']
            zn = forms.cleaned_data['zn']
            aluc = forms.cleaned_data['aluc']
            ss = forms.cleaned_data['ss']
            pb = forms.cleaned_data['pb']
            pvc = forms.cleaned_data['pvc']
            fibre = forms.cleaned_data['fibre']
            others1 = forms.cleaned_data['others1']
            others2 = forms.cleaned_data['others2']
            nm = forms.cleaned_data['nm']
            total = forms.cleaned_data['total']

            MixMaterial.objects.create(
                alu = alu, zn=zn, aluc=aluc, ss=ss, pb=pb, pvc=pvc, fibre=fibre, others1=others1,
                others2=others2, nm=nm, total=total, yard = yard
            )

        return redirect('material-list')
    context = {
        'form': forms,
    }
    return render(request, 'store/create-mixture-material.html', context)  


def create_material_mix(request):
    forms = MatMixform()
    if request.method == 'POST':
        forms = MatMixform(request.POST)
        if forms.is_valid():
            yard = forms.cleaned_data['yard']
            cha = forms.cleaned_data['cha']
            oil = forms.cleaned_data['oil']
            vp = forms.cleaned_data['vp']
            oh = forms.cleaned_data['oh']
            dep = forms.cleaned_data['dep']
            trans = forms.cleaned_data['trans']
            flux = forms.cleaned_data['flux']
            cusi = forms.cleaned_data['cusi']
            extrasi = forms.cleaned_data['extrasi']
            gst = forms.cleaned_data['gst']
            extracost = forms.cleaned_data['extracost']
            total = forms.cleaned_data['total']

            MatMix.objects.create(
                cha = cha, oil=oil, vp=vp, oh=oh, dep=dep, trans=trans, flux=flux, cusi=cusi,
                extrasi=extrasi, gst=gst, extracost=extracost, total=total, yard = yard
            )

        return redirect('material-mix-list')
    context = {
        'form': forms,
    }
    return render(request, 'store/create_material-mix.html', context)    



class mixmateriallist(ListView):
    model = MatMix
    template_name = 'store/material_mix_list.html'
    context_object_name = 'material'




class materialmixlist(ListView):
    model = MixMaterial
    template_name = 'store/material_list.html'
    context_object_name = 'material'

# class materialmixlistp(ListView):
#     model = MaterialMixP
#     template_name = 'store/material_list.html'
#     context_object_name = 'materialp'    


# def materialmix_list(request):
#     MaterialMix = MaterialMix.objects.filter(is_delete=False)
#     MaterialMixP = MaterialMixP.objects.filter(is_delete=False)
#     context = {'MaterialMix': MaterialMix, 'MaterialMixP':MaterialMixP}
#     return render(request, 'store/material-list.html', context)




# def create_material_mix_p(request):
#     forms = MaterialMixformP()
#     if request.method == 'POST':
#         forms = MaterialMixform(request.POST)
#         if forms.is_valid():
#             alu = forms.cleaned_data['alu']
#             zn = forms.cleaned_data['zn']
#             aluc = forms.cleaned_data['aluc']
#             ss = forms.cleaned_data['ss']
#             pb = forms.cleaned_data['pb']
#             pvc = forms.cleaned_data['pvc']
#             fibre = forms.cleaned_data['fibre']
#             others1 = forms.cleaned_data['others1']
#             others2 = forms.cleaned_data['others2']
#             nm = forms.cleaned_data['nm']
#             total = forms.cleaned_data['total']

#             MaterialMix.create.objects(
#                 alu = alu, zn=zn, aluc=aluc, ss=ss, pb=pb, pvc=pvc, fibre=fibre, others1=others1,
#                 others2=others2, nm=nm, total=total
#             )

#         return redirect('materialmix-list')
#     context = {
#         'formp': forms
#     }
#     return render(request, 'store/create-material-mix.html', context)        


