# import sqlite3

from peewee import *


db = SqliteDatabase('nivel_avanzado.db')
class BaseModel(Model):
    class Meta:
        database = db
                
class Noticia(BaseModel):
    titulo = CharField(unique=True)
    descripcion=TextField()
db.connect()
db.create_tables([Noticia])


class Abmc:
    def __init__(
        self,
    ):
        pass       

    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records=mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)       

        
        for fila in Noticia.select():
            print(fila)
            mitreeview.insert("", 0, text=fila.id, values=(fila.titulo, fila.descripcion))

    def cerrar_conexion(
        self,
    ):
        print("cerrar_conexion")



    def alta(self, titulo, descripcion, mitreeview):
        noticia = Noticia()
        noticia.titulo = titulo.get()
        noticia.descripcion = descripcion.get()
        noticia.save()        
        self.actualizar_treeview(mitreeview)
        
    def guarda(variables, popupGuardar, elobjeto):   
        popupGuardar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
        noticia = Noticia()
        noticia.titulo = lista[0]
        noticia.descripcion = lista[1]
        noticia.save()
        elobjeto.mostrar()
        
    def borrar(variables, popupEliminar, elobjeto):
        popupEliminar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())

        borrar = Noticia.get(Noticia.id == lista[0])
        borrar.delete_instance()

        elobjeto.mostrar()
        
    def modificar(variables, popupModificar, elobjeto):
        popupModificar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())

        actualizar = Noticia.update(titulo = lista[1], descripcion =
        lista[2]).where(Noticia.id == lista[0])
        actualizar.execute()

        elobjeto.mostrar()