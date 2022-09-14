#STATUS
#Conversão para dict completa.
#Inclusão de Pandas e JSON - 30%

alunos = []
datahandle= {}
alunose= []
alunosap= []
alunosrep= []
médiase=[]


print('Digite o nome dos alunos. (Quando terminar digite "done")')
while True:
    stop = input()
    try:
        str(stop)
    except:
        print('Nome inválido')
        continue
    if stop == 'done' or stop=='DONE'or stop=='Done':
        break
    else:
        datahandle["Nome"]=stop
        datahandle["Média"]=0
        datahandle["Situação"]="Nulo"
        alunos.append(datahandle.copy())
        print(alunos)
print('CÁLCULO NP1 E NP2')
for i in alunos:
    total=0
    média=0
    n = 0
    print(f'Coloque as notas do {i["Nome"]}:')
    while n <2:
        nota = 0
        n = n +1
        try:
            nota = float(input())
            if nota>10 or nota <0:
                print('Nota inválida, coloque as 2 notas denovo')
                n=0
                continue
        except:
            print('Nota inválida, coloque as 2 notas denovo')
            n=0
            continue  
        total = total + nota
    média = total/2
    if média >=7.0:
        datahandle['Situação']='APROVADO'
        datahandle['Média']=média
        datahandle['Nome']=i["Nome"]
        alunosap.append(datahandle.copy())
        print(f'{datahandle["Nome"]},{datahandle["Média"]}, APROVADO')
    else:
        datahandle['Situação']='EXAME'
        datahandle['Média']=média
        datahandle['Nome']=i["Nome"]
        alunose.append(datahandle.copy())
        médiase.append(média)
        print(f'{datahandle["Nome"]},{datahandle["Média"]}, EXAME')
print('CÁLCULO EXAME')
nn=-1
for i in alunose:
    nn+=1
    notaE = float(input(f'Nota do Exame do {i["Nome"]}: '))
    média = (médiase[nn] + notaE)/2
    if média >=5.0:
        datahandle["Situação"]="APROVADO"
        datahandle["Média"]=média
        datahandle["Nome"]=i["Nome"]
        alunosap.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')
    else:
        datahandle["Situação"]="REPROVADO"
        datahandle["Média"]=média
        datahandle["Nome"]=i["Nome"]
        alunosrep.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')          
#print(alunosap)
#print()
#print(alunosrep[0])

print('RESUMO')
print()
print('Foram APROVADOS')
for i in alunosap:
    print(f'Nome: {i["Nome"]} Média: {i["Média"]}')
print()
print('Foram APROVADOS')
for i in alunosrep:
    print(f'Nome: {i["Nome"]} Média: {i["Média"]}')
print('Dos,',len(alunos),'alunos ', round(int(len(alunosap))/int(len(alunos))*100,1),'% passaram direto, e,', round(int(len(alunosrep))/int(len(alunos))*100),'%, reprovaram')