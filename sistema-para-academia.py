class Aluno:
    nome = None
    cpf = None
    peso = 0
    altura = 0
    imc = 0
    status = False

class Exercicio:
    nome = None
    reps = 0
    series = 0
    carga = 0 

alunos = []
treinos = []

def validaCPF(cpf):
    numbers = list(map(int, cpf))

    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

def calculaIMC(peso, altura):
    return peso / altura ** 2

def cadastroAluno(nome, cpf, peso, altura):
    global alunos
    cpf = cpf

    while not validaCPF(cpf):
        cpf = input("CPF inválido, digite novamente:\n")

    aluno = Aluno()
    aluno.nome = nome
    aluno.cpf = cpf
    aluno.peso = peso
    aluno.altura = altura
    aluno.imc = calculaIMC(peso, altura)

    alunos.append(aluno)
    treinos.append([])

    print('Aluno cadastrado com sucesso!')

def menuPrincipal():
    print('----------------------------')
    print('Sistema Academia Morte Ativa')
    print('----------------------------')
    print('Selecione a opção desejada:')
    print('1 - Cadastrar aluno')
    print('2 - Gerenciar treino')
    print('3 - Consultar aluno')
    print('4 - Atualizar cadastro do aluno')
    print('5 - Excluir aluno')
    print('6 - Relatório de alunos')
    print('7 - Encerrar execução')
    print('----------------------------')

def printAluno(aluno):
    print('----------------------------')
    print(f"Aluno: {aluno.nome}")
    print(f"CPF: {aluno.cpf}")
    print(f"Peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")
    print(f"IMC: {aluno.imc}")
    print(f"Status: {aluno.status}")
    print()
    
def printExercicio(exercicio):
    print('----------------------------')
    print(f"Exercício: {exercicio.nome}")
    print(f"{exercicio.series} x {exercicio.reps}")
    print(f"{exercicio.carga}kg")
    print()    

def gerarRelatorio(tipo):
    if(tipo==1):
        for aluno in alunos:
            printAluno(aluno)
    if(tipo==2):
        for aluno in alunos:
            if aluno.status:
                printAluno(aluno)
    if(tipo==3):
        for aluno in alunos:
            if not aluno.status:
                printAluno(aluno)

def encontraAluno(nome):
    global alunos
    
    for i in range(len(alunos)):
        if(alunos[i].nome.casefold() == nome.casefold()):
            return [alunos[i], i]
    return [None, False]

def encontraExercicio(index, nome):
    global treinos
    treino = treinos[index]
    for i in range(len(treino)):
        if(treino[i].nome.casefold() == nome.casefold()):
            return [treino[i], i]
    return [None, False]

cadastroAluno('Julio', '97769164737', 72.2, 1.78)

while True:
    menuPrincipal()
    opc = int(input())
    print('----------------------------')
    
    if opc == 1:
        nome = input("Insira o nome: ")
        cpf = input("Insira o CPF: ")
        peso = float(input("Insira o peso: "))
        altura = float(input("Insira o altura: "))
        cadastroAluno(nome, cpf, peso, altura)
        
    if opc == 2:
        nome = input('Insira o nome do aluno a ser consultado:\n')
        print('----------------------------')
        aluno, i = encontraAluno(nome)
        print('Selecione a opção desejada:')
        print('1 - Incluir/Alterar exercício')
        print('2 - Excluir um exercício')
        print('3 - Excluir todos os exercícios')
        opc = int(input())
        if opc == 1:
            if(len(treinos[i]) <= 10):
                nome = input('Insira o nome do exercício:\n')
                print('----------------------------')
                exercicio, j = encontraExercicio(i, nome)
                series = int(input("Insira a quantidade de séries: "))
                reps = int(input("Insira a quantidade de repetições: "))
                carga = float(input("Insira a carga: "))
                
                if exercicio: 
                    exercicio.series = series
                    exercicio.reps = reps
                    exercicio.carga = carga
                    treinos[i][j] = exercicio
                else:
                    novoExercicio = Exercicio()
                    novoExercicio.nome = nome
                    novoExercicio.series = series
                    novoExercicio.reps = reps
                    novoExercicio.carga = carga
                    treinos[i].append(novoExercicio)
                    aluno.status = True
                    alunos[i] = aluno
            else: 
                print('Limite de exercícios alcançado!') 
        if opc == 2:
            nome = input('Insira o nome do exercício a ser excluido:\n')
            print('----------------------------')
            exercicio, j = encontraExercicio(i, nome)
            if exercicio: 
                treinos[i].pop(j)
                print('Exercício deletado com sucesso!')
                if(len(treinos[i]) == 0):
                    aluno.status = False
                    alunos[i] = aluno
            else:
                print('Exercício não encontrado!')
        if opc == 3:
            treinos[i].clear()
            aluno.status = False
            alunos[i] = aluno
        
    
    if opc == 3:
        nome = input('Insira o nome do aluno a ser consultado:\n')
        print('----------------------------')
        aluno, i = encontraAluno(nome)
        if aluno: 
            printAluno(aluno)
            treino = treinos[i]
            for exercicio in treino:
                printExercicio(exercicio)
        else:
            print('Aluno não encontrado!')
    
    if opc == 4:
        nome = input('Insira o nome do aluno a ser atualizado:\n')
        print('----------------------------')
        aluno, i = encontraAluno(nome)
        if aluno: 
            print("Para manter os dados anteriores não informe dados")
            nome = input("Insira o nome: ")
            cpf = input("Insira o CPF: ")
            if(cpf and not validaCPF(cpf)):
                while not validaCPF(cpf):
                    cpf = input("CPF inválido, digite novamente:\n")
            
            peso = input("Insira o peso: ")
            altura = input("Insira o altura: ")

            if(nome):
                aluno.nome = nome
            if(cpf):
                aluno.cpf = cpf
            if(peso):
                aluno.peso = float(peso)
            if(altura):
                aluno.altura = float(altura)
                
            aluno.imc = calculaIMC(aluno.peso, aluno.altura)
            alunos[i] = aluno
            print('Aluno atualizado com sucesso!')
        else:
            print('Aluno não encontrado!')
    
    if(opc == 5):
        nome = input('Insira o nome do aluno a ser excluido:\n')
        print('----------------------------')
        aluno, i = encontraAluno(nome)
        if aluno: 
            alunos.pop(i)
            treinos.pop(i)
            print('Aluno deletado com sucesso!')
        else:
            print('Aluno não encontrado!')
    
    if(opc == 6):
        print('Selecione a opção desejada:')
        print('1 - Todos os alunos')
        print('2 - Alunos ativos')
        print('3 - Alunos inativos')
        gerarRelatorio(int(input()))
    
    if(opc == 7):
        print('Obrigado por usar o Sistema Academia Morte Ativa')
        break