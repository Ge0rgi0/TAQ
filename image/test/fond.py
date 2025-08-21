import pygame
import numpy as np
import math
import random

# Constantes globales
TOTAL_FRAMES = 60 * 61
SCREEN_HEIGHT = 700
SCREEN_WIDTH = SCREEN_HEIGHT // 2

MAX_SPEED = 3.99
N = random.randint(1, int(MAX_SPEED * 100)) / 100
INITIAL_VELOCITY = np.array([N, MAX_SPEED - N], dtype=float)

# Traînée
TRAINEE_COLOR = [(i, i, i) for i in range(240, 0, -12)]
TRAINEE_MULT = [0.97 ** i for i in range(len(TRAINEE_COLOR))]

class Ball:
    def __init__(self, radius, color, c_radius, c_color):
        self.radius = radius
        self.color = color
        self.c_radius = c_radius
        self.c_color = c_color
        self.pos = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], dtype=float)
        self.velocity = INITIAL_VELOCITY.copy()
        self.trainee_coords = [self.pos.tolist()] * len(TRAINEE_COLOR)

    def draw(self, screen):
        pygame.draw.circle(screen, self.c_color, self.pos.astype(int), int(self.c_radius))
        pygame.draw.circle(screen, self.color, self.pos.astype(int), int(self.radius))

    def update(self):
        self.trainee_coords.pop(-1)
        self.trainee_coords = [self.pos.tolist()] + self.trainee_coords
        self.velocity[1] += 0.2
        self.pos += self.velocity

    def apply_change(self, change):
        self.pos += change

class Circle:
    def __init__(self, radius, thickness, color, start_angle,speed):
        self.radius = radius
        self.thickness = thickness
        self.color = color
        self.center = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])
        self.hole_angle = start_angle
        self.hole_width = 40  # Taille du trou en degrés
        self.visible = True
        self.countdown = 50
        self.speed = random.randint(100, 200) / 100
        print(self.speed)
        if self.speed > 1.95:
            self.color = (210, 39, 48)
        elif self.speed > 1.7:
            self.color = (210, 220, 34)
        else:
            self.color = (100, 150, 255)

    def update_hole(self):
        self.hole_angle = (self.hole_angle - self.speed) % 360

    def draw(self, screen):
        start_deg = (self.hole_angle + self.hole_width) % 360
        end_deg = self.hole_angle
        start_rad = math.radians(start_deg)
        end_rad = math.radians(end_deg)
        rect = [
            self.center[0] - self.radius,
            self.center[1] - self.radius,
            2 * self.radius,
            2 * self.radius
        ]

        if self.visible:
            pygame.draw.arc(screen, self.color, rect, start_rad, end_rad, self.thickness)
        elif self.countdown > 0:
            self.countdown -= 1
            self.color = tuple(max(c - 10, 0) for c in self.color)
            pygame.draw.arc(screen, self.color, rect, start_rad, end_rad, self.thickness)

    def check_collision(self, ball):
        direction = ball.pos - self.center
        distance = np.linalg.norm(direction)
        total_radius = self.radius
        if self.visible and distance + ball.radius >= total_radius + 5:
            self.visible = False
            # Augmenter la vitesse de la balle de 10% quand un cercle est détruit
            speed = np.linalg.norm(ball.velocity)
            if speed > 0:
                ball.velocity = ball.velocity / speed * (speed * 1.025)
        elif self.visible and distance + ball.radius >= total_radius - 7:
            vec = direction
            angle = math.degrees(math.atan2(-vec[1], vec[0])) % 360
            hole_start = self.hole_angle
            hole_end = (self.hole_angle + self.hole_width) % 360

            # Ajustement pour ne pas trop rebondir si partiellement dans le trou
            tolerance = (ball.c_radius * 0.5) // 2
            in_hole = False
            if hole_start < hole_end:
                in_hole = hole_start + tolerance <= angle <= hole_end - tolerance
            else:
                in_hole = angle >= hole_start or angle <= hole_end

            if not in_hole and distance != 0:
                normal = direction / distance
                ball.velocity -= 2 * np.dot(ball.velocity, normal) * normal
                
                if ball.pos[1] > SCREEN_HEIGHT * 1.05// 2:
                    return np.array([0.0, -3.0])
                if ball.pos[1] <= SCREEN_HEIGHT * 0.95 // 2:
                    return np.array([0.0, 3.0])
                if ball.pos[0] > SCREEN_WIDTH * 1.05 // 2:
                    return np.array([-3.0, 0.0])
                if ball.pos[0] <= SCREEN_WIDTH * 0.95 // 2:
                    return np.array([3.0, 0.0])
        return np.array([0.0, 0.0])

class Circles:
    def __init__(self, circles):
        self.circles = circles
        self.normal_radius = [circles[i].radius for i in range(len(circles))]

    def __iter__(self):
        return iter(self.circles)

    def draw(self, screen):
        if not self.circles[0].visible and self.circles[0].countdown != 1:
            self.circles.pop(0)
            self.circles.append(    Circle(
                radius=int(SCREEN_WIDTH * 2.4) // 2,
                thickness=4,
                color=(255, 255, 255),
                start_angle=random.randint(0, 360),
                speed=random.randint(100,200)/100
            ))
        for i in range(len(self.circles)):
            circle = self.circles[i]
            if circle.radius > self.normal_radius[i]:
                circle.radius -= 1
            circle.draw(screen)

    def update_holes(self):
        for circle in self.circles:
            circle.update_hole()

    def active_circle(self):
        if self.circles and not self.circles[0].visible and self.circles[0].countdown <= 0:
            self.circles.pop(0)
        if self.circles:
            return self.circles[0]
        return None


# Initialisation
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
frame_count = 0

# Attente avant le mouvement des balles
wait_frames = int(0.5 * 60)  # 0.5 seconde à 60 FPS

# Création des objets
ball_radius = SCREEN_WIDTH * 0.03
# Balle noire, un peu à gauche du centre
ball = Ball(
    radius=ball_radius,
    color=(0,0,0),
    c_radius=ball_radius * 1.2,
    c_color=(255, 255, 255)
)
ball.pos = np.array([SCREEN_WIDTH // 2 - SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2], dtype=float)
ball.trainee_coords = [ball.pos.tolist()] * len(TRAINEE_COLOR)  # Corrige la traînée

# Balle blanche, un peu à droite du centre
ball2 = Ball(
    radius=ball_radius,
    color=(255,255,255),
    c_radius=ball_radius * 1.2,
    c_color=(0, 0, 0)
)
ball2.pos = np.array([SCREEN_WIDTH // 2 + SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2], dtype=float)
ball2.velocity = INITIAL_VELOCITY.copy()
ball2.trainee_coords = [ball2.pos.tolist()] * len(TRAINEE_COLOR)  # Corrige la traînée

CIRCLE_THICKNESS = 3
CIRCLES = Circles([
    Circle(
        radius=int(SCREEN_WIDTH * 0.4) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 0.6) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 0.8) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 1.2) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 1.4) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 1.6) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 1.8) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 2) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 2.2) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    ),
    Circle(
        radius=int(SCREEN_WIDTH * 2.4) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=random.randint(0, 360),
        speed=random.randint(100,200)/100
    )
])

# Boucle principale
background_red_timer = 0  # Timer pour fond rouge
background_red_duration = 30  # Durée totale du fondu rouge->noir (en frames)

while running and frame_count < TOTAL_FRAMES:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Gestion du fond ---
    # 1. Fond rouge -> noir avec fondu si un cercle vient d'être brisé
    if background_red_timer > 0:
        t = background_red_timer / background_red_duration
        r = int(80 * t)  # Rouge moins vif
        g = 0
        b = 0
        screen.fill((r, g, b))
        background_red_timer -= 1
    else:
        # 2. Fond noir dynamique selon le rapetissement des cercles
        min_dark = 0
        max_dark = 80  # Plus ce nombre est élevé, plus le fond peut devenir sombre
        shrink_amount = 0
        shrink_count = 0
        for i, circle in enumerate(CIRCLES.circles):
            if circle.radius < CIRCLES.normal_radius[i]:
                shrink_amount += (CIRCLES.normal_radius[i] - circle.radius)
                shrink_count += 1
        if shrink_count > 0:
            base = 255         # couleur de départ (blanc)
            min_value = 25     # valeur minimale (gris foncé)
            range_shade = base - min_value  # écart total possible (230)
            
            # Calcule un coefficient entre 0 et 1 selon la progression
            progress_ratio = min(shrink_amount / (shrink_count * 20), 1)
            
            # Interpolation de la couleur vers min_value
            shade = int(base - progress_ratio * range_shade)
            screen.fill((shade+25, shade+25, shade+25))
        else:
            screen.fill((25, 25, 25))


    # Mise à jour et affichage
    CIRCLES.update_holes()
    CIRCLES.draw(screen)
    # Traînée pour les deux balles
    for i in range(len(ball.trainee_coords)-1,0,-1):
         pygame.draw.circle(screen, TRAINEE_COLOR[i], ball.trainee_coords[i], ball.radius * TRAINEE_MULT[i])
    for i in range(len(ball2.trainee_coords)-1,0,-1):
         pygame.draw.circle(screen, TRAINEE_COLOR[i], ball2.trainee_coords[i], ball2.radius * TRAINEE_MULT[i])
    ball.draw(screen)
    ball2.draw(screen)

    if frame_count >= wait_frames:
        # Collision et physique pour les deux balles avec les cercles
        for circle in CIRCLES:
            if circle.visible or circle.countdown > 0:
                prev_visible = circle.visible
                change = circle.check_collision(ball)
                if prev_visible and not circle.visible:
                    background_red_timer = background_red_duration  # Démarre le fondu rouge->noir
                if not np.allclose(change, [0.0, 0.0]):
                    ball.apply_change(change)
                    break
        for circle in CIRCLES:
            if circle.visible or circle.countdown > 0:
                prev_visible = circle.visible
                change = circle.check_collision(ball2)
                if prev_visible and not circle.visible:
                    background_red_timer = background_red_duration  # Démarre le fondu rouge->noir
                if not np.allclose(change, [0.0, 0.0]):
                    ball2.apply_change(change)
                    break

        # Collision entre les deux balles (élastique, échange de direction sans perte de vitesse)
        direction = ball2.pos - ball.pos
        distance = np.linalg.norm(direction)
        if distance < ball.radius + ball2.radius:
            normal = direction / distance if distance != 0 else np.array([1.0, 0.0])
            tangent = np.array([-normal[1], normal[0]])
            v1n = np.dot(ball.velocity, normal)
            v1t = np.dot(ball.velocity, tangent)
            v2n = np.dot(ball2.velocity, normal)
            v2t = np.dot(ball2.velocity, tangent)
            # Échange des composantes normales, tangentes inchangées
            ball.velocity = v2n * normal + v1t * tangent
            ball2.velocity = v1n * normal + v2t * tangent
            # Séparer les balles pour éviter le chevauchement
            overlap = (ball.radius + ball2.radius - distance) / 2
            ball.pos -= normal * overlap
            ball2.pos += normal * overlap

        ball.update()
        ball2.update()
    # Sinon, ne pas mettre à jour la physique ni les positions

    pygame.display.flip()
    clock.tick(60)
    frame_count += 1

pygame.quit()
