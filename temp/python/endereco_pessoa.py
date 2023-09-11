from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')

print("INSERT INTO [scPessoa].[Endereco] (pais, estado, cidade, bairro, rua, numero, complemento, cep)\nVALUES")

for var_x in range(1000):
    if var_x % 2 != 0:
        var_pais = choice(['Brasil', 'Japão', 'Canadá', 'Estados Unidos', 'França', 'Itália', 'Reino Unido', 'Austrália', 'China', 'Índia', 'Rússia', 'México', 'Argentina', 'Espanha', 'Alemanha', 'Holanda', 'Suíça', 'Suécia', 'Noruega', 'Dinamarca', 'Finlândia', 'África do Sul', 'Nigéria', 'Egito', 'Arábia Saudita', 'Emirados Árabes Unidos', 'Turquia', 'Coreia do Sul', 'Tailândia', 'Indonésia', 'Malásia', 'Vietnã', 'Singapura'])
    else:
        var_pais = 'Brasil'

    var_estado = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_cidade = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_bairro = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_rua = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}')
    var_numero = randint(1, 999)

    if var_x % 5 == 0:
        var_complemento = f"'Apto {var_x}'"
    else:
        var_complemento = 'NULL'

    var_cep = randint(1111111, 99999999)

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_pais}', '{var_estado}', '{var_cidade}', '{var_bairro}', '{var_rua}', '{var_numero}', {var_complemento}, '{var_cep}'){var_sep}")


print("GO")
