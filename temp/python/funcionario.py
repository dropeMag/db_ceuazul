from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')
lst_cpf = list()

print("INSERT INTO [scFuncionario].[Funcionario] (nome, sobrenome, dt_nascimento, cpf, rg, sexo,\
 id_email, id_telefone, contato_emergencia, id_endereco, id_funcao, id_deposito, id_conta, status)\nVALUES")

cnt_1 = 1
cnt_2 = 1
cnt_3 = 1

for var_x in range(500):
    var_nome = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_sobrenome = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)} {choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_dt_nascimento = str(f'{randint(1950, 2001)}-{randint(1, 12)}-{randint(1, 28)}')
    var_cpf = randint(11111111111, 99999999999)
    while var_cpf in lst_cpf:
        var_cpf = randint(11111111111, 99999999999)
    lst_cpf.append(var_cpf)

    var_rg = randint(1111111, 9999999)
    var_sexo = choice(['m', 'f'])
    var_id_email = cnt_1
    var_id_telefone = cnt_1
    var_contato_emergencia = 2
    var_id_endereco = cnt_1
    var_id_funcao = cnt_3

    cnt_3 += 1
    if cnt_3 == 25:
        cnt_3 = 1

    var_id_deposito = var_x + 1
    cnt_1 += 2

    if var_id_funcao in [16, 20, 21, 22, 24]:
        var_id_conta = "NULL"
    else:
        var_id_conta = f"'{cnt_2}'"
        cnt_2 += 1

    if var_x < 300:
        var_status = 1
    else:
        var_status = 0

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_nome}', '{var_sobrenome}', '{var_dt_nascimento}', '{var_cpf}', '{var_rg}', '{var_sexo}', '{var_id_email}', '{var_id_telefone}', '{var_contato_emergencia}', '{var_id_endereco}', '{var_id_funcao}', '{var_id_deposito}', {var_id_conta}, '{var_status}'){var_sep}")


print("GO")
