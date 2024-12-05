def diccionario():
    return {
        "ValidarNombre": validar,
        "ManejoNombre": manejoNombre,
        "AbrirArchivo":openFile,
		"ValdidarInt":ValidarEntero,
		"ValidarFloat":ValidarFloat
    }

def validar(nombre):  # bool
    invalid_chars = ('0', '1', '2', '3', '4', '5',
                     '6', '7', '8', '9', '@', ',', '.')
    # Check if any invalid character is in the name
    for char in nombre:
        if char in invalid_chars:
            return False
    return True

def manejoNombre(nombre):  # string
    while True:
        if not validar(nombre):
            nombre = input("- Ingrese un nombre correcto, por favor: ")
        else:
            return nombre
        
def openFile(nombrearchivo): #object archivo
    
    try:
        archivo = open(nombrearchivo, 'rb')
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None

def ValidarEntero(n): #int
	
	valor = 0 #int
	
	while (True):
		try:
			valor = int(n)

			if(valor < 2):
				n = input("- Los valores correctos son numeros postivos: ")
			else:
				return valor
		
		except ValueError:
			print("Valor erroneo: Cant not convert data to int\n")
			n = input("- Ingrese un valor ENTERO, no string por favor: ")
			
def ValidarFloat(n): #float
	valor = 0.0 # float
	
	while (True):
		try:
			valor = float(n)
			if(n <= 0):
				return valor
			else:
				n = input("- Ingrese un valor mayor a 1: ")

		except ValueError:
			print("Valor erroneo: Cant not convert data to float\n")
			n = input("- Por favor introduzca un valor correcto: ")
			
Utiles = diccionario()