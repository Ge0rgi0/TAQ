import pygame
import numpy as np
import math
import random
import os
import shutil

# === CONSTANTES MODIFIABLES ===

NAME = "Emma"

# Nombre maximal de cercles à briser
NB_CIRCLES = 1  # <-- Ajout : définis ici le nombre de cercles

# Dimensions écran
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 540

# Physique balles
MAX_SPEED = 7.99
BALL_RADIUS_RATIO = 0.03  # proportion de la largeur
BALL_COLOR_YES = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Couleur aléatoire pour la balle "Yes"
BALL_COLOR_NO = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Couleur aléatoire pour la balle "No"
BALL_CONTOUR_COLOR = (255, 255, 255)
BALL_MAX_VELOCITY = 10.0  # Limite de vitesse des balles (pixels/frame)

# Traînée
TRAIL_LENGTH = 10  # Un peu plus longue
TRAIL_MULT_BASE = 0.97

# Cercles
CIRCLE_THICKNESS = 2
CIRCLE_SPEED = 4.0
CIRCLE_HOLE_WIDTH = 60
CIRCLE_HOLE_OFFSET = 5
CIRCLE_HOLE_START_ANGLE = random.randint(0,359)
CIRCLE_RADIUS_FACTORS = list(range(30, 240, 3))
CIRCLE_SHRINK_SPEED = 5  # <-- Ajout : vitesse de rapetissement des cercles (pixels/frame)

# Difficulté/probabilités/couleurs
DIFFICULTY_PROBS = {
    "easy": 0.33,    # 1 point
    "medium": 0.34,  # 2 points
    "hard": 0.33     # 5 points
}
DIFFICULTY_COLORS = {
    "easy": (255,255,255),
    "medium": (255,255,255),
    "hard": (255,255,255)
}
"""easy": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),  # Couleur aléatoire pour "easy"
"medium": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),  # Couleur aléatoire pour "medium"
"hard": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))   # Couleur aléatoire pour "hard"
"""
# Animation/fond
BACKGROUND_RED_DURATION = 30

# Score
TOTAL_FRAMES = 60 * 61

# Textes (modifiables facilement)
TEXT_TITLE = " Tag your friend ! Who's hotter ?"
TEXT_SUBTITLE = "Bro's mom or Dragon on Shrek ?"  # (texte en noir)
TEXT_YES = "YES"
TEXT_NO = "NO"
TEXT_BOTTOM = ["follow and comment", "to be picked for the next video"]

# Constantes global
SCREEN_HEIGHT = 1920//2  # Modifié
SCREEN_WIDTH = 1080//2   # Modifié

MAX_SPEED = 1.99
N = random.randint(1, int(MAX_SPEED * 100)) / 100
INITIAL_VELOCITY = np.array([N, MAX_SPEED - N], dtype=float)

# Traînée : du gris clair vers le noir du fond (25,25,25)
def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

TRAIL_BG_COLOR = (25, 25, 25)
TRAIL_COLOR_START = (220, 220, 220)
TRAINEE_COLOR = [
    lerp_color(TRAIL_COLOR_START, TRAIL_BG_COLOR, i/(TRAIL_LENGTH-1))
    for i in range(TRAIL_LENGTH)
]
TRAINEE_MULT = [TRAIL_MULT_BASE ** i for i in range(TRAIL_LENGTH)]

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
        # Limitation de la vitesse
        speed = np.linalg.norm(self.velocity)
        if speed > BALL_MAX_VELOCITY:
            self.velocity = self.velocity / speed * BALL_MAX_VELOCITY
        self.pos += self.velocity

    def apply_change(self, change):
        self.pos += change

class Circle:
    def __init__(self, radius, thickness, color, start_angle, speed):
        self.radius = radius
        self.thickness = thickness
        # Détermination de la difficulté et de la couleur associée
        r = random.random()
        if r < DIFFICULTY_PROBS["easy"]:
            self.difficulty = "easy"
            self.color = DIFFICULTY_COLORS["easy"]
        elif r < DIFFICULTY_PROBS["easy"] + DIFFICULTY_PROBS["medium"]:
            self.difficulty = "medium"
            self.color = DIFFICULTY_COLORS["medium"]
        else:
            self.difficulty = "hard"
            self.color = DIFFICULTY_COLORS["hard"]
        self.center = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])
        # Angle du trou
        self.hole_angle = start_angle % 360
        self.hole_width = CIRCLE_HOLE_WIDTH
        self.visible = True
        self.countdown = 50
        self.speed = CIRCLE_SPEED
        # Optionnel : couleur alternative pour effet visuel
        n = random.randint(100, 200) / 100
        if n > 1.90:
            self.color = DIFFICULTY_COLORS["hard"]
        elif n > 1.7:
            self.color = DIFFICULTY_COLORS["medium"]
        else:
            self.color = DIFFICULTY_COLORS["easy"]

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
        elif self.visible and distance + ball.radius >= total_radius - 10:
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

                # Ajoute un cercle à chaque rebond (si limite non atteinte)
                
                CIRCLES.add_circle()
                ball._last_bounce_frame = frame_count

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
        self.normal_radius = [c.radius for c in circles]
        self.created = len(circles)

    def __iter__(self):
        return iter(self.circles)

    def add_circle(self):
        # Ajoute un cercle autour du plus grand cercle existant (extérieur), si on n'a pas dépassé NB_CIRCLES
        if self.created < NB_CIRCLES:
            # Cherche le plus grand rayon déjà présent
            if self.circles:
                max_idx = max(range(len(self.circles)), key=lambda i: self.circles[i].radius)
                prev_circle = self.circles[max_idx]
                factor = CIRCLE_RADIUS_FACTORS[min(self.created, len(CIRCLE_RADIUS_FACTORS)-1)]
                radius = int(SCREEN_WIDTH * factor/100) // 2
                new_angle = (prev_circle.hole_angle + CIRCLE_HOLE_OFFSET) % 360
            else:
                radius = int(SCREEN_WIDTH * CIRCLE_RADIUS_FACTORS[0]/100) // 2
                new_angle = 0
            new_circle = Circle(
                radius=radius,
                thickness=CIRCLE_THICKNESS,
                color=(255, 255, 255),
                start_angle=new_angle,
                speed=2.0
            )
            self.circles.append(new_circle)
            self.normal_radius.append(radius)
            self.created += 1

    def draw(self, screen):
        # Ne crée un nouveau cercle que si on n'a pas dépassé NB_CIRCLES
        if self.circles and not self.circles[0].visible and self.circles[0].countdown != 1:
            if self.created < NB_CIRCLES:
                prev_angle = self.circles[-1].hole_angle if self.circles else 0
                new_angle = (prev_angle + CIRCLE_HOLE_OFFSET) % 360
                self.circles.pop(0)
                self.circles.append(Circle(
                    radius=int(SCREEN_WIDTH * 2.4) // 2,
                    thickness=CIRCLE_THICKNESS,
                    color=(255, 255, 255),
                    start_angle=new_angle,
                    speed=2.0
                ))
                self.normal_radius.append(self.circles[-1].radius)
                self.created += 1
            else:
                # Si on a atteint NB_CIRCLES, on retire juste le cercle sans en ajouter
                self.circles.pop(0)
                self.normal_radius.pop(0)
        for i in range(len(self.circles)):
            circle = self.circles[i]
            if circle.radius > self.normal_radius[i]:
                circle.radius = max(self.normal_radius[i], circle.radius - CIRCLE_SHRINK_SPEED)
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
ball_radius = SCREEN_WIDTH * BALL_RADIUS_RATIO
# Balle unique
ball = Ball(
    radius=ball_radius,
    color=BALL_COLOR_YES,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR
)
ball.pos = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], dtype=float)
ball.trainee_coords = [ball.pos.tolist()] * len(TRAINEE_COLOR)

remaining_circles = NB_CIRCLES

CIRCLES = Circles([
    Circle(
        radius=int(SCREEN_WIDTH * factor/100) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=(i * CIRCLE_HOLE_OFFSET) % 360,
        speed=2.0
    )
    for i, factor in enumerate(CIRCLE_RADIUS_FACTORS[:NB_CIRCLES])
])

# Scores pour chaque balle
score_yes = 0

# Création du dossier d'images si besoin et vidage du dossier
image_dir = r"C:\Users\derbl\OneDrive\Documents\Bureau\test\image"
if os.path.exists(image_dir):
    for f in os.listdir(image_dir):
        fp = os.path.join(image_dir, f)
        if os.path.isfile(fp):
            os.remove(fp)
else:
    os.makedirs(image_dir, exist_ok=True)

# Ajout : chargement de l'image pour l'affichage final
DRAGON_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "dragon.jpg")
dragon_img = pygame.image.load(DRAGON_IMAGE_PATH).convert_alpha()

# Boucle principale
background_red_timer = 0  # Timer pour fond rouge
background_red_duration = BACKGROUND_RED_DURATION  # Utilise la constante

last_bounce_frame = -100

while running and frame_count < TOTAL_FRAMES:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dernières 5*60 frames : affiche juste le texte final
    if frame_count >= TOTAL_FRAMES - 5*60:
        screen.fill((25, 25, 25))
        # Texte de la réponse finale
        font_big = pygame.font.SysFont(None, 96)
        if score_yes > score_no:
            end_text = "sorry bro"
        else:
            end_text = "GG bro"
        sorry_text = font_big.render(end_text, True, (255, 255, 255))
        sorry_rect = sorry_text.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2)
        screen.blit(sorry_text, sorry_rect)
    else:
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
        # Traînée pour la balle (couleur de plus en plus noire)
        for i in range(len(ball.trainee_coords)-1,0,-1):
            pygame.draw.circle(screen, TRAINEE_COLOR[i], ball.trainee_coords[i], ball.radius)
        ball.draw(screen)

        # Affichage du nombre de cercles restants au centre de l'écran
        font_count = pygame.font.SysFont(None, 36)  # Encore plus petit
        count_text = font_count.render(str(remaining_circles), True, (255, 255, 255))
        count_rect = count_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(count_text, count_rect)

        # Texte en haut de l'écran, en blanc sur fond rouge, plus gros et sur deux lignes
        top_font = pygame.font.SysFont(None, 54)
        top_lines = [
            "If the ball escapes,",
            "Trump will soon disappear !"
        ]
        y_start = 60  # Position de départ plus bas
        padding = 16
        for i, line in enumerate(top_lines):
            top_text = top_font.render(line, True, (255, 255, 255))
            top_rect = top_text.get_rect(centerx=SCREEN_WIDTH // 2, top=y_start + i * (top_font.get_height() + padding))
            # Dessine le fond rouge derrière chaque ligne
            bg_rect = pygame.Rect(
                top_rect.left - 24,
                top_rect.top - 8,
                top_rect.width + 48,
                top_rect.height + 16
            )
            pygame.draw.rect(screen, (220, 0, 0), bg_rect, border_radius=12)
            screen.blit(top_text, top_rect)

    if frame_count >= wait_frames:
        if CIRCLES.circles:
            for circle in CIRCLES:
                if circle.visible or circle.countdown > 0:
                    change = circle.check_collision(ball)
                    if not np.allclose(change, [0.0, 0.0]):
                        ball.apply_change(change)
                        # Ajoute un cercle à chaque rebond (si limite non atteinte)
                        if frame_count - last_bounce_frame > 2:
                            CIRCLES.add_circle()
                            last_bounce_frame = frame_count
                        break
        ball.update()

    # Sinon, ne pas mettre à jour la physique ni les positions

    pygame.display.flip()
    # Sauvegarde de l'image à chaque frame
    pygame.image.save(screen, os.path.join(image_dir, f"frame_{frame_count:05d}.png"))

    clock.tick(60)
    frame_count += 1

pygame.quit()
