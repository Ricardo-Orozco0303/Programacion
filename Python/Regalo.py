import pygame
import sys
import random
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fuegos Artificiales Automáticos")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Clase para representar partículas (chispas)
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel = pygame.Vector2(0, 0)
        self.gravity = 0.2
        self.alpha = 255

    def update(self):
        # Actualizar la posición de la partícula con la gravedad simulada
        self.vel.y += self.gravity
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        # Decrementar la opacidad (alpha) para eventualmente eliminar la partícula
        self.alpha -= 5
        if self.alpha < 0:
            self.kill()

# Función para crear un conjunto de partículas (explosión)
def create_explosion(x, y, color):
    num_particles = 100
    for _ in range(num_particles):
        # Crear partícula con posición y color
        particle = Particle(x, y, color)
        # Configurar una dirección y velocidad aleatoria para la partícula
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 5)
        particle.vel.from_polar((speed, math.degrees(angle)))
        # Agregar la partícula al grupo
        particles.add(particle)

# Grupo de sprites para las partículas
particles = pygame.sprite.Group()

# Reloj para controlar la velocidad de la simulación
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Crear automáticamente explosiones de fuegos artificiales
    if random.randint(1, 100) == 1:
        firework_x = random.randint(50, WIDTH - 50)
        firework_y = random.randint(0, HEIGHT // 2)
        firework_color = (random.randint(150, 255), random.randint(0, 150), random.randint(0, 150))
        create_explosion(firework_x, firework_y, firework_color)

    # Actualizar y dibujar las partículas
    particles.update()
    screen.fill(BLACK)
    particles.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de la simulación
    clock.tick(60)

# Salir del programa
pygame.quit()
sys.exit()




