def aumentar(preco=0, taxa=0, formato=False):
    aumento = preco+((taxa*preco)/100)
    return aumento if not formato else moeda(aumento)


def reduzir(preco=0, taxa=0, formato=False):
    reducao = preco-((taxa*preco)/100)
    return reducao if not formato else moeda(reducao)


def dobro(preco=0, formato=False):
    dob = preco*2
    return dob if not formato else moeda(dob)


def metade(preco=0, formato=False):
    met = preco/2
    return met if not formato else moeda(met)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print('Preço analisado:', f'{moeda(preco):>12}')
    print('Dobro do preço:', f'{dobro(preco, True):>13}')
    print('Metade do preço:', f'{metade(preco, True):>12}')
    print(f'{aumento}% de aumento:', f'{aumentar(preco, aumento, True):>13}')
    print(f'{reducao}% de redução:', f'{reduzir(preco, reducao, True):>13}')
    print('-'*30)


def leiaDin(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
