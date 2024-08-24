import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado

country = input("Digite o código do País: ")
funcao = "CountryFlag"
payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>{country}</sCountryISOCode>
    </{funcao}>
  </soap:Body>
</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
content = parseString(response.text)
print(response.text)
print(content.documentElement.getElementsByTagName(f"m:{funcao}Result")[0].firstChild.nodeValue)
#