# Gerenciador de Tópicos e Entradas

Uma aplicação Django para gerenciar tópicos e entradas associadas. Usuários podem adicionar, editar e remover tópicos e suas entradas.

## Funcionalidades

- **Página Inicial:** Exibe uma página inicial simples.
- **Visualização de Tópicos:** Lista todos os tópicos do usuário.
- **Detalhes do Tópico:** Exibe as entradas associadas a um tópico específico.
- **Criação de Tópicos:** Permite ao usuário adicionar novos tópicos.
- **Criação de Entradas:** Permite ao usuário adicionar novas entradas a um tópico.
- **Edição de Entradas:** Permite ao usuário editar entradas existentes.
- **Remoção de Tópicos e Entradas:** Permite ao usuário remover tópicos e entradas.
- **Registro de Usuário:** Permite que novos usuários se registrem na aplicação.
- **Login e Logout:** Permite que os usuários façam login e logout da aplicação.

## Modelos de Dados

### Topic

- **`text`** (CharField): O título ou nome do tópico (máx. 200 caracteres).
- **`date_added`** (DateTimeField): Data e hora em que o tópico foi criado.
- **`owner`** (ForeignKey): Referência ao usuário que criou o tópico.

Método especial:
- **`__str__()`**: Retorna o texto do tópico.

### Entry

- **`topic`** (ForeignKey): Referência ao tópico ao qual a entrada pertence.
- **`text`** (TextField): O conteúdo da entrada.
- **`date_added`** (DateTimeField): Data e hora em que a entrada foi criada.

Configuração de metadados:
- **`verbose_name_plural`**: Define o nome plural para o modelo como 'entries'.

Método especial:
- **`__str__()`**: Retorna os primeiros 50 caracteres do texto da entrada, seguido por '...'.

## Autenticação de Usuário

### Registro

- **Endpoint:** `/register/`
- **Método:** GET e POST
- **Descrição:** Permite que novos usuários se registrem. O formulário de registro padrão do Django é usado para criar um novo usuário e realizar o login automaticamente após o registro bem-sucedido.

### Login

- **Endpoint:** `/login/` (Você pode precisar implementar essa view se não estiver configurada)
- **Método:** GET e POST
- **Descrição:** Permite que os usuários façam login na aplicação.

### Logout

- **Endpoint:** `/logout/`
- **Método:** POST
- **Descrição:** Permite que os usuários façam logout e retorna à página inicial após a saída.

## Requisitos

- Python 3.x
- Django 3.x ou superior