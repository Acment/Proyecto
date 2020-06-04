from reviewTransaction import PaymentTypes
from modulo import PaymentGateway
pg = PaymentGateway() 
payment_types = PaymentTypes()
count = 0


class Facturacion:
    def __init__(self):
        self.resultado = "---------"
        self.sub_total = 0
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

        op = input("""Escriba cualquier letra para comprar \nEscriba "no" para cancelar la compra\n""")
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

            self.op = input("""¿Va a seguir comprando?\n Escriba cualquier letra para seguir \nEscriba "no" para dejar de comprar \n""")

        #_____________

            # Impresión
        if op != "no":
            self.fix = input("Escriba culquier letra para continuar\n")

            if self.fix != "psoapkms91":
                # ITBMS más el subtotal
                self.itbms = (self.sub_total * 0.07)
                str(round(self.itbms,2))
                self.total_itbms = (self.sub_total + self.itbms)

                #Variables para reducción
                self.total_15 = (self.sub_total * 0.15)
                str(round(self.total_15))
                    
                self.total_10 = (self.sub_total * 0.10)
                str(round(self.total_10))

                self.total_fix = self.total_itbms
                self.total_fix_15 = self.total_itbms - self.total_15
                self.total_fix_10 = self.total_itbms - self.total_10
                    
                # Reducción 
                if self.sub_total <= 600 and self.sub_total >= 200:
                    self.total = self.total_fix_15
                elif self.sub_total >= 100:
                    self.total = self.total_10
                else:
                    self.total = self.total_itbms
        
        
                if self.fix != "nosawedsz21":
                    while True:
                        
                        try:
                            types = int(input("1- Efectivo\n"
                            "2- Cheque\n"
                            "3- CreditCard local\n"
                            "4- CreditCard online\n"))

                        except:
                            types = -1

                        if types == 1:
                            types = "Efectivo"
                            num_type = payment_types.paymentTypesIs(types = types)
                            break

                        elif types == 2:
                            types = "Cheque"
                            num_type = payment_types.paymentTypesIs(types = types)
                            break

                        elif types == 3:
                            types = "CreditCard local"
                            num_type = payment_types.paymentTypesIs(types = types)
                            break

                        elif types == 4:
                            types = "CreditCard online"
                            num_type = payment_types.paymentTypesIs(types = types)
                            transaction = input('Tipo de transaccion: ')
                            mount = self.total
                            card = input('ID Card: ')
                            self.resultado = pg.do_sale(
                                transaction=transaction, 
                                cost=mount, 
                                card=card
                                )
                            break
                
        
                    count = count + 1
                    print("\nEl Gran Almacén")
                    print("RUC 564-35-98512")
                    print("DV 34")
                    print("Teléfono: 666-66666")
                    print("FACTURA [",count,"]") #

                    print(self.document_code)
                    print("Cliente: " + self.user)

                    for i in self.products_general:
                        print(i)

                    print(types, num_type)
                    print("Compra Online: " + str(self.resultado))
                    print("Subtotal:",self.sub_total)
                    print("ITMBS:+",self.itbms)
                    
                    #Total
                    if self.sub_total <= 600 and self.sub_total >= 200:
                        self.total = print("Reducción del 15%: -",self.total_15,"\nTotal:",self.total_itbms - self.total_15)
                    
                    elif self.sub_total >= 100:
                        self.total = print("Reducción del 10%: -",self.total_10,"\nTotal:",self.total_itbms - self.total_10)
                    
                    else:
                        self.total = print("Total:",self.total_itbms)
                    
                    print(self.total)
                
                #_________________________________

                    print("\nEl Gran Almacén")
                    print("RUC 564-35-98512")
                    print("DV 34")
                    print("Teléfono: 666-66666")
                    print("COMPROBANTE [",count,"]") #

                    print("CR")
                    print("Cliente: " + self.user)

                    for i in self.products_general:
                        print(i)

                    print(types, num_type)
                    print("Compra Online: " + str(self.resultado))
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
