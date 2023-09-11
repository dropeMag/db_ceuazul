from random import randint

print("INSERT INTO [scHospede].[Hospede_Classe] (id_hospede, id_tp_hospede)\nVALUES")

cnt_1 = 1

for var_x in range(500):
    var_id_tp_hospede = randint(1, 3)
    var_id_hospede = cnt_1
    cnt_1 += 1

    if var_x != 499:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_id_hospede}', '{var_id_tp_hospede}'){var_sep}")


print("GO")
