import sistema.interface as sistema
import vampiradb.banco as db
from rich import print

db.iniciardb()
while True:

    sistema.titulo('VAMPIRA MASCARA PYTHON(ALPHA)')
    sistema.opcoes(['Cadastrar personagem', 'Lista de personagens',
                    'Deletar personagem', 'Alterar personagem', 'Sair do programa'])

    continuar = sistema.sistema_escolha('Escolha sua opção: ')

    if continuar is False:
        print('[magenta]Até logo![/]')
        break