# -*- coding: utf8 -*-
import tkinter
import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox

window = Tk()
window.title('Volvox chat')

def menu():
        Button(command=lambda: b.grid_forget()) # Удаление страницы
        list = window.grid_slaves()
        for l in list:
             l.destroy()
             
        # This is UI block
        lbl = Label(window, text = ' Volvox Chat ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
        lbl.grid(row = 0, columnspan = 4, ipady = 5, ipadx = 80)
        
        Button(window, text='Общий чат', command = chat).grid(row = 1, padx = 15, pady = 5, ipadx = 57, columnspan = 4)  
        
        Button(window, text='Все чаты (в разработке)', command = logs_chat).grid(row = 2, padx = 15, pady = 5, ipadx = 12, columnspan = 4)  
            
        Button(window, text='Все пользователи', command = logs).grid(row = 3, padx = 15, pady = 5, ipadx = 33, columnspan = 4)  
        
        Button(window, text='О программе', command = about).grid(row = 4, padx = 15, pady = 5, ipadx = 48, columnspan = 4)  
            
        lbl = Label(window, text = 'All rights belongs to Volvox Software inc')
        lbl.grid(row = 5, columnspan = 4)
                                                
        lbl = Label(window, text = 'Coded and designed by Krylov Vladimir')
        lbl.grid(row = 6, columnspan = 4)        

def log_in():        
        
        global stat
        stat = '(User)'
        stat2 = '(Admin)'
        stat3 = '(Fool)'
        
        if nick.get() == 'krylofficial':
                stat = stat2
                
        nickname = nick.get() + stat + "\n"
        global nick2
        nick2 = nick.get()
        
        nickname = nick.get() + stat+ ':'
        nickname2 = nick.get() + stat + '\n'
        reg_file = open("logs.txt", "r").readlines()
        
        if nickname2 not in reg_file:
                
                f = open(nick.get() + ".txt", "w")
                first_password = password.get()
                massive_password = []
                end_password = ''
                pos = 0
                letters = ['Q','A','Z','W','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','M','I','K','O','L','P','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','0','9','2','8','3','7','4','6','5','й','ф','ц','я','ы','у','ч','в','к','с','а','е','м','п','н','и','р','г','т','о','ш','ь','л','щ','б','д','з','ю','ж','х','э','ъ','Й','Ц','Ф','У','Ы','Я','К','В','Ч','Е','А','С','Н','П','М','Г','Р','И','Ш','О','Т','Щ','Л','Ь','З','Д','Б','Х','Ж','Ю','Ъ','Э']
                for r in range(0, 1):
                    for p in range(0, len(first_password)):
                        for i in range(0, len(letters)):
                            if first_password[p] == letters[i]:
                                if first_password[p] == letters[-1]:
                                    massive_password.append(letters[0])
                                else:
                                    massive_password.append(letters[i + 1])            
                    first_password = ''
                    for z in range(0,len(massive_password)):
                        first_password += massive_password[z] 
                    for i in range(0, len(first_password)):
                        end_password += first_password[i]
                        
                f.write( end_password + "\n") # ДОБАВЛЕНИЕ НЕЗАШИФРОВАННОГО ПАРОЛЯ
                f.close()
                d = open("logs.txt", "a")
                d.write(nick.get() + stat + "\n")
                d.close()                
                messagebox.showinfo('Регистрация успешна', 'Регистрация нового пользователя прошла успешно')
                pass
        
        pas_file = open(nick.get() + ".txt", "r").readlines()
                
        first_password = password.get()
        massive_password = []
        end_password = ''
        pos = 0
        letters = ['Q','A','Z','W','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','M','I','K','O','L','P','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','0','9','2','8','3','7','4','6','5','й','ф','ц','я','ы','у','ч','в','к','с','а','е','м','п','н','и','р','г','т','о','ш','ь','л','щ','б','д','з','ю','ж','х','э','ъ','Й','Ц','Ф','У','Ы','Я','К','В','Ч','Е','А','С','Н','П','М','Г','Р','И','Ш','О','Т','Щ','Л','Ь','З','Д','Б','Х','Ж','Ю','Ъ','Э']
        for r in range(0, 1):
                for p in range(0, len(first_password)):
                        for i in range(0, len(letters)):
                            if first_password[p] == letters[i]:
                                if first_password[p] == letters[-1]:
                                    massive_password.append(letters[0])
                                else:
                                    massive_password.append(letters[i + 1])            
                first_password = ''
                for z in range(0,len(massive_password)):
                        first_password += massive_password[z] 
                for i in range(0, len(first_password)):
                        end_password += first_password[i]
                        
        password2 = end_password + '\n' # ЧТЕНИЕ НЕЗАШИФРОВАННОГО ПАРОЛЯ        
        if password2 not in pas_file:
                messagebox.showinfo('Неверный пароль', 'Неверный пароль для введенного пользователя')
                return
                                
        Button(command=lambda: b.grid_forget()) # Удаление страницы
        list = window.grid_slaves()
        for l in list:
            l.destroy()  
            
        stat = '(User)'
        stat2 = '(Administrator)'
        stat3 = '(Fool)'       
        
        def send():
                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
                messages_list_text.grid(row = 2, padx = 15, pady = 5) 
                messages = open("test_message_list.txt", "r").read()
                messages_list_text.insert(INSERT, messages)                
                message_sent = messages_letter_text.get() + '\n'
                message_sent2 = nickname + message_sent
                f = open("test_message_list.txt", "a")
                f.write(message_sent2) 
                f.close()        
                messages_list_text.insert(INSERT, message_sent2) 
                messages_letter_text.delete(0, END)
        
        def refresh():
                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)                   
                messages_list_text.destroy()
                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
                messages_list_text.grid(row = 2, padx = 15, pady = 5) 
                messages = open("test_message_list.txt", "r").read()
                messages_list_text.insert(INSERT, messages)                      
        
        # This is UI block
         
        lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
        lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')
                
        messages_preview_text = Label(text="    Список сообщений")
        messages_preview_text.grid(row = 1, column = 0, sticky = 'W')
        
        refresh()                
        
        Button(window, text='Обновить', command = refresh).grid(row = 1, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
        
        messages_letter_text = Entry()
        messages_letter_text.grid(row = 3, padx = 15, pady = 10, ipadx = 25, ipady = 3, sticky="W")
        messages_letter_text.insert(INSERT, '')
                
        button_send = Button( text="Отправить", command = send)
        button_send.grid(row = 3, padx = 15, pady = 10, ipadx = 10, sticky = 'E')                
        
        def chat():
                Button(command=lambda: b.grid_forget()) # Удаление страницы
                list = window.grid_slaves()
                for l in list:
                        l.destroy()
                
                        def send():
                                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
                                messages_list_text.grid(row = 2, padx = 15, pady = 5) 
                                messages = open("test_message_list.txt", "r").read()
                                messages_list_text.insert(INSERT, messages)                
                                message_sent = messages_letter_text.get() + '\n'
                                message_sent2 = nickname + message_sent
                                f = open("test_message_list.txt", "a")
                                f.write(message_sent2) 
                                f.close()        
                                messages_list_text.insert(INSERT, message_sent2) 
                                messages_letter_text.delete(0, END)
        
                        def refresh():
                                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)                   
                                messages_list_text.destroy()
                                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
                                messages_list_text.grid(row = 2, padx = 15, pady = 5) 
                                messages = open("test_message_list.txt", "r").read()
                                messages_list_text.insert(INSERT, messages)                 
                
                        
                lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
                lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')
                       
                messages_preview_text = Label(text="    Список сообщений")
                messages_preview_text.grid(row = 1, column = 0, sticky = 'W')
        
                refresh()                
        
                Button(window, text='Обновить', command = refresh).grid(row = 1, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
        
                messages_letter_text = Entry()
                messages_letter_text.grid(row = 3, padx = 15, pady = 10, ipadx = 25, ipady = 3, sticky="W")
                messages_letter_text.insert(INSERT, '')
                
                button_send = Button( text="Отправить", command = send)
                button_send.grid(row = 3, padx = 15, pady = 10, ipadx = 10, sticky = 'E')
                
                Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
        
        Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
                        
def logs():
        Button(command=lambda: b.grid_forget()) # Удаление страницы
        list = window.grid_slaves()
        for l in list:
                l.destroy()
                                             
        lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
        lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')
                                       
        messages_preview_text = Label(text="    Список пользователей Volvox Chat")
        messages_preview_text.grid(row = 1, column = 0, sticky = 'W')
        messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
        messages_list_text.grid(row = 2, padx = 15, pady = 15) 
        messages = open("logs.txt", "r").read()
        messages_list_text.insert(INSERT, messages)
        Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')

def logs_chat():
        def new_chat():
                
                Button(command=lambda: b.grid_forget()) # Удаление страницы
                list = window.grid_slaves()
                for l in list:
                        l.destroy()
                
                lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
                lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')
                Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
                
                messages_preview_text = Label(text="Новый чат:")
                messages_preview_text.grid(row = 1, column = 0, sticky = 'W')
                
                nick_password = Label(text="Введите получателя")
                nick_password.grid(row = 2, column = 0, sticky = 'W', padx = 10, pady = 10)                                      
                
                chat_nick = Entry()
                chat_nick.grid(row = 2, column = 0, padx = 108, pady = 10)
                chat_nick.insert(INSERT, '')
                
                
                
        Button(command=lambda: b.grid_forget()) # Удаление страницы
        list = window.grid_slaves()
        for l in list:
                l.destroy()
        
        lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
        lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')
        
        messages_preview_text = Label(text="    Список чатов с пользователями:")
        messages_preview_text.grid(row = 1, column = 0, sticky = 'W')
        
        Button(window, text='Начать чат', command = new_chat).grid(row = 1, padx = 108, pady = 5, ipadx = 10, sticky = 'E')
            
        Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
        
        
        
def about():
        
        Button(command=lambda: b.grid_forget()) # Удаление страницы
        list = window.grid_slaves()
        for l in list:
             l.destroy()
        
        lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
        lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')
        
        Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')
        
        lbl = Label(window, text = ' ') #44
        lbl.grid(row = 1, columnspan = 4)
        
        lbl = Label(window, text = 'Volvox chat это чат для пользователей одного') #44
        lbl.grid(row = 2, columnspan = 4)        

        lbl = Label(window, text = 'локального соединения. Вы можете общаться как в общем чате')
        lbl.grid(row = 3, columnspan = 4)                
        
        lbl = Label(window, text = 'так и в личных переписках. Все пароли мгновенно шифруются')
        lbl.grid(row = 4, columnspan = 4)        
        
        lbl = Label(window, text = 'алгоритмом Volvox Crypting System, и находятся')
        lbl.grid(row = 5, columnspan = 4)                
        
        lbl = Label(window, text = 'в полной безопасности.')
        lbl.grid(row = 6, columnspan = 4)
        
        lbl = Label(window, text = '')
        lbl.grid(row = 7, columnspan = 4)
        
        lbl = Label(window, text = 'All rights belongs to Volvox Software inc')
        lbl.grid(row = 8, columnspan = 4)
                
        lbl = Label(window, text = 'Coded and designed by Krylov Vladimir')
        lbl.grid(row = 9, columnspan = 4)        

# This is UI block
lbl = Label(window, text = ' Volvox Chat ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
lbl.grid(row = 0, columnspan = 4, ipady = 5, ipadx = 80)

nick_label = Label(text="Введите ник")
nick_label.grid(row = 4, column = 0, sticky = 'W', padx = 10, pady = 10)

global nick
nick = Entry()
nick.grid(row = 4, column = 2, padx = 15, pady = 10)
nick.insert(INSERT, '')
        
nick_password = Label(text="Введите пароль")
nick_password.grid(row = 6, column = 0, sticky = 'W', padx = 10, pady = 10)
        
password = Entry()
password.grid(row = 6, column = 2, padx = 15, pady = 10)
password.insert(INSERT, '')
        
Button(window, text=' Ввод ', command = log_in).grid(row = 7, columnspan = 3, padx = 15, pady = 5, ipadx = 55, sticky = 'E')  
        
lbl = Label(window, text = 'All rights belongs to Volvox Software inc')
lbl.grid(row = 8, columnspan = 4)
        
lbl = Label(window, text = 'Coded and designed by Krylov Vladimir')
lbl.grid(row = 9, columnspan = 4)

def chat():
        Button(command=lambda: b.grid_forget()) # Удаление страницы
        list = window.grid_slaves()
        for l in list:
                l.destroy()              
                
        stat = '(User)'
        stat2 = '(Admin)'
        stat3 = '(Fool)'
        
        def send():
                stat = '(User)'
                stat2 = '(Admin)'
                stat3 = '(Fool)'   
                
                nick2 == str(nick2)
                if nick2 == 'krylofficial':
                        stat = stat2                
                nickname = nick2 + stat+ ':'
                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
                messages_list_text.grid(row = 2, padx = 15, pady = 5) 
                messages = open("test_message_list.txt", "r").read()
                messages_list_text.insert(INSERT, messages)                
                message_sent = messages_letter_text.get() + '\n'
                message_sent2 = nickname + message_sent
                f = open("test_message_list.txt", "a")
                f.write(message_sent2) 
                f.close()        
                messages_list_text.insert(INSERT, message_sent2) 
                messages_letter_text.delete(0, END)

        def refresh():
                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)                   
                messages_list_text.destroy()
                messages_list_text = scrolledtext.ScrolledText(window, width=40, height=10)  
                messages_list_text.grid(row = 2, padx = 15, pady = 5) 
                messages = open("test_message_list.txt", "r").read()
                messages_list_text.insert(INSERT, messages)                 


        lbl = Label(window, text = ' Volvox Chat                               ', font=("Arial Bold", 20), bg = 'green', fg = 'white')
        lbl.grid(row = 0, ipadx = 10, ipady = 5, sticky = 'W')

        messages_preview_text = Label(text="    Список сообщений")
        messages_preview_text.grid(row = 1, column = 0, sticky = 'W')

        refresh()                

        Button(window, text='Обновить', command = refresh).grid(row = 1, padx = 10, pady = 5, ipadx = 10, sticky = 'E')

        messages_letter_text = Entry()
        messages_letter_text.grid(row = 3, padx = 15, pady = 10, ipadx = 25, ipady = 3, sticky="W")
        messages_letter_text.insert(INSERT, '')

        button_send = Button( text="Отправить", command = send)
        button_send.grid(row = 3, padx = 15, pady = 10, ipadx = 10, sticky = 'E')

        Button(window, text='Меню', command = menu).grid(row = 0, padx = 10, pady = 5, ipadx = 10, sticky = 'E')


window.mainloop()
