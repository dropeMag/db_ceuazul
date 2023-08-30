from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')

print("INSERT INTO [scHospede].[Hospede] (nome, sobrenome, dt_nascimento, cpf, rg, sexo, email, id_telefone, id_endereco)\nVALUES")

for var_x in range(1000):
    var_nome = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_sobrenome = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)} {choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_dt_nascimento = str(f'{randint(1950, 2001)}-{randint(1, 12)}-{randint(1, 28)}')
    var_cpf = randint(11111111111, 99999999999)
    var_rg = randint(1111111, 9999999)
    var_sexo = choice(['m', 'f'])
    var_email = str(f'{var_nome}.{var_sobrenome[:10]}{randint(1111, 9999)}@{choice(["gmail", "email", "hotmail", "outmail"])}.com')
    var_id_telefone = var_x + 7
    var_id_endereco = var_x + 8

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_nome}', '{var_sobrenome}', '{var_dt_nascimento}', '{var_cpf}', '{var_rg}', '{var_sexo}', '{var_email}', '{var_id_telefone}', '{var_id_endereco}'){var_sep}")


print("GO")
