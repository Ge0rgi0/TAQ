import pygame
import numpy as np
import math
import random
import os
import shutil

# === CONSTANTES MODIFIABLES ===

# Couleurs et textes
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_POINTS = 1
BALL_COLOR = (0, 0, 0)
BALL1_CONTOUR_COLOR = (255, 50, 50)   # Contour "YES"
BALL2_CONTOUR_COLOR = (50, 150, 255)  # Contour "NO"
BALL1_TRAIL_COLOR = BALL1_CONTOUR_COLOR
BALL2_TRAIL_COLOR = BALL2_CONTOUR_COLOR
BALL1_TEXT = "NO"
BALL2_TEXT = "YES"
BALL1_TEXT_COLOR = (255, 255, 255)
BALL2_TEXT_COLOR = (255, 255, 255)

NAME = "Julien"
ANSWER_YES = ""
ANSWER_NO = "Mais c'était sûr en fait !"
QUESTION = "Are you adopted ?"

# Dimensions écran
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 540

# Physique balles
MAX_SPEED = 5.99  # Augmente la vitesse initiale
BALL_RADIUS_RATIO = 0.05  # proportion de la largeur
BALL_COLOR_YES = BALL_COLOR
BALL_COLOR_NO = BALL_COLOR
BALL_CONTOUR_COLOR_YES = BALL1_CONTOUR_COLOR
BALL_CONTOUR_COLOR_NO = BALL2_CONTOUR_COLOR
BALL_MAX_VELOCITY = 6.0  # Augmente la vitesse maximale des balles

# Traînée
TRAIL_LENGTH = 10  # Un peu plus longue
TRAIL_MULT_BASE = 0.97

# Cercles
CIRCLE_THICKNESS = 4
CIRCLE_SPEED = 5
CIRCLE_HOLE_WIDTH = 70
CIRCLE_HOLE_OFFSET = 4
CIRCLE_HOLE_START_ANGLE = random.randint(0,359)
CIRCLE_RADIUS_FACTORS = list(range(35, 240, 5))
CIRCLE_SHRINK_SPEED = 7  # <-- Ajout : vitesse de rapetissement des cercles (pixels/frame)

# Difficulté/probabilités/couleurs
DIFFICULTY_PROBS = {
    "easy": 1.0,    # Tous les cercles sont "easy"
    "medium": 0.0,
    "hard": 0.0
}
DIFFICULTY_COLORS = {
    "easy": CIRCLE_COLOR,
    "medium": CIRCLE_COLOR,
    "hard": CIRCLE_COLOR
}

# Animation/fond
BACKGROUND_RED_DURATION = 30

# Score
TOTAL_FRAMES = 60 * 61

# Textes (modifiables facilement)
TEXT_TITLE = " Tag your friend ! Who's hotter ?"
TEXT_SUBTITLE = "Bro's mom or Dragon on Shrek ?"  # (texte en noir)
TEXT_YES = "NO"
TEXT_NO = "YES"
TEXT_BOTTOM = ["follow and comment", "to be picked for the next video"]

# Constantes global
SCREEN_HEIGHT = 1920//2  # Modifié
SCREEN_WIDTH = 1080//2   # Modifié

MAX_SPEED = 3.99  # Augmente la vitesse initiale (cohérent avec plus haut)
N = random.randint(1, int(MAX_SPEED * 100)) / 100
INITIAL_VELOCITY = np.array([N, MAX_SPEED - N], dtype=float)

# Traînée : couleur selon la balle
def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

TRAIL_BG_COLOR = (0,0,0)
def make_trail_color(trail_color):
    return [
        lerp_color(trail_color, TRAIL_BG_COLOR, i/(TRAIL_LENGTH-1))
        for i in range(TRAIL_LENGTH)
    ]

TRAIL_COLOR_YES = make_trail_color(BALL1_TRAIL_COLOR)
TRAIL_COLOR_NO = make_trail_color(BALL2_TRAIL_COLOR)

class Ball:
    def __init__(self, radius, color, c_radius, c_color, trail_color, text, text_color):
        self.radius = radius
        self.color = color
        self.c_radius = c_radius
        self.c_color = c_color
        self.trail_color = trail_color
        self.text = text
        self.text_color = text_color
        self.pos = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], dtype=float)
        self.velocity = INITIAL_VELOCITY.copy()
        self.trainee_coords = [self.pos.tolist()] * TRAIL_LENGTH

    def draw(self, screen):
        pygame.draw.circle(screen, self.c_color, self.pos.astype(int), int(self.c_radius))
        pygame.draw.circle(screen, self.color, self.pos.astype(int), int(self.radius))
        # Affiche le texte au centre de la balle
        font = pygame.font.SysFont(None, int(self.radius * 1.2))
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.pos.astype(int))
        screen.blit(text_surf, text_rect)

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
        self.difficulty = "easy"
        self.color = CIRCLE_COLOR
        self.center = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT * (4/10)])
        self.hole_angle = start_angle % 360
        self.hole_width = CIRCLE_HOLE_WIDTH
        self.visible = True
        self.countdown = 50
        self.speed = CIRCLE_SPEED
        self.normal_radius = radius

    def update_hole(self):
        # Toujours tourner, même si invisible ou countdown > 0
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
        # --- Cas 1 : cercle détruit (inchangé) ---
        if self.visible and distance + ball.radius >= total_radius + 5:
            self.visible = False
            speed = np.linalg.norm(ball.velocity)
            if speed > 0:
                ball.velocity = ball.velocity / speed * (speed * 1.025)
        # --- Cas 2 : collision avec cercle (rebond ou décalage selon rapetissement) ---
        elif self.visible and distance + ball.radius >= total_radius - 10:
            vec = direction
            angle = math.degrees(math.atan2(-vec[1], vec[0])) % 360
            hole_start = self.hole_angle
            hole_end = (self.hole_angle + self.hole_width) % 360
            tolerance = (ball.c_radius * 0.5) // 2
            in_hole = False
            if hole_start < hole_end:
                in_hole = hole_start + tolerance <= angle <= hole_end - tolerance
            else:
                in_hole = angle >= hole_start or angle <= hole_end

            if not in_hole and distance != 0:
                normal = direction / distance
                REBOUND_FACTOR = 1.15  # >1 pour rebondir plus fort
                # Si le cercle rapetisse, rebond + décalage, mais ne brise pas le cercle
                if self.radius < self.normal_radius:
                    # Rebond (même code que d'habitude)
                    ball.velocity -= 2 * np.dot(ball.velocity, normal) * normal
                    ball.velocity *= REBOUND_FACTOR  # Ajout : rebond amplifié
                    # Décale la balle à l'intérieur du cercle
                    target_distance = total_radius - ball.radius - 11
                    ball.pos = self.center + normal * target_distance
                    return np.array([0.0, 0.0])
                # Sinon, comportement normal (rebond + éventuellement correction de position)
                ball.velocity -= 2 * np.dot(ball.velocity, normal) * normal
                ball.velocity *= REBOUND_FACTOR  # Ajout : rebond amplifié
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

    def __iter__(self):
        return iter(self.circles)

    def draw(self, screen):
        if not self.circles[0].visible and self.circles[0].countdown != 1:
            # Décalage de l'angle du nouveau cercle par rapport au précédent
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
# Balle "YES"
ball = Ball(
    radius=ball_radius,
    color=BALL_COLOR_YES,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR_YES,
    trail_color=BALL1_TRAIL_COLOR,
    text=BALL1_TEXT,
    text_color=BALL1_TEXT_COLOR
)
ball.pos = np.array([SCREEN_WIDTH // 2 - SCREEN_WIDTH // 32, SCREEN_HEIGHT * (4/10)], dtype=float)
ball.trainee_coords = [ball.pos.tolist()] * TRAIL_LENGTH

# Balle "NO"
ball2 = Ball(
    radius=ball_radius,
    color=BALL_COLOR_NO,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR_NO,
    trail_color=BALL2_TRAIL_COLOR,
    text=BALL2_TEXT,
    text_color=BALL2_TEXT_COLOR
)
ball2.pos = np.array([SCREEN_WIDTH // 2 + SCREEN_WIDTH // 32, SCREEN_HEIGHT * (4/10)], dtype=float)
ball2.velocity = INITIAL_VELOCITY.copy()
ball2.trainee_coords = [ball2.pos.tolist()] * TRAIL_LENGTH

CIRCLES = Circles([
    Circle(
        radius=int(SCREEN_WIDTH * factor/100) // 2,
        thickness=CIRCLE_THICKNESS,
        color=(255, 255, 255),
        start_angle=(i * CIRCLE_HOLE_OFFSET) % 360,  # Décale chaque cercle de CIRCLE_HOLE_OFFSET degrés
        speed=2.0  # Vitesse fixe à 2
    )
    for i, factor in enumerate(CIRCLE_RADIUS_FACTORS)
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

# Ajout : chargement de l'image pour l'affichage final
DRAGON_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "dragon.jpg")
dragon_img = pygame.image.load(DRAGON_IMAGE_PATH).convert_alpha()

# Boucle principale
background_red_timer = 0  # Timer pour fond rouge
background_red_duration = BACKGROUND_RED_DURATION  # Utilise la constante

while running and frame_count < TOTAL_FRAMES:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dernières 5*60 frames : affiche juste la question et la réponse
    if frame_count >= TOTAL_FRAMES - 5*60:
        screen.fill((0, 0, 0))  # fond noir
        # Affiche la question en haut
        top_font = pygame.font.SysFont(None, 55)
        top_text = top_font.render(QUESTION, True, (255, 255, 255))
        top_rect = top_text.get_rect()
        top_rect.centerx = SCREEN_WIDTH // 2
        top_rect.top = 24 + 100 + 12
        top_bg = pygame.Rect(
            top_rect.left - 24,
            24 + 100,
            top_rect.width + 48,
            top_rect.height + 24
        )
        pygame.draw.rect(screen, (40, 40, 40), top_bg, border_radius=15)
        pygame.draw.rect(screen, (255, 255, 255), top_bg, border_radius=14, width=3)  # contour blanc
        screen.blit(top_text, top_rect)
        # Affiche uniquement la réponse finale, centrée verticalement
        font_big = pygame.font.SysFont(None, 100)
        if score_yes > score_no:
            winner_text = TEXT_YES
        else:
            winner_text = TEXT_NO
        answer_text = font_big.render(winner_text, True, (255, 255, 255))
        answer_rect = answer_text.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2 + 80)
        screen.blit(answer_text, answer_rect)
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
            screen.fill((0, 0, 0))  # fond noir forcé


        # Mise à jour et affichage
        CIRCLES.update_holes()
        CIRCLES.draw(screen)
        # Traînée pour les deux balles (couleur de plus en plus noire, même taille que le contour)
        for i in range(len(ball.trainee_coords)-1, 0, -1):
            pygame.draw.circle(screen, TRAIL_COLOR_YES[i], ball.trainee_coords[i], ball.c_radius)
        for i in range(len(ball2.trainee_coords)-1, 0, -1):
            pygame.draw.circle(screen, TRAIL_COLOR_NO[i], ball2.trainee_coords[i], ball2.c_radius)
        ball.draw(screen)
        ball2.draw(screen)

        # Rectangle en haut avec la question
        top_font = pygame.font.SysFont(None, 55)
        top_text = top_font.render(QUESTION, True, (255, 255, 255))
        top_rect = top_text.get_rect()
        top_rect.centerx = SCREEN_WIDTH // 2
        top_rect.top = 24 + 100 + 12
        top_bg = pygame.Rect(
            top_rect.left - 24,
            24 + 100,
            top_rect.width + 48,
            top_rect.height + 24
        )
        pygame.draw.rect(screen, (40, 40, 40), top_bg, border_radius=15)
        pygame.draw.rect(screen, (255, 255, 255), top_bg, border_radius=14, width=3)  # contour blanc
        screen.blit(top_text, top_rect)

        # Petits rectangles réponses sur une seule ligne, texte grand, rectangles réduits
        big_font = pygame.font.SysFont(None, 48)
        rects_top = SCREEN_HEIGHT // 4

        # YES rectangle (left)
        yes_text = big_font.render(f"{TEXT_YES}: {score_yes}", True, (255, 255, 255))
        yes_rect = yes_text.get_rect()
        yes_rect.centerx = SCREEN_WIDTH // 2 - 80
        yes_rect.centery = rects_top
        yes_bg = pygame.Rect(
            yes_rect.left - 10,
            yes_rect.top - 6,
            yes_rect.width + 20,
            yes_rect.height + 12
        )
        pygame.draw.rect(screen, BALL1_CONTOUR_COLOR, yes_bg, border_radius=10)
        screen.blit(yes_text, yes_rect)

        # NO rectangle (right)
        no_text = big_font.render(f"{TEXT_NO}: {score_no}", True, (255, 255, 255))
        no_rect = no_text.get_rect()
        no_rect.centerx = SCREEN_WIDTH // 2 + 80
        no_rect.centery = rects_top
        no_bg = pygame.Rect(
            no_rect.left - 10,
            no_rect.top - 6,
            no_rect.width + 20,
            no_rect.height + 12
        )
        pygame.draw.rect(screen, BALL2_CONTOUR_COLOR, no_bg, border_radius=10)
        screen.blit(no_text, no_rect)

    if frame_count >= wait_frames:
        # Collision et physique pour les deux balles avec les cercles
        for circle in CIRCLES:
            if circle.visible or circle.countdown > 0:
                prev_visible = circle.visible
                change = circle.check_collision(ball)
                # Attribution des points pour la balle "YES"
                if prev_visible and not circle.visible:
                    background_red_timer = background_red_duration
                    score_yes += CIRCLE_POINTS
                if not np.allclose(change, [0.0, 0.0]):
                    ball.apply_change(change)
                    break
        for circle in CIRCLES:
            if circle.visible or circle.countdown > 0:
                prev_visible = circle.visible
                change = circle.check_collision(ball2)
                # Attribution des points pour la balle "NO"
                if prev_visible and not circle.visible:
                    background_red_timer = background_red_duration
                    score_no += CIRCLE_POINTS
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
