class Prototipo():
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione
    

    def modifica_nome(self, nuovo_nome):
        self.nome = nuovo_nome
        print('Nome aggiornato: ', self.nome)


    def stampa_prototipo(self):
        print('Nome prototipo: ', self.nome, '\nDescrizione: ', self.descrizione)

 
class Dipartimento():
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []

    def inserisci(self):
        pass

    def modifica(self):
        pass

    def elimina(self):
        pass

    def ricerca(self):
        pass

    def stampa_catalogo(self):
        pass