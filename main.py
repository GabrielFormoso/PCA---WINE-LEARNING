from tkinter import *
import random
from tkinter import messagebox
game = Tk()
game.title('Wine Learning')
game.geometry('800x600')
game.wm_iconbitmap('imagens/Food_and_cheese.ico')
game.configure(background = '#581d22')
#Não permite mudar o tamanho da janela
game.resizable(False,False)

#Label de boas vindas
my_label = Label(game, text = 'Aprenda a Harmonizar vinhos de forma simples!', bg= '#ff6633',bd = 8.5, relief="solid", font=('comic sans ms', 24),)
my_label.pack(pady = 30,)

#criar pares
matches = {'Vinho do Porto': 'Brownie', 'Pinot Noir': 'Fillet Mignon', 'Malbec': 'Churrasco', 'Sangiovese': 'Pizza', 'Sauvignon Blanc': 'Frutos do Mar', 'Vinho Verde': 'Bacalhau'}
match_list = []
for k, v in matches.items():
    match_list.append(k)
    match_list.append(v)

random.shuffle(match_list)

#create button frame
my_frame = Frame(game)
my_frame.pack(pady=10)
my_frame.configure(background = '#f00')

#definição de variaveis
count = 0
corretas = 0
answer_list = []
answer_dict = {}


def acerto():
    global count, corretas, answer_list, answer_dict
    for key in answer_dict:
        key['state'] = 'disabled'
    count = 0
    answer_list = []
    answer_dict = {}
    corretas += 2


def erro():
    global count, answer_list
    count = 0
    answer_list = []

#função para o click dos botoes
def button_click(b, number):
    global count, corretas, answer_list, answer_dict

    if b['text'] == '' and count < 2:
        b['text'] = match_list[number]
        #adicionar numero à answer list
        answer_list.append(match_list[number])
        #adicionar botao e numero ao Answer dict
        answer_dict[b] = match_list[number]
        #incrementar contador
        count += 1

    #determinar certo ou errado
    if len(answer_list) == 2:
        if answer_list[0] in matches:
            #1o - Tipo de Vinho
            if answer_list[1] in matches:
                #2o - Tipo de Vinho
                messagebox.showinfo('INCORRETO!', 'Você selecionou dois tipos de vinho!')
                erro()
            else:
                #2o Acompanhamento
                if matches[answer_list[0]] == answer_list[1]:
                    messagebox.showinfo('PARABÉNS!', '{} com {} combinam muito bem!' .format(answer_list[0], answer_list[1]))
                    acerto()
                else:
                    messagebox.showinfo('INCORRETO!', 'Essa não é a melhor combinação!')
                    erro()
        else:
            #1o Acompanhamento
            if answer_list[1] in matches:
                #2o - Tipo de Vinho
                if matches[answer_list[1]] == answer_list[0]:
                    messagebox.showinfo('PARABÉNS!', '{} com {} combinam muito bem!' .format(answer_list[1], answer_list[0]))
                    acerto()
                else:
                    messagebox.showinfo('INCORRETO!', 'Essa não é a melhor combinação!')
                    erro()
            else:
                #2o Acompanhamento
                messagebox.showinfo('INCORRETO!', 'Você selecionou dois tipos de acompanhamento!')
                erro()

        for key in answer_dict:
            key['text'] = ''
        answer_dict = {}

    if corretas == 12:
        messagebox.showinfo('PARABÉNS!', 'Você completou todas as combinações!')

#define our buttons
b0 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b0, 0))
b1 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b1, 1))
b2 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b2, 2))
b3 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b3, 3))
b4 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b4, 4))
b5 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b5, 5))
b6 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b6, 6))
b7 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b7, 7))
b8 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b8, 8))
b9 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b9, 9))
b10 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b10, 10))
b11 = Button(my_frame, text ='',bg = '#ff6633', font=('comic sans ms', 12), height = 6, width = 12, command = lambda: button_click(b11, 11))

#grid our buttons

b0.grid(row = 0, column = 0)
b1.grid(row = 0, column = 1)
b2.grid(row = 0, column = 2)
b3.grid(row = 0, column = 3)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)
b7.grid(row = 1, column = 3)

b8.grid(row = 2, column = 0)
b9.grid(row = 2, column = 1)
b10.grid(row = 2, column = 2)
b11.grid(row = 2, column = 3)


game.mainloop()
