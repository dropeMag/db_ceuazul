from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')
lst_usuarios = list()

print("INSERT INTO [scFuncionario].[Conta_Funcionario] (usuario, senha)\nVALUES")

for var_x in range(500):
    var_usuario = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{randint(0, 99999)}')
    var_senha = str(f'{choice(lst_letras)}{choice(lst_letras)}{randint(0, 999)}{choice(["@", "_", "$", "&"])}{choice(lst_letras)}{choice(["@", "_", "$", "&"])}{choice(lst_letras)}{randint(0, 999)}')

    while var_usuario in lst_usuarios:
        var_usuario = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(["@", "_", "$", "&"])}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{randint(0, 99999)}')

    lst_usuarios.append(var_usuario)

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_usuario}', '{var_senha}'){var_sep}")


print("GO")