from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')
lst_cpf = list()

print("INSERT INTO [scHospede].[Hospede] (nome, sobrenome, dt_nascimento, cpf, rg, sexo, email_id, telefone_id, endereco_id, categoria_id)\nVALUES")

cnt_1 = 2

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
    var_id_endereco = cnt_1

    cnt_1 += 2
    var_categoria = randint(1, 3)

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_nome}', '{var_sobrenome}', '{var_dt_nascimento}', '{var_cpf}', '{var_rg}', '{var_sexo}', '{var_id_email}', '{var_id_telefone}', '{var_id_endereco}', '{var_categoria}'){var_sep}")


print("GO")
