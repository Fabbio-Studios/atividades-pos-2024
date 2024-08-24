from zeep import Client

# URL do WSDL
wsdl = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl"

client = Client(wsdl=wsdl)

# Número pra converter
number = input("Digite Qualquer número: ")

# Chama o método NumberToWords com o número desejado
response = client.service.NumberToWords(ubiNum=number)

# Imprime o resultado
print(f"O número {number} por extenso é: {response}")
