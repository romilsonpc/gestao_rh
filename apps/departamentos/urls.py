from django.urls import path
from .views import DepartamentosList, DepartamentosCreate

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentosCreate.as_view(), name='create_departamento'),
]