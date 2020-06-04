from Facturación import Facturacion
from reviewTransaction import PaymentTypes
from Cotizar import Cotizar


payment_types = PaymentTypes()

if __name__ == "__main__":
    print("Menú:\n(1)Facturación\n (2)Cotización\n (3)Salir")
    
    while True:
        try:
            option = int(input("Ingrese la opción\n"))
        
        except:
            option = -1
                
        if option == 1:
            fa = Facturacion()
            fa.while_method()
            print("Menú:\n(1)Facturación\n (2)Cotización\n (3)Salir")


        elif option == 2:
            co = Cotizar()
            co.while_method()
            print("Menú:\n(1)Facturación\n (2)Cotización\n (3)Salir")
            
        elif option == 3:
            break
        