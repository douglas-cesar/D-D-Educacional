import principal

op = input('Digite Sim ou não:')
while (op != 'sim') and (op != 'não'):
    op = input('ERRROR! Digite Sim ou não:')
while (op == 'sim') or (op == 'não'):
    if op.lower() == 'sim':
        cpf = int(input('Informe o nome do CPF do aluno: '))
        nome = input('Nome do aluno:')
        data_nascimento = input('Data Nascimento:')
        cod_tur = input('Em qual turma deseja Cadastrar o aluno?')
        id_resp = input('Quem é o responsável:')
        principal.insert_aluno(cpf, nome, data_nascimento,cod_tur,id_resp)
        op = input('Digite Sim ou não')

    else:
        print('Ok, não cadastrar')
        break
