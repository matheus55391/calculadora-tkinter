from tkinter import * # vem todo mundo 

# ======================================
# Documentation in Portuguese of Brazil
# ======================================


#
# Meu primeiro projeto TK
# estou aprendendo ainda então desculpa as cagadas :P kkk
# Calculadorazinha foda d+
#


tk = Tk() # iniciando a classe 


 #aqui tem um monte de função que faz oq diz fazer
def soma():
    return str(int(num1.get()) + int(num2.get()))
def subtrai():
    return str(int(num1.get()) - int(num2.get()))
def mult():
    return str(int(num1.get()) * int(num2.get()))
def div():
    return str(int(num1.get()) / int(num2.get()))


def bt_click(op): #quando o botão é clicado chama essa função
    resultado = str()
    
    if op == '+':
        resultado = str(soma())
    if op == '-':
        resultado = subtrai()
    if op == '*':
        resultado = mult()
    if op == '/':
        resultado = div()
    
    lb["text"] = resultado #converte o label para retornar o resultado



num1 = Entry(tk) #lugar onde vai ser colocado os 2 numeros
num2 = Entry(tk) # aqui é o segundo numero ta
num1.grid(row = 0, column = 1,columnspan = 5)
num2.grid(row = 2, column = 1,columnspan = 5)

# KKK ATE AQUI O CODIGO TA MT FODA NE MAS SE PREPARA PQ EU CONSEGUI FAZER UMA COISA MT PIKA ALI EMBAIXO KKKK
 
lb = Label(tk, text = 'Resultado = ')
lb.grid(row = 4, column = 1)
lb = Label(tk, text = '...')  #AQUI SÃO OS LABIOS 
lb.grid(row = 4, column = 2)

ops = ('+', '-', '/', '*')
c = 0 
for op in ops: #blz ta aqui a coisa foda, pesquisei um pouco e decidi usar o lambda para passar o botão
    # ai praticamente o lambda fica em um loop infinito ou sla um bglh foda que quando é clicado ele é chama a função
    # do click do botão que vai alterar o dereg jhonson la kkkk do karalho
    action = lambda x = op : bt_click(x)
    bt = Button(tk, text = op, command = action, width = 4, height = 2, relief = RAISED)
    bt.grid(row = 3, column = c)
    c += 1



#uns coiso do tk blablbal banana requeijao suco de uva sla to com fome são 23:16 do dia 06/01/2020 amanha tenhoe que trabalhar :p
tk.title('calculadora')
tk.geometry('200x100')
tk.mainloop()


#
# Feito por meguinha :D ou matheus55391 sla me chama como quiser
#