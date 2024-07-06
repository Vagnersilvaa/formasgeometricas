import math
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_circulo(raio):
    return math. pi * raio ** 2


def main():
    while True:
        
        print("\nEscolha uma forma Geometrica para calcular:")
        print("1: Triangulo")
        print("2: Retangulo")
        print("3: Quadrado")
        print("4: Circulo")
        print("5: Sair")
    
        opcao = input ("Opção: ")
    
        if opcao == "1":
         base = float(input("Digite o valor da base do triangulo:"))
         altura = float(input("Digite o valor da altura do triangulo:"))
         area = calcular_area_triangulo(base, altura)
         print (f"A area do triangulo e: {area}")
        
        
        elif opcao == "2":
            base = float(input("Digite o calor da base do retangullo:"))
            altura = float(input("Digite o valor da altura do retangulo:"))
            area = calcular_area_retangulo(base, altura)
            print(f" A area do retangulo e: {area}")
             
             
        elif opcao == "3":
            lado = float(input("Digite o valor do lado do quadrado:"))
            area = calcular_area_quadrado(lado)
            print(f"A area do circulo e: {area}")
        
        
        elif opcao == "4":
            raio = float(input("Digite o valor do raio do circulo:"))
            calcular_area_circulo(raio)
            print(f"A area do circulo e: {area}") 
            
            
        else:
            print("Opção invalida. Por favor, escolha uma opção valida.")
           
           
if __name__ == "__main__":
               main() 