from django.urls import path
from . import views
from .views import RecetaListView, RecetaDetailView, RecetaCreateView, RecetaUpdateView, RecetaDeleteView

urlpatterns = [
    path('', RecetaListView.as_view(), name='lista_recetas'),
    path('receta/<int:pk>/', RecetaDetailView.as_view(), name='detalle_receta'),
    path('receta/crear/', RecetaCreateView.as_view(), name='crear_receta'),
    path('receta/<int:pk>/editar/', RecetaUpdateView.as_view(), name='editar_receta'),
    path('receta/<int:pk>/borrar/', RecetaDeleteView.as_view(), name='borrar_receta'),
    path('registro/', views.register, name='registro'),
]