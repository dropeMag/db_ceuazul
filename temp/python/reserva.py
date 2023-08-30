from random import randint, choice
from datetime import datetime, timedelta

print("INSERT INTO [scReserva].[Reserva] (data_checkin, data_checkou, funcion_checkin,\
 funcion_checkout, hospede_principal, num_hospede, id_quarto, tipo_pagamento, tipo_contato,\
  valor_total, status, cancelamento)\nVALUES")

var_data = datetime(2020, 1, 1)
var_quarto = 0

for var_x in range(1000):
    if var_quarto == 8:
        var_quarto = 1
        var_data += timedelta(days=5)
    else:
        var_quarto += 1

    var_data_checkin = var_data
    var_data_checkou = var_data + timedelta(days=5)
    var_funcion_checkin = randint(10, 999)
    var_funcion_checkout = randint(10, 999)
    var_hospede_principal = var_x + 3
    var_num_hospede = randint(1, 5)
    var_id_quarto = var_quarto
    var_tipo_pagamento = randint(1, 4)
    var_tipo_contato = randint(1, 6)
    var_valor_total = randint(1111, 9999)
    var_status = 0
    var_cancelamento = choice(['NULL', randint(1, 8)])

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"('{var_data_checkin}', '{var_data_checkou}', '{var_funcion_checkin}', '{var_funcion_checkout}', '{var_hospede_principal}', '{var_num_hospede}', '{var_id_quarto}', '{var_tipo_pagamento}', '{var_tipo_contato}', '{var_valor_total}', '{var_status}', '{var_cancelamento}'){var_sep}")


print("GO")