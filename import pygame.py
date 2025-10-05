import pygame
import random
import sys

# Inicializar o pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# Configurações da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🐍 Jogo da Cobrinha")

# Relógio para controlar FPS
clock = pygame.time.Clock()
fps = 10

# Tamanho dos blocos
tamanho_bloco = 20

# Fonte para pontuação
fonte = pygame.font.SysFont("Arial", 25)

def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontuação: {pontos}", True, BRANCO)
    tela.blit(texto, [10, 10])

def jogo():
    # Posição inicial da cobrinha
    x = largura // 2
    y = altura // 2
    x_vel = 0
    y_vel = 0

    # Corpo da cobrinha
    corpo = []
    comprimento = 1

    # Comida aleatória
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_vel == 0:
                    x_vel = -tamanho_bloco
                    y_vel = 0
                elif evento.key == pygame.K_RIGHT and x_vel == 0:
                    x_vel = tamanho_bloco
                    y_vel = 0
                elif evento.key == pygame.K_UP and y_vel == 0:
                    y_vel = -tamanho_bloco
                    x_vel = 0
                elif evento.key == pygame.K_DOWN and y_vel == 0:
                    y_vel = tamanho_bloco
                    x_vel = 0

        x += x_vel
        y += y_vel

        # Fim de jogo se bater nas bordas
        if x < 0 or x >= largura or y < 0 or y >= altura:
            rodando = False

        # Atualiza posição
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeça = [x, y]
        corpo.append(cabeça)
        if len(corpo) > comprimento:
            del corpo[0]

        # Fim de jogo se bater em si mesmo
        for parte in corpo[:-1]:
            if parte == cabeça:
                rodando = False

        for parte in corpo:
            pygame.draw.rect(tela, VERDE, [parte[0], parte[1], tamanho_bloco, tamanho_bloco])

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comprimento += 1

        mostrar_pontuacao(comprimento - 1)
        pygame.display.update()
        clock.tick(fps)

    # Tela de fim de jogo
    tela.fill(PRETO)
    texto = fonte.render("Game Over! Pressione qualquer tecla para sair.", True, VERMELHO)
    tela.blit(texto, [largura // 2 - 200, altura // 2])
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Iniciar o jogo
jogo()
