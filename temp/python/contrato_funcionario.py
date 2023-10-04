from random import randint, choice

print("INSERT INTO [scFuncionario].[Contrato] (funcionario_id, dt_admissao, \
cargo_id, salario, vale_alimentacao, vale_transporte, \
dt_demissao, demissao_id)\nVALUES")

cnt_1 = 1000

for var_x in range(500):
    var_id_funcionario = cnt_1
    cnt_1 += 1
    var_dt_admissao = str(f'{randint(2016, 2019)}-{randint(1, 12)}-{randint(1, 28)}')

    if var_id_funcionario < 321:
        var_dt_demissao = "NULL"
        var_motivo_demissao = "NULL"
    else:
        var_dt_demissao = str(f"'{randint(2020, 2022)}-{randint(1, 12)}-{randint(1, 28)}'")
        var_motivo_demissao = f"'{randint(1, 13)}'"

    var_cargo_id = randint(1, 24)
    var_salario = randint(2000, 8000)
    var_vale_alimentacao = choice([f"'{randint(400, 800)}'", "NULL"])
    var_vale_transporte = choice([f"'{randint(200, 400)}'", "NULL"])

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_id_funcionario}', '{var_dt_admissao}', '{var_cargo_id}', '{var_salario}', {var_vale_alimentacao}, {var_vale_transporte}, {var_dt_demissao}, {var_motivo_demissao}){var_sep}")


print("GO")
