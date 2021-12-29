import requests
import re


def main():

    padrao_cep= re.compile('[0-9]{5}-?[0-9]{3}')

    cep = input('Insira o CEP: ')

    if padrao_cep.fullmatch(cep):
        cep = cep.strip('-')
    else:
        raise ValueError('CEP inválido!')

    r = requests.get(url=f'https://viacep.com.br/ws/{cep}/json')

    resposta = r.json()

    cep_resposta = resposta['cep']
    logradouro = resposta['logradouro']
    complemento = resposta['complemento'] or 's/ complemento'
    bairro = resposta['bairro']
    cidade = resposta['localidade']
    uf = resposta['uf']

    print(f'O CEP {cep_resposta} corresponde a: {logradouro}, {complemento},'
          f' no bairro {bairro}, município {cidade} ({uf})')


if __name__ == '__main__':
    main()
