# import sqlite3

from peewee import *


db = SqliteDatabase("nivel_avanzado.db")


class BaseModel(Model):
    """Clase que genera el uso del ORM."""

    class Meta:
        """Clase que genera el name_space database."""

        database = db


class Noticia(BaseModel):
    """Clase que genera la tabla Noticias."""
    
    # id = IntegerField(unique=True)
    titulo = CharField(unique=True)
    descripcion = TextField()


db.connect()
db.create_tables([Noticia])


class Abmc:
    """Clase para lograr el CRUD"""

    def __init__(
        self,
    ):
        pass

    def actualizar_treeview(self, mitreeview):
        """Metodo: limpieza de tabla."""

        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        for fila in Noticia.select():
            print(fila)
            mitreeview.insert(
                "", 0, text=fila.id, values=(fila.titulo, fila.descripcion)
            )

    def cerrar_conexion(self):
        """Metodo para un print????"""

        print("cerrar_conexion")

    def alta(self, titulo, descripcion, mitreeview):
        """Metodo que genera el Alta."""

        noticia = Noticia()
        noticia.titulo = titulo.get()
        noticia.descripcion = descripcion.get()
        noticia.save()
        self.actualizar_treeview(mitreeview)

    def guarda(variables, popupGuardar, elobjeto):
        """Metodo para guardar."""

        popupGuardar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
        noticia = Noticia()
        noticia.titulo = lista[0]
        noticia.descripcion = lista[1]
        noticia.save()
        elobjeto.mostrar()

    def borrar(self, titulo, descripcion, mitreeview):
        """Metodo para eliminar."""

        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        
        borrar = Noticia.get(Noticia.titulo == titulo.get())
        borrar.delete_instance()
        
        self.actualizar_treeview(mitreeview)       

    def modificar(self, titulo, descripcion, mitreeview):
        """Metodo para modificar."""

        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        
        for selec in mitreeview.selection():
            item = mitreeview.item(selec)
            record = item["values"]
            titulo.set(record[0])
            descripcion.set(record[1])
        
        actualizar = Noticia.update(descripcion = descripcion.get()).where(
            Noticia.titulo == titulo.get())
        
        actualizar.execute()

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
