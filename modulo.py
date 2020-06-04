#Nombre: David Diaz
#Cedula: 8-930-2006

import re

class PaymentGateway():

    def __init__(self):
        self.card = ''
        self.result = []
        self.box = ['auth', 'capture','sale']

    def do_sale(self, transaction, cost, card):

        if re.match('((^a)(uth)$)|((^c)(apture)$)|((^s)(ale)$)', transaction):

            if cost >= 1 and cost <= 150000:

                if re.match('(^4|5|6)([0-9]{15}$)', card):
                    
                    if self.box.index(transaction) == 0:
                        self.result.append('1')
                        self.type_card(card=card, result=self.result)
                        return self.result

                    elif self.box.index(transaction) == 1:
                        self.result.append('2')
                        self.type_card(card=card, result=self.result)
                        return self.result

                    elif self.box.index(transaction) == 2:
                        self.result.append('3')
                        self.type_card(card=card, result=self.result)
                        return self.result

                else:
                    return {"error": 500, "Mensaje":
                            "Esto no es una transaccion permitida"}

            else:
                return {"error": 500, "Mensaje":
                        "Este monto no es permitido"}
        
        else:
            return {"error": 500,
                    "Mensaje": "Esto no es una transaccion permitida"}
    def type_card(self, card, result):
        if int(card[0:1]) == 4:
            result.append('Visa')
        if int(card[0:1]) == 5:
            result.append('Master Card')
        if int(card[0:1]) == 6:
            result.append('American Express')

