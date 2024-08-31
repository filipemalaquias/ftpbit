# Brute Force FTP

Este script em Python realiza ataques de força bruta em servidores FTP. 
Ele pode tentar diferentes senhas para um usuário específico, diferentes usuários com uma senha específica ou combinações de usuários e senhas.

## Criador

- **Nome: Filipe Malaquias Londrino**  
- **E-mail: malaquias@devdesucesso.net** 
- **Contacto: 933146546**
- **GitHub:** [https://github.com/seunome](https://github.com/seunome)

## Requisitos

- Python 3 ou superiores

## Instalação

Siga as etapas abaixo para instalar e executar o script:

### 1. Instalar o Python

Certifique-se de que o Python 3 ou superiores, esteja instalado em seu sistema. Você pode baixar o Python a partir do site oficial:

- [Download Python](https://www.python.org/downloads/)

Siga as instruções fornecidas para o seu sistema operacional para concluir a instalação.

### 2. Baixar o Script

1. **Clonar o Repositório**:

Baixar o Arquivo:

Acesse o repositório no GitHub.
Baixe o arquivo ZIP do repositório.
Extraia o conteúdo do arquivo ZIP para uma pasta de sua escolha.


3. Navegar até a Pasta do Script
Abra um terminal (ou prompt de comando) e navegue até a pasta onde o script foi baixado ou extraído. Por exemplo:

bash
Copiar código
cd caminho/para/a/pasta/bruteforce-ftp


4. Executar o Script
Use o seguinte comando para executar o script, substituindo <servidor>, <usuario>, <senha>, <lista_usuarios>, e <lista_senhas> pelos valores apropriados:

Testar diferentes senhas para um usuário específico:

bash
Copiar código
python bruteforce.py <servidor> -U <usuario> -PL <lista_senhas>
Testar diferentes usuários com uma senha específica:

bash
Copiar código
python bruteforce.py <servidor> -P <senha> -UL <lista_usuarios>
Testar todas as combinações de usuários e senhas:


Opções
use **--help** para ler o manual de ajuda.
--help : Mostra este manual de ajuda.
