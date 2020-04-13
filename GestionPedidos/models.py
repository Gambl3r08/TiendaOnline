from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return f"\nNombre: {self.nombre}\n Dirección: {self.direccion}\n Email: {self.email}\n Telefono:{self.telefono}\n"

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"\nNombre: {self.nombre} \n Sección: {self.seccion} \n Precio: {self.precio}\n"

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"\nNumero: {self.numero}\n Fecha: {self}\n Entregado: {self.entregado}\n"