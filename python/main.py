import sys
from busca_preco import buscar_produtos
from db import salvar_no_bd

def main():
    produtoDesejado = sys.argv[1]
    salvarDados = buscar_produtos(produtoDesejado)
    salvar_no_bd(salvarDados)

if __name__ == "__main__":
    main()
