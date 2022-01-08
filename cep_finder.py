import requests


def main():

    print('Qual das opções se adequa melhor a você?')
    print('(1) Tenho um CEP e quero descobrir o endereço')
    print('(2) Tenho um endereço e quero descobrir seu CEP\n')

    opcao = int(input())

    if opcao == 1:
        encontrar_endereco()
    elif opcao == 2:
        encontrar_cep()
    else:
        print('Opção inválida!')


def encontrar_endereco():
    cep = input('\nInsira o CEP: ').strip('-')

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
              f' no bairro {bairro}, município {cidade} ({uf})')
    else:
        print('CEP inexistente!')


def imprime_resultados(resposta):
    numero_resultados = len(resposta)

    print(f'\nSua busca retornou {numero_resultados} resultados!\n')

    pagina = 1
    for i in range(numero_resultados):
        for j in range(10 * (pagina - 1), 10 * pagina):
            if j == numero_resultados:
                break

            bairro = resposta[j]['bairro']
            logradouro_resposta = resposta[j]['logradouro']
            complemento = resposta[j]['complemento'] or 's/ complemento'
            cep = resposta[j]['cep']

            print(f'{bairro}, {logradouro_resposta}, {complemento}: CEP {cep}')

        if j == numero_resultados:
            print('\nTodos os resultados exibidos')
            break

        print('\nVocê encontrou o que procurava? \n (1) Sim (2) Não')
        cep_ok = int(input())

        while cep_ok not in [1, 2]:
            print('Opção inválida!')
            print('Você encontrou o que procurava? \n (1) Sim (2) Não')
            cep_ok = int(input())

        if cep_ok == 1:
            break
        else:
            pagina += 1


def encontrar_cep():
    uf = input('\nInsira a UF (ex: RJ): ').upper()
    cidade = input('Insira o nome da cidade: ')
    logradouro = input('Insira o nome do logradouro (ex: Avenida Presidente Vargas): ')

    r = requests.get(url=f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json')

    if r.status_code == 400:
        print('\nOs nomes da cidade e do logradouro devem conter ao menos 3 caracteres')
        return

    resposta = r.json()

    imprime_resultados(resposta)


if __name__ == '__main__':
    main()
