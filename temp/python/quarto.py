from random import randint

print("INSERT INTO [scEstalagem].[Quarto] (num_andar, num_camas, valor_diaria, tipo_quarto, status)\nVALUES")

cnt_piso = 1
cnt_andar = 1
cnt_tipo = 1

for var_x in range(30):
    var_num_andar = cnt_andar

    if cnt_tipo == 1:
        var_num_camas = 1
        var_valor_diaria = randint(300, 500)
    elif cnt_tipo == 2:
        var_num_camas = 3
        var_valor_diaria = randint(350, 550)
    elif cnt_tipo == 3:
        var_num_camas = 1
        var_valor_diaria = randint(250, 380)
    elif cnt_tipo == 4:
        var_num_camas = randint(1, 2)
        var_valor_diaria = randint(150, 250)
    elif cnt_tipo == 5:
        var_num_camas = 2
        var_valor_diaria = randint(200, 300)
    else:
        var_num_camas = 6
        var_valor_diaria = randint(460, 690)

    var_tipo_quarto = cnt_tipo
    var_status = 0

    if cnt_piso == 6:
        cnt_piso = 1
        cnt_andar += 1
        cnt_tipo = 1
    else:
        cnt_piso += 1
        cnt_tipo += 1

    if var_x != 29:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_num_andar}', '{var_num_camas}', '{var_valor_diaria}', '{var_tipo_quarto}', '{var_status}'){var_sep}")


print("GO")
