from xml.dom.minidom import parse

dom = parse("xsd/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName("prato")

while (True):
    print("\n" + "="*15 + " Cardapio " + "="*15 + "\n")
    for prato in pratos:
        prato_id = prato.getAttribute("id")
        prato_nome = prato.getElementsByTagName("nome") [0]
        nome = prato_nome.firstChild.nodeValue
        print(f"{prato_id}. {nome}")
    print("0. Finalizar")

    entrada = input("\n Digite uma opção: ")
    if entrada == "0":
        break

    for prato in pratos:
        prato_id = prato.getAttribute("id")
        if entrada == prato_id:
            print("")
            prato_nome = prato.getElementsByTagName("nome")[0]
            nome = prato_nome.firstChild.nodeValue
            print("="*15 + f" {nome} " + "="*15 + "\n")

            prato_description = prato.getElementsByTagName("descricao")[0]
            description = prato_description.firstChild.nodeValue
            print(f"{description} \n")

            ingredientes = prato.getElementsByTagName("ingrediente")
            print("Ingredientes")

            numbering = 1
            for ingrediente in ingredientes:
                ingrediente_nome = ingrediente.firstChild.nodeValue
                print(f" {numbering}. {ingrediente_nome} ")
                numbering += 1
            print("")

            prato_price = prato.getElementsByTagName("preco")[0]
            price = prato_price.firstChild.nodeValue
            print(f"Preço: {price}")

            prato_ptime = prato.getElementsByTagName("tempoPreparo")[0]
            ptime = prato_ptime.firstChild.nodeValue
            print(f"Tempo de Preparo: {ptime}")

            prato_calories = prato.getElementsByTagName("calorias")[0]
            calories = prato_calories.firstChild.nodeValue
            print(f"Calorias: {calories}")

            entrada = input("\nEnter. Voltar ao menu \n")


