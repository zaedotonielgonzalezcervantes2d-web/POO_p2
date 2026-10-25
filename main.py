from estudiantes import estudiantes, estudiantesBD


class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("\n\t\t\t...::: Presione una tecla para continuar :::...\n")

    def menu_acciones(self, tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::...\n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\t\t Elige una opción: ").strip().lower()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t\t\t...::: Operación realizada con éxito :::...\n")
        else:
            print("\n\t\t\t...::: Ocurrió un error al realizar la operación :::...\n")
        self.esperarTecla()

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t\t\t...::: Datos del {tipo} :::...\n")
        estudiantito = {}
        estudiantito["nombre"] = input("\t nombre: ").strip().upper()
        estudiantito["nota"] = input("\t nota: ").strip()
        return estudiantito

    def mostrar_registros(self, registros):
        num_estudiante = 1
        for fila in registros:
            print(f"Estudiante # {num_estudiante}\n\t ID: {fila[0]}\n\t Nombre: {fila[1]}\n\t Nota (calificación): {fila[2]}\n")
            num_estudiante += 1

    def menu_estudiante(self):
        opcion= True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")
            match opcion:
                case "1":
                    self.borrarPantalla()
                    estudiantitos= self.datos_estudiante("Estudiante")
                    estudiante1= estudiantes.Estudiantes(estudiantitos["nombre"], estudiantitos["nota"])

                    estudianteBD= estudiantesBD.EstudiantesBD(estudiantitos["nombre"], estudiantitos["nota"])
                    respuesta= estudianteBD.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                    del estudianteBD

                case "2":
                    self.borrarPantalla()
                    id = input("\n\t Ingrese el ID del estudiante a eliminar: ").strip()
                    respuesta= estudiantes.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)

                case "3":
                    id = input("\n\t Ingrese el ID del estudiante a actualizar: ").strip()
                    estudiantitos= self.datos_estudiante("Estudiante")
                    estudiante1= estudiantes.Estudiantes(estudiantitos["nombre"], estudiantitos["nota"])

                    estudiante1= estudiantes.Estudiantes(estudiantitos["nombre"], estudiantitos["nota"])
                    respuesta= estudiante1.actualizar(estudiantitos["nombre"], estudiantitos["nota"], id)
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case "4":
                    self.borrarPantalla()
                    registros= estudiantes.Estudiantes.consultar()
                    if len(registros)>0:
                        num_estudiantes= 1
                        for fila in registros:
                            print(f"Estudiante # {num_estudiantes}\n\t ID: {fila[0]}\n\t Nombre: {fila[1]}\n\t Nota (calificación): {fila[2]}\n")
                            num_estudiantes+= 1
                            self.esperarTecla()
                    else:
                        print("\n\n\t... No hay registros para mostrar por el momento ...")
                    self.esperarTecla()

                case "5":
                    self.borrarPantalla()
                    opcion= False

                case _:
                    input("\n\t...::: Opción inválida, vuelva a intentarlo :::...\n")
                    self.esperarTecla()

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\n\t\t\t...::: Menu Principal :::...\n\n\t 1.- Estudiantes\n\t 2.- Salir\n\n\t Elige una opción: ").strip().lower()
            match opcion:
                case "1":
                    self.menu_estudiante()
                case "2":
                    self.borrarPantalla()
                    print("\n\t ... Salir del Sistema ...")
                    opcion = False
                case _:
                    print("\n\t...::: Opción inválida, vuelva a intentarlo :::...\n")
                    self.esperarTecla()


if __name__ == "__main__":
    app = App()
    app.main()