# Desenvolvimento-de-Interface-Web-CRUD-com-FastAPI

# Loja de Roupas Feminina

Este projeto é uma aplicação web simples desenvolvida em **FastAPI** com suporte a templates HTML renderizados usando **Jinja2**. Ele simula a interface de um sistema de gestão de loja de roupas feminina com funcionalidades de login, listagem, adição, edição e exclusão de produtos. Não utiliza banco de dados real, apenas dados simulados em memória.

---

## **Funcionalidades Implementadas**

1. **Login**:
   - Página de login inicial obrigatória.
   - Validação de email e senha para acessar a aplicação.

2. **Página Inicial**:
   - Lista todos os produtos disponíveis.
   - Botões para editar ou excluir produtos.

3. **Formulário de Cadastro/Edição**:
   - Formulário unificado para adicionar novos produtos ou editar existentes.

4. **Rotas no Backend**:
   - Renderização de templates HTML com dados dinâmicos fornecidos pelo backend.
   - Manipulação de formulários para criar, atualizar e excluir registros simulados.

5. **Design Responsivo e Moderno**:
   - Utilização de CSS básico com foco em uma interface limpa e profissional.
   - Opção de adicionar frameworks CSS como **Bootstrap** para melhorias adicionais.

---

## **Estrutura do Projeto**

### **1. Diretórios**

- **`templates/`**: Contém os templates HTML.
  - `base.html`: Template base com cabeçalho e rodapé.
  - `login.html`: Tela de login.
  - `index.html`: Página inicial para listar produtos.
  - `form.html`: Formulário para adicionar ou editar produtos.

- **`static/`**: Contém arquivos CSS e outros recursos estáticos.
  - `styles.css`: Arquivo de estilos para toda a aplicação.

- **`main.py`**: Arquivo principal da aplicação em FastAPI.

### **2. Templates HTML**

#### **`base.html`**
Define a estrutura comum (layout) para as páginas, como cabeçalho, rodapé e bloco de conteúdo dinâmico.

#### **`login.html`**
Página inicial do sistema, solicitando email e senha para acessar o restante das funcionalidades.

#### **`index.html`**
Exibe a lista de produtos cadastrados com opções para editar ou excluir cada item.

#### **`form.html`**
Formulário que permite criar novos produtos ou editar produtos existentes.

---

## **CSS**
O design é limpo, moderno e responsivo, com:

- Paleta de cores suaves.
- Bordas arredondadas e sombras sutis.
- Campos de formulário centralizados e estilizados.
- Layout baseado em caixas ("cards") para a exibição de produtos.

---

## **Configuração do Projeto**

### **1. Pré-requisitos**
- **Python 3.9+**
- **FastAPI**
- **Uvicorn**

Instale as dependências com:
```bash
pip install fastapi uvicorn jinja2
```

### **2. Estrutura de Diretórios**
Certifique-se de que o projeto está estruturado como abaixo:
```
project/
├── main.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── index.html
│   ├── form.html
├── static/
│   └── styles.css
```

### **3. Executando a Aplicação**
Para rodar o servidor:
```bash
uvicorn main:app --reload
```
Acesse o sistema no navegador em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **Fluxo do Sistema**

### **1. Tela de Login**
- Acesse a aplicação com um email e senha (simulados no backend).
- Se os dados forem válidos, você será redirecionado para a página inicial.

### **2. Página Inicial**
- Lista os produtos cadastrados.
- Cada produto possui botões para editar ou excluir.

### **3. Formulário de Produto**
- Adicione um novo produto preenchendo os campos obrigatórios.
- Edite um produto existente acessando o formulário com os dados pré-carregados.

### **4. Lógica de Dados**
- Os produtos são armazenados em uma lista Python no backend, simulando um banco de dados.

