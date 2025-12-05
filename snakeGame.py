import pygame
import random
import sys

pygame.init()

LARGURA = 800
ALTURA = 600
TAMANHO_CELULA = 20
VELOCIDADE = 10  

COR_FUNDO = (15, 15, 30)
COR_COBRA = (50, 205, 50)
COR_CABECA = (0, 255, 0)
COR_MACA = (255, 50, 50)
COR_TEXTO = (255, 255, 255)
COR_BORDA = (40, 40, 70)

CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)

class Cobra:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.corpo = [(LARGURA // 2, ALTURA // 2)]
        self.direcao = DIREITA
        self.nova_direcao = DIREITA
        self.crescer = False
        self.pontuacao = 0
        
        for _ in range(2):
            self.crescer_cobra()
    
    def mudar_direcao(self, direcao):
        if (direcao[0] * -1, direcao[1] * -1) != self.direcao:
            self.nova_direcao = direcao
    
    def mover(self):
        self.direcao = self.nova_direcao
        
        cabeca_x, cabeca_y = self.corpo[0]
        nova_cabeca_x = cabeca_x + self.direcao[0] * TAMANHO_CELULA
        nova_cabeca_y = cabeca_y + self.direcao[1] * TAMANHO_CELULA
        
        if nova_cabeca_x >= LARGURA:
            nova_cabeca_x = 0
        elif nova_cabeca_x < 0:
            nova_cabeca_x = LARGURA - TAMANHO_CELULA
            
        if nova_cabeca_y >= ALTURA:
            nova_cabeca_y = 0
        elif nova_cabeca_y < 0:
            nova_cabeca_y = ALTURA - TAMANHO_CELULA
        
        nova_cabeca = (nova_cabeca_x, nova_cabeca_y)
        self.corpo.insert(0, nova_cabeca)
        
        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False
    
    def crescer_cobra(self):
        self.crescer = True
    
    def colisao_corpo(self):
        return self.corpo[0] in self.corpo[1:]
    
    def desenhar(self, tela):
        for i, (x, y) in enumerate(self.corpo):
            cor = COR_CABECA if i == 0 else COR_COBRA
            pygame.draw.rect(tela, cor, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
            pygame.draw.rect(tela, (0, 100, 0), (x, y, TAMANHO_CELULA, TAMANHO_CELULA), 1)
            
            if i == 0:
                olho_tamanho = TAMANHO_CELULA // 5
                if self.direcao == DIREITA:
                    olho1 = (x + TAMANHO_CELULA - olho_tamanho, y + olho_tamanho * 2)
                    olho2 = (x + TAMANHO_CELULA - olho_tamanho, y + TAMANHO_CELULA - olho_tamanho * 3)
                elif self.direcao == ESQUERDA:
                    olho1 = (x + olho_tamanho, y + olho_tamanho * 2)
                    olho2 = (x + olho_tamanho, y + TAMANHO_CELULA - olho_tamanho * 3)
                elif self.direcao == CIMA:
                    olho1 = (x + olho_tamanho * 2, y + olho_tamanho)
                    olho2 = (x + TAMANHO_CELULA - olho_tamanho * 3, y + olho_tamanho)
                else:  
                    olho1 = (x + olho_tamanho * 2, y + TAMANHO_CELULA - olho_tamanho)
                    olho2 = (x + TAMANHO_CELULA - olho_tamanho * 3, y + TAMANHO_CELULA - olho_tamanho)
                
                pygame.draw.circle(tela, (0, 0, 0), olho1, olho_tamanho)
                pygame.draw.circle(tela, (0, 0, 0), olho2, olho_tamanho)

class Maca:
    def __init__(self, cobra):
        self.posicao = (0, 0)
        self.colocar_nova(cobra)
    
    def colocar_nova(self, cobra):
        while True:
            x = random.randint(0, (LARGURA - TAMANHO_CELULA) // TAMANHO_CELULA) * TAMANHO_CELULA
            y = random.randint(0, (ALTURA - TAMANHO_CELULA) // TAMANHO_CELULA) * TAMANHO_CELULA
            self.posicao = (x, y)
            
            if self.posicao not in cobra.corpo:
                break
    
    def desenhar(self, tela):
        x, y = self.posicao
        pygame.draw.rect(tela, COR_MACA, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
        
        cabinho_x = x + TAMANHO_CELULA // 2
        cabinho_y = y - TAMANHO_CELULA // 4
        pygame.draw.rect(tela, (100, 70, 30), (cabinho_x - 1, cabinho_y, 2, TAMANHO_CELULA // 4))
        
        folha_pos = (cabinho_x + TAMANHO_CELULA // 8, cabinho_y + TAMANHO_CELULA // 8)
        folha = [(folha_pos[0], folha_pos[1]), 
                 (folha_pos[0] + TAMANHO_CELULA // 4, folha_pos[1]), 
                 (folha_pos[0] + TAMANHO_CELULA // 8, folha_pos[1] - TAMANHO_CELULA // 4)]
        pygame.draw.polygon(tela, (100, 255, 100), folha)

class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)
        self.fonte_pequena = pygame.font.SysFont(None, 24)
        
        self.cobra = Cobra()
        self.maca = Maca(self.cobra)
        self.estado = "JOGANDO"  
        
    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.KEYDOWN:
                if self.estado == "JOGANDO":
                    if evento.key == pygame.K_UP:
                        self.cobra.mudar_direcao(CIMA)
                    elif evento.key == pygame.K_DOWN:
                        self.cobra.mudar_direcao(BAIXO)
                    elif evento.key == pygame.K_LEFT:
                        self.cobra.mudar_direcao(ESQUERDA)
                    elif evento.key == pygame.K_RIGHT:
                        self.cobra.mudar_direcao(DIREITA)
                elif self.estado == "GAME_OVER":
                    if evento.key == pygame.K_SPACE:
                        self.reiniciar_jogo()
        
        return True
    
    def atualizar(self):
        if self.estado == "JOGANDO":
            self.cobra.mover()
            
            if self.cobra.corpo[0] == self.maca.posicao:
                self.cobra.crescer_cobra()
                self.cobra.pontuacao += 1
                self.maca.colocar_nova(self.cobra)
            
            if self.cobra.colisao_corpo():
                self.estado = "GAME_OVER"
    
    def reiniciar_jogo(self):
        self.cobra.reset()
        self.maca.colocar_nova(self.cobra)
        self.estado = "JOGANDO"
    
    def desenhar(self):
        self.tela.fill(COR_FUNDO)
        
        for x in range(0, LARGURA, TAMANHO_CELULA):
            pygame.draw.line(self.tela, (25, 25, 40), (x, 0), (x, ALTURA), 1)
        for y in range(0, ALTURA, TAMANHO_CELULA):
            pygame.draw.line(self.tela, (25, 25, 40), (0, y), (LARGURA, y), 1)
        
        pygame.draw.rect(self.tela, COR_BORDA, (0, 0, LARGURA, ALTURA), 4)
        
        self.maca.desenhar(self.tela)
        
        self.cobra.desenhar(self.tela)
        
        texto_pontuacao = self.fonte.render(f"Maçãs: {self.cobra.pontuacao}", True, COR_TEXTO)
        self.tela.blit(texto_pontuacao, (10, 10))
        
        texto_tamanho = self.fonte_pequena.render(f"Tamanho: {len(self.cobra.corpo)}", True, COR_TEXTO)
        self.tela.blit(texto_tamanho, (10, 50))
        
        if self.estado == "JOGANDO":
            instrucoes = self.fonte_pequena.render("Use as setas para mover a cobra", True, COR_TEXTO)
            self.tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA - 30))
        elif self.estado == "GAME_OVER":
            game_over = self.fonte.render("GAME OVER", True, (255, 50, 50))
            self.tela.blit(game_over, (LARGURA // 2 - game_over.get_width() // 2, ALTURA // 2 - 50))
            
            pontuacao_final = self.fonte.render(f"Pontuação: {self.cobra.pontuacao} maçãs", True, COR_TEXTO)
            self.tela.blit(pontuacao_final, (LARGURA // 2 - pontuacao_final.get_width() // 2, ALTURA // 2))
            
            reiniciar = self.fonte_pequena.render("Pressione ESPAÇO para jogar novamente", True, COR_TEXTO)
            self.tela.blit(reiniciar, (LARGURA // 2 - reiniciar.get_width() // 2, ALTURA // 2 + 50))
        
        pygame.display.flip()
    
    def executar(self):
        executando = True
        
        while executando:
            executando = self.tratar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(VELOCIDADE)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()