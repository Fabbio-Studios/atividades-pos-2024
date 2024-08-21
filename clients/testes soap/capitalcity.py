import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado
country = input("Digite o código do País: ")
payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>{country}</sCountryISOCode>
    </CapitalCity>
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
print(content.documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)