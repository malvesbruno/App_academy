import schedule
import time as tm
from datetime import time, timedelta, datetime
from win11toast import toast
import getpass
import os
import calendar
import sys
from tkinter import messagebox


loc_atual = sys.executable
loc_atual = str(loc_atual).replace("\clock.exe", "")

class Relogio:
    def __init__(self, *args, **kwargs):
        self.c = 0
        self.loc_atual = loc_atual
        try:
            path = self.loc_atual + r'\data\lista_dados.txt'
            with open(path, "r") as arquivo:
                lista = arquivo.read()

            hor = []
            horario = lista.replace("[", "").replace("'", "").replace("]]", "").split("],")
            for h in horario:
                h.split(",")
                h = h.strip().split(",")
                hor.append(h)
            for c in hor:
                cont = 0
                for i in c:
                    c[cont] = i.strip()
                    cont += 1
            horario = hor.copy()
            self.horario = horario
            date = datetime.today()
            hoje = calendar.day_name[date.weekday()]
            self.today = ""
            if hoje == "Sunday":
                self.today = "dom"
            elif hoje == "Monday":
                self.today = "seg"
            elif hoje == "Tuesday":
                self.today = "ter"
            elif hoje == "Wednesday":
                self.today = "qua"
            elif hoje == "Thursday":
                self.today = "qui"
            elif hoje == "Friday":
                self.today = "sex"
            elif hoje == "Saturday":
                self.today = "sab"
            self.inicio()
        except:
            pass

    def carregar_lista(self):
        try:
            path = self.loc_atual + r'\lista_dados.txt'
            with open(path, "r") as arquivo:
                lista = arquivo.read()

            hor = []
            horario = lista.replace("[", "").replace("'", "").replace("]]", "").split("],")
            for h in horario:
                h.split(",")
                h = h.strip().split(",")
                hor.append(h)
            for c in hor:
                cont = 0
                for i in c:
                    c[cont] = i.strip()
                    cont += 1
            horario = hor.copy()
            self.horario = horario
        except Exception as e:
            messagebox.showinfo("error", message=f"{e}")

    def glock(self):
        op = self.horario[self.c]
        path = self.loc_atual + r'\imgs\ '.strip()
        if self.horario[self.c][2] == "Beber":
            image = {
                'src': path + "beber.jpg",
                'placement': 'appLogoOverride'
            }
        elif self.horario[self.c][2] == "Treino":
            image = {
                'src': path + "treinar.jpg",
                'placement': 'appLogoOverride'
            }
        elif self.horario[self.c][2] == "Remédio":
            image = {
                'src': path + "remédio.jpg",
                'placement': 'appLogoOverride'
            }
        elif self.horario[self.c][2] == "Comer":
            image = {
                'src': path + "comer.jpg",
                'placement': 'appLogoOverride'
            }
        elif self.horario[self.c][2] == "Trabalhar":
            image = {
                'src': path + "trabalho.jpg",
                'placement': 'appLogoOverride'
            }
        elif self.horario[self.c][2] == "Estudar":
            image = {
                'src': path + "estudo.jpg",
                'placement': 'appLogoOverride'
            }
        elif self.horario[self.c][2] == "Dormir":
            image = {
                'src': path + "dormir.jpg",
                'placement': 'appLogoOverride'
            }
        if self.today in self.horario[self.c][3]:
            path = self.loc_atual + r"\pull-it.exe"
            if image:
                toast('Now', f"hey, it's time to {op[1]}", image=image)
            else:
                toast('Now', f"hey, it's time to {op[1]}")
        self.c += 1

    def inicio(self):
        path = self.loc_atual + r'\imgs\ '.strip()
        print(self.horario)
        min_pass = self.horario[0]
        agr = int(datetime.now().strftime("%H%M"))
        for h in range(0, len(self.horario)):
            hor = self.horario[h][0]
            t = int(hor.replace(":", ""))
            if t < agr:
                op = self.horario[h][1]
                if self.horario[h][2] == "Beber":
                    image = {
                        'src': path + "beber.jpg",
                        'placement': 'appLogoOverride'
                    }
                    print(image)
                elif self.horario[h][2] == "Treino":
                    image = {
                        'src': path + "treinar.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Remédio":
                    image = {
                        'src': path + "remédio.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Comer":
                    image = {
                        'src': path + "comer.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Trabalhar":
                    image = {
                        'src': path + "trabalho.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Estudar":
                    image = {
                        'src': path + "estudo.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Dormir":
                    image = {
                        'src': path + "dormir.jpg",
                        'placement': 'appLogoOverride'
                    }
                if self.today in self.horario[h][3]:
                    path = self.loc_atual + r"\pull-it.exe"
                    if image:
                        toast('Late', f"hey, you're late to {op}", image=image)
                    else:
                        toast('Late', f"hey, you're late to {op}")
                self.c += 1
            elif t == agr:
                op = self.horario[h][1]
                if self.horario[h][2] == "Beber":
                    image = {
                        'src': path + "beber.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Treino":
                    image = {
                        'src': path + "treinar.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Remédio":
                    image = {
                        'src': path + "remédio.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Comer":
                    image = {
                        'src': path + "comer.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Trabalhar":
                    image = {
                        'src': path + "trabalho.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Estudar":
                    image = {
                        'src': path + "estudo.jpg",
                        'placement': 'appLogoOverride'
                    }
                elif self.horario[h][2] == "Dormir":
                    image = {
                        'src': path + "dormir.jpg",
                        'placement': 'appLogoOverride'
                    }
                if self.today in self.horario[h][3]:
                    path = self.loc_atual + r"\pull-it.exe"
                    if image:
                        toast('Now', f"hey, it's time to {op}", image=image)
                    else:
                        toast('Now', f"hey, it's time to {op}")
                self.c += 1


        for c in range(0, len(self.horario)):
            hor = self.horario[c][0]
            schedule.every().day.at(f"{hor}").do(self.glock)
        schedule.every(10).minutes.do(self.carregar_lista)

        while True:
            schedule.run_pending()
            tm.sleep(60)


Relogio()
tm.sleep(60)
