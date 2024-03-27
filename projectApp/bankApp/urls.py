from django.urls import path
from . import views

urlpatterns = [
    path ('home', views.home, name= 'principal'),
    path ('getAll', views.getAllCust, name= 'ObtenerTodo'),
    path ('getOne/<int:id>', views.getOneCust, name= 'ObtenerUno'),
    path ('add', views.newCust, name= 'agregar'),
    path ('upDate/<int:id>', views.upDateCust, name= 'actualizar'),
    path ('delete/<int:id>', views.deleteCust, name= 'eliminar'),
    path ('acc/newAcc', views.newAcc, name= 'nuevaCuenta'),
    path ('acc/upDateAcc/<int:num>', views.upDateAcc, name= 'actualizarCuenta'),
    path ('acc/accDelete/<int:num>', views.deleteAcc, name= 'eliminarCuenta')

]


