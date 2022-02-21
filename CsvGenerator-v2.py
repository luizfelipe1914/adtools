#!/usr/bin/env python3

import csv
import AdTools
import datetime

def main():
    logins = {}
    grupos = []
    ous = []
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            content = file.read()
            #content = content.split('\n')
    except FileNotFoundError as err:
        print(err)

    
    for index in range(0, 3 ,len(content)+1):
        login = []
        name = AdTools.name_remove_prepositions(AdTools.name_sanitize(content[index]))
        login.append(AdTools.login_generator(name)[0])
        login.append(AdTools.login_generator(name)[1])
        grupos.append(content[index+1])
        ous.append(content[index+2])
        logins[content[index]] = login 


    try:
        with open('users.csv', 'w', newline='', encoding='utf-8') as csv_file:
            arq =  csv.writer(csv_file, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            arq.writerow(["username1", "username2", "nome", "sobrenome", "senha", "email1","email2" ,"grupo", "ou"])
            contador = 0
            for l in logins:
                palavras = l.split()
                nome = palavras[0]
                sobrenome = ' '.join(palavras[1:len(palavras)])
                arq.writerow([f'{logins[l][0]}', 
                              f'{logins[l][1]}', 
                              nome, 
                              sobrenome, 
                              f"pmp@{datetime.datetime.now().year}", 
                              f'{logins[l][0]}@parnamirim.rn.gov.br', 
                              f'{logins[l][1]}@parnamirim.rn.gov.br', 
                              f'{grupos[contador]}',
                              f'{ous[contador]}'])
                contador+=1
    except FileNotFoundError as err:
        print(err)
if(__name__ == '__main__'):
    main()