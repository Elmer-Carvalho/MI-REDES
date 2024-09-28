# Problema 1 - MI de Concorrência e Conectividade

## Resumo
O setor de aviação de baixo custo (LCCs) democratizou o transporte aéreo, tornando-o mais acessível. Este projeto acadêmico simula o desenvolvimento de um sistema cliente-servidor para a venda de passagens aéreas via Internet, utilizando sockets TCP/IP. O sistema foi implementado em Python, operando via terminal e lidando com requisições concorrentes. Testado em contêineres Docker, o backend oferece escalabilidade. A simulação demonstra a consulta e compra de trechos de voo, assegurando a integridade das transações em múltiplas instâncias.


## Introdução
A aviação de baixo custo (Low-Cost Carriers - LCCs) transformou o transporte aéreo ao oferecer voos mais acessíveis, permitindo que mais pessoas possam viajar. Este projeto acadêmico simula o desenvolvimento de um sistema de venda de passagens aéreas para a VendePass, uma companhia fictícia de baixo custo. O objetivo é automatizar o processo de consulta e compra de trechos de voos pela Internet, utilizando a comunicação cliente-servidor via sockets TCP/IP.

O sistema foi implementado em Python e faz uso de contêineres Docker tanto no backend quanto no frontend. A comunicação entre os contêineres é estabelecida através da rede Bridge do Docker, permitindo a criação de múltiplas instâncias de clientes e servidores que compartilham uma rede isolada para testes. Isso facilita o teste de concorrência e o gerenciamento das requisições em tempo real, garantindo a integridade das transações.

A seção de Metodologia detalhará as escolhas tecnológicas e arquiteturais, bem como a configuração da rede e o ambiente de testes utilizado para validar o sistema.


## Fundamentação Teórica e Metodologia
O sistema desenvolvido para a VendePass utiliza uma arquitetura cliente-servidor, fundamental para aplicações que exigem comunicação entre usuários e servidores. Essa abordagem permite a interação eficiente entre Frontend e Backend através do protocolo TCP/IP, que assegura a entrega confiável de pacotes de dados.

**Conceitos Fundamentais:** A arquitetura cliente-servidor é central para a comunicação de dados em tempo real, possibilitando que múltiplos clientes façam requisições simultaneamente. Os conceitos de concorrência e controle de acesso são essenciais para garantir a integridade das transações em ambientes de múltiplos usuários.

**Tecnologias Específicas:**

- Python: Utilizada para o desenvolvimento do sistema, proporcionando facilidade de implementação e manutenção.
- TCP/IP: Protocolo utilizado para a comunicação entre o cliente e o servidor.
- JSON: Formato de troca de mensagens que facilita a serialização e deserialização dos dados.
- Threads: Utilizadas para gerenciar a concorrência, permitindo que cada conexão com um cliente seja atendida simultaneamente.
- Docker: Utilizado para containerizar o sistema, facilitando a execução e testes em múltiplas instâncias, além de assegurar que o ambiente de desenvolvimento e produção seja consistente.
- Algoritmo de Dijkstra: Implementado para encontrar os trechos de voo disponíveis, considerando a disponibilidade de assentos.

**Metodologia de Implementação:** O sistema foi estruturado para garantir uma comunicação clara e eficiente. As mensagens entre cliente e servidor são organizadas em dicionários Python, convertidos em JSON para transmissão. No servidor, um controller filtra as requisições e acessa a lógica de negócio, enquanto um controller no cliente gerencia os estados e exibe as interfaces adequadas.

Para lidar com a concorrência, a implementação de Threads permite que o sistema atenda múltiplas conexões simultaneamente, com um controle rigoroso que limita o acesso a métodos críticos a uma única thread por vez. A busca por trechos disponíveis utiliza o algoritmo de Dijkstra, que é adaptado para considerar a disponibilidade de assentos. Se algum trecho estiver sem vagas, o sistema encontra automaticamente um trecho alternativo.

Essas escolhas tecnológicas e metodológicas visam garantir que o sistema seja capaz de atender a demanda de clientes em tempo real, enquanto mantém a integridade das transações e a fluidez da comunicação entre cliente e servidor.

## Execução
### 1.1 Clone o repositório 
```bash
    git clone https://github.com/Elmer-Carvalho/MI-REDES.git
