<h1>Projeto Mercearia - Python Full</h1>

<p>Este projeto faz parte do curso Python Full e foi desenvolvido para treinar e compreender melhor o padrão MVC (Model, View, Controller).</p>

<p>O padrão MVC é uma arquitetura de software muito utilizada. É um padrão completo, organizado e fácil de se trabalhar em equipe. Uma das vantagens de trabalhar com ele é a facilidade de dividir responsabilidades, onde cada pessoa pode ser responsável por uma parte específica do projeto. Isso facilita a organização e a localização de possíveis problemas que possam surgir. Por exemplo, um problema na Controller não prejudica o que já foi desenvolvido na Model e na View, pois cada parte é uma unidade independente de código que interage com as outras.</p>

<h3>Model:</h3>
<p>Armazenamento e estrutura dos dados, modelagem dos dados.</p>

<h3>Dal:</h3>
<p>Faz o acesso ao banco de dados ou arquivo. Define como que vai ser salvo no banco de dados ou no arquivo texto, como que vai ser feita a leitura dos dados.</p>

<h3>Controller:</h3>
<p>Responsável pela lógica do problema, pelas verificações. Por exemplo, validação de CPF: o usuário insere o CPF na View e esse CPF é enviado para a Controller, que vai verificar esse CPF. Se estiver tudo certo, ele passa para a Model; se houver algum erro, ele devolve para a View indicando que há um erro.</p>

<h3>View:</h3>
<p>Responsável pela interface gráfica, ou seja, o que o usuário vai ver. Aceitei o desafio proposto no curso Python Full e criei uma interface gráfica utilizando CustomTkinter (CTk). Além disso, estruturei o código em pastas para melhor organização.</p>

<h1>Como Iniciar o Projeto</h1>

<h3>Criar o Ambiente Virtual</h3>
<p>Crie um ambiente virtual para isolar as dependências do projeto.</p>
<p><em>python -m venv venv</em></p>

<h3>Ativar o Ambiente Virtual</h3>
<p>No Windows:</p>
<p><em>.\venv\Scripts\activate</em></p>
<p>No Linux ou macOS:</p>
<p><em>source venv/bin/activate</em></p>

<h3>Instalar as Dependências</h3>
<p>Certifique-se de que você tenha o Python instalado em sua máquina. Em seguida, instale as dependências do projeto que estão listadas no arquivo <em>requirements.txt</em>.</p>
<p><em>pip install -r requirements.txt</em></p>

<h3>Executar o Programa</h3>
<p>Após ativar o ambiente virtual e instalar as dependências, execute o programa utilizando o comando:</p>
<p><em>python app.py</em></p>

<p>Com esses passos, você terá o projeto rodando e poderá explorar a implementação do padrão MVC com a interface gráfica criada.</p>