from random import randint

print("INSERT INTO [scHospede].[Hospede_Classe] (id_tp_hospede, id_hospede)\nVALUES")

for var_x in range(1000):
    var_id_tp_hospede = randint(1, 3)
    var_id_hospede = var_x + 4

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_id_tp_hospede}', '{var_id_hospede}'){var_sep}")


print("GO")
