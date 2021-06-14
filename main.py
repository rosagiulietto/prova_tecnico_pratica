class Prototipo():
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione
    

    def modifica_nome(self, nuovo_nome):
        self.nome = nuovo_nome
        print('Nome aggiornato: ', self.nome)


    def stampa_dettagli(self):
        print('Nome prototipo: ', self.nome, '\nDescrizione: ', self.descrizione)

 
class Dipartimento():
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []


    def inserisci(self, prototipo): # OK
        self.catalogo.append(prototipo)
        print('Prototipo aggiunto')


    def elimina(self, prototipo): # OK
        if prototipo in self.catalogo:
            self.catalogo.remove(prototipo)
            print('Prototipo eliminato')
        else:
            print('Prototipo non presente...')


    def ricerca(self, nome_prototipo):
        for p in self.catalogo:
            if p.nome == nome_prototipo:
                print('Prototipo trovato:\n', p.stampa_dettagli)
            else:
                print('Prototipo non trovato...')


    def stampa_catalogo(self): # OK
        print('Catalogo:')
        for p in self.catalogo:
            print(p.nome)


# CREAZIONE PROTOTIPI
prototipo1 = Prototipo('plantare n.1', 'plantare ortopedico - mal di schiena')
prototipo2 = Prototipo('plantare n.2', 'plantare ortopedico - tallonite')


# CREAZIONE DIPARTIMENTO E RELATIVO CATALOGO
dipartimento1 = Dipartimento('ortopedia')


# INSERIMENTO PROTOTIPI
dipartimento1.inserisci(prototipo1)
dipartimento1.inserisci(prototipo2)


# ELIMINAZIONE PROTOTIPO
dipartimento1.elimina(prototipo2)


# RICERCA PROTOTIPO
dipartimento1.ricerca('plantare n.3')


# MODIFICA NOME 
prototipo2.modifica_nome('plantare universitario')
