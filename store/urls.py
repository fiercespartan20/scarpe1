from django.urls import path

from .views import (
    CostListView,
    create_overheadCost,
    create_supplier,
    create_yard,
    SupplierListView,
    YardListView,
    create_material_mix,
    delete_supplier,
    materialmixlist,
    mixmateriallist,
    update_items,
    delete_items,
    update_supplier,
    create_mixture_material,
    create_material_mix
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-yard/', create_yard, name='create-yard'),
    path('create-mixture-material/', create_mixture_material, name='create-mixture-material'),
    path('create-material-mix/', create_material_mix, name='create-material-mix'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('yard-list/', YardListView.as_view(), name='yard-list'),
    path('update_items/<str:pk>/', update_items, name="update_items"),

    path('overhead_cost/', create_overheadCost, name='create-overheadcost'),
    path('cost-list/', CostListView.as_view(), name='cost-list'),


    path('update_supplier/<str:pk>/', update_supplier, name="update_supplier"),
    
    path('material-list/', materialmixlist.as_view(), name='material-list'),
    path('material-mix-list/', mixmateriallist.as_view(), name='material-mix-list'),
    
    
    path('delete_items/<str:pk>/', delete_items, name="delete_items"),
    path('delete_supplier/<str:pk>/', delete_supplier, name="delete_supplier"),
]
