from random import randint, choice, uniform

print("INSERT INTO [scReserva].[Reserva_Servico] (id_reserva, id_servico, num_solicitacao)\nVALUES")

for var_x in range(1000):
    var_id_reserva = var_x + 2004
    var_id_servico = randint(2, 5)
    var_num_solicitacao = randint(1, 3)

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_id_reserva}', '{var_id_servico}', '{var_num_solicitacao}'){var_sep}")


print("GO")