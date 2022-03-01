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
"""
    def baja(self, mitreeview):
        item_seleccionado=mitreeview.focus()
        valor_id=mitreeview.item(item_seleccionado)
        con=self.conexion()
        cursor=con.cursor()
        sql="DELETE FROM noticias WHERE id=?"
        datos=(valor_id["text"],)
        print(datos, sql)
        cursor.execute(sql, datos)
        con.commit()
        self.actualizar_treeview(mitreeview)

    def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado=mitreeview.focus()
        valor_id=mitreeview.item(item_seleccionado)
        con=self.conexion()

        cursor=con.cursor()
        sql="UPDATE noticias SET (titulo, descripcion)=(?,?) WHERE id=?"
        datos=(titulo.get(), descripcion.get(), valor_id["text"])
        cursor.execute(sql, datos)
        con.commit()
        print(sql, datos)

        self.actualizar_treeview(mitreeview)

"""