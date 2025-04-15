import pygame
import sys
 
# Initialisation
pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Interface ADI")
 
# Couleurs
GRIS = (200, 200, 200)
NOIR = (0, 0, 0)
BLEU = (0, 102, 204)
JAUNE = (255, 255, 0)
VERT = (100, 255, 100)
BLANC = (255, 255, 255)
 
# Police
font = pygame.font.SysFont("arial", 16)
font_big = pygame.font.SysFont("arial", 26, bold=True)
 
# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    screen.fill(GRIS)
 
    # --- Zone principale gauche ---
    # Smiley
    pygame.draw.circle(screen, JAUNE, (70, 60), 25)
    pygame.draw.circle(screen, NOIR, (60, 50), 5)  # œil gauche
    pygame.draw.circle(screen, NOIR, (80, 50), 5)  # œil droit
    pygame.draw.arc(screen, NOIR, (55, 55, 30, 20), 3.14, 0, 2)  # bouche
 
    # Grille 3x3
    top_left = (40, 100)
    cell_size = 20
    for i in range(4):
        # lignes horizontales
        pygame.draw.line(screen, BLEU, (top_left[0], top_left[1] + i*cell_size),
                         (top_left[0] + 3*cell_size, top_left[1] + i*cell_size), 2)
        # lignes verticales
        pygame.draw.line(screen, BLEU, (top_left[0] + i*cell_size, top_left[1]),
                         (top_left[0] + i*cell_size, top_left[1] + 3*cell_size), 2)
 
    # Texte en bas à gauche
    texte = font.render("Solveur 3x3", True, NOIR)
    screen.blit(texte, (40, 180))
 
    # --- Barre noire de séparation ---
    pygame.draw.rect(screen, NOIR, (220, 0, 10, 300))
 
    # --- Zone droite (onglets noirs) ---
    pygame.draw.rect(screen, NOIR, (250, 20, 100, 30))  # Onglet 1
    pygame.draw.rect(screen, NOIR, (250, 55, 100, 30))  # Onglet 2
    pygame.draw.rect(screen, NOIR, (250, 90, 100, 30))  # Onglet 3
 
    # Texte des onglets
    texte1 = font_big.render("ADI", True, VERT)
    screen.blit(texte1, (270, 25))
 
    texte2 = font.render("Algorithme", True, VERT)
    screen.blit(texte2, (260, 65))
 
    # Rafraîchir l'écran
    pygame.display.flip()
