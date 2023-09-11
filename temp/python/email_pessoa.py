from random import randint, choice

lst_letras = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'b', 'n', 'm')
lst_emails = list()

print("INSERT INTO [scPessoa].[Email] (email)\nVALUES")

for var_x in range(1000):
    var_email = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{randint(0, 99999)}@gmail.com')

    while var_email in lst_emails:
        var_email = str(f'{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{choice(lst_letras)}{randint(0, 99999)}@gmail.com')

    lst_emails.append(var_email)

    if var_x != 999:
        var_sep = ','
    else:
        var_sep = ''

    print(f"    ('{var_email}'){var_sep}")


print("GO")