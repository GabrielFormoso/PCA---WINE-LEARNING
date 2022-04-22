from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("WineLearning")
root.geometry("500x550")

#criar pares
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
matches[0]
#shuffle our matches
random.shuffle(matches)

#create button frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#definição de variaveis
count= 0
answer_list = []
answer_dict = {}

#função para o click dos botoes
def button_click(b, number):
    global count, answer_list, answer_dict


    if b["text"] == '' and count < 2:
        b['text'] = matches[number]
        #adicionar numero à answer list
        answer_list.append(number)
        #adicionar botao e numero ao Answer dict
        answer_dict[b] = matches[number]
        #incrementar contador
        count += 1

    #determinar certo ou errado
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text= "Match!!")
            #messagebox.showinfo("Correct", "WOW!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
        else:
            my_label.config (text = 'Doh!!')
            count = 0
            answer_list = []
            #pop up box
            messagebox.showinfo("Incorrect!", "Incorrect!")
        #reset buttons
        for key in answer_dict:
            key["text"] = ""

        answer_dict = {}

#define our buttons
b0= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b0, 0))
b1= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b1, 1))
b2= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b2, 2))
b3= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b3, 3))
b4= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b4, 4))
b5= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b5, 5))
b6= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b6, 6))
b7= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b7, 7))
b8= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b8, 8))
b9= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b9, 9))
b10= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b10, 10))
b11= Button(my_frame, text="", font=('Helvetica', 20), height = 3, width=6, command = lambda: button_click(b11, 11))

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

my_label = Label(root, text = '')
my_label.pack(pady=20)

root.mainloop()