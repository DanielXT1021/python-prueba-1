
def evaluar(nota):
    total= nota * 2400
    return total
def main():
    calificacion=input("Ingrese la calificacion: ")
    dinero=evaluar(calificacion)
    print(f"La calificacion correspondiente {calificacion} y el dinero que recibe es: {dinero}")


if __name__=='__main__':
    main()  
