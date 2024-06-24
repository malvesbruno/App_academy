import requests
import json
import uuid
import cryptocode
from random import randint
import os


class MyFireBase():
    LINK = "https://projetoacademia-6ed77-default-rtdb.firebaseio.com/"
    try:
        with open("key.txt", "r") as arquivo:
            KEY = arquivo.read()
    except:
        pass

    def SingUp(self, email, senha):
        link = self.LINK + "/.json"
        res = False
        try:
            requisicao = requests.get(link)
            requisicao = requisicao.text.replace("true", "True")
            rect_dict = eval(requisicao)
            email_exist = False
            for c, i in rect_dict.items():
                i_email = i["auth"]["email"]
                i_email = cryptocode.decrypt(i_email, self.KEY)
                if str(i_email) == str(email):
                    print(email, i_email)
                    email_exist = True
            if email_exist == True:
                raise Exception("email já existe")
            else:
                senha = cryptocode.encrypt(senha, self.KEY)
                email = cryptocode.encrypt(email, self.KEY)
                data = {'auth': {'email': email, 'senha': senha}, "info": {}, "eventos": {}}
                requisicao = requests.post(link, json.dumps(data))
                dict_id = eval(requisicao.text)
                id = dict_id["name"]

                with open("tokken.txt", 'w') as arquivo:
                    arquivo.write(id)
                return True
        except Exception as e:
            print(e)

    def LogIn(self, email, senha):
        link = self.LINK + "/.json"
        requisicao = requests.get(link)
        requisicao = requisicao.text.replace("true", "True")
        rect_dict = eval(requisicao)
        id = ""
        for c, i in rect_dict.items():
            i_email = i["auth"]["email"]
            i_email = cryptocode.decrypt(i_email, self.KEY)
            if i_email == email:
                id = c
        try:
            link = self.LINK + id + "/auth/.json"
            requesicao = requests.get(link)
            dic_requisicao = requesicao.json()
            senha_db = cryptocode.decrypt(dic_requisicao['senha'], self.KEY)
            email_db = cryptocode.decrypt(dic_requisicao['email'], self.KEY)
            if email_db == email and senha_db == senha:
                with open("tokken.txt", "w") as arquivo:
                    arquivo.write(f"{id}")
                return True
            elif email_db == email and senha_db != senha:
                frase = "Senhas diferentes"
                return frase
            else:
                return False
        except:
            frase = "Usuário não encontrado"
            return frase

    def add_info(self, nome, data_nascimento, altura, p_f):
        with open("tokken.txt", 'r') as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/info/.json"
        data = {"nome": nome, "data_nascimento": data_nascimento, "altura": altura, "pratica Atividade Fisica": p_f}
        requesicao = requests.post(link, json.dumps(data))

    def add_event(self, horario, nome, tipo, dias):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/eventos/.json"
        data = {"horario": horario, "nome": nome, "tipo": tipo, "dias": dias}
        requesicao = requests.post(link, json.dumps(data))

    def edit_event(self, Old_dictInfo, New_dictInfo):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/eventos/.json"
        requesicao = requests.get(link)
        rect_dict = eval(requesicao.text)
        chaves = ["dias", "horario", 'nome', "tipo"]
        for c, i in rect_dict.items():
            cont = 0
            for x in chaves:
                if str(i[x]) == str(Old_dictInfo[x]):
                    cont += 1
            if cont >= 3:
                print(cont)
                link = self.LINK + id + "/eventos/" + c + "/.json"
                requesicao = requests.patch(link, json.dumps(New_dictInfo))

    def edit_info(self, New_dictInfo):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/info/.json"
        requesicao = requests.get(link)
        requesicao = requesicao.text.replace("true", "True")
        rect_dict = eval(requesicao)
        for x, v in rect_dict.items():
            link = self.LINK + id + "/info/" + x + "/.json"
            requesicao = requests.patch(link, json.dumps(New_dictInfo))
        # cont = 0

    def edit_auth(self, New_dictAuth):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        new_auth = {}
        if "email" in list(New_dictAuth.keys()):
            email = New_dictAuth["email"]

            link = self.LINK + "/.json"
            requisicao = requests.get(link)
            rect_dict = eval(requisicao.text)
            email_exist = False
            for c, i in rect_dict.items():
                i_email = i["auth"]["email"]
                i_email = cryptocode.decrypt(i_email, self.KEY)
                if i_email == email:
                    email_exist = True
            if email_exist:
                return False
            else:
                email = cryptocode.encrypt(email, self.KEY)
                new_auth["email"] = email
        if "senha" in list(New_dictAuth.keys()):
            senha = New_dictAuth["senha"]
            senha = cryptocode.encrypt(senha, self.KEY)
            new_auth["senha"] = senha

        link = self.LINK + id + "/auth/.json"
        requesicao = requests.patch(link, json.dumps(new_auth))
        return True


    def del_event(self, Old_dictInfo):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/eventos/.json"
        requesicao = requests.get(link)
        rect_dict = eval(requesicao.text)
        chaves = ["dias", "horario", 'nome', "tipo"]
        for c, i in rect_dict.items():
            cont = 0
            for x in chaves:
                if str(i[x]) == str(Old_dictInfo[x]):
                    cont += 1
                    print(cont)
            if cont == 4:
                print(Old_dictInfo, i)
                link = self.LINK + id + "/eventos/" + c + "/.json"
                requesicao = requests.delete(link)

    def get_events(self):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/eventos/.json"
        requesicao = requests.get(link)
        rect_dict = eval(requesicao.text)
        lista_eventos = []
        cont = 0
        for c, i in rect_dict.items():
            lista_eventos.append(list(i.values()))
        for c, evento in enumerate(lista_eventos):
            evento = [evento[1], evento[2], evento[3], evento[0]]
            lista_eventos[c] = evento
        return lista_eventos

    def get_info(self):
        with open("tokken.txt", "r") as arquivo:
            id = arquivo.read()
        link = self.LINK + id + "/info/.json"
        requesicao = requests.get(link)
        requesicao = requesicao.text.replace("true", "True")
        rect_dict = eval(requesicao)
        info = []
        cont = 0
        for c, i in rect_dict.items():
            info.append(list(i.values()))
        return info

