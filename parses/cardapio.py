from xml.dom.minidom import parse

dom = parse("xsd/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementByTagName("prato")

while (True):
    print("\n" + "="*15 + " Cardapio " + "="*15 + "\n")
    for prato in pratos:
        prato_id = prato.getAttribute("id")
        prato_nome = prato.getElementByTagName("nome") [0]
        