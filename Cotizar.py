count = 0
class Cotizar:
    def __init__(self):
        

        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        products_names = []
        products_price = []
        products_general = []
        document_code = "FA" #
        
        # Self en arreglos y variable
        self.products_names = products_names
        self.products_price = products_price
        self.products_general = products_general
        
        self.document_code = document_code
        
        
    def while_method(self):
        global count
        user_name = input("Ingrese el nombre del cliente\n")
        self.user = user_name
        
        op = input("""Escriba cualquier letra para cotizar \nEscriba "no" para cancelar la cotizar\n""")
        if op == "no":
            print("\n") 
        
        self.op = op
        

        while self.op != "no":
            
            # Entrada de datos
            single_name_product = input("Ingrese el producto\n")
            
            single_price_product = input("Ingrese el precio\n")
            
            while single_price_product[0] not in self.numbers:
                print("Error: Ingrese una cantidad numérica")
                single_price_product = input("Ingrese el precio\n")
            
            single_quantity_product = input("Ingrese la cantidad a comprar\n")
        
            while single_quantity_product[0] not in self.numbers:
                print("Error: Ingrese una cantidad numérica")
                single_quantity_product = input("Ingrese la cantidad a comprar\n")

            # self en variables
            self.name = single_name_product
            self.price = float(single_price_product)
            self.quantity = float(single_quantity_product)

            # Multiplicación de la cantidad por el precio
            self.products_names.append(self.name)
            self.products_price.append(self.price * self.quantity)
            
            #Subtotal de la cantidad comprada
            self.subtotal_quantity = (self.price * self.quantity)
            
            # Subtotal
            total = 0
            for suma in self.products_price:
                total = total + suma
            self.sub_total = total
            
            # Descripción general
            self.products_general.extend(("Nombre del producto: " + self.name, "Precio:", self.price , "Cantidad:" ,self.quantity,"subtotal de cantidad comprada:", self.subtotal_quantity))

            self.op = input("""¿Va a seguir comprando?\n Escriba cualquier letra para seguir \nEscriba "no" para dejar de comprador \n""")

        #_________

        if op != "no":
            self.fix = input("Escriba cualquier letra para continuar\n")

            if self.fix != "nospqkem91":
                # ITBMS más el subtotal
                self.itbms = (self.sub_total * 0.07)
                str(round(self.itbms,2))
                self.total_itbms = (self.sub_total + self.itbms)

            # Variables para reducción
                self.total_15 = (self.sub_total * 0.15)
                str(round(self.total_15))
                
                self.total_10 = (self.sub_total * 0.10)
                str(round(self.total_10))
            
                
                # Impresión
                count = count + 1
                print("\nEl Gran Almacén")
                print("RUC 564-35-98512")
                print("DV 34")
                print("Teléfono: 666-66666")
                print("COTIZACIÓN [",count,"]") #

                print(self.document_code)
                print("Cliente: " + self.user)

                for i in self.products_general:
                    print(i)

                print("Subtotal:",self.sub_total)
                print("ITMBS:+",self.itbms)

                # Reducción 
                if self.sub_total <= 600 and self.sub_total >= 200:
                    self.total = print("Reducción del 15%: -",self.total_15,"\nTotal:",self.total_itbms - self.total_15)
                elif self.sub_total >= 100:
                    self.total = print("Reducción del 10%: -",self.total_10,"\nTotal:",self.total_itbms - self.total_10)
                else:
                    self.total = print("Total:",self.total_itbms)
                
                #Total
                return(self.total)

                #input("Quiere volver su cotización factura?")

        