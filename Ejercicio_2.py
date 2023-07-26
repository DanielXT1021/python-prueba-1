def areacirculo(r):
    area=3.1416*(r**2)
    return area
def volumencilindro(h,r):
    volumen=3.1416*(r**2)*h
    return volumen
def main():

    radio=float(input("Ingrese el radio: "))
    altura=float(input("Ingrese la altura: "))

    area_c=areacirculo(radio)
    volumen_c=volumencilindro(radio,altura)
    
    print(f"el area del circulo es: {area_c} y el volumen de cilindro es: {volumen_c}")

if __name__=='__main__':
    main()   