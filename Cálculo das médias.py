total=0
alunos = list()
médiasAD = list()
aprovadosD=list()
alunosExame = list()
médiasE = list()
aprovadosE = list()
médiasAE = list()
reprovados = list()
médiasR = list()
infoExame = list()


print('Digite o nome dos alunos. (Quando terminar digite "done")')
while True:
    stop = input()
    if stop == 'done':
        break
    else:
        alunos.append(stop)

print('CÁLCULO NP1 E NP2')
for aluno in alunos:
    total=0
    média=0
    n = 0
    print(f'Coloque as notas do {aluno}:')
    while n <2:
        nota = 0
        n = n +1
        nota = float(input())
        if nota>10:
            print('Nota inválida, coloque as 2 notas denovo')
            total=0
            média=0
            n = 0
            continue
        total = total + nota
    média = total/2
    if média >=7.0: 
        médiasAD.append(média)
        aprovadosD.append(aluno)
        print(f'{aluno},{média}, APROVADO')
    else:
        alunosExame.append(aluno)
        médiasE.append(média)
        print(f'{aluno},{média}, EXAME')


infoExame.append(alunosExame)
infoExame.append(médiasE)

print('CÁLCULO EXAME')
nn=0
for aluno in infoExame[0]:
    notaE = float(input(f'Nota do Exame do {aluno}: '))
    média = (infoExame[1][-1+nn] + notaE)/2
    if média >=5.0: 
        médiasAE.append(média)
        aprovadosE.append(aluno)
        print(f'{aluno},{média}, APROVADO')
    else:
        reprovados.append(aluno)
        médiasR.append(média)
        print(f'{aluno},{média}, REPROVADO')


print('RESUMO') 
print(f'{str(aprovadosD)[1:-1]} foi/foram aprovados direto com,{str(médiasAD)[1:-1]} de média respectivamente')
print(f'{str(aprovadosE)[1:-1]} foi/foram aprovados depois do exame com, {str(médiasAE)[1:-1]} de média respectivamente')
print(f'{str(reprovados)[1:-1]} foi/foram reprovados com, {str(médiasR)[1:-1]} de média respectivamente')
print('Dos,',len(alunos),'alunos ', int(len(aprovadosD))/int(len(alunos))*100,'% passaram direto, ',int(len(aprovadosE))/int(len(alunos))*100,'% passaram com a ajuda do exame e ',int(len(reprovados))/int(len(alunos))*100,'%, reprovaram')