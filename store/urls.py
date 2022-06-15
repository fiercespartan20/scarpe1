from django.urls import path

from .views import (
    CostListView,
    GradeListView,
    MetalListView,
    # create_overheadCost,
    create_cost,
    create_grade,
    create_metal,
    create_supplier,
    create_yard,
    SupplierListView,
    YardListView,
    create_material_mix,
    delete_cost,
    delete_grade,
    delete_metal,
    delete_supplier,
    delete_yard,

    

    materialmixlist,
    mixmateriallist,
    update_cost,
    update_grade,
    update_items,
    delete_items,
    update_metal,
    update_supplier,
    create_mixture_material,
    create_material_mix,
    update_mat_mix_items,
    delete_mat_mix_items,
    update_yard
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-yard/', create_yard, name='create-yard'),
    path('create-mixture-material/', create_mixture_material, name='create-mixture-material'),
    path('create-material-mix/', create_material_mix, name='create-material-mix'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('yard-list/', YardListView.as_view(), name='yard-list'),
    path('update_yard/<str:pk>/', update_yard, name="update_yard"),
    path('delete_yard/<str:pk>/', delete_yard, name="delete_yard"),



    path('update_items/<str:pk>/', update_items, name="update_items"),

    path('update_grade/<str:pk>/', update_grade, name="update_grade"),
    path('delete_grade/<str:pk>/', delete_grade, name="delete_grade"),


    path('update_cost/<str:pk>/', update_cost, name="update_cost"),
    path('delete_cost/<str:pk>/', delete_cost, name="delete_cost"),


    path('update_metal/<str:pk>/', update_metal, name="update_metal"),
    path('delete_metal/<str:pk>/', delete_metal, name="delete_metal"),

    # path('overhead_cost/', create_overheadCost, name='create-overheadcost'),
    path('create_cost/', create_cost, name='create_cost'),
    path('cost-list/', CostListView.as_view(), name='cost-list'),
    path('create_metal/', create_metal, name='create_metal'),
    path('metal-list/', MetalListView.as_view(), name='metal-list'),

    path('create_grade/', create_grade, name='create_grade'),
    path('grade-list/', GradeListView.as_view(), name='grade-list'),



    path('update_supplier/<str:pk>/', update_supplier, name="update_supplier"),

    
    # path('material-list/', materialmixlist.as_view(), name='material-list'),
    # path('material-mix-list/', mixmateriallist.as_view(), name='material-mix-list'),
    # path('update_mat_mix_items/<str:pk>/', update_mat_mix_items, name="update_mat_mix_items"),
    # path('delete_material-mixture/<str:pk>/', delete_mat_mix_items, name="delete_mat_mix_items"),
    
    # path('delete_items/<str:pk>/', delete_items, name="delete_items"),
    path('delete_supplier/<str:pk>/', delete_supplier, name="delete_supplier"),
]
