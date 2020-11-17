class Cliente():
    def __init__(self, DNI, Nombre, Apellidos, AB):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.ab = AB

class Empleado():
    def __init__(self, nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor
        self.antiguedad = antiguedad

    def infoEmpleado(self):
        print("Nombre: " + self.nombre)
        print("Apellidos: "+self.apellidos)
        print("DNI: "+self.DNI)
        print("Direccion: "+self.direccion)
        print(+self.telefono)
        print(+self.salario)
        print("Supervisor: "+self.supervisor)

    def camSupervisor(self, supervisor):
        self.supervisor = supervisor

    def incrementSalario(self, incremento):
        self.salario = (self.salario*(100+incremento))/100

class Secretario(Empleado):
    def __init__(self, nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad, fax):
        super().__init__(nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad)
        self.despacho = True
        self.fax = fax
        self.incrementSalario(5)

    def infoSecre(self):
        self.infoEmpleado()
        print(self.despacho)
        print(self.fax)
        print("Puesto: Secretario")

class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad, matricula, marca, modelo, areaVenta, listaClientes, AB):
        super().__init__(nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad)
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.areaVenta = areaVenta
        self.listaClientes = listaClientes
        self.incrementSalario(10)
        self.ab = AB

    def infoVen(self):
        self.infoEmpleado()
        print("Matricula Coche: "+self.matricula)
        print("Marca Coche: "+self.marca)
        print("Modelo Coche: "+self.modelo)
        print(self.areaVenta)
        print(self.listaClientes)

    def darAlta(self, cliente):
        cliente.ab = True

    def darBaja(self, cliente):
        cliente.ab = False

    def camCoche(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

class JefeZona(Empleado):
    def __init__(self, nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad, matricula, marca, modelo, secretario, vendedoresACargo):
        super().__init__(nombre, apellidos, DNI, direccion, telefono, salario, supervisor, antiguedad)
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.secretario = secretario
        self.vendedores = vendedoresACargo
        self.incrementSalario(20)

    def infoJefeZona(self):
        self.infoEmpleado()
        print("Matricula Coche: "+self.matricula)
        print("Marca Coche: "+self.marca)
        print("Modelo Coche: "+self.modelo)
        print("Secretario a su cargo: ")
        self.secretario.infoSecre()
        print("Vendedores a su disposicion: ")
        for i in range(len(vendedores)):
            print(vendedores[i].infoVen())

    def camSecretario(self, secretario):
        self.secretario = secretario

    def camCoche(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

    def darVendedorAltaOBaja(self, vendedor):
        if vendedor.ab == True:
            vendedor.ab = False
        else:
            vendedor.ab = True

secretario = Secretario("David2", "Gallardo", "45925080Z", "C/Falsa", 603601349, 900, "Rodrigo", 3, 222333666)
# per.infoSecre()

vendedor1 = Vendedor("Juan", "Gallardo", "555846X", "C/Mola", 666888222, 800, "Yo", 2, "5874SDF", "Fiat", "500", "Madrid", "Hola", True)
vendedor2 = Vendedor("Juan2", "Gallardo2", "555846X", "C/Mola", 666888222, 800, "Yo", 2, "5874SDF", "Fiat", "500", "Madrid", "Hola", True)

vendedores = [vendedor1, vendedor2]

jefe = JefeZona("David", "Gallardo", "45925080Z", "C/Falsa", 603601349, 900, "Rodrigo", 3, "0047BLT", "Ford", "Escort", secretario, vendedores)
jefe.infoJefeZona()