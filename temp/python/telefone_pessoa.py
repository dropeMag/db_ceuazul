from random import randint

print("INSERT INTO [scPessoa].[Telefone] (codigo_pais, codigo_area, telefone)\nVALUES")

for var_x in range(1000):
    var_codigo_pais = randint(1, 99)
    var_codigo_area = randint(1, 99)
    var_telefone = randint(11111111, 99999999)

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_codigo_pais}', '{var_codigo_area}', '{var_telefone}'){var_sep}")


print("GO")
