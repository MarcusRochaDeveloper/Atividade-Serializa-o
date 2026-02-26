# Simulador de Carro com Serialização JSON

Este é um script simples em Python que simula as ações básicas de um carro (acelerar e frear) e demonstra como serializar e desserializar objetos Python usando o formato JSON.

## O que o código faz?

O script `car.py` contém:
- Uma classe `Carro` com atributos de `posicao_x`, `posicao_y` e `velocidade`.
- Métodos para interagir com o carro: `acelerar()` e `freiar()`.
- Métodos para converter o estado do carro em um dicionário (`to_dict()`) e em uma string JSON (`to_json()`).
- Métodos para salvar state atual do carro em um arquivo `carro.json` e carregá-lo novamente do arquivo (`salvar()` e `carregar()`).
- Uma interface de terminal interativa (`menu()`) que permite ao usuário criar um carro, controlar sua velocidade e, ao finalizar, salva e demonstra o carregamento dos dados do JSON.

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária (utiliza apenas o módulo `json` padrão do Python).

## Como rodar o projeto

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta onde o arquivo `car.py` está localizado.
3. Execute o script com o comando:
   ```bash
   python car.py
   ```

## Como usar

Ao rodar o script, você verá um menu interativo no terminal:

1. **Cadastro inicial:** O programa solicitará a posição inicial (X e Y) e a velocidade inicial do carro.
2. **Menu de ações:** Você poderá escolher entre:
   - `1 - Acelerar`: Digite o valor que deseja aumentar a velocidade.
   - `2 - Frear`: Digite o valor que deseja diminuir da velocidade.
   - `3 - Finalizar`: Encerra as ações do carro.
3. **Resultado:** Ao finalizar, o script irá:
   - Exibir os dados do carro no formato JSON.
   - Salvar essas informações em um arquivo chamado `carro.json` no mesmo diretório.
   - Ler os dados desse arquivo para criar um novo objeto `Carro` (desserialização) e imprimir os valores recuperados para confirmar que o processo funcionou.
