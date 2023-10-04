from random import randint, choice, uniform

print("INSERT INTO [scEstadia].[Reserva_Hospede] (id_reserva, id_hospede)\nVALUES")

cn = 1
cm = 701
for var_x in range(700):
    var_id_reserva = cm
    id_hospede = cn

    cn += 1
    cm += 1

    if cn == 501:
        cn = 1

    if var_x != 699:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_id_reserva}', '{id_hospede}'){var_sep}")


print("GO")
print(" ")
print(" ")




cm = 701

print("INSERT INTO [scEstadia].[Reserva_Servico] (id_reserva, id_servico, num_solicitacao, funcionario_id, dt_solicitacao)\nVALUES")

for var_x in range(700):
    var_id_reserva = cm
    var_id_servico = randint(1, 7)
    var_num_solicitacao = randint(1, 4)

    cm += 1

    if var_x != 699:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_id_reserva}', '{var_id_servico}', '{var_num_solicitacao}', '1000', '2020-05-05'){var_sep}")


print("GO")



print(" ")
print(" ")

cm = 701


print("INSERT INTO [scEstadia].[Reserva_Bar] (id_reserva, id_produto, num_pedidos)\nVALUES")

for var_x in range(700):
    var_id_reserva = cm
    var_id_servico = randint(1, 17)
    var_num_solicitacao = randint(1, 4)

    cm += 1

    if var_x != 699:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_id_reserva}', '{var_id_servico}', '{var_num_solicitacao}'){var_sep}")


print("GO")