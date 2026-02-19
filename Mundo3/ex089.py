while True:
    nome = str(input('Nome: '))
    nota_1 = int(input('Nota 1: '))
    nota_2 = int(input('Nota 2: '))
    media = nota_1 + nota_2

    want_continue = str(input('Deseja continuar[S/N]? ')).lower()
    if not want_continue.startswith('s'):
        break
    Show_Notes = int(input('Deseja olhar as notas de qual aluno? '))