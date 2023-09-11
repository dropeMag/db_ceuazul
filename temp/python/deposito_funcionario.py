from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')
lst_numero = list()

print("INSERT INTO [scFuncionario].[Deposito_Funcionario] (numero_conta, codigo_agencia, tipo_conta, nome_banco)\nVALUES")

for var_x in range(500):
    var_numero_conta = randint(11111111, 99999999)
    var_codigo_agencia = randint(1111, 4444)
    var_tipo_conta = randint(1, 2)
    var_nome_banco = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')

    while var_numero_conta in lst_numero:
        var_numero_conta = randint(11111111, 99999999)

    lst_numero.append(var_numero_conta)

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_numero_conta}', '{var_codigo_agencia}', '{var_tipo_conta}', '{var_nome_banco}'){var_sep}")

print("GO")