from xml.dom.minidom import parse

dom = parse("xsd/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName("prato")
namespace = "http://cardapio.org"

while True:
    print("\n" + "="*15 + " Cardápio " + "="*15 + "\n")
    for prato in pratos:
        prato_id = prato.getAttribute("id")
        prato_nome = prato.getElementsByTagName("nome")[0]
        nome = prato_nome.firstChild.nodeValue
        print(f"{prato_id}. {nome}")
    print("0. Finalizar")

    entrada = input("\nDigite uma opção: ")
    if entrada == "0":
        break

    prato_selecionado = None
    for prato in pratos:
        prato_id = prato.getAttribute("id")
        if entrada == prato_id:
            prato_selecionado = prato
            break

    if prato_selecionado is None:
        print("\nOpção inválida. Tente novamente.")
        continue

    prato_nome = prato_selecionado.getElementsByTagName("nome")[0]
    nome = prato_nome.firstChild.nodeValue
    print("\n" + "="*15 + f" {nome} " + "="*15 + "\n")

    prato_descricao = prato_selecionado.getElementsByTagName("descricao")
    descricao = prato_descricao[0].firstChild.nodeValue if prato_descricao else "Descrição não disponível"
    print(f"{descricao} \n")

    ingredientes = prato_selecionado.getElementsByTagName("ingrediente")
    print("Ingredientes")

    for i, ingrediente in enumerate(ingredientes, start=1):
        ingrediente_nome = ingrediente.firstChild.nodeValue
        print(f"{i}. {ingrediente_nome}")

    prato_preco = prato_selecionado.getElementsByTagName("preco")[0]
    preco = prato_preco.firstChild.nodeValue
    print(f"Preço: {preco}")

    prato_calorias = prato_selecionado.getElementsByTagName("calorias")[0]
    calorias = prato_calorias.firstChild.nodeValue
    print(f"Calorias: {calorias}")

    prato_tempo_preparo = prato_selecionado.getElementsByTagNameNS(namespace, "tempodepreparo")
    if prato_tempo_preparo:
        tempo_preparo = prato_tempo_preparo[0].firstChild.nodeValue
        print(f"Tempo de Preparo: {tempo_preparo}")
    else:
        print("Tempo de Preparo: Informação não disponível")

    input("\nEnter. Voltar ao menu\n")
