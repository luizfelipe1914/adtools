# FUNÇÃO QUE GERA OS LOGINS:
def login_generator(names):
	i = 0
	logins = []
	while(i <= len(names) -1 ):
		j = len(names) -1
		while(j >= 0):
			if(i != j):
				logins.append(f'{names[i]}.{names[j]}')
			j -= 1
		i += 1
	return logins


# FUNÇÃO QUE REMOVE TODOS OS ACENTOS E CARACTERES COM TIL:
# RECEBE COMO PARÂMETRO O NOME E O RETORNA SEM ACENTOS, TILS OU CE-CEDILHA

def name_sanitize(nome):
	nome = nome.lower()
	caracteres = {'á':'a',
				  'é':'e',
				  'í':'i',
				  'ó':'o',
				  'ú':'u',
				  'ê':'e',
				  'ô':'o',
				  'ã':'a',
				  'õ':'o',
				  'î':'i',
				  'ç':'c',
				  'ü':'u',
				  'ũ':'u'
				 }
	for c in caracteres:
		nome = nome.replace(c, caracteres[c])
	return nome

# FUNÇÃO QUE REMOVE AS PREPOSIÇÕES DO NOME:
# RECEBE O NOME COMO PARÂMETRO E RETORNO UMA LISTA COM OS NOMES SEM AS PREPOSIÇÕES

def name_remove_prepositions(name):
	prep = ['de', 'da', 'dos', 'e','\n']
	name = name.split()
	for p in prep:
		if(p in name):
			name.remove(p)
	return name

