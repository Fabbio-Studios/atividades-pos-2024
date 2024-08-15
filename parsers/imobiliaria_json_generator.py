
from xml.dom.minidom import parse
import json

dom = parse("xsd/imobiliaria.xml")
imobiliaria_xml = dom.documentElement
imoveis = imobiliaria_xml.getElementsByTagName("imovel")

# Lista para armazenar os imóveis
lista_imoveis = []

# Contador de ID
number = 1
for imovel in imoveis:
    imovel_data = {}

    imovel_data['id'] = number
    number += 1

    # Descrição do imóvel
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
    imovel_data['descricao'] = descricao

    # dados do proprietário
    proprietario = imovel.getElementsByTagName("proprietario")[0]
    nome_proprietario = proprietario.getElementsByTagName("nome")[0].firstChild.nodeValue
    imovel_data['proprietario'] = {'nome': nome_proprietario}

    # Email do proprietario
    email = proprietario.getElementsByTagName("email")
    if email:
        imovel_data['proprietario']['email'] = email[0].firstChild.nodeValue

    # Telefones do proprietario
    telefones = proprietario.getElementsByTagName("telefone")
    if telefones:
        lista_telefones = []
        for telefone in telefones:
            lista_telefones.append(telefone.firstChild.nodeValue)
        imovel_data['proprietario']['telefones'] = lista_telefones

    # Endereço do imóvel
    endereco = imovel.getElementsByTagName("endereco")[0]
    rua = endereco.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = endereco.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = endereco.getElementsByTagName("cidade")[0].firstChild.nodeValue

    numero = endereco.getElementsByTagName("numero")
    if numero:
        numero = numero[0].firstChild.nodeValue
    else:
        numero = "Sem número"

    imovel_data['endereco'] = {
        'rua': rua,
        'bairro': bairro,
        'cidade': cidade,
        'numero': numero
    }

    # Características do imóvel
    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]
    tamanho = caracteristicas.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    num_quartos = caracteristicas.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    num_banheiros = caracteristicas.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue
    imovel_data['caracteristicas'] = {
        'tamanho': tamanho,
        'numQuartos': num_quartos,
        'numBanheiros': num_banheiros
    }

    # Valor do imóvel
    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue
    imovel_data['valor'] = valor

    # adiciona o imóvel na lista
    lista_imoveis.append(imovel_data)

# Cria o JSON
imobiliaria_json = {
    "imobiliaria": {
        "imovel": lista_imoveis
    }
}

# Escreve o JSON em um arquivo Json (lógico, num xml que não seria kkkk)
with open("parsers/imobiliaria.json", "w", encoding="utf-8") as json_file:
    json.dump(imobiliaria_json, json_file, indent=2, ensure_ascii=False)
