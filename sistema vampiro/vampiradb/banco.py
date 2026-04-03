import sqlite3



def iniciardb():

    conexao = sqlite3.connect('sistemavampira.db')
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
    conexao.commit()
    conexao.close()

def mostra_personagensdb():

    conexao = sqlite3.connect('sistemavampira.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT id, name, player, chronicle, nature, 
                             demeanor, clan, generation FROM personagens''')
    personagens = cursor.fetchall()
    for personagem in personagens:
        id, name, player, chronicle, nature, demeanor, clan, generation = personagem
        print(f'''ID: {id} - nome: {name} | Jogador: {player} | Campanha: {chronicle}
Natureza: {nature} | Demeanor: {demeanor} | Clan: {clan} | Generation {generation}''')

def cadastrar(cad_dict):

    adc = []
    for item in cad_dict.values():
        adc.append(item)
    dados = tuple(adc)

    conexao = sqlite3.connect('sistemavampira.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO personagens(name, player, chronicle, nature,
    demeanor, clan, generation) VALUES(?,?,?,?,?,?,?)''',dados)
    conexao.commit()
    conexao.close()

def excluir_personagemdb(id):
    conexao = sqlite3.connect('sistemavampira.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM personagens WHERE id = ?',(id,))
    conexao.commit()
    conexao.close()

def id_check():
    conexao = None
    try:
        conexao = sqlite3.connect('sistemavampira.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT id FROM personagens')
        idgeral = cursor.fetchall()
        ids = []
        for a in idgeral:
            ids.append(a[0])
        return ids
    except:
        print('Nao foi possivel checar ids (nao sei os codigos de erro ainda)')
    finally:
        if conexao:
            conexao.close()

def alterardb(id,campo, alt):
    conexao = None
    try:
        conexao = sqlite3.connect('sistemavampira.db')
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE personagens SET {campo} = ? WHERE id = ?',(alt, id))
        conexao.commit()
    except:
        print('Erro, nao foi possivel alterar os dados')
    finally:
        if conexao:
            conexao.close()
