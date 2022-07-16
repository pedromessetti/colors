def leia_din(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: Digitação inválida!\033[m')
        else:
            valido = True
            return float(entrada)


def leia_int(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número válido!\033[m')
            continue
        else:
            return num


def leia_float(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número real válido!\033[m')
            continue
        else:
            return num


def leia_din2(txt):
    while True:
        try:
            num = str(input(txt)).replace(',', '.')
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um valor válido!\033[m')
            continue
        else:
            return num
