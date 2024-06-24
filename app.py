from tkinter import *
from tkinter import font
from customtkinter import *
from PIL import ImageTk, Image, ImageOps, ImageEnhance
from ctype import windll, byref, sizeof, c_int
from tktimepicker import AnalogPicker, AnalogThemes
from tksheet import *
from tkinter import ttk
from datetime import datetime
import calendar
from myfirebase import MyFireBase
from operator import itemgetter
from main import Relogio
import getpass
import os
import sys
import subprocess
import wmi



database = MyFireBase()



op_now = reg_now = True

date = datetime.today()
hoje = calendar.day_name[date.weekday()]
today = ""
if hoje == "Sunday":
    today = "dom"
elif hoje == "Monday":
    today = "seg"
elif hoje == "Tuesday":
    today = "ter"
elif hoje == "Wednesday":
    today = "qua"
elif hoje == "Thursday":
    today = "qui"
elif hoje == "Friday":
    today = "sex"
elif hoje == "Saturday":
    today = "sab"

loc_atual = sys.executable
loc_atual = str(loc_atual).replace("\pull-it.exe", "")




f = wmi.WMI()
relogio_created = False
try:
    for c in f.Win32_Process():
        if c.name == "clock.exe":
            relogio_created = True
            break
except Exception as e:
    relogio_created = False
try:
    if not relogio_created:
        print(loc_atual)
        path = loc_atual + "\clock.exe"
        os.startfile(path)
        relogio_created = True
except:
    relogio_created = False

try:
    with open(f"{loc_atual}\data\\dia_salvo.txt", "r") as arquivo:
        dia_salvo = arquivo.read()
    if dia_salvo == today:
        pass
    else:
        with open(f"{loc_atual}\data\\checked.txt", "w") as arquivo:
            arquivo.write("")
        with open(f"{loc_atual}\data\\dia_salvo.txt", "w") as arquivo:
            arquivo.write(f"{today}")
except:
    with open(f"{loc_atual}\data\\dia_salvo.txt", "w") as arquivo:
        arquivo.write(f"{today}")


agenda_i = []

agenda_v = False
try:
    with open(f"{loc_atual}\data\\open.txt", "r") as arquivo:
        r = arquivo.read()
    if r == "1":
        agenda_v = True
    else:
        agenda_v = False
except:
    pass

try:
    with open(f"{loc_atual}\data\\\relogio_created.txt", "r") as arquivo:
        res = arquivo.read()
    pass
except:
    with open(f"{loc_atual}\data\\relogio_created.txt", "w") as arquivo:
        arquivo.write("1")


janela = CTk()
janela.title("pull-it train")
janela.geometry("355x520+600+200")

janela.iconbitmap("calendar.ico")

janela.resizable(width=FALSE, height=FALSE)
janela.config(background="#000000")

HWND = windll.user32.GetParent(janela.winfo_id())
titlebar_color = 0x00141414
windll.dwmapi.DwmSetWindowAttribute(HWND,
                                    35,
                                    byref(c_int(titlebar_color)),
                                    sizeof(c_int))



e_mail = StringVar(janela)
password = StringVar(janela)
nome_user = StringVar(janela)
idade_user = StringVar(janela)
altura_user = StringVar(janela)
var = IntVar(janela)
tipo = StringVar(janela)
peso = StringVar(janela)
seg = IntVar(janela)
ter = IntVar(janela)
qua = IntVar(janela)
qui = IntVar(janela)
sex = IntVar(janela)
sab = IntVar(janela)
dom = IntVar(janela)

hora = StringVar()
nome_event = StringVar()

confirm = Image.open("imgs/confirm_button.png")
confirm = confirm.resize((60, 40))
confirm = ImageTk.PhotoImage(confirm)

arrow_r = Image.open("imgs/arrow_r.png")
arrow_r = arrow_r.resize((142, 60))
arrow_r = ImageTk.PhotoImage(arrow_r)

configure = Image.open("imgs/configure.png")
configure = configure.resize((40, 40))
configure = ImageTk.PhotoImage(configure)


home = Image.open("imgs/home.png")
home = home.resize((60, 60))
home = ImageTk.PhotoImage(home)

home_a = Image.open("imgs/home_active.png")
home_a = home_a.resize((60, 60))
home_a = ImageTk.PhotoImage(home_a)

agenda_vazia = Image.open("imgs/agenda_vazia.png")
agenda_vazia = agenda_vazia.resize((80, 80))
agenda_vazia = ImageTk.PhotoImage(agenda_vazia)

home_vazia = Image.open("imgs/home_vazia.png")
home_vazia = home_vazia.resize((80, 80))
home_vazia = ImageTk.PhotoImage(home_vazia)


calendar = Image.open("imgs/calendar.png")
calendar = calendar.resize((60, 60))
calendar = ImageTk.PhotoImage(calendar)

calendar_a = Image.open("imgs/calendar_active.png")
calendar_a = calendar_a.resize((60, 60))
calendar_a = ImageTk.PhotoImage(calendar_a)


balance = Image.open("imgs/balance.png")
balance = balance.resize((60, 60))
balance = ImageTk.PhotoImage(balance)

balance_a = Image.open("imgs/balance_active.png")
balance_a = balance_a.resize((60, 60))
balance_a = ImageTk.PhotoImage(balance_a)

arrow_back = Image.open("imgs/arrow_back.png")
arrow_back = arrow_back.resize((40, 40))
arrow_back = ImageTk.PhotoImage(arrow_back)

dc = True


images=[]


USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = sys.executable
        file_path = str(file_path).replace("\pull-it.exe", "")
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open_clock.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path + "\clock.exe")
    try:
        with open(f"{loc_atual}\data\\lista_dados.txt", "r") as arquivo:
            lista = arquivo.read()
        
    except:
        pass


loc_atual = sys.executable
loc_atual = str(loc_atual).replace("\pull-it.exe", "")
# print(loc_atual)


try:
    with open(f"{loc_atual}\data\\loc_saved", "r") as arquivo:
        loc_saves = arquivo.read()
    if loc_atual == loc_saves:
        # print(loc_saves, loc_atual)
        pass
    else:
        with open(f"{loc_atual}\data\\loc_saved", "w") as arquivo:
            arquivo.write(f"{loc_atual}")
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        os.remove(bat_path + "\open_clock.bat")
        add_to_startup()
except:
    with open(f"{loc_atual}\data\\loc_saved", "w") as arquivo:
        arquivo.write(f"{loc_atual}")
    add_to_startup()


def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

def pop_destroyer():
    global agenda_v
    global botao_add
    global  botao_edit
    global botao_home, botao_agenda, botao_balance
    if pop_up or not agenda_v:
        pop_up.destroy()
        agenda_v = True
        with open(f"{loc_atual}\data\\open.txt", "w") as arquivo:
            arquivo.write("1")
        botao_add.configure(state=NORMAL)
        botao_edit.configure(state=NORMAL)
        botao_agenda.configure(state=NORMAL)
        botao_home.configure(state=NORMAL)
        botao_balance.configure(state=NORMAL)


def add_event():
    global time_input
    dias = ""
    error = False
    if ":" not in hora.get() or hora.get() == "":
        error = True
    else:
        hh, mm = str(hora.get()).split(":")
        if int(hh) > 23 or int(hh) < 0:
            error = True
        if int(mm) > 59 or int(mm) < 0:
            error = True
        if int(hh) < 10 and hh != "00" and len(hh) == 1:
            hh = "0" + hh
            ho = hh + ":" + mm
            hora.set(value=ho)
        if int(mm) < 10 and mm != "00" and len(mm) == 1:
            mm = "0" + mm
            ho = hh + ":" + mm
            hora.set(value=ho)

    if dom.get() == 1:
        dias += "-dom"
    if seg.get() == 1:
        dias += "-seg"
    if ter.get() == 1:
        dias += "-ter"
    if qua.get() == 1:
        dias += "-qua"
    if qui.get() == 1:
        dias += "-qui"
    if sex.get() == 1:
        dias += "-sex"
    if sab.get() == 1:
        dias += "-sab"
    dias = dias[1:]
    if not error:
        database.add_event(horario=hora.get(), nome=nome_event.get(), tipo=tipo.get(), dias=dias)
        global agenda_i
        loc_atual = sys.executable
        loc_atual = str(loc_atual).replace("\pull-it.exe", "")
        agenda_i = database.get_events()
        agenda_i.sort(key= lambda x: x[0])
        with open(f"{loc_atual}\data\\lista_dados.txt", "w") as arquivo:
            arquivo.write(f"{agenda_i}")
        with open(f"{loc_atual}\data\\lista_dados.txt", "r") as arquivo:
            lista = arquivo.read()
        try:
            f = wmi.WMI()
            relogio_ativo = False
            for c in f.Win32_Process():
                if c.name == "clock.exe":
                    relogio_ativo = True
                    break
            print(relogio_ativo)
            if not relogio_ativo:
                path = loc_atual + "\clock.exe"
                os.startfile(path)
        except:
            pass
        agenda()
    else:
        time_input.configure(border_color='#e80042')

def calcular_imc():
    global labelsimc, imc_result
    if altura_user.get() == "":
        altura_user.set(value="1,70")
    altura = float(str(altura_user.get()).replace(",", "."))
    peso_a = float(str(peso.get().replace(",", ".")))
    imc = peso_a/(altura * altura)
    imc = float(f"{imc:.2f}")
    for k, la in labelsimc.items():
        la.configure(text_color="#dbdbdb")
        if imc < 16.9 and int(k) == 0:
            la.configure(text_color="#820303")
            imc_result.configure(text=f"{imc:.2f}", text_color="#820303")
        elif 18.49 > imc > 17 and int(k) == 1:
            la.configure(text_color="#00e82e")
            imc_result.configure(text=f"{imc:.2f}", text_color="#00e82e")
        elif 24.99 > imc > 18.5 and int(k) == 2:
            la.configure(text_color="#00E88F")
            imc_result.configure(text=f"{imc:.2f}", text_color="#00E88F")
        elif 29.99 > imc > 25 and int(k) == 3:
            la.configure(text_color="#00e82e")
            imc_result.configure(text=f"{imc:.2f}", text_color="#00e82e")
        elif 34.99 > imc > 30 and int(k) == 4:
            la.configure(text_color="#e80042")
            imc_result.configure(text=f"{imc:.2f}", text_color="#e80042")
        elif 40 > imc > 35 and int(k) == 5:
            la.configure(text_color="#e80000")
            imc_result.configure(text=f"{imc:.2f}", text_color="#e80000")
        elif imc > 40 and int(k) == 6:
            la.configure(text_color="#820303")
            imc_result.configure(text=f"{imc:.2f}", text_color="#820303")
    peso.set(value="")
    altura_user.set(value="")


def calculoImc():
    global canvas3
    canvas3.destroy()
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=180, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text=f'Cálculo IMC', fg_color="#141414", width=200, height=20,
                     font=("Arial", 15),
                     pady=10)
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=130, width=2000)
    rect.place(relx=0.4, rely=1, anchor=CENTER)
    botao_home = Button(canvas3, image=home, command=home_page,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_home.place(relx=0.1, rely=0.9)
    botao_agenda = Button(canvas3, image=calendar, command=agenda,
                          cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_agenda.place(relx=0.45, rely=0.9)
    botao_balance = Button(canvas3, image=balance_a, command=calculoImc,
                           cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_balance.place(relx=0.8, rely=0.9)
    label_peso = CTkLabel(canvas3, text="Seu peso Atual", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                          font=("Arial", 15), pady=10)
    label_peso.place(relx=0.35, rely=0.23, anchor=CENTER)
    peso_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=peso,
                          text_color="#141414", corner_radius=0, border_color="white")
    peso_input.place(relx=0.2, rely=0.25)
    botao_calculateImc = Button(canvas3, image=confirm, command=calcular_imc,
                           cursor="hand2", compound=LEFT, borderwidth=0, fg="#F0F0F0")
    botao_calculateImc.place(relx=0.5, rely=0.35, anchor=CENTER)
    global labelsimc, imc_result
    labelsimc = {}
    imc_result = CTkLabel(canvas3, text="14", fg_color="#F0F0F0", text_color="#F0F0F0", width=200, height=20,
                          font=("Arial", 25), pady=10)
    imc_result.place(relx=0.5, rely=0.45, anchor=CENTER)
    for c in range(0, 7):

        labelsimc[f"{c}"] = CTkLabel(canvas3, text="oioi", fg_color="#F0F0F0", text_color="#F0F0F0", width=200, height=20,
                          font=("Arial", 15), pady=10)
    for k, la in labelsimc.items():
        aum = int(k) / 20
        if int(k) == 0:
            la.configure(text="Muito abaixo do peso: Menor que 16,9")
        if int(k) == 1:
            la.configure(text="Abaixo do peso: 17 a 18,4")
        if int(k) == 2:
            la.configure(text="Peso ideal: 18,5 a 24,9")
        if int(k) == 3:
            la.configure(text="Acima do peso: 25 a 29,9")
        if int(k) == 4:
            la.configure(text="Obesidade grau I: 30 a 34,9")
        if int(k) == 5:
            la.configure(text="Obesidade grau II: 35 a 40")
        if int(k) == 6:
            la.configure(text="Obesidade grau III: Maior que 40")
        la.place(relx=0.5, rely=0.53 + aum, anchor=CENTER)

def add_event_page():
    global canvas3
    hora.set(value="")
    nome_event.set(value="")
    tipo.set(value="")
    dom.set(value=0)
    seg.set(value=0)
    ter.set(value=0)
    qua.set(value=0)
    qui.set(value=0)
    sex.set(value=0)
    sab.set(value=0)
    canvas3.destroy()
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=175, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text=f'Adicionando evento', fg_color="#141414", width=200, height=20,
                     font=("Arial", 15),
                     pady=10)
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    botao_back = Button(canvas3, image=arrow_back, command=agenda,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_back.place(relx=0.05, rely=0.07)
    label_hora = CTkLabel(canvas3, text="Horário", fg_color="#F0F0F0", text_color="#141414", width=200, height=2,
                          font=("Arial", 15), pady=10)
    label_hora.place(relx=0.3, rely=0.20, anchor=CENTER)
    global time_input
    time_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=hora,
                          text_color="#141414", corner_radius=0, border_color="white")
    time_input.place(relx=0.2, rely=0.22)

    label_nome = CTkLabel(canvas3, text="Nome", fg_color="#F0F0F0", text_color="#141414", width=200,
                          height=20,
                          font=("Arial", 15), pady=10)
    label_nome.place(relx=0.3, rely=0.32, anchor=CENTER)
    nome_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=nome_event,
                          text_color="#141414", corner_radius=0, border_color="white")
    nome_input.place(relx=0.2, rely=0.34)
    options = ["Treino",
               "Beber",
               "Remédio",
               "Comer",
               "Trabalhar",
               'Estudar',
               "Dormir"]
    label_tipo = CTkLabel(canvas3, text="Tipo", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                          font=("Arial", 15), pady=10)
    label_tipo.place(relx=0.3, rely=0.44, anchor=CENTER)
    tipo_input = OptionMenu(canvas3, tipo, *options)
    tipo_input.config(width=40, background="#F0F0F0")
    tipo_input.place(relx=0.2, rely=0.46)

    label_dia = CTkLabel(canvas3, text="Dias da Semana", fg_color="#F0F0F0", text_color="#141414",
                         width=200,
                         height=20,
                         font=("Arial", 15), pady=10)
    label_dia.place(relx=0.48, rely=0.58, anchor=CENTER)
    c1 = CTkCheckBox(canvas3, text='Seg', variable=seg, onvalue=1, offvalue=0,
                     text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c1.place(relx=0.38, rely=0.64, anchor=CENTER)
    c2 = CTkCheckBox(canvas3, text='Ter', variable=ter, onvalue=1, offvalue=0,
                     text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c2.place(relx=0.68, rely=0.64, anchor=CENTER)

    c3 = CTkCheckBox(canvas3, text='Qua', variable=qua, onvalue=1, offvalue=0, text_color="#141414",
                     checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c3.place(relx=0.38, rely=0.70, anchor=CENTER)
    c4 = CTkCheckBox(canvas3, text='Qui', variable=qui, onvalue=1, offvalue=0, text_color="#141414",
                     checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c4.place(relx=0.68, rely=0.70, anchor=CENTER)

    c5 = CTkCheckBox(canvas3, text='Sex', variable=sex, onvalue=1, offvalue=0, text_color="#141414",
                     checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c5.place(relx=0.38, rely=0.76, anchor=CENTER)
    c6 = CTkCheckBox(canvas3, text='Sab', variable=sab, onvalue=1, offvalue=0, text_color="#141414",
                     checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F",border_width=2)
    c6.place(relx=0.68, rely=0.76, anchor=CENTER)

    c7 = CTkCheckBox(canvas3, text='Dom', variable=dom, onvalue=1, offvalue=0, text_color="#141414",
                     checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c7.place(relx=0.38, rely=0.82, anchor=CENTER)
    botao_confirm = Button(canvas3, image=confirm, command=add_event,
                           cursor="hand2", compound=LEFT, borderwidth=0, fg="#F0F0F0")
    botao_confirm.place(relx=0.48, rely=0.9, anchor=CENTER)


def salvar_info():
    global dict_info
    new_info = {"nome": nome_user.get(), 'email': e_mail.get(), "senha": password.get(), "altura": altura_user.get()}
    chaves = ["nome", "email", "senha", "altura"]
    auth = {}
    info = {}
    for x in chaves:
        if new_info[x] == dict_info[x]:
            pass
        else:
            if x == "email" or x == "senha":
                auth[x] = new_info[x]
            else:
                info[x] = new_info[x]
    if len(info) > 0 or len(auth) > 0:
        if len(info) > 0:
            database.edit_info(New_dictInfo=info)
            info = database.get_info()
            altura_user.set(value=info[0][0])
            idade_user.set(value=info[0][1])
            nome_user.set(value=info[0][2])
            var.set(value=info[0][3])
        if len(auth) > 0:
            global label_error, email_input, senha_input
            if "email" in list(auth.keys()) and "senha" in list(auth.keys()):
                if "@" in auth["email"] or ".com" in auth["email"] or len(auth["email"]) > 0 or len(auth["senha"]) >= 8:
                    re = database.edit_auth(New_dictAuth=auth)
                    if not re:
                        label_error.configure(text_color="#e80042", text="Este Email já foi utilizado")
                        email_input.configure(border_color="#e80042")
                    else:
                        home_page()
                else:
                    label_error.configure(text_color="#e80042")
                    if "@" not in auth["email"] or ".com" not in auth["email"] or len(auth["email"]) == 0:
                        email_input.configure(border_color="#e80042")
                        label_error.configure(text="Email Inválido")
                    if len(auth["senha"]) < 8:
                        senha_input.configure(border_color="#e80042")
                        label_error.configure(text="Senha inválida")
            elif "senha" in list(auth.keys()) and "email" not in list(auth.keys()):
                if len(auth["senha"]) >= 8:
                    database.edit_auth(New_dictAuth=auth)
                    home_page()
                else:
                    label_error.configure(text_color="#e80042")
                    senha_input.configure(border_color="#e80042")
                    label_error.configure(text="Senha inválida")
            elif "email" in list(auth.keys()) and "senha" not in list(auth.keys()):
                if "@" in auth["email"] or ".com" in auth["email"] or len(auth["email"]) > 0:
                    re = database.edit_auth(New_dictAuth=auth)
                    if not re:
                        label_error.configure(text_color="#e80042", text="Este Email já foi utilizado")
                        email_input.configure(border_color="#e80042")
                    else:
                        home_page()
                else:
                    label_error.configure(text_color="#e80042")
                    email_input.configure(border_color="#e80042")
                    label_error.configure(text="Email Inválido")

def sair_auth():
    with open(f"{loc_atual}\data\\auth.txt", "w") as arquivo:
        arquivo.write("")
    with open(f"{loc_atual}\data\\checked.txt", "w") as arquivo:
        arquivo.write("")
    with open(f"{loc_atual}\data\\lista_dados.txt", "w") as arquivo:
        arquivo.write("")
    with open(f"{loc_atual}\data\\open.txt", "w") as arquivo:
        arquivo.write("")
    with open(f"tokken.txt", "w") as arquivo:
        arquivo.write("")
    global canvas3, op_now
    canvas3.destroy()
    e_mail.set(value="")
    password.set(value="")
    nome_user.set(value="")
    altura_user.set(value="")
    idade_user.set(value="")
    global agenda_i
    agenda_i.clear()
    op_now = True
    SingIn_LogIn()

def configure_page():
    global canvas3
    canvas3.destroy()
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=175, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text=f'Configurações', fg_color="#141414", width=200, height=20,
                     font=("Arial", 15),
                     pady=10)
    global dict_info
    dict_info = {"nome": nome_user.get(), 'email': e_mail.get(), "senha": password.get(), "altura": altura_user.get()}
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    botao_back = Button(canvas3, image=arrow_back, command=home_page,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_back.place(relx=0.05, rely=0.07)
    label_nome = CTkLabel(canvas3, text="Nome", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                          font=("Arial", 15), pady=10)
    label_nome.place(relx=0.3, rely=0.20, anchor=CENTER)
    nome_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=nome_user,
                          text_color="#141414", corner_radius=0, border_color="white")
    nome_input.place(relx=0.2, rely=0.22)

    label_email = CTkLabel(canvas3, text="Email", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                          font=("Arial", 15), pady=10)
    label_email.place(relx=0.3, rely=0.32, anchor=CENTER)
    global email_input
    email_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=e_mail,
                          text_color="#141414", corner_radius=0, border_color="white")
    email_input.place(relx=0.2, rely=0.34)

    label_senha = CTkLabel(canvas3, text="Senha", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                           font=("Arial", 15), pady=10)
    label_senha.place(relx=0.3, rely=0.44, anchor=CENTER)
    global senha_input
    senha_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=password,
                           text_color="#141414", corner_radius=0, border_color="white")
    senha_input.place(relx=0.2, rely=0.46)

    label_altura = CTkLabel(canvas3, text="Altura", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                           font=("Arial", 15), pady=10)
    label_altura.place(relx=0.3, rely=0.56, anchor=CENTER)
    altura_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=altura_user,
                           text_color="#141414", corner_radius=0, border_color="white")
    altura_input.place(relx=0.2, rely=0.58)
    global label_error
    label_error = CTkLabel(canvas3, text="Altura", fg_color="#F0F0F0", text_color="#F0F0F0", width=200, height=20,
                           font=("Arial", 15), pady=10)
    label_error.place(relx=0.5, rely=0.72, anchor=CENTER)
    botao_salvar = Button(canvas3, text="Salvar", width=20, background="#00E88F", activebackground="#08784d",
                        activeforeground="#141414", fg="#FFFFFF", font=("Arial", 13), borderwidth=0, command=salvar_info,
                        cursor="hand2")
    botao_salvar.place(relx=0.5, rely=0.70, anchor=CENTER)

    botao_sair = Button(canvas3, text="Sair da Conta", width=20, background="#e80042", activebackground="#e80042",
                          activeforeground="#FFFFFF", fg="#FFFFFF", font=("Arial", 13), borderwidth=0,
                          command=sair_auth,
                          cursor="hand2")
    botao_sair.place(relx=0.5, rely=0.95, anchor=CENTER)

def aumentar_barra():
    global dict_button
    with open(f"{loc_atual}\data\\checked.txt", "r") as arquivo:
        dados = arquivo.read()
    dados = list(dados)
    th = 0
    for event in agenda_i:
        if today in event[-1]:
            th += 1
    aum = 1 / th
    global progress_bar
    progress_bar.set(value=1)
    cont = 0
    for k, c in dict_button.items():
        if c.get() == 0:
            progress_bar.set(value= progress_bar.get() - aum)
            dados[cont] = "0"
        if c.get() == 1:
            dados[cont] = "1"
        cont += 1
    dados_new = ""
    for i in dados:
        dados_new += i
    with open(f"{loc_atual}\data\\checked.txt", "w") as arquivo:
        arquivo.write(dados_new)

    global label_porcentagem
    if 0.5 > progress_bar.get() >= 0:
        label_porcentagem.configure(text="Vamos lá! Há muito pela frente")
    if progress_bar.get() == 1:
        label_porcentagem.configure(text="Parabéns! Tudo concluído por hoje")
    if 0.7 > progress_bar.get() >= 0.5:
        label_porcentagem.configure(text="Vamos! Já temos meio caminho andado")
    if 1 > progress_bar.get() >= 0.7:
        label_porcentagem.configure(text="Quase lá! Só falta um pouco")

def home_page():
    global canvas3
    global agenda_i
    global op_now, relogio_created, reg_now
    try:
        if op_now:
            agenda_i = database.get_events()
            agenda_i.sort(key= lambda x: x[0])
            with open(f"{loc_atual}\data\\lista_dados.txt", "w") as arquivo:
                arquivo.write(f"{agenda_i}")
            with open(f"{loc_atual}\data\\lista_dados.txt", "r") as arquivo:
                lista = arquivo.read()
            op_now = False
        else:
            pass
    except:
        pass
    try:
        info = database.get_info()
        altura_user.set(value=info[0][0])
        idade_user.set(value=info[0][1])
        nome_user.set(value=info[0][2])
        var.set(value=info[0][3])
    except:
        pass
    try:
        if canvas3:
            canvas3.destroy()
    except:
        pass

    try:
        botao2.destroy()
        botao.destroy()
        label2.destroy()
        label3.destroy()
        senha.destroy()
        email.destroy()
    except:
        pass
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=180, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=130, width=2000)
    rect.place(relx=0.4, rely=1, anchor=CENTER)
    if nome_user.get() == '':
        title = CTkLabel(canvas3, text=f'Home', fg_color="#141414", width=200, height=20,
                         font=("Arial", 15),
                         pady=10)
    else:
        title = CTkLabel(canvas3, text=f'{nome_user.get()}', fg_color="#141414", width=200, height=20,
                         font=("Arial", 15),
                         pady=10)
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    botao_configure = Button(canvas3, image=configure, command=configure_page,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_configure.place(relx=0.85, rely=0.065)
    botao_edit = Button(canvas3, text="edit", width=10, background="#141414", activebackground="#08784d",
                        activeforeground="#00E88F", fg="#00E88F", font=("Arial", 13), borderwidth=0, command=edit,
                        cursor="hand2")

    botao_home = Button(canvas3, image=home_a, command=home_page,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_home.place(relx=0.1, rely=0.9)
    botao_agenda = Button(canvas3, image=calendar, command=agenda,
                          cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_agenda.place(relx=0.45, rely=0.9)
    botao_balance = Button(canvas3, image=balance, command=calculoImc,
                           cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_balance.place(relx=0.8, rely=0.9)
    if len(agenda_i) > 0:
        iframe = CTkScrollableFrame(canvas3, height=250, width=300, fg_color="#F0F0F0", scrollbar_fg_color="#F0F0F0", scrollbar_button_color="#F0F0F0", scrollbar_button_hover_color="#F0F0F0")
        iframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        global  progress_bar
        progress_bar = CTkProgressBar(canvas3, orientation="horizontal", progress_color="#00E88F", fg_color="#dbdbdb")
        progress_bar.set(value=0)
        progress_bar.place(relx=0.5, rely=0.23, anchor=CENTER)
        global dict_button
        dict_button = {}
        cont = 0
        for event in agenda_i:
            if today in event[-1]:
                dict_button[f"{cont}"] = CTkCheckBox(iframe, text=f'{event[1]}', onvalue=1, offvalue=0, command=aumentar_barra,
                         text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                         hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
                aum = cont/20

                #dict_button[f'{cont}'].place(relx=0.5, rely=0.3 + aum, anchor=CENTER)
                dict_button[f"{cont}"].pack(pady=10)
                cont += 1
                if cont == 6:
                    iframe.configure(scrollbar_fg_color="#F0F0F0", scrollbar_button_color="#dbdbdb", scrollbar_button_hover_color="#00E88F")
        n_cont = cont
        try:
            with open(f"{loc_atual}\data\\checked.txt", "r") as arquivo:
                saved_dados = arquivo.read()
            saved_dados = list(saved_dados)
            if len(saved_dados) != n_cont:
                res = n_cont - len(saved_dados)
                for c in range(0, res):
                    saved_dados.append(0)
                dados_new = ""
                for i in saved_dados:
                    dados_new += i
                with open(f"{loc_atual}\data\\checked.txt", "w") as arquivo:
                    arquivo.write(dados_new)


                with open(f"{loc_atual}\data\\checked.txt", "r") as arquivo:
                    saved_dados = arquivo.read()
            co = 0
            aum = 1 / cont
            progress_bar.set(value=1)
            for k, c in dict_button.items():
                if saved_dados[co] == '1':
                    c.select()
                if saved_dados[co] == '0':
                    progress_bar.set(value=progress_bar.get() - aum)
                co += 1

        except:
            dados = "0" * cont
            with open(f"{loc_atual}\data\\checked.txt", "w") as arquivo:
                arquivo.write(f"{dados}")
        if cont == 0:
            canvas3.create_image(220, 250, anchor=CENTER, image=home_vazia)
            label_dia_vazio = CTkLabel(canvas3, text="Parece que não há nada hoje", fg_color="#f0f0f0", width=200, height=20,
                                          font=("Arial", 15),
                                          pady=10, text_color="#dbdbdb")
            label_dia_vazio.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            global label_porcentagem
            label_porcentagem = CTkLabel(canvas3, text=f'Vamos lá! Há muito pela frente', fg_color="#F0F0F0", text_color="#00E88F", width=200, height=20,
                                         font=("Arial", 15),
                                         pady=10)
            label_porcentagem.place(relx=0.5, rely=0.8, anchor=CENTER)
            try:
                if 0.5 > progress_bar.get() >= 0:
                    label_porcentagem.configure(text="Vamos lá! Há muito pela frente")
                if progress_bar.get() == 1:
                    label_porcentagem.configure(text="Parabéns! Tudo concluído por hoje")
                if 0.7 > progress_bar.get() >= 0.5:
                    label_porcentagem.configure(text="Vamos! Já temos meio caminho andado")
                if 1 > progress_bar.get() >= 0.7:
                    label_porcentagem.configure(text="Quase lá! Só falta um pouco")
            except:
                pass
    else:
        canvas3.create_image(220, 250, anchor=CENTER, image=home_vazia)
        label_home_vazia = CTkLabel(canvas3, text="Sua Agenda está vazia", fg_color="#f0f0f0", width=200, height=20,
                                      font=("Arial", 15),
                                      pady=10, text_color="#dbdbdb")
        label_home_vazia.place(relx=0.5, rely=0.5, anchor=CENTER)


def atualizar_sheet():
    global sheet, evento
    
    dias = ""
    error = False
    print(hora.get())
    if ":" not in hora.get() or hora.get() == "":
        print("error")
        error = True
    else:
        hh, mm = str(hora.get()).split(":")
        if int(hh) > 23 or int(hh) < 0:
            error = True
        if int(mm) > 59 or int(mm) < 0:
            error = True
        if int(hh) < 10 and hh != "00" and len(hh) == 1:
            hh = "0" + hh
            ho = hh + ":" + mm
            hora.set(value=ho)
        if int(mm) < 10 and mm != "00" and len(mm) == 1:
            mm = "0" + mm
            ho = hh + ":" + mm
            hora.set(value=ho)

    row = evento[0][0]
    #       dom.get(), seg.get(), ter.get(), qua.get(), qui.get(), sex.get(), sab.get())
    dias = ""
    if dom.get() == 1:
        dias += "-dom"
    if seg.get() == 1:
        dias += "-seg"
    if ter.get() == 1:
        dias += "-ter"
    if qua.get() == 1:
        dias += "-qua"
    if qui.get() == 1:
        dias += "-qui"
    if sex.get() == 1:
        dias += "-sex"
    if sab.get() == 1:
        dias += "-sab"
    dias = dias[1:]
    if not error:
        evento_novo = {"horario": hora.get(), "nome": nome_event.get(), "tipo": tipo.get(), "dias": dias}
        chaves = ["horario", "nome", "tipo", "dias"]
        att = {}
        for x in chaves:
            if evento_novo[x] == dict_event[x]:
                pass
            else:
                att[x] = evento_novo[x]
        print(dict_event)
        print(att)
        database.edit_event(Old_dictInfo=dict_event, New_dictInfo=att)
        global agenda_i
        agenda_i = database.get_events()
        agenda_i.sort(key= lambda x: x[0])

        with open(f"{loc_atual}\data\\lista_dados.txt", "w") as arquivo:
            arquivo.write(f"{agenda_i}")
        with open(f"{loc_atual}\data\\lista_dados.txt", "r") as arquivo:
            lista = arquivo.read()
        
        agenda()
    else:
        global time_input
        time_input.configure(border_color='#e80042')

    # evento_antigo = list(dict_event.values())
    # for c in agenda_i:
    #     if c == evento_antigo:
    #         agenda_i.pop(cont)
    #         agenda_i.append(evento_novo)
    #     cont += 1
    # agenda()

def edit_event_page(cont, eventos):
    global canvas3, sheet
    cont = cont
    global evento
    evento = eventos
    for info in evento:
        span = sheet.span(info).data
    global dict_event
    dict_event = {"horario": sheet.span(evento[0]).data, "nome": sheet.span(evento[1]).data, "tipo": sheet.span(evento[2]).data, "dias": sheet.span(evento[3]).data}
    hora.set(value=f"{dict_event['horario']}")
    nome_event.set(value=f"{dict_event['nome']}")
    tipo.set(f"{dict_event['tipo']}")
    if "dom" in dict_event["dias"]:
        dom.set(value=1)
    if "seg" in dict_event["dias"]:
        seg.set(value=1)
    if "ter" in dict_event["dias"]:
        ter.set(value=1)
    if "qua" in dict_event["dias"]:
        qua.set(value=1)
    if "qui" in dict_event["dias"]:
        qui.set(value=1)
    if "sex" in dict_event["dias"]:
        sex.set(value=1)
    if "sab" in dict_event["dias"]:
        sab.set(value=1)
    canvas3.destroy()
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=175, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text=f'Editando evento "{nome_event.get()}"', fg_color="#141414", width=200, height=20, font=("Arial", 15),
                     pady=10)
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    botao_back = Button(canvas3, image=arrow_back, command=agenda,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_back.place(relx=0.05, rely=0.07)
    label_hora = CTkLabel(canvas3, text="Horário", fg_color="#F0F0F0", text_color="#141414", width=200, height=2,
                          font=("Arial", 15), pady=10)
    label_hora.place(relx=0.3, rely=0.20, anchor=CENTER)
    global time_input
    time_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=hora,
                          text_color="#141414", corner_radius=0, border_color="white")
    time_input.place(relx=0.2, rely=0.22)

    label_nome = CTkLabel(canvas3, text="Nome", fg_color="#F0F0F0", text_color="#141414", width=200,
                           height=20,
                           font=("Arial", 15), pady=10)
    label_nome.place(relx=0.3, rely=0.32, anchor=CENTER)
    nome_input = CTkEntry(canvas3, width=200, fg_color="white", border_width=1, textvariable=nome_event,
                          text_color="#141414", corner_radius=0, border_color="white")
    nome_input.place(relx=0.2, rely=0.34)
    options = ["Treino",
               "Beber",
               "Remédio",
               "Comer",
               "Trabalhar",
               'Estudar',
               "Dormir"]
    label_tipo = CTkLabel(canvas3, text="Tipo", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                            font=("Arial", 15), pady=10)
    label_tipo.place(relx=0.3, rely=0.44, anchor=CENTER)
    tipo_input = OptionMenu(canvas3, tipo, *options)
    tipo_input.config(width=40, background="#F0F0F0")
    tipo_input.place(relx=0.2, rely=0.46)

    label_dia = CTkLabel(canvas3, text="Dias da Semana", fg_color="#F0F0F0", text_color="#141414",
                            width=200,
                            height=20,
                            font=("Arial", 15), pady=10)
    label_dia.place(relx=0.48, rely=0.58, anchor=CENTER)
    c1 = CTkCheckBox(canvas3, text='Seg', variable=seg, onvalue=1, offvalue=0,
                     text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c1.place(relx=0.38, rely=0.64, anchor=CENTER)
    c2 = CTkCheckBox(canvas3, text='Ter', variable=ter, onvalue=1, offvalue=0,
                     text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c2.place(relx=0.68, rely=0.64, anchor=CENTER)

    c3 = CTkCheckBox(canvas3, text='Qua', variable=qua, onvalue=1, offvalue=0, text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c3.place(relx=0.38, rely=0.70, anchor=CENTER)
    c4 = CTkCheckBox(canvas3, text='Qui', variable=qui, onvalue=1, offvalue=0, text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c4.place(relx=0.68, rely=0.70, anchor=CENTER)

    c5 = CTkCheckBox(canvas3, text='Sex', variable=sex, onvalue=1, offvalue=0, text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c5.place(relx=0.38, rely=0.76, anchor=CENTER)
    c6 = CTkCheckBox(canvas3, text='Sab', variable=sab, onvalue=1, offvalue=0, text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c6.place(relx=0.68, rely=0.76, anchor=CENTER)

    c7 = CTkCheckBox(canvas3, text='Dom', variable=dom, onvalue=1, offvalue=0, text_color="#141414", checkmark_color="#141414", checkbox_width=20, checkbox_height=20,
                     hover_color="#79f2c4", border_color="#dbdbdb", corner_radius=5, fg_color="#00E88F", border_width=2)
    c7.place(relx=0.38, rely=0.82, anchor=CENTER)
    botao_confirm = Button(canvas3, image=confirm, command=atualizar_sheet,
                   cursor="hand2", compound=LEFT, borderwidth=0, fg="#F0F0F0")
    botao_confirm.place(relx=0.48, rely=0.9, anchor=CENTER)
    # radio1 = CTkRadioButton(canvas3, text="Sim", variable=var, value=1, fg_color=("white", "#00E88F"),
    #                         border_color="white", hover_color='#00FF9D', bg_color="#F0F0F0", text_color="#141414",
    #                         radiobutton_width=15, radiobutton_height=15)
    # radio1.place(relx=0.38, rely=0.64, anchor=CENTER)
    # radio2 = CTkRadioButton(canvas3, text="Não", variable=var, value=0, fg_color=("white", "#00E88F"),
    #                         border_color="white", hover_color='#00FF9D', bg_color="#F0F0F0", text_color="#141414",
    #                         radiobutton_height=15, radiobutton_width=15)
    # radio2.place(relx=0.68, rely=0.64, anchor=CENTER)


def att_del():
    global dict_event, evento
    
    try:
        database.del_event(Old_dictInfo=dict_event)
        global agenda_i
        try:
            agenda_i = database.get_events()
            agenda_i.sort(key= lambda x: x[0])
            with open(f"{loc_atual}\data\\lista_dados.txt", "w") as arquivo:
                arquivo.write(f"{agenda_i}")
            num = evento[0][0]
            with open(f"{loc_atual}\data\\checked.txt", "r") as arquivo:
                list_num = list(arquivo.read())
            list_num[num] = ""
            nov_list = ""
            for c in list_num:
                nov_list += c
            with open(f"{loc_atual}\data\\checked.txt", "w") as arquivo:
                arquivo.write(nov_list)
            with open(f"{loc_atual}\data\\lista_dados.txt", "r") as arquivo:
                lista = arquivo.read()
            agenda_i = database.get_events()

        except:
            agenda_i = []
        agenda()
    except:
        pass



def del_event_page(cont, eventos):
    global canvas3, sheet
    cont = cont
    global evento
    evento = eventos
    for info in evento:
        span = sheet.span(info).data
    global dict_event
    dict_event = {"horario": sheet.span(evento[0]).data, "nome": sheet.span(evento[1]).data, "tipo": sheet.span(evento[2]).data, "dias": sheet.span(evento[3]).data}
    att_del()

def del_cell():
    global canvas3
    lista_cell = sheet.get_selected_cells(get_rows = True, get_columns = True)
    linha = []
    pos = []
    events = []
    cont = 0
    for c in lista_cell:
        for i in c:
            linha.append(i)
            if len(linha) == 2:
                pos.append(linha.copy())
                linha.clear()
    lista_eventos = []
    evento = []
    # for p in pos:
    #     if p[1] == 0:
    #         p[1] = 4
    pos.sort()
    u_p = pos[0][0]
    cont = 0
    for p in pos:
        cont += 1
        if p[0] == u_p:
            evento.append(p)
        elif p[0] != u_p:
            lista_eventos.append(evento.copy())
            evento.clear()
            evento.append(p)
        if cont == len(pos):
            lista_eventos.append(evento.copy())
            evento.clear()
        u_p = p[0]
    cont = 1
    for evento in lista_eventos:
        del_event_page(cont = cont, eventos=evento)
        break


def edit_cell():
    global canvas3
    lista_cell = sheet.get_selected_cells(get_rows = True, get_columns = True)
    linha = []
    pos = []
    events = []
    cont = 0
    for c in lista_cell:
        for i in c:
            linha.append(i)
            if len(linha) == 2:
                pos.append(linha.copy())
                linha.clear()
    lista_eventos = []
    evento = []
    # for p in pos:
    #     if p[1] == 0:
    #         p[1] = 4
    pos.sort()
    u_p = pos[0][0]
    cont = 0
    for p in pos:
        cont += 1
        if p[0] == u_p:
            evento.append(p)
        elif p[0] != u_p:
            lista_eventos.append(evento.copy())
            evento.clear()
            evento.append(p)
        if cont == len(pos):
            lista_eventos.append(evento.copy())
            evento.clear()
        u_p = p[0]
    cont = 1
    for evento in lista_eventos:
        edit_event_page(cont = cont, eventos=evento)
        break



def edit():
    global canvas3
    canvas3.destroy()
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=180, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    title = CTkLabel(canvas3, text="Edit", fg_color="#141414", width=200, height=20, font=("Arial", 15),
                     pady=10)
    cont_l = 0
    cont_c = 0
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    botao_back = Button(canvas3, image=arrow_back, command=agenda,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_back.place(relx=0.05, rely=0.07)
    global agenda_i
    for i in agenda_i:
        cont_l += 1
    for info in agenda_i[0]:
        cont_c += 1
    cont_l = [c for c in range(0, cont_l)]
    cont_c = [c for c in range(0, cont_c)]
    cont_c.pop(0)
    cont_l.pop(0)
    global sheet
    sheet = Sheet(canvas3, table_bg="#FFFFFF", index_bg="#FFFFFF", header_bg="#141414", height=200, width=400,
                  header_fg="#00E88F", frame_bg="#141414", header_grid_fg="#141414", index_grid_fg="#FFFFFF",
                  row_index_width=20, align="center", column_width=80,
                  table_selected_cells_border_fg="#000000", table_selected_cells_bg="#FFFFFF",
                  table_selected_cells_fg="#000000",
                  table_selected_box_cells_fg="#000000", table_selected_box_rows_fg="#FFFFFF",
                  table_selected_box_columns_fg='#000000',
                  table_selected_columns_border_fg="#000000", table_selected_columns_bg="#FFFFFF",
                  table_selected_columns_fg="#000000",
                  table_selected_rows_border_fg="#000000", table_selected_rows_bg="#FFFFFF",
                  table_selected_rows_fg="#000000",
                  header_selected_cells_bg="#00E88F", header_selected_cells_fg="#000000",
                  header_selected_columns_bg="#00E88F", header_selected_columns_fg="#000000",
                  index_selected_cells_bg="#00E88F", index_selected_cells_fg="#000000",
                  index_selected_rows_bg="#00E88F", index_selected_rows_fg="#000000",
                  popup_menu_fg="#000000", popup_menu_bg='#FFFFFF', popup_menu_highlight_bg="#00E88F",
                  popup_menu_highlight_fg="#000000", headers=["horário", "nome", "tipo", "dias"],
                  )
    # sheet.row_index(newindex=0)
    # sheet.enable_bindings(["single_select", "toggle_select", "drag_select", "select_all", "column_select", "row_select",
    #                        "up", "down", "left", "right","prior", "next", "rc_select"])
    sheet.enable_bindings(["single_select","row_select","up", "down", "left", "right", "prior", "next"])
    #sheet.disable_bindings(["column_drag_and_drop", "move_columns", "row_drag_and_drop", "move_rows", "row_drag_and_drop", "rc_insert_row", "rc_insert_column", "row_width_resize", "column_height_resize"])
    # sheet.display_columns(cont_c, all_columns_displayed=False, reset_col_positions=True, refresh=True)
    # sheet.display_rows(cont_l, all_rows_displayed=False, reset_row_positions=True, refresh=True)
    sheet.set_sheet_data(data=agenda_i)
    sheet.column_width(column=3, width=200, redraw=True)
    sheet.column_width(column=1, width=150, redraw=True)
    # sheet.change_theme("light green", redraw=True)
    # sheet.place(relx=0.5, rely=0.4, anchor=CENTER)
    sheet.pack(padx=60, pady=150)
    items = sheet["A1"].expand().options(header=True, index=True).data
    botao_edit = Button(canvas3, text="edit", width=10, background="#00E88F", activebackground="#08784d",
                        activeforeground="#141414", fg="#141414", font=("Arial", 13), borderwidth=0, command=edit_cell,
                        cursor="hand2")
    botao_edit.place(relx=0.5, rely=0.82, anchor=CENTER)
    botao_del = Button(canvas3, text="delete", width=10, background="#e80042", activebackground="#94032c",
                        activeforeground="#FFFFFF", fg="#FFFFFF", font=("Arial", 13), borderwidth=0, command=del_cell,
                        cursor="hand2")
    botao_del.place(relx=0.5, rely=0.88, anchor=CENTER)
    label_delete = CTkLabel(canvas3, text="Selecione uma linha por vez", fg_color="#F0F0F0", text_color="#141414", width=200,
                           height=10,
                           font=("Arial", 10), pady=10)
    label_delete.place(relx=0.5, rely=0.72, anchor=CENTER)


def agenda():
    global canvas2

    try:
        if canvas2:
            canvas2.destroy()
    except:
        pass
    global canvas3
    try:
        if canvas3:
            canvas3.destroy()
    except:
        pass
    global agenda_i
    try:
        agenda_i = database.get_events()
    except:
        pass
    canvas3 = CTkCanvas(janela, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.configure(background="#141414")
    global botao_edit
    botao_edit = Button(canvas3, text="edit", width=10, background="#141414", activebackground="#08784d",
                        activeforeground="#00E88F", fg="#00E88F", font=("Arial", 13), borderwidth=0, command=edit,
                        cursor="hand2")
    global botao_add
    botao_add = Button(canvas3, text="+", width=10, background="#00E88F", activebackground="#1bfaa5",
                       activeforeground="#000000", fg="#000000", font=("Arial", 13), borderwidth=0,
                       command=add_event_page,
                       cursor="hand2")
    if not agenda_v:
        global pop_up
        pop_up = Toplevel(canvas3)
        pop_up.configure(borderwidth=1, border=2)
        canvas_pop = CTkCanvas(pop_up, highlightthickness=1)
        canvas_pop.pack(fill="both", expand=True)
        canvas_pop.create_rectangle(1, 1, 290, 190, outline="#141414")
        pos = janela.winfo_geometry()
        pos = pos[pos.find("+") + 1:]
        x, y = pos.split("+")
        x = int(x) + 80
        y = int(y) + 200
        pop_up.geometry(f'300x200+{x}+{y}')
        pop_up.resizable(width=FALSE, height=FALSE)
        pop_up.overrideredirect(True)
        pop_up.title('Agenda')
        label_pop = CTkLabel(pop_up, text="Deseja Adicionar uma Agenda?", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                 font=("Arial", 15), pady=10)
        label_pop.place(relx=0.5, rely=0.15, anchor=CENTER)
        botao_pop = Button(pop_up, text="Sim", width=10, background="#3b7a3b", activebackground="#FFFFFF",
                       activeforeground="black", fg="white", font=("Arial", 13), borderwidth=0, command=pop_destroyer,
                       cursor="hand2")
        botao_pop.place(relx=0.3, rely=0.50, anchor=CENTER)
        botao_pop2 = Button(pop_up, text="Não", width=10, background="red", activebackground="#FFFFFF",
                           activeforeground="black", fg="white", font=("Arial", 13), borderwidth=0, command=home_page,
                           cursor="hand2")
        botao_pop2.place(relx=0.7, rely=0.50, anchor=CENTER)
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=180, width=2000)
    rect.place(relx=0.4, rely=0, anchor=CENTER)
    rect = CTkLabel(canvas3, text='', fg_color='#141414', height=130, width=2000)
    rect.place(relx=0.4, rely=1, anchor=CENTER)
    title = CTkLabel(canvas3, text="Agenda", fg_color="#141414", width=200, height=20, font=("Arial", 15),
                     pady=10)
    cont_l = 0
    cont_c = 0
    title.place(relx=0.4, rely=0.1, anchor=CENTER)
    canvas3.configure(background="#F0F0F0")
    if len(agenda_i) == 0:
        canvas3.create_image(220, 250, anchor=CENTER, image=agenda_vazia)
        label_agenda_vazia = CTkLabel(canvas3, text="Agenda Vazia", fg_color="#f0f0f0", width=200, height=20, font=("Arial", 15),
                     pady=10, text_color="#dbdbdb")
        label_agenda_vazia.place(relx=0.5, rely=0.5, anchor=CENTER)
    # agenda_i.append(["10:35", "agua", "beber", "dom-seg-ter-qua-qui-sex-sab"])
    # agenda_i.append(["10:35", "treino", "treino", "dom-seg-ter-qua-qui-sex-sab"])
    if len(agenda_i) > 0:
        for i in agenda_i:
            cont_l += 1
        for info in agenda_i[0]:
            cont_c += 1
        cont_l = [c for c in range(0, cont_l)]
        cont_c = [c for c in range(0, cont_c)]
        cont_c.pop(0)
        cont_l.pop(0)

        sheet = Sheet(canvas3, table_bg="#FFFFFF", index_bg="#FFFFFF", header_bg="#141414", height=200, width=400,
                      header_fg="#00E88F", frame_bg="#141414", header_grid_fg="#141414", index_grid_fg="#FFFFFF", row_index_width=20, align="center", column_width=80,
                      table_selected_cells_border_fg="#00E88F", table_selected_cells_bg="#FFFFFF", table_selected_cells_fg="#000000",
                      table_selected_box_cells_fg="#00E88F", table_selected_box_rows_fg="#FFFFFF", table_selected_box_columns_fg='#000000',
                      table_selected_columns_border_fg = "#00E88F", table_selected_columns_bg="#FFFFFF", table_selected_columns_fg="#000000",
                      table_selected_rows_border_fg="#00E88F", table_selected_rows_bg="#FFFFFF", table_selected_rows_fg="#000000",
                      header_selected_cells_bg = "#00E88F", header_selected_cells_fg = "#000000", header_selected_columns_bg="#00E88F",header_selected_columns_fg="#000000",
                      index_selected_cells_bg="#00E88F",  index_selected_cells_fg="#000000", index_selected_rows_bg="#00E88F", index_selected_rows_fg="#000000",
                      popup_menu_fg="#000000", popup_menu_bg='#FFFFFF', popup_menu_highlight_bg="#00E88F", popup_menu_highlight_fg="#000000",
                      headers=["horário", "nome", "tipo", "dias"]
        )
        # sheet.enable_bindings()
        # sheet.display_columns(cont_c, all_columns_displayed=False, reset_col_positions=True, refresh=True)
        # sheet.display_rows(cont_l, all_rows_displayed=False, reset_row_positions=True, refresh=True)

        sheet.set_sheet_data(data=agenda_i)
        sheet.column_width(column=3, width=200, redraw=True)
        sheet.column_width(column=1, width=150, redraw=True)
        # sheet.change_theme("light green", redraw=True)
        # sheet.place(relx=0.5, rely=0.4, anchor=CENTER)
        sheet.pack(padx=60, pady=150)
        items = sheet["A1"].expand().options(header=True, index=True).data
        if not agenda_v:
            botao_edit.configure(state=DISABLED)
        botao_edit.place(relx=0.5, rely=0.75, anchor=CENTER)

    global botao_home, botao_agenda, botao_balance
    botao_add = Button(canvas3, text="+", width=10, background="#00E88F", activebackground="#1bfaa5",
                       activeforeground="#000000", fg="#000000", font=("Arial", 13), borderwidth=0, command=add_event_page,
                       cursor="hand2")
    botao_add.place(relx=0.5, rely=0.7, anchor=CENTER)


    botao_home = Button(canvas3, image=home, command=home_page,
                        cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_home.place(relx=0.1, rely=0.9)
    botao_agenda = Button(canvas3, image=calendar_a, command=agenda,
                          cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_agenda.place(relx=0.45, rely=0.9)
    botao_balance = Button(canvas3, image=balance, command=calculoImc,
                           cursor="hand2", compound=LEFT, borderwidth=0, fg="#141414", background="#141414")
    botao_balance.place(relx=0.8, rely=0.9)
    if not agenda_v:
        botao_add.configure(state=DISABLED)
        botao_home.configure(state=DISABLED)
        botao_agenda.configure(state=DISABLED)
        botao_balance.configure(state=DISABLED)
    botao_add.place(relx=0.5, rely=0.7, anchor=CENTER)
    if var.get() == 1:
        e_user = True
    elif var.get() == 0:
        e_user = False

def add_info():
    global nome_input, idade_input, altura_input, label_info
    if nome_user.get() == "" or idade_user.get() == "" or altura_user.get() == '':
        if nome_user.get() == "":
            nome_input.configure(border_color='#e80042')
            label_info.configure(text="O campo nome tem que ser preenchido")
        if idade_input.get() == "":
            idade_input.configure(border_color='#e80042')
            label_info.configure(text="O campo idade precisa ser preenchido")
        if altura_input.get() == "":
            altura_input.configure(border_color='#e80042')
            label_info.configure(text="O campo altura precisa ser preenchido")
        label_info.configure(text_color="#e80042")
    else:
        if "/" not in idade_input.get() or "," in altura_user.get() or "." not in altura_user.get():
            if "/" not in idade_input.get():
                label_info.configure(text_color="e80042")
                label_info.configure(text='É necessário separar o dia, o mês e o ano com "/"')
            else:
                dd, mm, aa = str(idade_input.get()).split('/')
                if int(dd) > 31 or int(dd) < 0 or int(mm) > 12 or int(mm) < 0:
                    if int(dd) > 31 or int(dd) < 0:
                        label_info.configure(text_color="e80042")
                        label_info.configure(text=f'Dia {dd} não é válido')
                    if int(mm) > 12 or int(mm) < 0:
                        label_info.configure(text_color="e80042")
                        label_info.configure(text=f'Mês {mm} não é válido')
            if "," in altura_user.get():
                altura = altura_user.get().replace(",", "")
                altura_user.set(value=altura)
            if "," not in altura_user.get() or "." not in altura_user.get():
                altura = str(altura_user.get())[0] + "." + str(altura_user.get())[1:]
                altura_user.set(value=altura)
        else:
            if var.get() == 1:
                p_f = True
            else:
                p_f = False
            database.add_info(nome=nome_user.get(), data_nascimento=idade_user.get(), altura=altura_user.get(), p_f=p_f)
            agenda()

def logIn():
    label4 = CTkLabel(janela, text="Os campos acima precisam ser preenchidos...", fg_color="#141414",
                      text_color="red",
                      width=200, height=20, font=("Arial", 10), pady=10)
    if e_mail.get() != "" and password.get() != "":
        if "@" in e_mail.get() and ".com" in e_mail.get() and len(password.get().strip()) >= 8:
            res = database.LogIn(email=e_mail.get(), senha=password.get())
            if res == "Senhas diferentes":
                label4.place(relx=0.5, rely=0.83, anchor=CENTER)
                label4.configure(text="Senha incorreta!")
            elif res == "Usuário não encontrado":
                label4.place(relx=0.5, rely=0.83, anchor=CENTER)
                label4.configure(text="Usuário não encontrado")
            elif res:
                global canvas1
                canvas1.destroy()
                with open(f"{loc_atual}\data\\auth.txt", "w") as arquivo:
                    arquivo.write(f"{e_mail.get()}\n{password.get()}")
                home_page()
            else:
                label4.place(relx=0.5, rely=0.83, anchor=CENTER)
                label4.configure("Informações inválidas")
        else:
            label4.place(relx=0.5, rely=0.83, anchor=CENTER)
            if "@" not in e_mail.get() or ".com" not in e_mail.get():
                label4.configure(text="Email inválido")
            elif len(password.get().strip()) < 8:
                label4.configure(text='A senha deve possuir mais que 8 dígitos')
    elif e_mail.get() == '' or password.get() == "":
        label4.place(relx=0.5, rely=0.83, anchor=CENTER)
        if password.get() == "" and e_mail.get() == "":
            label4.configure(text="os campos precisam ser preenchidos...")
        elif e_mail.get() == "":
            label4.configure(text="o campo Email precisa ser preenchido...")
        elif password.get() == "":
            label4.configure(text="o campo Senha precisa ser preenchido...")

def SignIn():
    label4 = CTkLabel(janela, text="Os campos acima precisam ser preenchidos...", fg_color="#141414",
                      text_color="red",
                      width=200, height=20, font=("Arial", 10), pady=10)
    if e_mail.get() != "" and password.get() != "":
        if "@" in e_mail.get() and ".com" in e_mail.get() and len(password.get().strip()) >= 8:
            res = database.SingUp(email=e_mail.get(), senha=password.get())
            if res == True:
                with open(f"{loc_atual}\data\\auth.txt", "w") as arquivo:
                    arquivo.write(f"{e_mail.get()}\n{password.get()}")
                canvas1.destroy()
                global canvas2
                canvas2 = CTkCanvas(janela, highlightthickness=0)
                canvas2.pack(fill="both", expand=True)
                canvas2.configure(background="#141414")
                rect = CTkLabel(canvas2, text='', fg_color='#141414', height=180, width=2000)
                rect.place(relx=0.4, rely=0, anchor=CENTER)
                title = CTkLabel(canvas2, text="Dados Pessoais", fg_color="#141414", width=200, height=20, font=("Arial", 15),
                                  pady=10)
                title.place(relx=0.4, rely=0.1, anchor=CENTER)
                canvas2.configure(background="#F0F0F0")
                label_nome = CTkLabel(canvas2, text="Nome", fg_color="#F0F0F0",text_color="#141414" , width=200, height=20, font=("Arial", 15), pady=10)
                label_nome.place(relx=0.3, rely=0.20, anchor=CENTER)
                global nome_input, idade_input, altura_input
                nome_input = CTkEntry(canvas2, width=200, fg_color="white", border_width=1, textvariable=nome_user,
                                 text_color="#141414", corner_radius=0, border_color="white")
                nome_input.place(relx=0.2, rely=0.22)

                label_idade = CTkLabel(canvas2, text="Data de nascimento", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                                      font=("Arial", 15), pady=10)
                label_idade.place(relx=0.4, rely=0.32, anchor=CENTER)
                idade_input = CTkEntry(canvas2, placeholder_text="12/30/2000", width=200, fg_color="white", border_width=1, textvariable=idade_user,
                                      text_color="#141414", corner_radius=0, border_color="white", placeholder_text_color="#141414")
                idade_input.place(relx=0.2, rely=0.34)

                label_altura = CTkLabel(canvas2, text="Altura", fg_color="#F0F0F0", text_color="#141414", width=200, height=20,
                                       font=("Arial", 15), pady=10)
                label_altura.place(relx=0.3, rely=0.44, anchor=CENTER)
                altura_input = CTkEntry(canvas2, width=200, fg_color="white", border_width=1, textvariable=altura_user,
                                       text_color="#141414", corner_radius=0, border_color="white")
                altura_input.place(relx=0.2, rely=0.46)

                label_treina = CTkLabel(canvas2, text="Pratica Atividade Física?", fg_color="#F0F0F0", text_color="#141414", width=200,
                                        height=20,
                                        font=("Arial", 15), pady=10)
                label_treina.place(relx=0.48, rely=0.58, anchor=CENTER)
                radio1 = CTkRadioButton(canvas2, text="Sim", variable=var, value=1, fg_color=("white", "#00E88F"),border_color="white", hover_color='#00FF9D', bg_color="#F0F0F0", text_color="#141414", radiobutton_width=15, radiobutton_height=15)
                radio1.place(relx=0.38, rely=0.64, anchor=CENTER)
                radio2 = CTkRadioButton(canvas2, text="Não", variable=var, value=0, fg_color=("white", "#00E88F"), border_color="white", hover_color='#00FF9D', bg_color="#F0F0F0", text_color="#141414", radiobutton_height=15, radiobutton_width=15)
                radio2.place(relx=0.68, rely=0.64, anchor=CENTER)
                global label_info
                label_info = CTkLabel(canvas2, text="Os campos acima precisam ser preenchidos", fg_color="#F0F0F0", text_color="#F0F0F0", width=200,
                                        height=20,
                                        font=("Arial", 15), pady=10)
                label_info.place(relx=0.5, rely=0.7, anchor=CENTER)
                botao = Button(canvas2, image=arrow_r, command=add_info,
                               cursor="hand2", compound=LEFT, borderwidth=0, fg="#F0F0F0")
                botao.pack()
                botao.place(relx=0.48, rely=0.83, anchor=CENTER)
            else:
                label4.configure(text="Este email já foi usado")
                label4.place(relx=0.5, rely=0.83, anchor=CENTER)


        else:
            label4.place(relx=0.5, rely=0.83, anchor=CENTER)
            if "@" not in e_mail.get() or ".com" not in e_mail.get():
                label4.configure(text="Email inválido")
            elif len(password.get().strip()) < 8:
                label4.configure(text='A senha deve possuir mais que 8 dígitos')
    elif e_mail.get() == '' or password.get() == "":
        label4.place(relx=0.5, rely=0.83, anchor=CENTER)
        if password.get() == "" and e_mail.get() == "":
            label4.configure(text="os campos precisam ser preenchidos...")
        elif e_mail.get() == "":
            label4.configure(text="o campo Email precisa ser preenchido...")
        elif password.get() == "":
            label4.configure(text="o campo Senha precisa ser preenchido...")

def LogIn_Page():
    botao.configure(text="Login", command=logIn)
    botao2.configure(text="Sign Up", command=SignUp_Page)

def SignUp_Page():
    global botao, botao2
    botao.configure(text="Sign In", command=SignIn)
    botao2.configure(text="LogIn", command=LogIn_Page)

def SingIn_LogIn():
    global botao, botao2
    try:
        with open(f"{loc_atual}\data\\auth.txt", "r") as arquivo:
            info = arquivo.read()
        info = info.split("\n")
        email, senha = info
        e_mail.set(value=email)
        password.set(value=senha)
        re = database.LogIn(email=email, senha=senha)
        if re:
            try:
                f = wmi.WMI()
                relogio_ativo = False
                for c in f.Win32_Process():
                    if c.name == "clock.exe":
                        relogio_ativo = True
                        break
                print(relogio_ativo)
                if not relogio_ativo:
                    path = loc_atual + "\clock.exe"
                    os.startfile(path)
            except Exception as e:
                print(e)
                pass
            home_page()
        # else:
        #     raise Exception("Auth denied")
    except Exception as e:
        font.families()


        img = Image.open("imgs/bg.jpg")
        img = img.resize((700, 700))
        bg = ImageTk.PhotoImage(img)
        janela.bg = bg


        global canvas1
        canvas1 = CTkCanvas(janela, highlightthickness=0)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, 0, image=bg,
                             anchor="nw")


        shade  = Image.new( mode = "RGBA", size = (600, 900), color = (20, 20, 20, 180))
        shade.save("imgs/img.png")
        shade = Image.open("imgs/img.png")
        enhancer = ImageEnhance.Contrast(shade)
        shade = enhancer.enhance(0.9)
        shade = ImageTk.PhotoImage(shade)
        janela.shade = shade
        canvas1.create_image(0, 0, image=shade,
                             anchor="nw")

        img = Image.open("imgs/pull-it.jpg")
        img = img.resize((350, 150))
        img = ImageTk.PhotoImage(img)
        janela.img = img
        canvas1.create_image(45, 110, image=img, anchor="nw")

        label2 = CTkLabel(janela, text="Email", fg_color="#141414", width=200, height=20, font=("Arial", 15), pady=10)
        label2.place(relx=0.5, rely=0.6, anchor=CENTER)

        label_rect = CTkLabel(canvas1, text='', bg_color='#F0F0F0', height=500, width=280)
        label_rect.place(relx=0.5, rely=1, anchor=CENTER)

        label_rect = CTkLabel(canvas1, text='', fg_color='#141414', height=498, width=279)
        label_rect.place(relx=0.5, rely=1, anchor=CENTER)


        email = CTkEntry(janela, width=200, fg_color="#FFFFFF", border_width=0, textvariable=e_mail, text_color="#141414")
        email.place(relx=0.5, rely=0.65, anchor=CENTER)

        label3 = CTkLabel(janela, text="Senha", fg_color="#141414", width=200, height=20, font=("Arial", 15), pady=10)
        label3.place(relx=0.5, rely=0.73, anchor=CENTER)
        senha = CTkEntry(janela, width=200, fg_color="#FFFFFF", border_width=0, textvariable=password, text_color="#141414")
        senha.configure(show="*")
        senha.place(relx=0.5, rely=0.78, anchor=CENTER)

        botao = Button(janela, text="Login", width=20, background="#3b7a3b", activebackground="#FFFFFF", activeforeground="black", fg="white", font=("Arial", 13), borderwidth=0, command=logIn, cursor="hand2")
        botao.place(relx=0.5, rely=0.88, anchor=CENTER)

        botao2 = Button(janela, text="Sing Up", width=0, background="#141414", activeforeground="#51519e", activebackground="#141414", fg="#7f7ff5", font=("Arial", 13), borderwidth=0, command=SignUp_Page, cursor="hand2")
        botao2.place(relx=0.5, rely=0.93, anchor=CENTER)
SingIn_LogIn()

janela.mainloop()

