# 🔎 Script Caça-Palavras

Automação em Python para o jogo **Caça-Palavras**, utilizando **Selenium WebDriver** para acessar o jogo, identificar as palavras disponíveis e selecionar automaticamente as respectivas letras no tabuleiro.

O projeto foi desenvolvido como um estudo prático de **Python, Selenium e automação de páginas web**.

> **Aviso:** Este é um projeto independente, desenvolvido para fins de estudo e aprendizado. Não possui afiliação oficial com o G1 ou com a Globo.

---

## 🎯 Objetivo

O objetivo do projeto é automatizar a resolução do Caça-Palavras por meio da identificação das palavras e das células correspondentes no tabuleiro.

O programa realiza as seguintes etapas:

1. Abre o navegador;
2. Acessa o jogo;
3. Inicia a partida;
4. Fecha a tela de ajuda inicial;
5. Captura as palavras apresentadas no jogo;
6. Captura as células do tabuleiro;
7. Agrupa as células utilizando seus identificadores;
8. Seleciona automaticamente as células de cada palavra;
9. Exibe informações sobre as palavras e grupos encontrados;
10. Aguarda a confirmação do usuário;
11. Fecha o navegador.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Selenium WebDriver**
* **Google Chrome**
* **ActionChains**
* **CSS Selectors**
* **WebDriverWait**
* **Expected Conditions**
* **Git / GitHub**

---

## 📂 Estrutura do projeto

```text
Script_Caca_Palavras/
│
├── config.py
├── inicio.py
├── main.py
├── navegador.py
├── palavras.py
└── README.md
```

> O diretório `__pycache__` também pode ser gerado pelo Python durante a execução. Recomenda-se adicioná-lo ao `.gitignore`, pois são arquivos temporários gerados automaticamente.

---

## 🧩 Funcionamento dos arquivos

### `main.py`

É o ponto de entrada da aplicação e coordena todo o fluxo de automação.

O programa importa as funções dos demais módulos e executa as etapas principais:

```text
                    ┌─────────────────┐
                    │     main.py     │
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     navegador.py    │
                  │   Abre o navegador  │
                  └──────────┬──────────┘
                             │
                             ▼
                     ┌───────────────┐
                     │   inicio.py   │
                     │ Inicia o jogo │
                     └───────┬───────┘
                             │
                             ▼
                    ┌────────────────┐
                    │   palavras.py  │
                    │ Captura dados  │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ ActionChains   │
                    │ Seleciona      │
                    │ as palavras    │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ Finalização    │
                    └────────────────┘
```

O fluxo pode ser observado diretamente em `main.py`, que chama `iniciar_navegador()`, `iniciar_jogo()`, `capturar_palavras_dia()`, `capturar_celulas()` e `selecionar_palavras()`.

---

### `navegador.py`

Responsável pelo gerenciamento do navegador utilizado na automação.

O módulo possui as funções relacionadas à inicialização e ao encerramento do WebDriver.

Essa separação permite que o gerenciamento do navegador fique isolado da lógica específica do jogo.

---

### `inicio.py`

Responsável pelas ações necessárias para iniciar a partida.

O módulo utiliza:

* `WebDriverWait`;
* `Expected Conditions`;
* CSS Selectors;
* Selenium WebDriver.

Primeiro, o programa aguarda o botão de início do jogo e realiza o clique. Em seguida, aguarda o botão de fechamento da tela de ajuda e também realiza o clique.

---

### `palavras.py`

É o principal módulo responsável pela identificação e seleção das palavras.

Ele possui três funções principais:

#### `capturar_palavras_dia()`

Localiza os elementos que representam as palavras apresentadas pelo jogo através do seletor:

```css
span.suggestion
```

Depois, coleta o texto de cada elemento e remove espaços desnecessários.

---

#### `capturar_celulas()`

Localiza as células do tabuleiro através do seletor:

```css
.letter-box text
```

Cada célula possui um atributo `data-id`, utilizado pelo programa para identificar a qual palavra aquela célula pertence.

As células são agrupadas em um dicionário:

```text
data-id → lista de células
```

Isso permite que o programa tenha uma sequência de células correspondente a cada palavra.

---

#### `selecionar_palavras()`

Responsável por realizar a seleção das letras no tabuleiro.

Para isso, o programa utiliza:

```python
ActionChains
```

O fluxo utilizado é:

```text
Primeira célula
      ↓
click_and_hold()
      ↓
Percorre as células
      ↓
move_to_element()
      ↓
release()
      ↓
Palavra selecionada
```

O pequeno intervalo entre os movimentos permite reproduzir o movimento de seleção das letras no jogo.

---

### `config.py`

Centraliza as configurações utilizadas pelo projeto.

A principal vantagem dessa abordagem é evitar que valores de configuração fiquem espalhados pelos diferentes módulos.

---

## ⚙️ Requisitos

Para executar o projeto, é necessário possuir:

* **Python 3**
* **Google Chrome**
* **Selenium**
* Conexão com a internet

O navegador precisa estar disponível na máquina utilizada para executar a automação.

---

## 📥 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/kaioabreu62/Script_Caca_Palavras.git
```

### 2. Acesse a pasta

```bash
cd Script_Caca_Palavras
```

### 3. Instale as dependências

Caso o projeto possua um arquivo de requisitos:

```bash
pip install -r requisitos.txt
```

Caso as dependências ainda não estejam listadas em um arquivo, instale o Selenium:

```bash
pip install selenium
```

---

## ▶️ Executando o projeto

Execute o arquivo principal:

```bash
python main.py
```

O navegador será iniciado e o programa acessará a página configurada no projeto.

Após o carregamento:

```text
Abrir navegador
      ↓
Acessar jogo
      ↓
Iniciar partida
      ↓
Fechar ajuda
      ↓
Capturar palavras
      ↓
Capturar células
      ↓
Agrupar células
      ↓
Selecionar palavras
```

Ao final, o programa apresenta no terminal as palavras identificadas e os grupos de células encontrados.

O programa então aguarda o usuário pressionar **Enter** antes de fechar o navegador.

---

## 🔎 Como as palavras são identificadas

Diferentemente de uma solução que tenta descobrir as palavras analisando todas as combinações possíveis da matriz, este projeto utiliza informações fornecidas pelo próprio jogo.

Primeiro, as palavras apresentadas na interface são capturadas:

```python
span.suggestion
```

Depois, as células do tabuleiro são identificadas:

```python
.letter-box text
```

Cada célula possui um `data-id`.

O programa utiliza esse identificador para agrupá-las:

```text
Palavra A
├── Célula 1
├── Célula 2
├── Célula 3
└── Célula 4

Palavra B
├── Célula 1
├── Célula 2
├── Célula 3
└── Célula 4
```

Por fim, cada grupo é selecionado utilizando `ActionChains`.

---

## 🤖 Automação com Selenium

O projeto utiliza diferentes recursos do Selenium para interagir com a página.

### Localização de elementos

São utilizados seletores CSS para localizar os componentes do jogo.

Exemplo:

```python
driver.find_elements(
    By.CSS_SELECTOR,
    "span.suggestion"
)
```

### Espera explícita

Para evitar que o programa tente clicar em elementos antes que estejam disponíveis, o projeto utiliza:

```python
WebDriverWait
```

em conjunto com:

```python
EC.element_to_be_clickable()
```

Essa abordagem é utilizada durante a inicialização do jogo.

### ActionChains

Para selecionar uma palavra, o programa simula uma ação de pressionar, movimentar e soltar o mouse:

```python
action.click_and_hold(primeira_celula)

for letra in celulas:
    action.move_to_element(letra)

action.release().perform()
```

Essa é a parte responsável pela interação com o tabuleiro.

---

## 📋 Exemplo de saída

Durante a execução, o programa apresenta informações no terminal semelhantes a:

```text
[INFO] Grupo '...' contém X células
[INFO] Palavra selecionada: (X letras)
[INFO] Palavras do dia: ...
[INFO] Células para serem agrupadas: ...
```

Essas mensagens ajudam a acompanhar o comportamento da automação durante a execução.

---

## 🧠 Conceitos utilizados

O projeto permite praticar diversos conceitos importantes de desenvolvimento em Python:

* Organização de código em módulos;
* Importação entre módulos;
* Funções;
* Dicionários;
* Listas;
* Estruturas de repetição;
* Tratamento de exceções;
* Manipulação de elementos HTML;
* Seletores CSS;
* Selenium WebDriver;
* `WebDriverWait`;
* `Expected Conditions`;
* `ActionChains`;
* Automação de interações com o mouse;
* Captura e processamento de informações de uma página web.

---

## 🚧 Possíveis melhorias

Algumas melhorias podem ser implementadas futuramente:

* [ ] Criar um `requirements.txt`;
* [ ] Adicionar `.gitignore`;
* [ ] Remover `__pycache__` do repositório;
* [ ] Substituir `time.sleep()` por esperas explícitas quando possível;
* [ ] Melhorar o tratamento de exceções;
* [ ] Criar logs estruturados;
* [ ] Adicionar testes automatizados;
* [ ] Melhorar a identificação de mudanças na estrutura HTML;
* [ ] Criar uma classe para encapsular o WebDriver;
* [ ] Separar a captura das palavras da lógica de seleção;
* [ ] Criar uma configuração centralizada para os seletores CSS;
* [ ] Adicionar screenshots em caso de erro;
* [ ] Permitir execução sem intervenção manual no final do programa.

---

## ⚠️ Observações

O projeto depende da estrutura HTML do jogo.

Como os elementos são localizados utilizando seletores CSS específicos, alterações futuras na página podem fazer com que determinados seletores deixem de funcionar.

Por exemplo, o código atualmente utiliza classes específicas do botão de início e do botão de fechamento da ajuda.

Da mesma forma, a captura das palavras e células depende dos seletores:

```css
span.suggestion
```

e

```css
.letter-box text
```

respectivamente.

---

## 🎓 Finalidade do projeto

Este projeto foi desenvolvido como uma aplicação prática de conceitos de **Python e automação web**.

Através dele, são aplicados conhecimentos de:

**Python + Selenium + WebDriver + CSS Selectors + ActionChains + Automação de navegador.**

O projeto também demonstra a utilização de uma arquitetura modular, separando responsabilidades entre inicialização do jogo, gerenciamento do navegador, captura das informações e seleção das palavras.

---

## 👨‍💻 Autor

**Kaio Abreu**

GitHub: [kaioabreu62](https://github.com/kaioabreu62)

---

## 📄 Licença

Este projeto não possui uma licença de software definida no momento.

Caso o projeto seja disponibilizado para reutilização por terceiros, recomenda-se adicionar uma licença de código aberto de acordo com a intenção do autor.
