import pygame
import numpy as np
import math
import random
import os
import shutil

# === CONSTANTES MODIFIABLES ===

# Dimensions écran
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 540

# Physique balles
MAX_SPEED = 3.99
BALL_RADIUS_RATIO = 0.03  # proportion de la largeur
BALL_COLOR_YES = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Couleur aléatoire pour la balle "Yes"
BALL_COLOR_NO = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Couleur aléatoire pour la balle "No"
BALL_CONTOUR_COLOR = (255, 255, 255)
BALL_MAX_VELOCITY = 5.0  # Limite de vitesse des balles (pixels/frame)

# Traînée
TRAIL_LENGTH = 10  # Un peu plus longue
TRAIL_MULT_BASE = 0.97

# Cercles
CIRCLE_THICKNESS = 3
CIRCLE_SPEED = 3.0
CIRCLE_HOLE_WIDTH = 60
CIRCLE_HOLE_OFFSET = 20
CIRCLE_HOLE_START_ANGLE = random.randint(0,359)
CIRCLE_RADIUS_FACTORS = list(range(30, 240, 10))
CIRCLE_SHRINK_SPEED = 2  # <-- Ajout : vitesse de rapetissement des cercles (pixels/frame)

# Difficulté/probabilités/couleurs
DIFFICULTY_PROBS = {
    "easy": 0.6,    # 1 point
    "medium": 0.3,  # 2 points
    "hard": 0.1     # 5 points
}
DIFFICULTY_COLORS = {
    "easy": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),  # Couleur aléatoire pour "easy"
    "medium": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),  # Couleur aléatoire pour "medium"
    "hard": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))   # Couleur aléatoire pour "hard"
}
# Animation/fond
BACKGROUND_RED_DURATION = 30

# Score
TOTAL_FRAMES = 60 * 61

# Textes (modifiables facilement)
TEXT_TITLE = " Are you autistic ?"
TEXT_SUBTITLE = "(respectfully)"  # (texte en noir)
TEXT_YES = "Yes"
TEXT_NO = "No"
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
        # Décalage du trou
        if not hasattr(Circle, "_angle_offset"):
            Circle._angle_offset = CIRCLE_HOLE_START_ANGLE  # Utilise la constante pour l'angle de départ
        self.hole_angle = Circle._angle_offset % 360
        Circle._angle_offset += CIRCLE_HOLE_OFFSET
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
            self.circles.append(Circle(
                radius=int(SCREEN_WIDTH * 2.4) // 2,
                thickness=CIRCLE_THICKNESS,
                color=(255, 255, 255),
                start_angle=0,
                speed=2.0
            ))
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
# Balle rouge (Yes), plus proche du centre
ball = Ball(
    radius=ball_radius,
    color=BALL_COLOR_YES,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR
)
ball.pos = np.array([SCREEN_WIDTH // 2 - SCREEN_WIDTH // 32, SCREEN_HEIGHT // 2], dtype=float)  # Modifié (plus proche)
ball.trainee_coords = [ball.pos.tolist()] * len(TRAINEE_COLOR)  # Corrige la traînée

# Balle verte (No), plus proche du centre
ball2 = Ball(
    radius=ball_radius,
    color=BALL_COLOR_NO,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR
)
ball2.pos = np.array([SCREEN_WIDTH // 2 + SCREEN_WIDTH // 32, SCREEN_HEIGHT // 2], dtype=float)  # Modifié (plus proche)
ball2.velocity = INITIAL_VELOCITY.copy()
ball2.trainee_coords = [ball2.pos.tolist()] * len(TRAINEE_COLOR)  # Corrige la traînée

CIRCLES = Circles([
    Circle(
        radius=int(SCREEN_WIDTH * factor/100) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=0,  # La valeur n'a plus d'importance, ignorée dans Circle
        speed=2.0  # Vitesse fixe à 2
    )
    for factor in CIRCLE_RADIUS_FACTORS
])

# Scores pour chaque balle
score_yes = 0
score_no = 0

# Création du dossier d'images si besoin et vidage du dossier
image_dir = r"C:\Users\derbl\OneDrive\Documents\Bureau\test\image"
if os.path.exists(image_dir):
    for f in os.listdir(image_dir):
        fp = os.path.join(image_dir, f)
        if os.path.isfile(fp):
            os.remove(fp)
else:
    os.makedirs(image_dir, exist_ok=True)

# Boucle principale
background_red_timer = 0  # Timer pour fond rouge
background_red_duration = BACKGROUND_RED_DURATION  # Utilise la constante

while running and frame_count < TOTAL_FRAMES:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dernières 5*60 frames : affiche juste la question et la réponse (pas d'image)
    if frame_count >= TOTAL_FRAMES - 5*60:
        screen.fill((25, 25, 25))
        # Rectangle blanc en haut avec texte noir (deux lignes)
        font = pygame.font.SysFont(None, 40)
        text1 = font.render(TEXT_TITLE, True, (0, 0, 0))
        text2 = font.render(TEXT_SUBTITLE, True, (0, 0, 0))
        text1_rect = text1.get_rect(centerx=SCREEN_WIDTH // 2, top=60)
        text2_rect = text2.get_rect(centerx=SCREEN_WIDTH // 2, top=text1_rect.bottom)
        padding = 24
        total_height = text1_rect.height + text2_rect.height + 2 * padding
        rect_bg = pygame.Rect(
            text1_rect.left - padding,
            text1_rect.top - padding,
            text1_rect.width + 2 * padding,
            total_height
        )
        pygame.draw.rect(screen, (255, 255, 255), rect_bg, border_radius=16)
        pygame.draw.rect(screen, (255, 255, 255), rect_bg, border_radius=16, width=4)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)

        # Affiche la réponse (texte de la balle gagnante) centré sous le rectangle
        font_resp = pygame.font.SysFont(None, 72)
        if score_yes > score_no:
            winner_text = TEXT_YES
        elif score_no > score_yes:
            winner_text = TEXT_NO
        else:
            winner_text = "Egalité"
        resp_text = font_resp.render(winner_text, True, (255, 255, 255))
        resp_rect = resp_text.get_rect(centerx=SCREEN_WIDTH // 2, top=rect_bg.bottom + 30)
        screen.blit(resp_text, resp_rect)

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
        # Traînée pour les deux balles (couleur de plus en plus noire)
        for i in range(len(ball.trainee_coords)-1,0,-1):
             pygame.draw.circle(screen, TRAINEE_COLOR[i], ball.trainee_coords[i], ball.radius)
        for i in range(len(ball2.trainee_coords)-1,0,-1):
             pygame.draw.circle(screen, TRAINEE_COLOR[i], ball2.trainee_coords[i], ball2.radius)
        ball.draw(screen)
        ball2.draw(screen)

        # Rectangle blanc en haut avec texte noir (deux lignes)
        font = pygame.font.SysFont(None, 40)
        text1 = font.render(TEXT_TITLE, True, (0, 0, 0))
        text2 = font.render(TEXT_SUBTITLE, True, (0, 0, 0))
        text1_rect = text1.get_rect(centerx=SCREEN_WIDTH // 2, top=60)
        text2_rect = text2.get_rect(centerx=SCREEN_WIDTH // 2, top=text1_rect.bottom)
        padding = 24
        total_height = text1_rect.height + text2_rect.height + 2 * padding
        rect_bg = pygame.Rect(
            text1_rect.left - padding,
            text1_rect.top - padding,
            text1_rect.width + 2 * padding,
            total_height
        )
        pygame.draw.rect(screen, (255, 255, 255), rect_bg, border_radius=16)
        pygame.draw.rect(screen, (255, 255, 255), rect_bg, border_radius=16, width=4)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)

        # Deux petits rectangles juste en dessous
        small_font = pygame.font.SysFont(None, 48)
        # Rectangle "Bro's mom" + score
        yes_text = small_font.render(TEXT_YES, True, (0, 0, 0))
        yes_score = small_font.render(str(score_yes), True, (0, 0, 0))
        yes_rect = yes_text.get_rect()
        yes_rect.centerx = SCREEN_WIDTH // 2 - 120
        yes_rect.top = rect_bg.bottom + 20
        yes_bg = pygame.Rect(
            yes_rect.left - 16,
            yes_rect.top - 12,
            yes_rect.width + 32,
            yes_rect.height + yes_score.get_height() + 32
        )
        pygame.draw.rect(screen, (255, 255, 255), yes_bg, border_radius=12)
        pygame.draw.rect(screen, BALL_COLOR_YES, yes_bg, border_radius=12, width=4)
        screen.blit(yes_text, yes_rect)
        # Affiche le score sous le texte
        yes_score_rect = yes_score.get_rect(centerx=yes_rect.centerx, top=yes_rect.bottom + 8)
        screen.blit(yes_score, yes_score_rect)

        # Rectangle "Dragon" + score
        no_text = small_font.render(TEXT_NO, True, (0, 0, 0))
        no_score = small_font.render(str(score_no), True, (0, 0, 0))
        no_rect = no_text.get_rect()
        no_rect.centerx = SCREEN_WIDTH // 2 + 120
        no_rect.top = rect_bg.bottom + 20
        no_bg = pygame.Rect(
            no_rect.left - 16,
            no_rect.top - 12,
            no_rect.width + 32,
            no_rect.height + no_score.get_height() + 32
        )
        pygame.draw.rect(screen, (255, 255, 255), no_bg, border_radius=12)
        pygame.draw.rect(screen, BALL_COLOR_NO, no_bg, border_radius=12, width=4)
        screen.blit(no_text, no_rect)
        # Affiche le score sous le texte
        no_score_rect = no_score.get_rect(centerx=no_rect.centerx, top=no_rect.bottom + 8)
        screen.blit(no_score, no_score_rect)

    if frame_count >= wait_frames:
        # Collision et physique pour les deux balles avec les cercles
        for circle in CIRCLES:
            if circle.visible or circle.countdown > 0:
                prev_visible = circle.visible
                change = circle.check_collision(ball)
                # Attribution des points pour la balle rouge (Yes)
                if prev_visible and not circle.visible:
                    background_red_timer = background_red_duration  # Démarre le fondu rouge->noir
                    # Attribution des points selon la difficulté du cercle
                    if getattr(circle, "difficulty", None) == "easy":
                        score_yes += 1
                    elif getattr(circle, "difficulty", None) == "medium":
                        score_yes += 2
                    elif getattr(circle, "difficulty", None) == "hard":
                        score_yes += 5
                if not np.allclose(change, [0.0, 0.0]):
                    ball.apply_change(change)
                    break
        for circle in CIRCLES:
            if circle.visible or circle.countdown > 0:
                prev_visible = circle.visible
                change = circle.check_collision(ball2)
                # Attribution des points pour la balle verte (No)
                if prev_visible and not circle.visible:
                    background_red_timer = background_red_duration  # Démarre le fondu rouge->noir
                    if getattr(circle, "difficulty", None) == "easy":
                        score_no += 1
                    elif getattr(circle, "difficulty", None) == "medium":
                        score_no += 2
                    elif getattr(circle, "difficulty", None) == "hard":
                        score_no += 5
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
    # Sauvegarde de l'image à chaque frame
    pygame.image.save(screen, os.path.join(image_dir, f"frame_{frame_count:05d}.png"))

    clock.tick(60)
    frame_count += 1

pygame.quit()
