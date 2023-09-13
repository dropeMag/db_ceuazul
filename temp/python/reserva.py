from random import randint, choice
from datetime import datetime, timedelta

print("INSERT INTO [scReserva].[Reserva] (data_checkin, data_checkout, funcion_checkin,\
 funcion_checkout, hospede_principal, num_hospede, id_quarto, id_pagamento, id_contato,\
  valor_total, status, id_cancelamento)\nVALUES")

var_data = datetime(2024, 1, 1)
cnt_dias = randint(1, 7)
cnt_quarto = 0

for var_x in range(700):
    if cnt_quarto == 30:
        cnt_quarto = 1
        var_data = var_data + timedelta(days=cnt_dias + 1)
        cnt_dias = randint(1, 7)
    else:
        cnt_quarto += 1

    var_data_checkin = var_data
    var_data_checkout = var_data + timedelta(days=cnt_dias)
    var_funcion_checkin = randint(21, 320)

    if var_x < 500:
        var_hospede_principal = var_x + 1
    else:
        var_hospede_principal = var_x - 499

    var_num_hospede = 1
    var_id_quarto = cnt_quarto
    var_id_contato = randint(1, 6)
    var_status = 0
    var_id_cancelamento = choice(['NULL', f"'{randint(1, 8)}'"])

    if var_id_cancelamento != 'NULL':
        var_funcion_checkout = 'NULL'
        var_valor_total = 'NULL'
        var_id_pagamento = 'NULL'
    else:
        var_funcion_checkout = f"'{randint(21, 320)}'"
        var_valor_total = f"'{randint(1111, 9999)}'"
        var_id_pagamento = f"'{randint(1, 4)}'"

    if var_x != 699:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_data_checkin}', '{var_data_checkout}', '{var_funcion_checkin}', {var_funcion_checkout}, '{var_hospede_principal}', '{var_num_hospede}', '{var_id_quarto}', {var_id_pagamento}, '{var_id_contato}', {var_valor_total}, '{var_status}', {var_id_cancelamento}){var_sep}")


print("GO")