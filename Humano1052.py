print("Actividad 9. Clase humano")
print("Kevin Carbajal Mat:22308051281052")
# Zona de clases
class Humano1052:
    #Zona de atributos
    ojos=0
    peso=0
    estatura=0
    genero=0
    fechadenacimiento=0
    #Zona de funciones
    def hablar1052(self,a):
        print(f"{a} esta hablando")
    def bailar1052(self,a):
        print(f"{a} esta bailando")
    def escribir1052(self,a):
        print(f"{a} esta escribiendo")
    def cantar1052(self,a):
        print(f"{a} esta cantando")
#Zona de creacion de objetos
kevin=Humano1052()
momodetwice=Humano1052()



#Zona de usando objetos
print("----Resultados para Kevin----")
kevin.ojos="Cafes"
print(f"Ojos:{kevin.ojos}")
kevin.peso="80kg"
print(f"Peso: {kevin.peso}")
kevin.estatura="1.72m"
print(f"Estatura: {kevin.estatura}")
kevin.genero="Masculino"
print(f"Genero: {kevin.genero}")
kevin.fechadennacimiento="3/12/2007"
print(f"Fecha de nacimiento: {kevin.fechadenacimiento}")
kevin.hablar1052("Kevin")
kevin.bailar1052("Kevin")
kevin.escribir1052("Kevin")
kevin.cantar1052("Kevin")

print("----Resultados para Momo de Twice----")
momodetwice.ojos="Cafes"
print(f"Ojos: {momodetwice.ojos}")
momodetwice.peso="48kg"
print(f"Peso: {momodetwice.peso}")
momodetwice.estatura="1.63m"
print(f"Estatura: {momodetwice.estatura}")
momodetwice.genero="Femenino"
print(f"Genero: {momodetwice.genero}")
momodetwice.fechadennacimiento="3/12/2007"
print(f"Fecha de nacimiento: {momodetwice.fechadenacimiento}")
momodetwice.hablar1052("Momo de Twice")
momodetwice.bailar1052("Momo de Twice")
momodetwice.cantar1052("Momo de Twice")