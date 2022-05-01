from tkinter import *
import random
from tkinter import messagebox
game = Tk()
game.title("WineLearning")
game.geometry("500x550")
game.configure(background = "#558")
#criar pares
#matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
#matches[0]
matches = {"Vinho Fino": "vitis vinifera", "Vinho de Mesa": "Vitis Labrusca", "Malbec": "Churrasco", "Sangiovese": "Pizza", "Sauvignon Blanc": "Frutos do Mar", "Vinho Verde": "Bacalhau" }
match_list = []
#randon_list = []
for k, v in matches.items():
    match_list.append(k)
    match_list.append(v)

print(matches)

#shuffle our matches
#randon_list = match_list
random.shuffle(match_list)
print(match_list)

#create button frame
my_frame = Frame(game)
my_frame.pack(pady=10)

#definição de variaveis
count= 0
answer_list = []
answer_dict = {}

#função para o click dos botoes
def button_click(b, number):
    global count, answer_list, answer_dict


    if b["text"] == '' and count < 2:
        b['text'] = match_list[number]
        #adicionar numero à answer list
        answer_list.append(match_list[number])
        #adicionar botao e numero ao Answer dict
        answer_dict[b] = match_list[number]
        #incrementar contador
        count += 1

    #determinar certo ou errado
    if len(answer_list) == 2:
        print(answer_list[0])
        print(answer_list[1])
        if answer_list[0] and answer_list[1] in matches.items(k,v):
            print ('AQUI')
            my_label.config(text= "Match!!")

            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
        else:
            my_label.config (text = 'OOPS!!')
            count = 0
            answer_list = []
            #pop up box
            messagebox.showinfo("ERROU!", "ERROU!")
        #reset buttons
        for key in answer_dict:
            key["text"] = ""

        answer_dict = {}

#define our buttons
b0= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b0, 0))
b1= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b1, 1))
b2= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b2, 2))
b3= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b3, 3))
b4= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b4, 4))
b5= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b5, 5))
b6= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b6, 6))
b7= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b7, 7))
b8= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b8, 8))
b9= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b9, 9))
b10= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b10, 10))
b11= Button(my_frame, text="", font=('Helvetica', 10), height = 10, width=10, command = lambda: button_click(b11, 11))

#grid our buttons

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(game, text = '')
my_label.pack(pady=20)

game.mainloop()