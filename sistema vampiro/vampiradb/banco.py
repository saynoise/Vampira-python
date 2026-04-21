import sqlite3
from rich import print



def iniciardb():
    try:
        with sqlite3.connect('sistemavampira.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('PRAGMA foreign_keys = ON')

            # Cria tabela principal
            cursor.execute('''CREATE TABLE IF NOT EXISTS personagens (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        player TEXT NOT NULL,
                        chronicle TEXT NOT NULL,
                        nature TEXT NOT NULL,
                        demeanor TEXT NOT NULL,
                        clan TEXT NOT NULL,
                        generation TEXT NOT NULL)''')

            # Cria tabela de atributos
            cursor.execute('''CREATE TABLE IF NOT EXISTS attributes (
                        personagem_id INTEGER PRIMARY KEY,
                        strength INTEGER NOT NULL DEFAULT 0,
                        dexterity INTEGER NOT NULL DEFAULT 0,
                        stamina INTEGER NOT NULL DEFAULT 0,
                        charisma INTEGER NOT NULL DEFAULT 0,
                        manipulation INTEGER NOT NULL DEFAULT 0,
                        appearance INTEGER NOT NULL DEFAULT 0,
                        perception INTEGER NOT NULL DEFAULT 0,
                        intelligence INTEGER NOT NULL DEFAULT 0,
                        wits INTEGER NOT NULL DEFAULT 0,
                        FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE)''')

            # Cria tabela de habilidades
            cursor.execute('''CREATE TABLE IF NOT EXISTS abilities (
                        personagem_id INTEGER PRIMARY KEY,
                        alertness INTEGER NOT NULL DEFAULT 0,
                        athletics INTEGER NOT NULL DEFAULT 0,
                        awareness INTEGER NOT NULL DEFAULT 0,
                        brawl INTEGER NOT NULL DEFAULT 0,
                        empathy INTEGER NOT NULL DEFAULT 0,
                        expression INTEGER NOT NULL DEFAULT 0,
                        intimidation INTEGER NOT NULL DEFAULT 0,
                        leadership INTEGER NOT NULL DEFAULT 0,
                        legerdemain INTEGER NOT NULL DEFAULT 0,
                        subterfuge INTEGER NOT NULL DEFAULT 0,
                        animal_ken INTEGER NOT NULL DEFAULT 0,
                        archery INTEGER NOT NULL DEFAULT 0,
                        commerce INTEGER NOT NULL DEFAULT 0,
                        crafts INTEGER NOT NULL DEFAULT 0,
                        etiquette INTEGER NOT NULL DEFAULT 0,
                        melee INTEGER NOT NULL DEFAULT 0,
                        performance INTEGER NOT NULL DEFAULT 0,
                        ride INTEGER NOT NULL DEFAULT 0,
                        stealth INTEGER NOT NULL DEFAULT 0,
                        survival INTEGER NOT NULL DEFAULT 0,
                        academics INTEGER NOT NULL DEFAULT 0,
                        enigmas INTEGER NOT NULL DEFAULT 0,
                        hearth_wisdom INTEGER NOT NULL DEFAULT 0,
                        investigation INTEGER NOT NULL DEFAULT 0,
                        law INTEGER NOT NULL DEFAULT 0,
                        medicine INTEGER NOT NULL DEFAULT 0,
                        occultism INTEGER NOT NULL DEFAULT 0,
                        politics INTEGER NOT NULL DEFAULT 0,
                        seneschal INTEGER NOT NULL DEFAULT 0,
                        theology INTEGER NOT NULL DEFAULT 0,
                        FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE)''')
            
            # Cria tabela de vantagens/magiazinha etc
            cursor.execute('''CREATE TABLE IF NOT EXISTS advantages (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           personagem_id INTEGER NOT NULL,
                           name TEXT NOT NULL,
                           value INTEGER NOT NULL DEFAULT 0,
                           FOREIGN KEY (personagem_id) REFERENCES personagens(id) ON DELETE CASCADE)''')
    except sqlite3.Error as e:
        print(f'Deu Erro {e}')


def mostra_personagensdb():

    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')

        cursor.execute('''SELECT id, name, player, chronicle, nature, 
                             demeanor, clan, generation FROM personagens''')
        return cursor.fetchall()

def cadastrar(cad_dict):
    dados = tuple(cad_dict.values())

    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')

        cursor.execute('''INSERT INTO personagens(name, player, chronicle, nature,
        demeanor, clan, generation) VALUES(?,?,?,?,?,?,?)''',dados)

        personagem_id = cursor.lastrowid
        cursor.execute('INSERT INTO attributes (personagem_id) VALUES (?)', (personagem_id,))

        cursor.execute('INSERT INTO abilities(personagem_id) VALUES (?)', (personagem_id,))

def cadastrar_abilities(cad_dict):
    pass
        
def excluir_personagemdb(id):
    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute('DELETE FROM personagens WHERE id = ?',(id,))

def id_check():
    try:
        with sqlite3.connect('sistemavampira.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('PRAGMA foreign_keys = ON')
            cursor.execute('SELECT id FROM personagens')
            idgeral = cursor.fetchall()
            ids = [a[0] for a in idgeral]
            return ids
    except sqlite3.Error as e:
        print(f'Erro ao checar ids: {e}')

def alterardb(id,campo, alt):
    campos_validos = {'name', 'player', 'chronicle', 'nature', 'demeanor',
                    'clan', 'generation'}
    if campo not in campos_validos:
        print(f'[red]campo inválido: {campo}[/]')
        return
    try:
        with sqlite3.connect('sistemavampira.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('PRAGMA foreign_keys = ON')
            cursor.execute(f'UPDATE personagens SET {campo} = ? WHERE id = ?',(alt, id))
    except sqlite3.Error as e:
        print(f'Erro Ao alterar dados: {e}')
