import vampiradb.banco as db
from rich import print
from rich.panel import Panel
from rich.table import Table

abilities_dict = {
    1: 'alertness',
    2: 'athletics',
    3: 'awareness',
    4: 'brawl',
    5: 'empathy',
    6: 'expression',
    7: 'intimidation',
    8: 'leadership',
    9: 'legerdemain',
    10: 'subterfuge',
    11: 'animal_ken',
    12: 'archery',
    13: 'commerce',
    14: 'crafts',
    15: 'etiquette',
    16: 'melee',
    17: 'performance',
    18: 'ride',
    19: 'stealth',
    20: 'survival',
    21: 'academics',
    22: 'enigmas',
    23: 'hearth_wisdom',
    24: 'investigation',
    25: 'law',
    26: 'medicine',
    27: 'occultism',
    28: 'politics',
    29: 'seneschal',
    30: 'theology'
}

def leiaint(txt=''):
    while True:
        try:
            resultado = int(input(txt))
            return resultado
        except ValueError:
            print('[red]ERROR! DIGITE UM VALOR INTEIRO VÁLIDO![/]')
        except KeyboardInterrupt:
            print('[red]ERROR! USUARIO NÃO DIGITOU NADA![/]')

def leiafloat(txt=''):
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

def alt_advantages(id):
    pass

def tabela_advantages(dados):
    tb = Table(title=f'TABELA VANTAGENS')
    tb.add_column('ID')
    tb.add_column('Vantagem')
    for key, value in dados.items():
        tb.add_row(str(key), value)
    print(tb)

def add_advantages(id):
    nome_vantagem = lerstr('Digite o nome da vantagem: ')
    nivel_vantagem = leiaint(f'Digite o nivel de {nome_vantagem}: ')
    db.adicionar_advantages(nome_vantagem, nivel_vantagem, id)

def attributes(id):
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
    while True:
        escolha = leiaint('Qual atributo deseja alterar: ')
        if escolha not in escolhas_attributes:
            print(f'[red]DIGITE UMA OPÇÃO VÁLIDA![/]')
        else:
            break
    valor = leiaint(f'Qual o novo valor de {escolhas_attributes[escolha]}: ')
    db.alterar_attributes(id, escolhas_attributes[escolha], valor)

def alt_attributes(id):
    dados = db.alterar_attributes(id)
    tabela_attributes(dados)

def criar_abilities(id):

    for habilidade in abilities_dict.values():
        while True:
            try:
                escolha = input(f'digite o valor de {habilidade}:')
                if escolha == '':
                    break
                escolha = int(escolha)
                db.alterar_abilities(id, habilidade, escolha)
                break
            except ValueError:
                print('[red]VALOR INVÁLIDO[/]')

def tabela_abilities(id):
    dados = db.mostra_abilities(id)
    count = 0
    tb = Table(title='Lista Abilities')
    tb.add_column('ID')
    tb.add_column('Ability')
    tb.add_column('Value')
    for ability, valor in zip(abilities_dict.values(), dados[0]):
        count += 1
        tb.add_row(str(count),str(ability),str(valor))
    print(tb)
        
def tabela_attributes(dados):
    tb = Table(title=f'Lista Atributos')
    tb.add_column('[yellow]ID[/]')
    tb.add_column('[yellow]Atributo[/]')
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

def header(escolhaid):
    lista_escolhas = {
        1: 'name',
        2: 'player',
        3: 'chronicle',
        4: 'nature',
        5: 'demeanor',
        6: 'clan',
        7: 'generation',
    }
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

def alterar_personagem():
    escolhaid = checar_id('Digite o ID do personagem que deseja alterar: ')
    linha()
    print('Escolha oq vc quer alterar')
    print('''1 - Header
2 - Atributos
3 - Habilidades
4 - Vantagens ''')
    linha()
    escolha_opc = leiaint()
    while escolha_opc not in range(1,5):
        print('OPÇAO INVALIDA, ESCOLHA UM NUMERO DE 1 A 4.')
        escolha_opc = leiaint()

    if escolha_opc == 1:
        header(escolhaid)
    
    elif escolha_opc == 2:
        attributes(escolhaid)
    
    elif escolha_opc == 3:
        while True:
            tabela_abilities(escolhaid)
            id_abilities = leiaint('Digite o ID da habilidade que deseja alterar: ')
            while id_abilities not in abilities_dict:
                print(f'[red]Digite um id entre 1 e 30![/]')
                id_abilities = leiaint('Digite o ID da habilidade que deseja alterar: ')

            while True:
                value_abilities = leiaint('Digite o novo valor da habilidade: ')
                if value_abilities <= 6 and value_abilities >= 0:
                    db.alterar_abilities(escolhaid, abilities_dict[id_abilities], value_abilities)
                    break
                else:
                    print('[red] DIGITE UM VALOR ENTRE 0 E 6![/]')

            print('Deseja Alterar mais alguma habilidade? [S/N]')
            
            loop_abilities = lerstr('').strip().upper()
            while not loop_abilities or loop_abilities[0] not in 'SN':
                print('Escolha entre Sim e Não!')
                loop_abilities = lerstr('').strip().upper()

            loop_abilities = loop_abilities[0]

            if loop_abilities == 'N':
                break
    
    elif escolha_opc == 4:
        print('1 - Adicionar Vantagem\n2 - Alterar Vantagem')
        while True:
            escolha_vantagem = leiaint()
            if escolha_vantagem == 1:
                add_advantages(escolhaid)
                break
            elif escolha_vantagem == 2:
                print('todo')
                break
            else:
                print('ESCOLHA INVÁLIDA, ESCOLHA ENTRE 1 E 2.')
