from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox

def bin_to_dec(digit):
    lenght=len(digit)
    chislo_dec=0
    for i in range(0, lenght):
        chislo_dec=chislo_dec+int(digit[i])*(pow(2,(lenght-i-1)))

    return chislo_dec



def clicked():
    txt_original = txt.get("1.0", 'end-1c')
    txt2.delete(1.0, END)
    txt4.delete(1.0, END)
    key = txt3.get("1.0", 'end-1c')
    count=0
    txt_result=''
    #if len(txt_original)==len(key):
    for i in txt_original:
        flag=0
        current_letter_binary = bin(ord(i))[2:]
        mask_binary=bin(ord(key[count%len(key)]))[2:]
        current_mask_binary=''
        additional_letter=''
        if len(current_letter_binary)>=len(mask_binary):
            while flag==0:
                if len(current_mask_binary)+len(mask_binary)==len(current_letter_binary):
                    current_mask_binary+=str(mask_binary)
                    mask_binary=current_mask_binary
                    flag=1
                else:
                    current_mask_binary+='0'

        else:
            while flag==0:
                if len(current_letter_binary)+len(additional_letter)==len(mask_binary):
                    additional_letter+=str(current_letter_binary)
                    current_letter_binary=additional_letter
                    flag=1
                else:
                    additional_letter+='0'

        answer = ''
        count_binary=0
        for j in current_letter_binary:
            if j == mask_binary[count_binary]:
                answer += '0'
            else:
                answer += '1'
            count_binary += 1
        print(current_letter_binary)
        print(mask_binary)
        print(answer)
        print('----------')
        txt_result += chr(bin_to_dec(answer))
        txt4.insert(INSERT,f'шифрую символ {i} символом {key[count%len(key)]}\n')
        txt4.insert(INSERT, f'{current_letter_binary}\n')
        txt4.insert(INSERT, f'{mask_binary}\n')
        txt4.insert(INSERT, f'--------------\n')
        txt4.insert(INSERT, f'{answer}\n')
        txt4.insert(INSERT,'\n')
        count += 1


    txt2.insert(INSERT, txt_result)
    print(len(txt_result))
    #else:
        #messagebox.showinfo('Ошибка!', f'Длины строк должны быть одинаковы')


def swap():
    temp = txt2.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temp)
    txt2.delete(1.0, END)

window = Tk()
window.title("Шифр Вернама")
window.geometry('500x650')

lbl = Label(window, text="Ключ")
lbl.grid(column=0, row=2)

txt3 = scrolledtext.ScrolledText(window, width=40, height=1)
txt3.grid(column=2, row=2)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)


btn = Button(window, text="Поменять значения", command=swap)
btn.grid(column=2, row=4)
lbl = Label(window)

lbl = Label(window, text="Ваше сообщение")
lbl.grid(column=0, row=0)

txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)


lbl = Label(window, text="Результат:")
lbl.grid(column=0, row=6)


txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=6)


txt4 = scrolledtext.ScrolledText(window, width=40, height=20)
txt4.grid(column=2, row=8)

window.mainloop()

