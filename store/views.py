from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django import forms as formsm

error = ""
error2 = ""

from users.models import User
from .models import (
    OverheadCost,
    Supplier,
    Yard,
    MatMix,
    MaterialMixP,
    MixMaterial,
    cost, grade, metal
)
from .forms import (
    CostUpdateform,
    GradeUpdateform,
    MetalUpdateform,
    OverheadCostForm,
    SupplierForm,
    YardForm,
    
    MaterialUpdateForm,
    MatMixUpdateform,
    MaterialMixformP,
    MatMixform,
    MixMatform,
    SupplierUpdateForm,
    YardUpdateForm, CostForm, GradeForm, MetalForm
)

# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        global error
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            # supp_id = forms.cleaned_data['supp_id']

            # try:
            #     Supplier._default_manager.get(user_id=supp_id)
            #     error = "ID already present.Please Use Another ID"
            #     # raise formsm.ValidationError("")

            # except Supplier.DoesNotExist:
            Supplier.objects.create(name=name, address=address)
            # Supplier.objects.create(name=name, address=address, user_id=supp_id)
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'




def update_supplier(request, pk):
	queryset = Supplier.objects.get(id=pk)
	form = SupplierUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = SupplierUpdateForm(request.POST, instance=queryset)
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





#############
##  Yard
############


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


class YardListView(ListView):
    model = Yard
    template_name = 'store/yard_list.html'
    context_object_name = 'yards'


def update_yard(request, pk):
	queryset = Yard.objects.get(id=pk)
	form = YardUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = YardUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('yard-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_yard.html', context)    


def delete_yard(request, pk):
	queryset = Yard.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('yard-list')
	return render(request, 'store/delete_items.html')    


     

#############################

###  Mixture Material 


#############################


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

        return redirect('material-mix-list')
    context = {
        'form': forms,
    }
    return render(request, 'store/create-mixture-material.html', context)  

def update_items(request, pk):
	queryset = MixMaterial.objects.get(id=pk)
	form = MaterialUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = MaterialUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('material-mix-list')

	context = {
		'form':form
	}
	return render(request, 'store/create-mixture-material.html', context)    


def delete_items(request, pk):
	queryset = MixMaterial.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('material-mix-list')
	return render(request, 'store/delete_items.html')



class mixmateriallist(ListView):
    model = MixMaterial
    template_name = 'store/material_list.html'
    context_object_name = 'material'



###########################
#     Material Mixture
##########


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

        return redirect('material-list')
    context = {
        'form': forms,
    }
    return render(request, 'store/create_material-mix.html', context)   


def update_mat_mix_items(request, pk):
	queryset = MatMix.objects.get(id=pk)
	form = MatMixUpdateform(instance=queryset)
	if request.method == 'POST':
		form = MatMixUpdateform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('material-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_material-mix.html', context)    


def delete_mat_mix_items(request, pk):
	queryset = MatMix.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('material-list')
	return render(request, 'store/delete_items.html')

class materialmixlist(ListView):
    model = MatMix
    template_name = 'store/material_mix_list.html'
    context_object_name = 'material'






#### 
# Overhead Cost
# #####    



# def create_overheadCost(request):
#     forms = OverheadCostForm()
#     if request.method == 'POST':
#         forms = OverheadCostForm(request.POST)
#         if forms.is_valid():
#             yard = forms.cleaned_data['yard']
#             name = forms.cleaned_data['name']
#             cost = forms.cleaned_data['cost']
#             OverheadCost.objects.create(
#                 yard=yard,
#                 name=name,
#                 cost=cost,
#             )
#             return redirect('cost-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/overhead_cost.html', context)


class CostListView(ListView):
    model = cost
    template_name = 'store/cost_list.html'
    context_object_name = 'cost'




def create_cost(request):
    forms = CostForm()
    if request.method == 'POST':
        forms = CostForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            shortform = forms.cleaned_data['shortform']
            rate = forms.cleaned_data['rate']
            misc = forms.cleaned_data['misc']
            cost.objects.create(
                name=name, shortform=shortform, rate=rate, misc=misc
            )
            return redirect('cost-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_cost.html', context)    



def update_cost(request, pk):
	queryset = cost.objects.get(id=pk)
	form = CostUpdateform(instance=queryset)
	if request.method == 'POST':
		form = CostUpdateform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('cost-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_cost.html', context)    


def delete_cost(request, pk):
	queryset = cost.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('cost-list')
	return render(request, 'store/delete_items.html')    


def create_metal(request):
    forms = MetalForm()
    if request.method == 'POST':
        forms = MetalForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            shortform = forms.cleaned_data['shortform']
            rate = forms.cleaned_data['rate']
            misc = forms.cleaned_data['misc']
            metal.objects.create(
                name=name, shortform=shortform, rate=rate, misc=misc
            )
            return redirect('metal-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_metal.html', context)  

def update_metal(request, pk):
	queryset = metal.objects.get(id=pk)
	form = MetalUpdateform(instance=queryset)
	if request.method == 'POST':
		form = MetalUpdateform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('metal-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_metal.html', context)    


def delete_metal(request, pk):
	queryset = metal.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('metal-list')
	return render(request, 'store/delete_items.html')      


class MetalListView(ListView):
    model = metal
    template_name = 'store/metal_list.html'
    context_object_name = 'metal'       


def create_grade(request):
    forms = GradeForm()
    if request.method == 'POST':
        forms = GradeForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            details = forms.cleaned_data['details']
            gradegrp = forms.cleaned_data['gradegrp']
            misc = forms.cleaned_data['misc']
            grade.objects.create(
                name=name, details=details, gradegrp=gradegrp, misc=misc
            )
            return redirect('grade-list')
    context = {
        'form': forms
    }       

    return redirect(request, 'store/create_grade.html', context) 

def update_grade(request, pk):
	queryset = grade.objects.get(id=pk)
	form = GradeUpdateform(instance=queryset)
	if request.method == 'POST':
		form = GradeUpdateform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('grade-list')

	context = {
		'form':form
	}
	return render(request, 'store/create_grade.html', context)    


def delete_grade(request, pk):
	queryset = grade.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('grade-list')
	return render(request, 'store/delete_items.html')      


class GradeListView(ListView):
    model = grade
    template_name = 'store/grade_list.html'
    context_object_name = 'grade'     






