#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Luiz Felipe
#
# Created:     06/02/2022
# Copyright:   (c) Luiz Felipe 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import AdTools
import csv
def main():
    logins = {}
    try:
        with open("users.txt", "r", encoding="utf-8") as users:
            for linha in users:
                line = linha.rstrip('\n')
                login = []
                nome = AdTools.name_remove_prepositions(AdTools.name_sanitize(line))
                login.append(AdTools.login_generator(nome)[0])
                login.append(AdTools.login_generator(nome)[1])
                logins[line] = login
            users.close()
    except FileNotFoundError as err:
        print(err)
    try:
        with open('users.csv', 'w', newline='', encoding='utf-8') as csv_file:
            arq =  csv.writer(csv_file, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            arq.writerow(["username1", "username2", "nome", "sobrenome", "senha", "email1","email2" ,"grupo", "ou"])
            for l in logins:
                palavras = l.split()
                nome = palavras[0]
                sobrenome = ' '.join(palavras[1:len(palavras)])
                arq.writerow([f'{logins[l][0]}', f'{logins[l][1]}', nome, sobrenome, "pmp@2022", f'{logins[l][0]}@parnamirim.rn.gov.br', f'{logins[l][1]}@parnamirim.rn.gov.br', f'{group}',f'{ou}'])
    except FileNotFoundError as err:
        print(err)

if __name__ == '__main__':
    main()
