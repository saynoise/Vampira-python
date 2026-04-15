# 🧛 Sistema Vampira: A Máscara — Gerenciador de Personagens

Aplicação em Python para gerenciar fichas de personagens do RPG **Vampiro: A Máscara**. Atualmente funciona como um CRUD completo, com banco de dados SQLite3 para armazenar personagens e seus atributos.

---

## 📋 Funcionalidades atuais

- Cadastrar personagens com informações básicas (nome, player, clã, crônica, etc.)
- Armazenar atributos físicos, sociais e mentais de cada personagem
- Armazenar habilidades (abilities) de cada personagem
- Atualizar e deletar personagens
- Banco de dados local com integridade referencial via chaves estrangeiras

---

## 🗄️ Estrutura do banco de dados

```
personagens
    ├── atributos      (Physical, Social, Mental)
    └── abilities      (Talents, Skills, Knowledges)
```

Todas as tabelas se relacionam com `personagens` via chave estrangeira com `ON DELETE CASCADE` — ao deletar um personagem, todos os dados relacionados são removidos automaticamente.

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.8+

```bash
# Clone o repositório
git clone https://github.com/saynoise/Vampira-python.git
cd Vampira-python

# Execute a aplicação
python main.py
```

Não é necessário instalar dependências externas — o projeto usa apenas bibliotecas padrão do Python (`sqlite3`).

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal
- **SQLite3** — banco de dados local

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
