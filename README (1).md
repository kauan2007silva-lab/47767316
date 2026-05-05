# 🐍 Projeto: Estruturas de Dados Lineares com Python

Três exercícios práticos desenvolvidos para a cadeira de **Programação de Computadores** — 1º Semestre de 2026.  
Docente: Marco Antonio Sanches | Universidade Cruzeiro do Sul

---

## 📂 Estrutura de Arquivos

```
projeto_estruturas_lineares/
├── desafio_01_votacao.py
├── desafio_02_editor_pilha.py
├── desafio_03_fila_atendimento.py
└── README.md
```

---

## 🗳️ Exercício 1 — Apuração de Votos para Representante de Turma

### O que o programa faz
Coleta os votos destinados a três candidatos — **Ana**, **Bruno** e **Carlos** — e, ao término da votação, apresenta o total de cada um e anuncia o vencedor. Em caso de empate, o programa identifica e informa.

### Recursos do Python utilizados
- **Lista** (`votos = []`) para guardar cada voto inserido
- **`count()`** para totalizar os votos por candidato
- **Laço `while`** para manter o programa rodando até o usuário digitar `"fim"`
- **Estruturas condicionais (`if/elif/else`)** para checar votos inválidos e detectar empates

### Executando o programa
```bash
python desafio_01_votacao.py
```

### Demonstração
```
Digite o nome do candidato (fim para encerrar): ana
  ✔ Voto registrado para Ana!
Digite o nome do candidato (fim para encerrar): bruno
  ✔ Voto registrado para Bruno!
Digite o nome do candidato (fim para encerrar): ana
  ✔ Voto registrado para Ana!
Digite o nome do candidato (fim para encerrar): fim

========================================
        RESULTADO DA VOTAÇÃO
========================================
Ana:    2 voto(s)
Bruno:  1 voto(s)
Carlos: 0 voto(s)
----------------------------------------
O vencedor é: Ana 🎉
```

---

## ✏️ Exercício 2 — Editor de Texto com Função de Desfazer (Pilha)

### O que o programa faz
Simula um editor básico em que o usuário insere palavras individualmente. A funcionalidade de **desfazer** retira a palavra mais recente, aplicando o comportamento de uma **Pilha (Stack)**.

### Recursos do Python utilizados
- **Lista usada como Pilha** (`pilha = []`) — lógica LIFO (último a entrar, primeiro a sair)
- **`append()`** para inserir a palavra no topo da pilha
- **`pop()`** para retirar o elemento mais recente
- **`" ".join(pilha)`** para reconstruir e exibir o texto completo
- Verificação de **pilha vazia** antes de executar o `pop()`, evitando erros

### Executando o programa
```bash
python desafio_02_editor_pilha.py
```

### Demonstração
```
[1] - Digitar palavra
[2] - Desfazer última palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 1
Digite uma palavra: minha
  ✔ Palavra adicionada: minha

Escolha uma opção: 1
Digite uma palavra: terra
  ✔ Palavra adicionada: terra

Escolha uma opção: 3
  Texto atual: minha terra

Escolha uma opção: 2
  ↩ Palavra removida: terra

Escolha uma opção: 3
  Texto atual: minha
```

---

## 🎓 Exercício 3 — Painel de Senhas da Secretaria Universitária (Fila)

### O que o programa faz
Gerencia a ordem de atendimento na secretaria acadêmica. Cada estudante recebe uma senha ao chegar e é chamado conforme a **sequência de chegada**, seguindo a lógica de uma **Fila (Queue)**.

### Recursos do Python utilizados
- **Lista usada como Fila** (`fila = []`) — lógica FIFO (primeiro a entrar, primeiro a sair)
- **`append()`** para incluir o aluno no **fim** da fila
- **`pop(0)`** para retirar o aluno do **início** (próximo a ser atendido)
- **`enumerate()`** para numerar e exibir a posição de cada pessoa na fila
- Verificação de **fila vazia** antes do `pop(0)` para prevenir falhas

### Executando o programa
```bash
python desafio_03_fila_atendimento.py
```

### Demonstração
```
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 1
Nome do aluno: Marco
  ✔ Marco entrou na fila de atendimento.
     Senha: 001

Escolha uma opção: 3
  Fila atual:
    1º - Marco  (Senha: 001)

Escolha uma opção: 2
  📢 Chamando aluno: Marco
     Senha: 001
     (A fila está agora vazia)

Escolha uma opção: 3
  A fila está vazia.
```

---

## 📖 Resumo dos Conceitos Abordados

| Conceito | Estrutura | Inserção | Remoção |
|----------|-----------|----------|---------|
| Lista simples | `list` | `append()` | `remove()` / índice |
| Pilha (Stack) — LIFO | `list` | `append()` | `pop()` |
| Fila (Queue) — FIFO | `list` | `append()` | `pop(0)` |
