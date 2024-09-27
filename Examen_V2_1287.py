print (" -- EXAMEN V2 -- ")
print (" Janna Ramirez Mat: 22308051281287")

# CREACION DE CLASE
class banco1287:

    # DICCIONARIOS 
    def cliente1287(self):
        clientes1287={
            "Nombre": "Roberto",
            "Apellido Paterno":"Gaytan",
            "Apellido Materno": "Mendoza"
        }
        print(clientes1287)
        for info, pers in clientes1287.items():
            print(f"{info}: {pers}")

    def cuenta1287(self):
        cuentas1287={
            "Numero de cuenta": 17248214248274,
            "Tipo": "Crédito",
            "Interés": "15%",
            "Saldo":"$10,000"
        }
        print(cuentas1287)
        for info,pers in cuentas1287.items():
            print(f"{info}: {pers}")

    def cantidad1287(self):
        cantidaad1287={
            "Fecha": "27-09-2024",
            "Cantidad": "$2,500",
            "Número de transacción": 18726381931245
        }
        print(cantidaad1287)
        for info,pers in cantidaad1287.items():
            print(f"{info}: {pers}")

# CREACIÓN DEL OBJETO 

banco = banco1287()

# MOSTRAR DATOS 
print("DATOS DEL CLIENTE")
banco.cliente1287()
print("\nDATOS DE LA CUENTA")
banco.cuenta1287()
print("\nDATOS DE LA TRANSACCIÓN")
banco.cantidad1287()
