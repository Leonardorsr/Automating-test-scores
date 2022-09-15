#STATUS
#Conversão para dict completa.
#Inclusão do JSON - 40%
#Inclusão do Pandas-60%

import pandas as pd
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
        datahandle["NP1"]=0
        datahandle["NP2"]=0
        datahandle["Exame"]="Nulo"
        datahandle["NPE"]=0
        datahandle["Média"]=0
        datahandle["Situação"]="Nulo"
        alunos.append(datahandle.copy())
print('CÁLCULO NP1 E NP2')
for i in alunos:
    total=0
    média=0
    n = 0
    print(f'Coloque as notas do {i["Nome"]}:')
    nota1 = 0
    nota2 = 0
    nota1 = float(input())
    nota2 = float(input())
    média = (nota1+nota2)/2
    if média >=7.0:
        datahandle["Situação"]="APROVADO"
        datahandle["Média"]=média
        datahandle["Nome"]=i["Nome"]
        datahandle["Exame"]="NÃO"
        datahandle["NP1"]=nota1
        datahandle["NP2"]=nota2
        alunosap.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, APROVADO')
    else:
        datahandle["Situação"]="Nulo"
        datahandle["Média"]=média
        datahandle["Nome"]=i["Nome"]
        datahandle["Exame"]="SIM"
        datahandle["NP1"]=nota1
        datahandle["NP2"]=nota2
        alunose.append(datahandle.copy())
        médiase.append(média)
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, EXAME')
print('CÁLCULO EXAME')
nn=-1
for i in alunose:
    nn+=1
    notae = float(input(f'Nota do Exame do {i["Nome"]}: '))
    média = (médiase[nn] + notae)/2
    if média >=5.0:
        datahandle["Situação"]="APROVADO"
        datahandle["Média"]=média
        datahandle["NPE"]=notae
        datahandle["NP1"]=i["NP1"]
        datahandle["NP2"]=i["NP2"]
        datahandle["Nome"]=i["Nome"]
        datahandle["Exame"]="SIM"
        alunosap.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')
    else:
        datahandle["Situação"]="REPROVADO"
        datahandle["Média"]=média
        datahandle["NPE"]=notae
        datahandle["NP1"]=i["NP1"]
        datahandle["NP2"]=i["NP2"]
        datahandle["Nome"]=i["Nome"]
        datahandle["Exame"]="SIM"
        alunosrep.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')          
tabelaap= pd.DataFrame(alunosap)
tabelarep=pd.DataFrame(alunosrep)
tabela_df=pd.concat([tabelaap,tabelarep], ignore_index=True)
print(tabela_df)
tabela_df.to_excel('tabela_teste.xlsx')
print('RESUMO')
print()
print('Foram APROVADOS')
for i in alunosap:
    print(f'Nome: {i["Nome"]}, Média: {i["Média"]}')
print()
print('Foram REPROVADO')
for i in alunosrep:
    print(f'Nome: {i["Nome"]}, Média: {i["Média"]}')
print('Dos,',len(alunos),'alunos ', round(int(len(alunosap))/int(len(alunos))*100),'% passaram e',round(int(len(alunosrep))/int(len(alunos))*100),'%, reprovaram')
