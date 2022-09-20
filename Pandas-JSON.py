#STATUS
#Conversão para dict-Completo.
#Inclusão do JSON - 70%
#Inclusão do Pandas-Completo

import json
import pandas as pd
alunos = []
datahandle= {}
alunose= []
alunosap= []
alunosrep= []
médiase=[]
nomes=[]
arquivo='info.xlsx'
classe={}
r1=input('Qual classe sera atualizada/criada? ')

r2=int(input('A tabela excel será atualizada ou criada? (0 ou 1 respectivamente) '))
def dhi(nome):
    datahandle["Nome"]=nome
    datahandle["NP1"]=0
    datahandle["NP2"]=0
    datahandle["Exame"]="Nulo"
    datahandle["NPE"]=0
    datahandle["Média"]=0
    datahandle["Situação"]="Nulo"
    alunos.append(datahandle.copy())
def dhap(média,nota1,nota2,i,r4):
    datahandle["Situação"]="APROVADO"
    datahandle["Média"]=média
    datahandle["Nome"]=i["Nome"]
    datahandle["Exame"]=r4
    datahandle["NP1"]=nota1
    datahandle["NP2"]=nota2
    alunosap.append(datahandle.copy())
def dhe(média,nota1,nota2,i,r4):
    datahandle["Situação"]="Nulo"
    datahandle["Média"]=média
    datahandle["Nome"]=i["Nome"]
    datahandle["Exame"]=r4
    datahandle["NP1"]=nota1
    datahandle["NP2"]=nota2
    alunose.append(datahandle.copy())
    médiase.append(média)
def dhrep(média,notae,i):
    datahandle["Situação"]="REPROVADO"
    datahandle["Média"]=média
    datahandle["NPE"]=notae
    datahandle["NP1"]=i["NP1"]
    datahandle["NP2"]=i["NP2"]
    datahandle["Nome"]=i["Nome"]
    datahandle["Exame"]="SIM"
    alunosrep.append(datahandle.copy())
    
if r2==0:
    arquivo=input('Digite o nome do arquivo. (Não esqueça do sufixo, ".xlsx") ')
    tabela_df=pd.read_excel(arquivo)
    for i in tabela_df["Nome"]:
        nomes.append(i)
    print(nomes)
    for nome in nomes:          
        dhi(nome)
    #print(alunos)
r3=input('Algum novo aluno será adicionado? (s ou n repectivamente) ')
if r3=='s' or r2==1: 
    print('Digite o nome dos alunos. (Quando terminar digite "done")')
    while True:
        nome = input()
        if nome == 'done'or nome =='DONE'or nome=='Done':
            break
        else:
            dhi(nome)
    #print(alunos)
    
print('CÁLCULO NP1 E NP2')
for i in alunos:
    total=0
    média=0
    n = 0
    print(f'Coloque as notas do {i["Nome"]}:')
    nota1 = float(input())
    nota2 = float(input())
    média = (nota1+nota2)/2
    if média >=7.0:
        r4="NÃO"
        dhap(média,nota1,nota2,i,r4)
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, APROVADO')
    else:
        r4="SIM"
        dhe(média,nota1,nota2,i,r4)
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
        dhrep(média,notae,i)
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')
        
                
tabelaap=pd.DataFrame(alunosap)
tabelarep=pd.DataFrame(alunosrep)
tabela_df=pd.concat([tabelaap,tabelarep], ignore_index=True)
print(tabela_df)
tabela_df.to_excel(arquivo)
classe[r1]=alunosap,alunosrep
api=json.dumps(classe)
print(api)

print('RESUMO')
print()
print('Foram APROVADOS')
for i in alunosap:
    print(f'Nome: {i["Nome"]}, Média: {i["Média"]}')
print()
print('Foram REPROVADOS')
for i in alunosrep:
    print(f'Nome: {i["Nome"]}, Média: {i["Média"]}')
print('Dos,',len(alunos),'alunos ', round(int(len(alunosap))/int(len(alunos))*100),'% passaram e',round(int(len(alunosrep))/int(len(alunos))*100),'%, reprovaram')
