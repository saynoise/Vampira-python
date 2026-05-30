"""
Módulo interface.py - Gerenciar a interface do terminal.

Responsável por: menus, tabelas, entrada de dados do usuário e navegação da aplicação.
"""
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

attributes_dict = {
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

def leiaint(txt=''):
    """Lê um inteiro do usuário com validação.
    
    Args:
        txt: Texto do prompt
        
    Returns:
        int: Valor inteiro inserido
    """
    while True:
        try:
            resultado = int(input(txt))
            return resultado
        except ValueError:
            print('[red]ERROR! DIGITE UM VALOR INTEIRO VÁLIDO![/]')
        except KeyboardInterrupt:
            print('[red]ERROR! USUARIO NÃO DIGITOU NADA![/]')

def leiafloat(txt=''):
    """Lê um número float do usuário com validação.
    
    Args:
        txt: Texto do prompt
        
    Returns:
        float: Valor float inserido
    """
    while True:
        try:
            resultado = float(input(txt).replace(',','.'))
            return resultado
        except ValueError:
            print('[red]ERROR! DIGITE UM NUMERO REAL VÁLIDO![/]')
        except KeyboardInterrupt:
            print('[red]ERROR! USUARIO NÃO DIGITOU NADA![/]')

def linha():
    """Imprime uma linha divisória."""
    print('-' * 42)

def titulo(txt):
    """Exibe um título centralizado com divisórias.
    
    Args:
        txt: Texto do título
    """
    linha()
    print(f'{txt}'.center(42))
    linha()

def opcoes(opc):
    """Exibe um menu com opções numeradas.
    
    Args:
        opc: Lista de opções a exibir
    """
    for id, item in enumerate(opc):
        print(f'{id+1} - {item}')
    linha()

def lerstr(txt):
    """Lê uma string do usuário.
    
    Args:
        txt: Texto do prompt
        
    Returns:
        str: String inserida
    """
    while True:
        try:
            resultado = str(input(f'{txt}'))
            return resultado
        except KeyboardInterrupt:
            print('[red]ERRO! USUARIO NAO DIGITOU NADA![/]')

def checar_id(txt):
    """Valida e retorna um ID de personagem existente.
    
    Args:
        txt: Texto do prompt
        
    Returns:
        int: ID válido do personagem
    """
    listaid = set(db.id_check())
    mostrar_personagens()
    while True:
        escolha = leiaint(f'{txt}')
        if escolha not in listaid:
            print('[red]ID INVALIDA, DIGITE UMA ID QUE ESTEJA NA LISTA![/]')
        else:
            return escolha

def cad_per():
    """Cadastra um novo personagem no banco de dados."""
    personagem_dict = {}
    requerimentos = ['name', 'player', 'chronicle', 'nature', 
                     'demeanor', 'clan', 'generation']
    for req in requerimentos:
        valor = lerstr(f'Digite o(a) {req} do personagem: ')
        personagem_dict[req] = valor
    cad = db.cadastrar(personagem_dict)

    criar_abilities(cad)

def alt_advantages(escolhaid):
    """Altera uma vantagem existente de um personagem."""
    while True:
        id_advantage = leiaint('Digite o ID da Vantagem que deseja alterar: ')

        ids_validos = [row[0] for row in db.mostra_advantages(escolhaid)]

        while id_advantage not in ids_validos:
            print('[red]ID INVALIDA! DIGITE UMA ID QUE ESTEJA EM:[/]')
            tabela_advantages(escolhaid)
            id_advantage = leiaint('Digite o ID da Vantagem que deseja alterar: ')
        print('O que deseja alterar? \n1 - Titulo\n2 - Valor')
        escolha = leiaint()
        while escolha not in (1,2):
            print('[red]ESCOLHA INVALIDA![/]')
            escolha = leiaint()

        name = ''
        value = None

        if escolha == 1:
            name = lerstr('Digite o novo nome: ')
            while name == '':
                print('[red]DIGITE UM NOME![/]')
                name = lerstr('')
        if escolha == 2:
            value = leiaint('Digite o novo valor: ')
        db.alterar_advantages(escolhaid, id_advantage, name, value)

        print('Deseja Alterar mais alguma habilidade? [S/N]')
        
        loop_advantage = lerstr('').strip().upper()
        while not loop_advantage or loop_advantage[0] not in 'SN':
            print('Escolha entre Sim e Não!')
            loop_advantage = lerstr('').strip().upper()

        loop_advantage = loop_advantage[0]

        if loop_advantage == 'N':
            break

def add_advantages(id):
    """Adiciona uma nova vantagem a um personagem.
    
    Args:
        id: ID do personagem
    """
    nome_vantagem = lerstr('Digite o nome da vantagem: ')
    nivel_vantagem = leiaint(f'Digite o nivel de {nome_vantagem}: ')
    db.adicionar_advantages(nome_vantagem, nivel_vantagem, id)

def attributes(id):
    """Altera um atributo de um personagem.
    
    Args:
        id: ID do personagem
    """
    tabela_attributes(attributes_dict)
    while True:
        escolha = leiaint('Qual atributo deseja alterar: ')
        if escolha not in attributes_dict:
            print(f'[red]DIGITE UMA OPÇÃO VÁLIDA![/]')
        else:
            break
    valor = leiaint(f'Qual o novo valor de {attributes_dict[escolha]}: ')
    db.alterar_attributes(id, attributes_dict[escolha], valor)

def criar_abilities(id):
    """Cria os valores iniciais de habilidades para um novo personagem.
    
    Args:
        id: ID do personagem recém-criado
    """
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

def tabela_advantages(escolhaid):
    """Exibe tabela com as vantagens de um personagem.
    
    Args:
        escolhaid: ID do personagem
    """
    dados = db.mostra_advantages(escolhaid)
    tb = Table(title='Lista Advantages')
    tb.add_column('ID')
    tb.add_column('Advantage')
    tb.add_column('Value')
    for id, advantage, value in dados:
        tb.add_row(str(id), str(advantage), str(value))
    print(tb)

def tabela_abilities(id):
    """Exibe tabela com as habilidades de um personagem.
    
    Args:
        id: ID do personagem
    """
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
    """Exibe tabela com atributos.
    
    Args:
        dados: Dicionário com atributos e seus IDs
    """
    tb = Table(title=f'Lista Atributos')
    tb.add_column('[yellow]ID[/]')
    tb.add_column('[yellow]Atributo[/]')
    for key, value in dados.items():
        tb.add_row(str(key), value)
    print(tb)    

def tabela_personagens(dados):
    """Exibe tabela com lista de personagens.
    
    Args:
        dados: Lista de personagens do banco de dados
    """
    tb = Table(title='LISTA DE PERSONAGENS')
    requerimentos = ['id','name', 'player', 'chronicle', 'nature', 
                     'demeanor', 'clan', 'generation']
    for a in requerimentos:
        tb.add_column(f'[yellow]{a}[/]')
    for a in dados:
        tb.add_row(*[str(item) for item in a])
    print(tb)
    
def mostrar_personagens():
    """Exibe a lista de todos os personagens cadastrados."""
    linha()
    tabela_personagens(db.mostra_personagensdb())
    linha()

def excluir_personagem():
    """Exclui um personagem do banco de dados."""
    escolha = checar_id('Digite o ID do personagem que quer excluir: ')
    db.excluir_personagemdb(escolha)

def sistema_escolha(txt):
    """Exibe o menu principal e executa a opção escolhida.
    
    Args:
        txt: Texto do prompt
        
    Returns:
        bool: False se usuário escolher sair, None caso contrário
    """
    lista_escolhas = {
        1: cad_per,
        2: mostrar_personagens,
        3: excluir_personagem,
        4: alterar_personagem,
        5: acessar_ficha
    }
    while True:
        escolha = leiaint(txt)
        if escolha not in lista_escolhas:
            if escolha == 6:
                return False
            print('Digite uma opção válida')
        else:
            break
    lista_escolhas[escolha]()

def header(escolhaid):
    """Altera os dados principais (header) de um personagem.
    
    Args:
        escolhaid: ID do personagem
    """
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

def abilities(id):
    """Altera as habilidades de um personagem.
    
    Args:
        id: ID do personagem
    """
    while True:
        tabela_abilities(id)
        id_abilities = leiaint('Digite o ID da habilidade que deseja alterar: ')
        while id_abilities not in abilities_dict:
            print(f'[red]Digite um id entre 1 e 30![/]')
            id_abilities = leiaint('Digite o ID da habilidade que deseja alterar: ')

        while True:
            value_abilities = leiaint('Digite o novo valor da habilidade: ')
            if value_abilities <= 6 and value_abilities >= 0:
                db.alterar_abilities(id, abilities_dict[id_abilities], value_abilities)
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

def del_advantage(escolhaid):
    """Exclui uma vantagem de um personagem.
    
    Args:
        escolhaid: ID do personagem
    """
    tabela_advantages(escolhaid)

    ids_validos = [row[0] for row in db.mostra_advantages(escolhaid)]

    id_del = leiaint('Digite o id da vantagem que deseja excluir: ')
    while id_del not in ids_validos:
        print('[red]ID INVÁLIDA DIGITE UM ID QUE ESTEJA EM:[/]')
        tabela_advantages(escolhaid)
        id_del = leiaint('Digite o id da vantagem que deseja excluir: ')
    
    db.excluir_advantage(escolhaid, id_del)

def alterar_personagem():
    """Menu para alterar dados de um personagem existente."""
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
        abilities(escolhaid)
    
    elif escolha_opc == 4:
        tabela_advantages(escolhaid)
        print('1 - Adicionar Vantagem\n2 - Alterar Vantagem\n3 - Excluir Vantagem')
        while True:
            escolha_vantagem = leiaint()
            if escolha_vantagem == 1:
                add_advantages(escolhaid)
                break
            elif escolha_vantagem == 2:
                alt_advantages(escolhaid)
                break
            elif escolha_vantagem == 3:
                del_advantage(escolhaid)
            else:
                print('ESCOLHA INVÁLIDA, ESCOLHA ENTRE 1 E 2.')

def acessar_ficha():
    """Acessa a ficha de um personagem para consultar e preparar dados para rolagem.
    
    Permite ao usuário:
    - Adicionar dados de abilities, attributes ou advantages para rolar
    - Remover dados da seleção
    - Finalizar a seleção
    """
    linha()
    print('Qual ficha deseja acessar?')
    linha()

    escolha_personagem = checar_id('Digite o ID da ficha que deseja usar: ')
    dados = []

    while True:
        print('''1 - Adicionar Dados
2 - Remover Dados
3 - Sair e Rodar Dados''')
        
        escolha = leiaint()
        while escolha not in range(1, 4):
            print('escolha inválida, escolha um numero entre 1 e 3!')
            escolha = leiaint()

        if escolha == 1:
            print('''1 - abilities
2 - attributes
3 - advantages''')
            escolha_dados = leiaint()
            while escolha_dados not in range(1,4):
                escolha_dados = leiaint('Escolha um numero entre 1 e 3! ')
            
            if escolha_dados == 1:
                tabela_abilities(escolha_personagem)
                id_abilities = leiaint('Digite o ID da habilidade que deseja rolar: ')
                while id_abilities not in abilities_dict:
                    print(f'[red]Digite um id entre 1 e 30![/]')
                    id_abilities = leiaint('Digite o ID da habilidade que deseja rolar: ')
                dados.append(db.mostra_abilities(escolha_personagem)[0][id_abilities - 1])

            if escolha_dados == 2:
                tabela_attributes(attributes_dict)
                id_attributes = leiaint('Digite o ID do Atributo que deseja rolar: ')
                while id_attributes not in attributes_dict:
                    print(f'[red]Digite um id entre 1 e 9![/]')
                    id_attributes = leiaint('Digite o ID do Atributo que deseja rolar: ')
                dados.append(db.mostra_attributes(escolha_personagem)[0][id_attributes - 1])

            if escolha_dados == 3:
                tabela_advantages(escolha_personagem)
                id_advantages = leiaint('Digite o ID da vantagem que deseja rolar: ')
                ids_validos = [row[0] for row in db.mostra_advantages(escolha_personagem)]
                while id_advantages not in ids_validos:
                    print('[red]ID INVÁLIDA DIGITE UM ID QUE ESTEJA EM:[/]')
                    tabela_advantages(escolha_personagem)
                    id_advantages = leiaint('Digite o ID da vantagem que deseja rolar: ')
                for advantage in db.mostra_advantages(escolha_personagem):
                    if advantage[0] == id_advantages:
                        dados.append(advantage[2])

        if escolha == 2:
            if dados:
                print(f'Dados selecionados: {dados}')
                escolha_remover = leiaint('Digite o índice do dado que deseja remover (começando do 0): ')
                if 0 <= escolha_remover < len(dados):
                    dados.pop(escolha_remover)
                    print('[green]Dado removido com sucesso![/]')
                else:
                    print('[red]Índice inválido![/]')
            else:
                print('[red]Nenhum dado selecionado![/]')

        if escolha == 3:
            if dados:
                print(f'[cyan]Dados para rolar: {dados}[/]')
            else:
                print('[yellow]Nenhum dado foi selecionado[/]')
            break
        