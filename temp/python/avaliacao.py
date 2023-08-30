from random import randint, choice, uniform

print("INSERT INTO [scComodo].[Avaliacao] (tipo_contato, id_reserva, conforto,\
 custo_beneficio, funcionarios, localizacao, limpeza)\nVALUES")

for var_x in range(1000):
    var_tipo_contato = randint(1, 6)
    var_id_reserva = var_x + 2004
    var_conforto = choice(["NULL", f"{uniform(4.0, 10.0):.2}"])
    var_custo_beneficio = choice(["NULL", f"{uniform(4.0, 10.0):.2}"])
    var_funcionarios = choice(["NULL", f"{uniform(4.0, 10.0):.2}"])
    var_localizacao = choice(["NULL", f"{uniform(4.0, 10.0):.2}"])
    var_limpeza = choice(["NULL", f"{uniform(4.0, 10.0):.2}"])

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_tipo_contato}', '{var_id_reserva}', {var_conforto}, {var_custo_beneficio}, {var_funcionarios}, {var_localizacao}, {var_limpeza}){var_sep}")


print("GO")
