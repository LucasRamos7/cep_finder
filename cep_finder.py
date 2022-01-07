import requests


def encontrar_cep():
    uf = input('Insira a UF (ex: RJ): ').upper()
    cidade = input('Insira o nome da cidade: ')
    logradouro = input('Insira o nome do logradouro (ex: Presidente Vargas): ')

    r = requests.get(url=f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json')


def main():

    print('Qual das opções se adequa melhor a você?')
    print('(1) Tenho um CEP e quero descobrir o endereço')
    print('(2) Tenho um endereço e preciso descobrir seu CEP\n\n')

    opcao = int(input())

    if opcao == 1:
        encontrar_endereco()
    elif opcao == 2:
        encontrar_cep()
    else:
        print('Opção inválida!')


def encontrar_endereco():
    cep = input('Insira o CEP: ').strip('-')

    resposta = faz_request(cep)

    imprime_endereco(resposta)


def faz_request(cep):
    r = requests.get(url=f'https://viacep.com.br/ws/{cep}/json')

    while r.status_code == 400:
        print('\nCEP inválido!\n')

        cep = input('Insira o CEP: ').strip('-')

        r = requests.get(url=f'https://viacep.com.br/ws/{cep}/json')

    resposta = r.json()
    return resposta


def imprime_endereco(resposta):
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
