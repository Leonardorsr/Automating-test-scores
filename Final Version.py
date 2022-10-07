#STATUS
#Conversão para dict-Completo.
#Inclusão do JSON - 100%
#Inclusão do Pandas-Completo


#Início- Imports e variáveis declaradas
import json
import requests
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
c=0
#FIM- Imports e variáveis declaradas

#Início- Funções do manuseio das informações
def dhi(nome):
    datahandle["Nome"]=nome
    datahandle["NP1"]=0
    datahandle["NP2"]=0
    datahandle["Exame"]="Nulo"
    datahandle["NPE"]=0
    datahandle["Média"]=0
    datahandle["Situação"]="Nulo"
    alunos.append(datahandle.copy())

def dh(c,i,nota1,nota2,média,notae):
    r4=0
    if c == 1:
        r4="NÃO"
        notae="Nulo"
        stc="APROVADO"     
    elif c == 2:
        r4="SIM"
        notae="Nulo"
        stc="Nulo"
    elif c == 3:
        r4="SIM"
        nota1=i["NP1"]
        nota2=i["NP2"]
        stc="APROVADO"
    elif c == 4:
        r4="SIM"
        nota1=i["NP1"]
        nota2=i["NP2"]
        stc="REPROVADO" 
    datahandle["Nome"]=i["Nome"]
    datahandle["NP1"]=nota1
    datahandle["NP2"]=nota2
    datahandle["Exame"]=r4
    datahandle["NPE"]=notae
    datahandle["Média"]=média
    datahandle["Situação"]=stc
#FIM- Funções do manuseio das informações

#Código principal
r1=input('Qual classe sera atualizada/criada? ')
r2=int(input('A tabela excel será atualizada ou criada? (0 ou 1 respectivamente) '))
if r2==0:
    arquivo=input('Digite o nome do arquivo. (Não esqueça do sufixo, ".xlsx") ')
    tabela_df=pd.read_excel(arquivo)
    for nome in tabela_df["Nome"]:
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
    notae=0
    print(f'Coloque as notas do {i["Nome"]}:')
    nota1 = float(input())
    nota2 = float(input())
    média = (nota1+nota2)/2
    if média >=7.0:
        c=1
        dh(c,i,nota1,nota2,média,notae)
        alunosap.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, APROVADO')
    else:
        c=2
        dh(c,i,nota1,nota2,média,notae)
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
        c=3
        dh(c,i,nota1,nota2,média,notae)
        alunosap.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')
    else:
        c=4
        dh(c,i,nota1,nota2,média,notae)
        alunosrep.append(datahandle.copy())
        #print(f'{datahandle["Nome"]},{datahandle["Média"]}, {datahandle["Situação"]}')
#FIM- Código Principal

#Início-Criação/atualização da tabela
tabelaap=pd.DataFrame(alunosap)
tabelarep=pd.DataFrame(alunosrep)
tabela_df=pd.concat([tabelaap,tabelarep], ignore_index=True)
print(tabela_df)
tabela_df.to_excel(arquivo)
#FIM-Criação/atualização da tabela

#Início-Criação/atualização da api
r5=input('Qual o link da api')
classe[r1]=alunosap,alunosrep
api=json.dumps(classe)
requests.post(r5,api)
#FIM-Criação/atualização da api

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
