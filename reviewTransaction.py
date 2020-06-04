class PaymentTypes():
    def __init__(self):
        self.paymentTypes = {
                "Efectivo": 10,
                "Cheque": 11,
                "CreditCard local": 12,
                "CreditCard online": 13
                }

    def paymentTypesIs(self, types):

        if types in self.paymentTypes.keys():
            if types == list(self.paymentTypes.keys())[0]:
                types = self.paymentTypes[types]
                return types

            elif types == list(self.paymentTypes.keys())[1]:
                types = self.paymentTypes[types]
                return types

            elif types == list(self.paymentTypes.keys())[2]:
                types = self.paymentTypes[types]
                return types

            elif types == list(self.paymentTypes.keys())[3]:
                types = self.paymentTypes[types]
                return types

        else:
            return {"Error":500,"Mensaje":"El tipo de transaccion no es valida"}

















