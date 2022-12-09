########## CRIANDO BANCO DE DADOS
import sqlite3

conn = sqlite3.connect("imc_database.db")
cursor = conn.cursor()

#Criando as tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS PACIENTE (Id_cad INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Nome TEXT, Endereco TEXT, Peso NUMERIC, Altura NUMERIC, Imc NUMERIC, Status TEXT);
""")
print("Conectado ao banco de dados")


########## INTERFACE GRÁFICA E FUNÇÕES
from logging import root
from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('CÁLCULO DE IMC   ÍNDICE DE MASSA CORPORAL')
app.geometry('450x230')
app.configure(bg='WHITE')

#Função Sair
def sair():
    app.destroy()

#Função Calcular
def calculo():
    nome = str(retorno_nome.get())
    endereco = str(retorno_end.get())
    peso = float(retorno_peso.get())
    altura = float(retorno_altura.get())
    alt = float(altura ** 2)
    imc = round(peso / alt, 1)
    fimc = imc

    if fimc < 18.5:
       resultado_texto['text'] = 'ABAIXO DO PESO'
    if fimc > 18.5 and fimc < 24.9:
       resultado_texto['text'] = 'PESO IDEAL'
    if fimc > 25 and fimc < 29.9:
       resultado_texto['text'] = 'SOBREPESO'
    if fimc > 30 and fimc < 34.9:
       resultado_texto['text'] = 'OBESIDADE GRAU I'
    if fimc > 35 and fimc < 39.9:
       resultado_texto['text'] = 'OBESIDADE GRAU II'
    if fimc > 40:
       resultado_texto['text'] = 'OBESIDADE GRAU III'

    resultado['text']=fimc

    return nome, endereco, peso, altura, fimc, resultado_texto['text']

#Função Salvar Inserindo dados na tabela
def salvar():
    nome, endereco, peso, altura, fimc, status = calculo()
    conn = sqlite3.connect("imc_database.db")
    cursor = conn.cursor()
    query = f"INSERT INTO PACIENTE (Nome, Endereco, Peso, Altura, Imc, Status) \
            VALUES ('{nome}', '{endereco}', {peso}, {altura}, '{fimc}', '{status}')"
    cursor.execute(query)
    conn.commit()
    messagebox.showinfo(title='Registro info', message='Registro salvo com sucesso')

    queryselect = "SELECT * FROM PACIENTE"
    cursor.execute(queryselect)
    res = cursor.fetchall()
    for i in res:
        print('\n')
        for v in i:
            print(v, end=' ')
    conn.close()

#Função limpar
def limpar():
    retorno_nome.delete(0, END)
    retorno_end.delete(0, END)
    retorno_altura.delete(0, END)
    retorno_peso.delete(0, END)
    resultado_texto['text'] = ''
    resultado['text'] = ''

# caixa texto nome
txtnome = Label(app, text="Nome do Paciente:", bg='white', fg='black', anchor=W)
txtnome.place(x=10, y=30, width=120, height=20)
retorno_nome = Entry(app,bg='light gray', fg='black')
retorno_nome.place(x=150, y=30, width=250, height=20)

# caixa texto Endereço
txtend = Label(app, text="Endereço Completo:", bg='white', fg='black', anchor=W)
txtend.place(x=10, y=60, width=120, height=20)
retorno_end = Entry(app,bg='light gray', fg='black')
retorno_end.place(x=150, y=60, width=250, height=20)

# caixa texto altura
txtaltura = Label(app, text="Altura (Metros)", bg='white', fg='black', anchor=W)
txtaltura.place(x=10, y=90, width=120, height=20)
retorno_altura = Entry(app,bg='light gray', fg='black')
retorno_altura.place(x=150, y=90, width=100, height=20)

# caixa texto peso
txtpeso = Label(app, text="Peso (Kg)", bg='white', fg='black', anchor=W)
txtpeso.place(x=10, y=120, width=120, height=20)
retorno_peso = Entry(app,bg='light gray', fg='black')
retorno_peso.place(x=150, y=120, width=100, height=20)

#janela de resultado
resultado = Label(app,bg='gray', fg='black',font= ('arial',15))
resultado.place(x=260, y=125, width=140, height=35)
resultado_texto = Label(app, text='',bg='gray', fg='black',font= ('arial', 10))
resultado_texto.place(x=260, y=90, width=140, height=35)

#botões
b_calcular = Button(app, command=calculo, text="Calcular")
b_calcular.place(x=120, y=180, width=70, height=20)
b_reiniciar = Button(app,command=limpar, text="Reiniciar")
b_reiniciar.place(x=192, y=180, width=70, height=20)
b_sair = Button(app,command=sair, text="Sair")
b_sair.place(x=350, y=180, width=70, height=20)
b_salvar = Button(app,command=salvar, text="Salvar")
b_salvar.place(x=278, y=180, width=70, height=20)

app.mainloop()
