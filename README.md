# Problema 1 - MI de Concorrência e Conectividade

## Resumo
O setor de aviação de baixo custo (LCCs) democratizou o transporte aéreo, tornando-o mais acessível. Este projeto acadêmico simula o desenvolvimento de um sistema cliente-servidor para a venda de passagens aéreas via Internet, utilizando sockets TCP/IP. O sistema foi implementado em Python, operando via terminal e lidando com requisições concorrentes. Testado em contêineres Docker, o backend oferece escalabilidade. A simulação demonstra a consulta e compra de trechos de voo, assegurando a integridade das transações em múltiplas instâncias.


## Introdução
A aviação de baixo custo (Low-Cost Carriers - LCCs) transformou o transporte aéreo ao oferecer voos mais acessíveis, permitindo que mais pessoas possam viajar. Este projeto acadêmico simula o desenvolvimento de um sistema de venda de passagens aéreas para a VendePass, uma companhia fictícia de baixo custo. O objetivo é automatizar o processo de consulta e compra de trechos de voos pela Internet, utilizando a comunicação cliente-servidor via sockets TCP/IP.

O sistema foi implementado em Python e faz uso de contêineres Docker tanto no backend quanto no frontend. A comunicação entre os contêineres é estabelecida através da rede Bridge do Docker, permitindo a criação de múltiplas instâncias de clientes e servidores que compartilham uma rede isolada para testes. Isso facilita o teste de concorrência e o gerenciamento das requisições em tempo real, garantindo a integridade das transações.

A seção de Metodologia detalhará as escolhas tecnológicas e arquiteturais, bem como a configuração da rede e o ambiente de testes utilizado para validar o sistema.
