def main():
    dia=-1
    mes=0
    año=0
    while dia<0 and dia>31:
        dia=int(input("Ingrese el dia de nacimiento (Del 0 al 31): "))
    mes=int(input("Ingrese el mes de nacimiento (Del 0 al 12): ")) 
    año=int(input("Ingrese el año de nacimiento: "))
    print(f"La fecha de nacimiento es \n dia: {dia} \nmes: {mes}\n año: {año}")

if __name__=='__main__':
    main()    