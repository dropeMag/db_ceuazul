from random import randint

print("INSERT INTO [scHospede].[Estadia] (id_hospede, id_reserva)\nVALUES")

for var_x in range(1000):
    var_id_hospede = var_x + 4
    var_id_reserva = var_x + 2004

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_id_hospede}', '{var_id_reserva}'){var_sep}")


print("GO")
