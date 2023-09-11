from random import randint

print("INSERT INTO [scFuncionario].[Contrato_Funcionario] (id_funcionario, dt_admissao, dt_demissao, motivo_demissao)\nVALUES")

cnt_1 = 21

for var_x in range(500):
    var_id_funcionario = cnt_1
    cnt_1 += 1
    var_dt_admissao = str(f'{randint(2016, 2019)}-{randint(1, 12)}-{randint(1, 28)}')

    if var_id_funcionario < 321:
        var_dt_demissao = "NULL"
        var_motivo_demissao = "NULL"
    else:
        var_dt_demissao = str(f"'{randint(2020, 2022)}-{randint(1, 12)}-{randint(1, 28)}'")
        var_motivo_demissao = f"'{randint(18, 30)}'"

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_id_funcionario}', '{var_dt_admissao}', {var_dt_demissao}, {var_motivo_demissao}){var_sep}")


print("GO")
