import vampiradb.banco as db
from rich import print
from rich.panel import Panel
from rich.table import Table

def leiaint(txt):
    while True:
        try:
            resultado = int(input(txt))
            return resultado
        except ValueError:
            print('[red]ERROR! DIGITE UM VALOR INTEIRO VÁLIDO![/]')
        except KeyboardInterrupt:
            print('[red]ERROR! USUARIO NÃO DIGITOU NADA![/]')

def leiafloat(txt):
    while True:
        try:
            resultado = float(input(txt).replace(',','.'))
            return resultado
        except ValueError:
            print('[red]ERROR! DIGITE UM NUMERO REAL VÁLIDO![/]')
        except KeyboardInterrupt:
            print('[red]ERROR! USUARIO NÃO DIGITOU NADA![/]')

def linha():
    print('-' * 42)

def titulo(txt):
    linha()
    print(f'{txt}'.center(42))
    linha()

def opcoes(opc):
    for id, item in enumerate(opc):
        print(f'{id+1} - {item}')
    linha()

def lerstr(txt):
    while True:
        try:
            resultado = str(input(f'{txt}'))
            return resultado
        except KeyboardInterrupt:
            print('[red]ERRO! USUARIO NAO DIGITOU NADA![/]')

def checar_id(txt):
    listaid = set(db.id_check())
    mostrar_personagens()
    while True:
        escolha = leiaint(f'{txt}')
        if escolha not in listaid:
            print('[red]ID INVALIDA, DIGITE UMA ID QUE ESTEJA NA LISTA![/]')
        else:
            return escolha

def cad_per():
    personagem_dict = {}
    requerimentos = ['name', 'player', 'chronicle', 'nature', 
                     'demeanor', 'clan', 'generation']
    for req in requerimentos:
        valor = lerstr(f'Digite o(a) {req} do personagem: ')
        personagem_dict[req] = valor
    db.cadastrar(personagem_dict)

def attributes():
    escolhas_attributes = {
        1: 'strength',
        2: 'dexterity',
        3: 'stamina',
        4: 'charisma',
        5: 'manipulation',
        6: 'appearance',
        7: 'perception',
        8: 'intelligence',
        9: 'wits'
    }
    tabela_attributes(escolhas_attributes)
    escolha = leiaint('Qual atributo deseja alterar: ')



# to do
def distribuir_pontos():

    abilities = ['alertness', 'athletics', 'awareness', 'brawl',
                 'empathy', 'expression', 'intimidation', 'leadership',
                 'legerdemain', 'subterfuge', 'animal_ken', 'archery',
                 'commerce', 'crafts', 'etiquette', 'melee',
                 'performance', 'ride', 'stealth', 'survival',
                 'academics', 'enigmas', 'hearth_wisdom', 'investigation',
                 'law', 'medicine', 'occultism', 'politics',
                 'seneschal', 'theology']
    
    escolha = leiaint('O que você deseja alterar? ')


def tabela_attributes(dados):
    tb = Table(title=f'Lista Atributos')
    tb.add_column('[yellow]id[/]')
    tb.add_column('[yellow]atributo[/]')
    for key, value in dados.items():
        tb.add_row(str(key), value)
    print(tb)
    

def tabela_personagens(dados):
    tb = Table(title='LISTA DE PERSONAGENS')
    requerimentos = ['id','name', 'player', 'chronicle', 'nature', 
                     'demeanor', 'clan', 'generation']
    for a in requerimentos:
        tb.add_column(f'[yellow]{a}[/]')
    for a in dados:
        tb.add_row(*[str(item) for item in a])
    print(tb)
    
def mostrar_personagens():
    linha()
    tabela_personagens(db.mostra_personagensdb())
    linha()

def excluir_personagem():
    escolha = checar_id('Digite o ID do personagem que quer excluir: ')
    db.excluir_personagemdb(escolha)

def sistema_escolha(txt):
    lista_escolhas = {
        1: cad_per,
        2: mostrar_personagens,
        3: excluir_personagem,
        4: alterar_personagem,
    }
    while True:
        escolha = leiaint(txt)
        if escolha not in lista_escolhas:
            if escolha == 5:
                return False
            print('Digite uma opção válida')
        else:
            break
    lista_escolhas[escolha]()

def alterar_personagem():
    escolhaid = checar_id('Digite o ID do personagem que deseja alterar: ')
    linha()
    lista_escolhas = {
        1: 'name',
        2: 'player',
        3: 'chronicle',
        4: 'nature',
        5: 'demeanor',
        6: 'clan',
        7: 'generation',
    }
    print('Escolha oq vc quer alterar')
    for key, value in lista_escolhas.items():
        print(f'{key} - {value}')
    linha()
    while True:
        escolha = leiaint('Sua opção: ')
        if escolha not in lista_escolhas:
            print('DIGITE UMA OPÇÃO VÁLIDA!')
        else:
            break
    linha()
    alt = str(input('Digite a alteração: '))
    db.alterardb(escolhaid, lista_escolhas[escolha], alt)
