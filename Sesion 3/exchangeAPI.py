from urllib.request import urlopen
import json

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

if __name__ == "__main__":
    client = ExchangeClient()
    client.connect()

    entrada = open("cantidades.txt")
    salida = open("evolucion.txt",'a')

    sal = "{}: \n".format(client.date)

    for lineas in entrada:
        moneda = lineas.split(", ")[0]
        cantidad = int(lineas.split(", ")[1])
        sal = sal + "   {} {} son {} euros \n".format(cantidad, moneda, client.convert(cantidad,moneda))

    salida.write(sal)
    entrada.close()
    salida.close()