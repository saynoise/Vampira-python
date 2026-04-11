import sqlite3
from rich import print



def iniciardb():

    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS personagens (
                      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        player TEXT NOT NULL,
        chronicle TEXT NOT NULL,
        nature TEXT NOT NULL,
        demeanor TEXT NOT NULL,
        clan TEXT NOT NULL,
        generation TEXT NOT NULL)''')


def mostra_personagensdb():

    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()

        cursor.execute('''SELECT id, name, player, chronicle, nature, 
                             demeanor, clan, generation FROM personagens''')
        return cursor.fetchall()

def cadastrar(cad_dict):
    # TEMPORARIO
    adc = []
    for item in cad_dict.values():
        adc.append(item)
    dados = tuple(adc)

    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO personagens(name, player, chronicle, nature,
        demeanor, clan, generation) VALUES(?,?,?,?,?,?,?)''',dados)

def excluir_personagemdb(id):
    with sqlite3.connect('sistemavampira.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM personagens WHERE id = ?',(id,))

def id_check():
    try:
        with sqlite3.connect('sistemavampira.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT id FROM personagens')
            idgeral = cursor.fetchall()
            ids = []
            for a in idgeral:
                ids.append(a[0])
            return ids
    except sqlite3.Error as e:
        print(f'Erro ao checar ids: {e}')

def alterardb(id,campo, alt):
    try:
        with sqlite3.connect('sistemavampira.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute(f'UPDATE personagens SET {campo} = ? WHERE id = ?',(alt, id))
    except sqlite3.Error as e:
        print(f'Erro Ao alterar dados: {e}')
