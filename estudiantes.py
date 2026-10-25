from conexionBD import cursor, conexion

class Estudiantes:
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota

    @property
    def Nombre(self):
        return self.nombre

    @property
    def Nota(self):
        return self.nota

    @nombre.setter
    def nombre(self, nombre):
        self.nombre= nombre

    @nota.setter
    def nota(self, nota):
        self.nota= nota

    def insertar(self):
        try:
            cursor.execute("insert into estudiantes values (NULL, %s, %s)",
            (self._nombre, self._nota))
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from estudiantes")
            return cursor.fetchall()
        except:
            return []    

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from estudiantes where id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False    

    def actualizar(self, nombre, nota, id):
        try:
            cursor.execute("update estudiante set nombre=%s, nota=%s where id=%s",
            (nombre, nota, id))
            conexion.commit()
            return True
        except:
            return False