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
    def verFecha(self):
        return self.__fecha_ingreso
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
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 

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
            6- Salir 
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

                from datetime import datetime
                while True:
                    fecha = input("Ingrese la fecha de ingreso (día/mes/año): ")
                    try:
                        datetime.strptime(fecha, "%d/%m/%Y")
                        break
                    except ValueError:
                        print("Formato de fecha inválido. Debe ser día/mes/año.")

                try:
                    nm = int(input("Ingrese cantidad de medicamentos: "))
                    if nm < 0:
                        print("La cantidad de medicamentos no puede ser negativa.")
                        continue
                except ValueError:
                    print("Debe ingresar un número válido.")
                    continue

                lista_med = []
                for i in range(nm):
                    nombre_medicamento = input(f"Ingrese el nombre del medicamento #{i+1}: ")
                    try:
                        dosis = int(input(f"Ingrese la dosis del medicamento #{i+1}: "))
                        if dosis <= 0:
                            print("La dosis debe ser mayor a cero.")
                            continue
                    except ValueError:
                        print("Debe ingresar un número válido para la dosis.")
                        continue

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
            try:
                q = int(input("Ingrese la historia clínica de la mascota: "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha:
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



if __name__=='__main__':
    main()