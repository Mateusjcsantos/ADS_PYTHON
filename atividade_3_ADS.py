from logging import root
from tkinter import *

app = Tk()
app.title('CÁLCULO DE IMC   ÍNDICE DE MASSA CORPORAL')
app.geometry('450x230')
app.configure(bg='white')

#Função Sair
def sair():
    app.destroy()

#Função Calcular
def calculo():
    nome = retorno_nome.get()
    peso = float(retorno_peso.get())
    altura = float(retorno_altura.get())**2
    imc = round(peso / altura, 1)
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

# #Função limpar
def limpar():
    retorno_nome.delete(0, END)
    retorno_end.delete(0, END)
    retorno_altura.delete(0, END)
    retorno_peso.delete(0, END)


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
txtaltura = Label(app, text="Altura (cm)", bg='white', fg='black', anchor=W)
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
b_calcular.place(x=140, y=180, width=70, height=20)
b_reiniciar = Button(app,command=limpar, text="Reiniciar")
b_reiniciar.place(x=223, y=180, width=70, height=20)
b_sair = Button(app,command=sair, text="Sair")
b_sair.place(x=350, y=180, width=70, height=20)


app.mainloop()
