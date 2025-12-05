# Snake Game

Jogo da cobrinha desenvolvido em Python com a biblioteca Pygame. O projeto combina código gerado por IA com ajustes manuais para melhorar lógica, interface e jogabilidade.

---

## Visão geral

Este repositório contém o jogo Snake implementado em Python utilizando Pygame. O propósito do documento é explicar como instalar, executar e compreender os principais pontos de implementação e as soluções adotadas para problemas comuns.

---

## Requisitos

- Python 3 instalado
- Biblioteca Pygame

---

## Instalação

1. Abra um terminal dentro da pasta do projeto.
2. Instale a dependência executando:

```bash
pip install pygame
```

---

## Executando o jogo

No terminal, dentro do diretório do projeto, execute:

```bash
python snakeGame.py
```

---

## Controles

- Setas do teclado: mover a cobra
- Espaço (após "Game Over"): reiniciar o jogo
- Esc: sair (se implementado no jogo)

> Observação: os controles podem variar conforme a implementação; confira os comentários no arquivo `snakeGame.py`.

---

## Principais desafios e soluções

### 1. Controle de direção da cobra
**Problema:** impedir que a cobra se mova imediatamente para a direção oposta (o que causaria colisão instantânea).

**Solução:** validar a nova direção antes de aplicá-la, mantendo a direção atual até que a mudança seja permitida:

```python
def mudar_direcao(self, direcao):
    # Impede direção oposta imediata
    if (direcao[0] * -1, direcao[1] * -1) != self.direcao:
        self.nova_direcao = direcao
```

### 2. Geração das maçãs
**Problema:** evitar que as maçãs apareçam em cima do corpo da cobra.

**Solução:** gerar posições aleatórias repetidamente até encontrar uma posição livre:

```python
def colocar_nova(self, cobra):
    while True:
        x = random.randint(0, (LARGURA - TAMANHO_CELULA) // TAMANHO_CELULA) * TAMANHO_CELULA
        y = random.randint(0, (ALTURA - TAMANHO_CELULA) // TAMANHO_CELULA) * TAMANHO_CELULA
        self.posicao = (x, y)
        if self.posicao not in cobra.corpo:
            break
```

---

## Funcionalidades implementadas

- Exibição de pontuação e tamanho da cobra durante o jogo
- Tela de Game Over com pontuação final
- Instruções de controle visíveis durante a partida
- Reinício do jogo com a tecla Espaço após Game Over

---

## Estrutura sugerida do projeto

Exemplo de organização de arquivos (ajuste conforme seu repositório):

```
/ (raiz do projeto)
├─ snakeGame.py        # arquivo principal do jogo
├─ assets/             # imagens, sons, fontes
├─ README.md           # documentação curta
└─ requirements.txt    # (opcional) dependências
```

---

## Testes e validação

- Teste manual das colisões e mudança de direção
- Verificar geração de maçã repetidamente para garantir que nunca apareça sobre a cobra
- Validar reinício e estado inicial após Game Over

---

## Conclusão

O projeto demonstra como o uso de ferramentas de IA pode acelerar a criação de protótipos, mantendo espaço para intervenções manuais que melhoram jogabilidade e experiência do usuário. A combinação resultou em um jogo funcional e com boa responsividade.

---

## Autores

Projeto desenvolvido em Python com Pygame utilizando a IA DeepSeek.

- Leonardo Cunha Melo Pessoa
- Felipe Leite Rodrigues
- Renan Villar Loureiro
- Vinicius Andre Passos Barreto de Lima
- Wellyngton Carlos Fernandes Costa
- Matheus do Nascimento Neto
- Guilherme Leonardo Alves

---

## Licença

Adicione aqui a licença do projeto (por exemplo, MIT) ou remova esta seção se não for aplicável.

