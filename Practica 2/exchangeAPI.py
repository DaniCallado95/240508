### GESTIÓN DE SISTEMAS DE INFORMACIÓN  ###
### Práctica 2 - Exchange API           ###
### Autor - Daniel Callado Martínez     ###
### Fecha - 04/10/2019                  ###

from urllib.request import urlopen
import json

### Clase ExchangeClient ###
class ExchangeClient:

    def __init__(self,api_url = 'https://api.exchangeratesapi.io/latest'):
        self.api_url = api_url

    def connect(self):
        response = urlopen(self.api_url)
        rates = json.loads(response.read())
        self.rates = rates['rates']
        self.date = rates['date']

    def convert(self, cantidad, moneda):
        return round(cantidad / self.rates[moneda],2)

### Main ###
if __name__ == "__main__":
    client = ExchangeClient()
    client.connect()

    entrada = open("divisas.txt")
    salida = open("ahorros.txt",'a')

    sal = "{}: \n".format(client.date)

    total = 0.0
    for lineas in entrada:
        moneda = lineas.split(", ")[0]
        if not moneda in client.rates:
            sal += "   {} no es una entrada valida \n".format(moneda)
        else:          
            cantidad = int(lineas.split(", ")[1])
            cantidad_convertida = client.convert(cantidad,moneda)
            sal += "   {} {} son {} euros \n".format(cantidad, moneda, cantidad_convertida)
            total += cantidad_convertida

    sal += "   Total: {} euros \n".format(total)
    salida.write(sal)

    entrada.close()
    salida.close()