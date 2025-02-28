Organização do Código
=====================

Para criar componentes reutilizáveis no React que funcionem tanto para cadastrar um produto novo quanto para editá-lo, você precisa adotar algumas estratégias que tornem o componente flexível e adaptável às diferentes situações.

1. Abstração e Propriedades (Props):

Componente Único: Crie um único componente para o formulário de produto, em vez de dois componentes separados (um para cadastro e outro para edição).
Props Dinâmicas: Utilize props para passar informações e comportamentos específicos para o componente, como:
- produtoInicial: Um objeto contendo os dados do produto (para edição) ou um objeto vazio (para cadastro).
- onSubmit: Uma função que será chamada quando o formulário for enviado, recebendo os dados do produto.
- modoEdicao: Um valor booleano que indica se o formulário está no modo de edição ou cadastro.
- textoBotao: O texto do botão de envio do formulário (por exemplo, "Cadastrar" ou "Salvar").

2. Gerenciamento de Estado:

Estado Local: Use o useState para gerenciar o estado dos campos do formulário.
Inicialização: Inicialize o estado com os dados do produtoInicial recebido por props. 
Isso garante que o formulário seja preenchido com os dados do produto na edição.

3. Lógica Condicional:

Modo de Edição: Utilize a prop modoEdicao para ajustar o comportamento do componente, como:
Exibir um título diferente ("Cadastrar Produto" ou "Editar Produto").
Realizar diferentes chamadas de API (POST para cadastro, PUT ou PATCH para edição).
Dados do Produto: Verifique se produtoInicial possui dados para pré-preencher os campos do formulário na edição.