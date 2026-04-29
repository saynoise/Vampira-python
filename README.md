# 🧛 Sistema Vampira: A Máscara — Gerenciador de Personagens

Aplicação em Python para gerenciar fichas de personagens do RPG **Vampiro: A Máscara**. Atualmente funciona como um CRUD completo, com banco de dados SQLite3 para armazenar personagens e seus atributos.

---

## 📋 Funcionalidades atuais

- Cadastrar personagens com informações básicas (nome, player, clã, crônica, natureza, comportamento, geração)
- Armazenar e editar atributos físicos, sociais e mentais de cada personagem
- Armazenar e editar habilidades (abilities) de cada personagem
- Gerenciar vantagens (disciplines, backgrounds, virtues, etc.) — adicionar, alterar e excluir
- Atualizar e deletar personagens
- Banco de dados local com integridade referencial via chaves estrangeiras

---

## 🗄️ Estrutura do banco de dados

```
personagens
    ├── attributes     (Physical, Social, Mental)
    ├── abilities      (Talents, Skills, Knowledges)
    └── advantages     (Disciplines, Backgrounds, Virtues, etc.)
```

Todas as tabelas se relacionam com `personagens` via chave estrangeira com `ON DELETE CASCADE` — ao deletar um personagem, todos os dados relacionados são removidos automaticamente.

---

## 🗂️ Estrutura do projeto

```
Vampira-python/
    ├── main.py
    ├── sistema/
    │   └── interface.py      # Interface do terminal (menus, tabelas, inputs)
    └── vampiradb/
        └── banco.py          # Lógica de banco de dados (CRUD com SQLite3)
```

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.8+

```bash
# Clone o repositório
git clone https://github.com/saynoise/Vampira-python.git
cd Vampira-python

# Instale as dependências
pip install rich

# Execute a aplicação
python main.py
```

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal
- **SQLite3** — banco de dados local
- **Rich** — formatação e tabelas no terminal

---

## 🔮 Roadmap

Funcionalidades planejadas para versões futuras:

- [ ] Rolagem de dados integrada ao app
- [ ] Bot para Discord que recebe os resultados das rolagens e os exibe no chat
- [ ] Interface gráfica ou CLI interativa para facilitar o uso durante as sessões
- [ ] Suporte a mais sistemas do Mundo das Trevas

---

## 📖 Sobre o sistema

**Vampiro: A Máscara** é um RPG de mesa do estilo *storytelling* ambientado no Mundo das Trevas, publicado pela White Wolf. Os personagens são vampiros navegando intrigas políticas, dilemas morais e a constante luta contra a Besta interior.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.