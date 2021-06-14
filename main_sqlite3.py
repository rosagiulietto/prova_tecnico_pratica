import sqlite3

conn = sqlite3.connect('database_prototipi.db')

c = conn.cursor()

# c.execute("""create table prototipi (
#     nome text,
#     descrizione text,
#     dipartimento text)""")


class Prototipo():
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione


    def stampa_dettagli(self):
        print('Nome prototipo: ', self.nome, '\nDescrizione: ', self.descrizione)

 
class Dipartimento():
    def __init__(self, nome, cursore):
        self.nome = nome
        self.cursore = cursore

    def inserisci(self, prototipo): # OK
        with conn:
            self.cursore.execute("insert into prototipi values(?, ?, ?)", 
                (prototipo.nome, prototipo.descrizione, self.nome))


    # OGNI DIPARTIMENTO HA LA FACOLTA' DI ELIMINARE SOLO I PROTOTIPI DEL PROPRIO CATALOGO
    def elimina(self): # OK
        print('Dipartimento di', self.nome)
        with conn:
            self.cursore.execute("SELECT oid, * FROM prototipi WHERE dipartimento = ?", (self.nome, ))
            for p in self.cursore.fetchall():
                print(p[0], p[2])
            p_id = input('Quale prototipo vuoi eliminare? Prototipo numero: ')
            self.cursore.execute("delete from prototipi where oid = ?", (p_id,))
            print('Prototipo eliminato!')


    # OGNI DIPARTIMENTO HA LA FACOLTA' DI MODIFICARE LA DESCRIZIONE DEI PROTOTIPI DEL PROPRIO CATALOGO
    def modifica_descrizione(self):
        print('Dipartimento di', self.nome)
        with conn:
            self.cursore.execute("SELECT oid, * FROM prototipi WHERE dipartimento = ?", (self.nome, ))
            for p in self.cursore.fetchall():
                print('ID', p[0], p[2])

            p_id = input('Quale prototipo vuoi modificare? Prototipo numero: ')
            nuova_descrizione = input('Nuova descrizione: ')

            self.cursore.execute("UPDATE prototipi SET descrizione = ? WHERE oid = ?", (nuova_descrizione, p_id))

            print("Prototipo aggiornato!")
            self.cursore.execute("SELECT oid, * FROM prototipi WHERE dipartimento = ?", (self.nome, ))
            for p in self.cursore.fetchall():
                print('ID', p[0], p[2])


    def ricerca(self, nome_prototipo):
        with conn:
            self.cursore.execute("SELECT * FROM prototipi WHERE nome = ?", (nome_prototipo, ))
            print(self.cursore.fetchall())


    def stampa_catalogo(self): # OK
        with conn:
            print('Catalogo Dipartimento di Ottica:')
            self.cursore.execute("SELECT * FROM prototipi WHERE dipartimento = 'ottica'")
            for p in self.cursore:
                print(p[1])

            print('\nCatalogo Dipartimento di Cosmetica:')
            self.cursore.execute("SELECT * FROM prototipi WHERE dipartimento = 'cosmetica'")
            for p in self.cursore:
                print(p[1])

            print('\nCatalogo Dipartimento di Ortopedia:')
            self.cursore.execute("SELECT * FROM prototipi WHERE dipartimento = 'ortopedia'")
            for p in self.cursore:
                print(p[1])


# CREAZIONE PROTOTIPI
p1 = Prototipo('lucidalabbra', 'lucidalabbra idratante con burro di karitè')
p2 = Prototipo('plantare', 'plantare ortopedico per tallonite')
p3 = Prototipo('montatura', 'montatura in fibra di carbonio')
p4 = Prototipo('eyeliner', 'eyeliner azzurro cangiante')
p5 = Prototipo('protesi', 'protesi a stelo corto')
p6 = Prototipo('lenti', 'lenti progressive')

# CREAZIONE DIPARTIMENTI
d1 = Dipartimento('cosmetica', c)
d2 = Dipartimento('ortopedia', c)
d3 = Dipartimento('ottica', c)

# INSERIMENTO PROTOTIPI IN DATABASE
d1.inserisci(p1)
d2.inserisci(p2)
d3.inserisci(p3)
d1.inserisci(p4)
d2.inserisci(p5)
d3.inserisci(p6)

# ELIMINAZIONE PROTOTIPO
d3.elimina()

# MODIFICA DESCRIZIONE DI UN PROTOTIPO
d3.modifica_descrizione()

# RICERCA PROTOTIPO
d1.ricerca('eyeliner')

# STAMPA CATALOGHI
d3.stampa_catalogo()

conn.close()