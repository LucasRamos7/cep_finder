import requests


def main():

    cep = input('Insira o CEP: ').strip('-')

    r = requests.get(url=f'https://viacep.com.br/ws/{cep}/json')

    while r.status_code == 400:
        print('\nCEP inválido!\n')

        cep = input('Insira o CEP: ').strip('-')

        r = requests.get(url=f'https://viacep.com.br/ws/{cep}/json')

    resposta = r.json()

    if 'erro' not in resposta:
        cep_resposta = resposta['cep']
        logradouro = resposta['logradouro']
        complemento = resposta['complemento'] or 's/ complemento'
        bairro = resposta['bairro']
        cidade = resposta['localidade']
        uf = resposta['uf']

        print(f'\nO CEP {cep_resposta} corresponde a: {logradouro}, {complemento},'
              f' no bairro {bairro}, município {cidade} ({uf})\n')
    else:
        print('CEP inexistente!')


if __name__ == '__main__':
    main()
