from datetime import datetime, date
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def asignarFecha(self, f: date):
        self.__fecha_ingreso = f
    def verFecha(self):
        return self.__fecha_ingreso.strftime("%d/%m/%Y")

    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n
    def eliminarMedicamento(self, nombre_medicamento):
        for med in self.__lista_medicamentos:
            if med.verNombre() == nombre_medicamento:
                self.__lista_medicamentos.remove(med)
                return True
        return False

    
class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}

    def verificarExiste(self, historia):
        return historia in self.__caninos or historia in self.__felinos

    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos)

    def ingresarMascota(self, mascota):
        historia = mascota.verHistoria()
        tipo = mascota.verTipo().strip().lower()
        if tipo == "canino":
            self.__caninos[historia] = mascota
        elif tipo == "felino":
            self.__felinos[historia] = mascota
        else:
            print("Tipo de mascota no reconocido. Solo se admiten caninos o felinos.")

    def verFechaIngreso(self, historia):
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            return mascota.verFecha()
        return "La mascota no está en el sistema."

    def verMedicamento(self, historia):
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            return mascota.verLista_Medicamentos()
        return "La mascota no está registrada en el sistema."

    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return True
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return True
        return False
    def eliminarMedicamentoMascota(self, historia, nombre_medicamento):
        mascota = self.__caninos.get(historia) or self.__felinos.get(historia)
        if mascota:
            return mascota.eliminarMedicamento(nombre_medicamento)
        return None  # No se encontró la mascota


def main():
    servicio_hospitalario = sistemaV()

    while True:
        print(f"\nCapacidad disponible: {10 - servicio_hospitalario.verNumeroMascotas()} mascotas")
        try:
            menu = int(input('''\nIngrese una opción: 
            1- Ingresar una mascota 
            2- Ver fecha de ingreso 
            3- Ver número de mascotas en el servicio 
            4- Ver medicamentos que se están administrando
            5- Eliminar mascota 
            6- SALIR
            7- Eliminar medicamento a una mascota
            La opción que usted desea escoger es: '''))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if menu == 1:  # Ingresar una mascota
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio disponible para nuevas mascotas.")
                continue

            try:
                historia = int(input("Ingrese la historia clínica de la mascota: "))
            except ValueError:
                print("Debe ingresar un número válido para la historia clínica.")
                continue

            if not servicio_hospitalario.verificarExiste(historia):
                nombre = input("Ingrese el nombre de la mascota: ")

                # Validación tipo
                while True:
                    tipo = input("Ingrese el tipo de mascota (felino o canino): ").strip().lower()
                    if tipo in ["canino", "felino"]:
                        break
                    else:
                        print("Tipo inválido. Debe ingresar 'canino' o 'felino'.")

                try:
                    peso = int(input("Ingrese el peso de la mascota (en kg): "))
                    if peso <= 0:
                        print("El peso debe ser mayor a cero.")
                        continue
                except ValueError:
                    print("Debe ingresar un número válido para el peso.")
                    continue

                while True:
                    fecha_input = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                    try:
                        fecha = datetime.strptime(fecha_input, "%d/%m/%Y").date()
                        break
                    except ValueError:
                        print("Formato de fecha inválido. Intente nuevamente con el formato dd/mm/aaaa.")

                try:
                    nm = int(input("Ingrese cantidad de medicamentos: "))
                    if nm < 0:
                        print("La cantidad de medicamentos no puede ser negativa.")
                        continue
                except ValueError:
                    print("Debe ingresar un número válido.")
                    continue

                lista_med = []
                nombres_medicamentos = set()

                for i in range(nm):
                    while True:
                        nombre_medicamento = input(f"Ingrese el nombre del medicamento #{i+1}: ").strip().lower()
                        if nombre_medicamento in nombres_medicamentos:
                            print("Ese medicamento ya fue ingresado. Por favor ingrese uno diferente.")
                        else:
                            nombres_medicamentos.add(nombre_medicamento)
                            break
                    while True:
                        try:
                            dosis = int(input(f"Ingrese la dosis para {nombre_medicamento}: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un número válido para la dosis.")

                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)


                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                print("Mascota ingresada con éxito.")
            else:
                print("Ya existe una mascota con ese número de historia clínica.")

        elif menu == 2:  # Ver fecha de ingreso
            while True:
                try:
                    q = int(input("Ingrese la historia clínica de la mascota: "))
                    break
                except ValueError:
                    print("Debe ingresar un número entero para la historia clínica.")
            
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha is not None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")


        elif menu == 3:  # Ver número de mascotas
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu == 4:  # Ver medicamentos
            try:
                q = int(input("Ingrese la historia clínica de la mascota: "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            medicamentos = servicio_hospitalario.verMedicamento(q)
            if medicamentos:
                print("Los medicamentos suministrados son: ")
                for m in medicamentos:
                    print(f"- {m.verNombre()} (Dosis: {m.verDosis()})")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5:  # Eliminar mascota
            try:
                q = int(input("Ingrese la historia clínica de la mascota: "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            if servicio_hospitalario.eliminarMascota(q):
                print("Mascota eliminada del sistema con éxito.")
            else:
                print("No se encontró una mascota con esa historia clínica.")

        elif menu == 6:
            while True:
                confirmacion = input("¿Está seguro que desea salir? (si/no): ").strip().lower()
                if confirmacion == 'si':
                    print("Usted ha salido del sistema de servicio de hospitalización...")
                    return
                elif confirmacion == 'no':
                    print("Cancelando salida. Regresando al menú principal.")
                    break
                else:
                    print("Entrada no válida. Por favor escriba 'si' o 'no'.")
        elif menu == 7:
            try:
                historia = int(input("Ingrese la historia clínica de la mascota: "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            if not servicio_hospitalario.verificarExiste(historia):
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                continue

            nombre_medicamento = input("Ingrese el nombre del medicamento a eliminar: ").strip().lower()
            resultado = servicio_hospitalario.eliminarMedicamentoMascota(historia, nombre_medicamento)

            if resultado is True:
                print(f"El medicamento '{nombre_medicamento}' ha sido eliminado.")
            elif resultado is False:
                print(f"El medicamento '{nombre_medicamento}' no se encontró en la lista de la mascota.")
            else:
                print("La mascota no está registrada en el sistema.")

if __name__=='__main__':
    main()