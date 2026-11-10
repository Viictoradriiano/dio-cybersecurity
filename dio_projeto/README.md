# Simulação Educacional de Ransomware e Keylogger em Python

Projeto educacional para estudar comportamentos associados a ransomware e keyloggers, compreender seus riscos e documentar medidas de prevenção e defesa.

A parte prática validada neste projeto consiste na criação de arquivos fictícios, na criptografia de cópias com Fernet e na recuperação dessas cópias em uma pasta separada, preservando os arquivos originais.

Os exemplos de captura de teclado e envio por e-mail estão incluídos como material de estudo, mas não foram validados nos testes documentados neste repositório.

> Aviso ético: este projeto destina-se exclusivamente ao aprendizado em ambientes autorizados e controlados. Não utilize os exemplos para monitorar pessoas, coletar dados de terceiros ou interferir em arquivos e sistemas sem autorização.

## Objetivos

- Estudar o funcionamento de uma simulação de ransomware.
- Demonstrar criptografia e descriptografia de arquivos fictícios com Python.
- Preservar os arquivos originais durante o experimento.
- Estudar os riscos associados à captura de teclado e ao envio de registros.
- Documentar medidas de prevenção, detecção e resposta.
- Registrar os resultados em um portfólio técnico no GitHub.

## Escopo e status dos experimentos

| Componente | Situação |
|---|---|
| Criação de arquivos fictícios | Executada |
| Criptografia de cópias com Fernet | Executada |
| Recuperação de cópias legíveis | Executada |
| Preservação dos arquivos originais | Informada pelo programa durante a execução |
| Comparação independente dos arquivos recuperados no computador utilizado | Não documentada |
| Exemplo de captura de teclado | Código incluído, sem execução documentada |
| Exemplo de envio de registros por e-mail | Código incluído, sem execução documentada |
| Furtividade, persistência e execução oculta | Não implementadas nesta versão |
| Reflexão sobre prevenção e defesa | Documentada |

A existência de um script no repositório não significa que ele tenha sido executado ou validado. Os resultados apresentados referem-se somente aos experimentos registrados.

## Estrutura do projeto

Os scripts ficam diretamente na pasta principal:

```text
dio_projeto/
├── README.md
├── requirements.txt
├── .gitignore
├── criar_arquivos_teste.py
├── criptografar.py
├── descriptografar.py
├── keylogger_local.py
├── enviar_email_simulado.py
├── medidas_de_defesa.md
├── mensagem_resgate.txt
├── LEIA_PRIMEIRO.txt
└── images/
    └── teste_criptografia_recuperacao.png
```

A pasta `images/` deve conter as capturas de tela realizadas durante os testes.

Após executar os scripts corrigidos, a seguinte estrutura é criada localmente:

```text
laboratorio_seguro/
├── originais/
│   ├── relatorio.txt
│   ├── anotacoes.txt
│   └── lista_de_compras.txt
├── criptografados/
│   ├── relatorio.txt.enc
│   ├── anotacoes.txt.enc
│   └── lista_de_compras.txt.enc
├── recuperados/
│   ├── relatorio.txt
│   ├── anotacoes.txt
│   └── lista_de_compras.txt
├── chave.key
└── mensagem_resgate.txt
```

A pasta `laboratorio_seguro/` contém os resultados locais e não deve ser publicada nesta configuração do projeto.

O arquivo `mensagem_resgate.txt` da pasta principal é um exemplo estático. A versão corrigida gera a mensagem utilizada no teste dentro de `laboratorio_seguro/`.

## Tecnologias

- Python 3.
- `cryptography`, com Fernet, para criptografia e descriptografia.
- `pathlib`, para manipulação dos caminhos dos arquivos.
- `pynput`, presente no exemplo de captura de teclado.
- `smtplib` e `email.message`, presentes no exemplo de envio por e-mail.
- Git e GitHub, para versionamento e publicação.

As bibliotecas `pathlib`, `smtplib` e `email.message` fazem parte da biblioteca padrão do Python.

## Preparação do ambiente

Execute os comandos na pasta que contém o arquivo `requirements.txt`.

Digite um comando por vez e aguarde sua conclusão.

### Windows — Prompt de Comando

Crie o ambiente virtual:

```bat
python -m venv venv
```

Ative o ambiente:

```bat
venv\Scripts\activate
```

Instale as dependências:

```bat
python -m pip install -r requirements.txt
```

Se um ambiente virtual já estiver ativado, não é necessário criá-lo novamente.

### Linux ou macOS

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Os testes registrados neste projeto foram realizados no Windows. A execução em outros sistemas não foi documentada.

## Executando a simulação de criptografia

Utilize as versões corrigidas dos três scripts.

Não coloque arquivos pessoais ou dados reais no laboratório.

### 1. Criar os arquivos fictícios

Na pasta principal do projeto, execute:

```bash
python criar_arquivos_teste.py
```

O script cria três arquivos dentro de `laboratorio_seguro/originais/`:

- `relatorio.txt`
- `anotacoes.txt`
- `lista_de_compras.txt`

Se um desses arquivos já existir, ele será preservado.

### 2. Gerar cópias criptografadas

Execute:

```bash
python criptografar.py
```

O script:

1. Localiza os arquivos fictícios pelos nomes definidos no código.
2. Gera uma chave Fernet na primeira execução, caso não exista uma chave.
3. Reutiliza a chave existente nas execuções seguintes.
4. Salva cópias criptografadas em `laboratorio_seguro/criptografados/`.
5. Preserva os arquivos originais.
6. Não sobrescreve arquivos de saída existentes.
7. Cria uma mensagem fictícia de resgate dentro do laboratório.

Se houver arquivos na pasta de criptografados e a chave estiver ausente, o programa interrompe a criação de uma nova chave.

A mensagem de resgate identifica explicitamente a simulação e não exige pagamento.

### 3. Recuperar cópias legíveis

Execute:

```bash
python descriptografar.py
```

O script utiliza a chave local para descriptografar as cópias e grava os resultados em:

```text
laboratorio_seguro/recuperados/
```

Os arquivos originais e as cópias criptografadas são mantidos.

Se um arquivo de saída já existir na pasta de recuperados, ele não será sobrescrito.

### Cuidados com a chave

A chave fica em:

```text
laboratorio_seguro/chave.key
```

- Não publique a chave no GitHub.
- Não substitua a chave enquanto precisar recuperar arquivos associados a ela.
- Uma chave nova não recupera arquivos criptografados com outra chave.
- Não utilize dados reais neste experimento.

Esta versão utiliza uma pasta diferente daquela usada pelos scripts originais. Ela não recupera automaticamente arquivos produzidos pela versão antiga do projeto.

## Como funciona a simulação

O experimento utiliza Fernet para transformar o conteúdo dos arquivos fictícios em dados criptografados e depois recuperar o conteúdo com a chave correspondente.

O fluxo é:

```text
Arquivo fictício original
          |
          v
Criptografia com a chave local
          |
          v
Cópia criptografada (.enc)
          |
          v
Descriptografia com a mesma chave
          |
          v
Cópia recuperada em outra pasta
```

A implementação demonstra o mecanismo de criptografia de arquivos, mas não reproduz todos os comportamentos de um ransomware real.

Nesta adaptação:

- Os originais permanecem disponíveis.
- Não ocorre propagação.
- Não há busca recursiva por arquivos no computador.
- Não há acesso a compartilhamentos de rede.
- Não existe cobrança de resgate.
- Não são utilizados mecanismos de persistência.
- A operação fica limitada aos três nomes de arquivos definidos no código.

Preservar os originais é uma decisão de segurança do laboratório, não um comportamento que se deve esperar de um ransomware real.

## Experimento realizado

Foram executados, nesta ordem:

```bash
python criar_arquivos_teste.py
python criptografar.py
python descriptografar.py
```

### Resultados observados

O terminal apresentou:

- Criação dos três arquivos fictícios.
- Geração das três cópias criptografadas.
- Mensagem de preservação dos originais.
- Recuperação das três cópias legíveis.
- Mensagem de preservação dos originais e dos arquivos criptografados.

Não foram exibidos erros nessa sequência.

A saída do terminal confirma o fluxo executado pelo programa. Uma comparação independente, byte a byte, entre os arquivos originais e recuperados no computador utilizado ainda não foi registrada como evidência.

### Evidência da execução

A captura abaixo deve ser salva na pasta `images/` com o nome indicado:

![Execução da criação, criptografia e recuperação dos arquivos](images/teste_criptografia_recuperacao.png)

## Estudo de keylogger

O arquivo `keylogger_local.py` contém um exemplo de registro de teclas com `pynput`.

O exemplo foi incluído para estudar:

- Como entradas de teclado podem ser registradas.
- Como registros locais podem expor informações.
- Por que programas com acesso ao teclado exigem atenção e consentimento.
- Quais medidas de defesa podem reduzir os riscos.

### Status e limitações

A execução desse script não faz parte das evidências apresentadas neste projeto.

O exemplo não deve ser considerado restrito à janela do terminal: a captura de teclado pode alcançar entradas feitas em outros aplicativos durante sua execução.

Não foram implementados mecanismos de ocultação, persistência, inicialização automática ou evasão.

O projeto não autoriza a captura de senhas, mensagens, dados bancários ou informações de terceiros.

## Estudo de envio por e-mail

O arquivo `enviar_email_simulado.py` contém um exemplo de envio de arquivo por e-mail utilizando `smtplib` e `email.message`.

O objetivo de estudo é compreender como um arquivo local poderia ser transmitido por uma conexão de e-mail e por que conexões de saída precisam ser monitoradas.

### Status e limitações

- O envio por e-mail não foi validado nos testes documentados.
- O script é separado do exemplo de captura.
- Não foi implementada uma rotina de envio periódico ou em segundo plano.
- Nenhuma credencial real deve ser publicada.
- O envio de registros pode expor dados sensíveis, mesmo quando realizado a partir de um ambiente de teste.

Os campos de configuração devem permanecer com valores fictícios no repositório público.

## Medidas de prevenção e defesa

A discussão complementar está em [medidas_de_defesa.md](medidas_de_defesa.md).

### Antivírus e EDR

Podem ajudar a identificar arquivos maliciosos e comportamentos suspeitos, como alterações em massa de arquivos ou atividades incompatíveis com a função de um aplicativo.

Não oferecem garantia absoluta de detecção.

### Firewall e controle de saída

Ajudam a controlar conexões de rede e podem limitar transmissões não autorizadas.

Um firewall não impede, por si só, que um processo com acesso aos arquivos locais os criptografe.

### Isolamento e sandboxing

Experimentos devem ocorrer em ambientes descartáveis e isolados, preferencialmente sem dados pessoais ou pastas compartilhadas com o computador principal.

Apenas criar uma pasta de teste não equivale a uma sandbox de segurança.

### Backups

Cópias offline, imutáveis ou protegidas contra alteração ajudam na recuperação após incidentes.

Os procedimentos de restauração devem ser testados. Cópias permanentemente acessíveis ao mesmo usuário comprometido também podem ser afetadas.

### Atualizações

Manter o sistema e os aplicativos atualizados reduz a exposição a vulnerabilidades conhecidas.

### Autenticação multifator

A MFA pode reduzir o risco de acesso indevido quando uma senha é comprometida.

Ela não impede a captura de teclado e não substitui a proteção do dispositivo.

### Conscientização

É importante verificar a origem de programas, anexos e links, além de desconfiar de solicitações inesperadas de credenciais.

### Menor privilégio

Usuários e programas devem ter apenas as permissões necessárias.

Isso limita o alcance de um processo comprometido, embora arquivos acessíveis ao usuário ainda possam estar em risco.

## Cuidados antes de publicar

Não envie para o repositório:

- Chaves de criptografia.
- Senhas, tokens ou credenciais.
- Registros de teclado.
- Dados pessoais.
- A pasta do ambiente virtual.
- Resultados locais que contenham informações sensíveis.
- ZIPs antigos com versões desatualizadas dos scripts.

Utilize o seguinte conteúdo no arquivo `.gitignore`:

```gitignore
venv/
.venv/
__pycache__/
*.pyc
*.key
.env
laboratorio_seguro/
teclas_capturadas.txt
*.zip
```

O `.gitignore` não remove arquivos que já tenham sido adicionados ao versionamento. Confira o conteúdo do repositório antes de publicá-lo.

## Aprendizados

- A gestão da chave é essencial para permitir a recuperação dos dados.
- Gerar uma nova chave sem preservar a anterior pode impedir a recuperação de arquivos.
- Separar originais, cópias criptografadas e recuperados facilita a análise.
- Testes repetidos não devem sobrescrever resultados ou destruir dados.
- Uma documentação técnica deve distinguir código incluído de código efetivamente testado.
- Captura de teclado e transmissão de registros apresentam riscos de privacidade.
- Segurança depende de prevenção, monitoramento, controle de acesso e capacidade de recuperação.

## Conclusão

O experimento documentado demonstrou a criação, a criptografia e a recuperação de cópias de três arquivos fictícios com Python.

A implementação foi adaptada para preservar os originais e evitar sobrescrita da chave e dos resultados existentes.

Os exemplos de keylogger e envio por e-mail permanecem identificados como materiais de estudo sem execução documentada. O foco do projeto é compreender os mecanismos envolvidos, reconhecer seus riscos e refletir sobre medidas de defesa.