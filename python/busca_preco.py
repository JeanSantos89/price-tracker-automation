import requests

def buscar_produtos(produtoDesejado):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={produtoDesejado}"
    req = requests.get(url)
    data = req.json()

    produtos = []
    for item in data["results"][:5]:
        produtos.append({
            "id": item["id"],
            "titulo": item["title"],
            "preco": item["price"],
            "link": item["permalink"]
        })
    return produtos
