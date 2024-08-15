import json

# Carrega o arquivo JSON
with open('parses/imobiliaria.json', encoding='utf-8') as json_file:
    parsed_data = json.load(json_file)

imoveis = parsed_data["imobiliaria"]["imovel"]

# lista de imóveis
print("Imóveis disponíveis:")
for imovel in imoveis:
    print(f"ID: {imovel['id']} - {imovel['descricao']}")
print("\n" + "="*30)

# Selecionar imóvel
try:
    id_selecionado = int(input("pra mais informações, digite o ID do imóvel: "))
    imovel = next((item for item in imoveis if item["id"] == id_selecionado), None)

    if imovel:
        descricao = imovel["descricao"]
        proprietario = imovel["proprietario"]
        tel_proprietario = proprietario.get("telefones", [])
        email_proprietario = proprietario.get("email", "")
        endereco = imovel["endereco"]
        caracteristicas = imovel["caracteristicas"]
        valor = imovel["valor"]

        print("\n" + "="*30)
        print("****** Descrição: ******")
        print(descricao)
        print("")

        print("****** Proprietário(a): ******")
        print(f"  - {proprietario['nome']}")
        print("")

        print("****** Tel.: ******")
        for tel in tel_proprietario:
            print(f"  - {tel}")
        print("")

        if email_proprietario:
            print("****** Email: ******")
            print(f"  - {email_proprietario}")
            print("")

        print("****** Endereço: ******")
        print(f"   Rua: {endereco['rua']}")
        print(f"   Bairro: {endereco['bairro']}")
        print(f"   Cidade: {endereco['cidade']}")
        print(f"   N°: {endereco['numero']}")
        print("")

        print("****** Características: ******")
        print(f"  Tamanho: {caracteristicas['tamanho']} m²")
        print(f"  N° de quartos: {caracteristicas['numQuartos']}")
        print(f"  N° de banheiros: {caracteristicas['numBanheiros']}")
        print("")

        print(f"****** Valor: {valor} ******")
    else:
        print("Imóvel não encontrado!")

    print("="*30)

except ValueError:
    print("SDigite um número válido!")
