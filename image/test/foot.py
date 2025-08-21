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
BALL_COLOR_YES = (0,0,0)
BALL_COLOR_NO = (0,0,0)
BALL_CONTOUR_COLOR = (255, 255, 255)
BALL_MAX_VELOCITY = 5.0  # Limite de vitesse des balles (pixels/frame)

# Traînée
TRAIL_LENGTH = 10  # Un peu plus longue
TRAIL_MULT_BASE = 0.97

# Cercles
CIRCLE_THICKNESS = 3
CIRCLE_SPEED = 3.0
CIRCLE_HOLE_WIDTH = 60
CIRCLE_HOLE_OFFSET = 3
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
    "easy": (255, 255, 255),   # blanc
    "medium": (0, 0, 0),       # noir
    "hard": (220, 30, 30)      # rouge
}

# Animation/fond
BACKGROUND_RED_DURATION = 30

# Score
TOTAL_FRAMES = 60 * 61

# Textes (modifiables facilement)
TEXT_TITLE = " Who will win Saturday ?"
TEXT_SUBTITLE = ""
TEXT_YES = "PSG"
TEXT_NO = "Inter"
TEXT_BOTTOM = ["follow and comment", "to be picked for the next video"]

# Constantes global
SCREEN_HEIGHT = 1920//2  # Modifié
SCREEN_WIDTH = 1080//2   # Modifié

MAX_SPEED = 1.99
N = random.randint(1, int(MAX_SPEED * 100)) / 100
INITIAL_VELOCITY = np.array([N, MAX_SPEED - N], dtype=float)

# Traînée : du blanc vers le vert du fond (34, 139, 34)
def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

TRAIL_BG_COLOR = (34, 139, 34)      # Vert pelouse
TRAIL_COLOR_START = (255, 255, 255) # Blanc
TRAINEE_COLOR = [
    lerp_color(TRAIL_COLOR_START, TRAIL_BG_COLOR, i/(TRAIL_LENGTH-1))
    for i in range(TRAIL_LENGTH)
]
TRAINEE_MULT = [TRAIL_MULT_BASE ** i for i in range(TRAIL_LENGTH)]

class Ball:
    def __init__(self, radius, color, c_radius, c_color, image):
        self.radius = radius
        self.color = color
        self.c_radius = c_radius
        self.c_color = c_color
        self.image = image
        self.pos = np.array([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], dtype=float)
        self.velocity = INITIAL_VELOCITY.copy()
        self.trainee_coords = [self.pos.tolist()] * len(TRAINEE_COLOR)

    def draw(self, screen):
        # Dessine le contour (cercle blanc)
        pygame.draw.circle(screen, self.c_color, self.pos.astype(int), int(self.c_radius))
        # Redimensionne l'image à la taille du cercle principal
        img_size = int(self.radius * 2)
        img = pygame.transform.smoothscale(self.image, (img_size, img_size))
        # Crée un masque circulaire pour l'image
        mask_surface = pygame.Surface((img_size, img_size), pygame.SRCALPHA)
        pygame.draw.circle(mask_surface, (255, 255, 255, 255), (img_size // 2, img_size // 2), img_size // 2)
        img.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        # Centre l'image sur la position de la balle
        rect_main = img.get_rect(center=(int(self.pos[0]), int(self.pos[1])))
        screen.blit(img, rect_main)

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

# Ajout : chargement des images pour les boules depuis le dossier courant
PSG_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "PSG.png")
LOTR_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "LOTR.png")
psg_img = pygame.image.load(PSG_IMAGE_PATH).convert_alpha()
lotr_img = pygame.image.load(LOTR_IMAGE_PATH).convert_alpha()

# Création des objets
ball_radius = SCREEN_WIDTH * BALL_RADIUS_RATIO
# Balle rouge (Yes), plus proche du centre
ball = Ball(
    radius=ball_radius,
    color=BALL_COLOR_YES,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR,
    image=psg_img
)
ball.pos = np.array([SCREEN_WIDTH // 2 - SCREEN_WIDTH // 32, SCREEN_HEIGHT // 2], dtype=float)
ball.trainee_coords = [ball.pos.tolist()] * len(TRAINEE_COLOR)

# Balle verte (No), plus proche du centre
ball2 = Ball(
    radius=ball_radius,
    color=BALL_COLOR_NO,
    c_radius=ball_radius * 1.2,
    c_color=BALL_CONTOUR_COLOR,
    image=lotr_img
)
ball2.pos = np.array([SCREEN_WIDTH // 2 + SCREEN_WIDTH // 32, SCREEN_HEIGHT // 2], dtype=float)
ball2.velocity = INITIAL_VELOCITY.copy()
ball2.trainee_coords = [ball2.pos.tolist()] * len(TRAINEE_COLOR)

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

    # --- Fond vert stade ---
    screen.fill((34, 139, 34))  # Vert "pelouse"

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

    # Rectangle blanc en haut avec texte noir (plus bas)
    font = pygame.font.SysFont(None, 40)
    text = font.render(TEXT_TITLE, True, (0, 0, 0))
    subtext = pygame.font.SysFont(None, 40).render(TEXT_SUBTITLE, True, (80, 80, 80))
    text_rect = text.get_rect()
    subtext_rect = subtext.get_rect()
    text_rect.centerx = SCREEN_WIDTH // 2
    text_rect.top = 60
    subtext_rect.centerx = SCREEN_WIDTH // 2
    subtext_rect.top = text_rect.bottom

    padding = 24
    total_height = text_rect.height + subtext_rect.height + 2 * padding
    rect_bg = pygame.Rect(
        text_rect.left - padding,
        text_rect.top - padding,
        text_rect.width + 2 * padding,
        total_height
    )
    pygame.draw.rect(screen, (255, 255, 255), rect_bg, border_radius=16)
    pygame.draw.rect(screen, (255, 255, 255), rect_bg, border_radius=16, width=4)
    screen.blit(text, text_rect)
    screen.blit(subtext, subtext_rect)

    # Deux petits rectangles juste en dessous
    small_font = pygame.font.SysFont(None, 48)
    # Rectangle "Yes\nscore"
    yes_text = small_font.render(TEXT_YES, True, (0, 0, 0))
    yes_text2 = small_font.render(str(score_yes), True, (0, 0, 0))
    yes_rect = yes_text.get_rect()
    yes_rect.centerx = SCREEN_WIDTH // 2 - 120
    yes_rect.top = rect_bg.bottom + 20
    yes_bg = pygame.Rect(
        yes_rect.left - 16,
        yes_rect.top - 12,
        yes_rect.width + 32,
        yes_rect.height * 2 + 24
    )
    pygame.draw.rect(screen, (255, 255, 255), yes_bg, border_radius=12)
    pygame.draw.rect(screen, BALL_COLOR_YES, yes_bg, border_radius=12, width=4)
    screen.blit(yes_text, yes_rect)
    yes_text2_rect = yes_text2.get_rect(centerx=yes_rect.centerx, top=yes_rect.bottom)
    screen.blit(yes_text2, yes_text2_rect)

    # Rectangle "NO\nscore"
    no_text = small_font.render(TEXT_NO, True, (0, 0, 0))
    no_text2 = small_font.render(str(score_no), True, (0, 0, 0))
    no_rect = no_text.get_rect()
    no_rect.centerx = SCREEN_WIDTH // 2 + 120
    no_rect.top = rect_bg.bottom + 20
    no_bg = pygame.Rect(
        no_rect.left - 16,
        no_rect.top - 12,
        no_rect.width + 32,
        no_rect.height * 2 + 24
    )
    pygame.draw.rect(screen, (255, 255, 255), no_bg, border_radius=12)
    pygame.draw.rect(screen, BALL_COLOR_NO, no_bg, border_radius=12, width=4)
    screen.blit(no_text, no_rect)
    no_text2_rect = no_text2.get_rect(centerx=no_rect.centerx, top=no_rect.bottom)
    screen.blit(no_text2, no_text2_rect)

    # Rectangle en bas avec texte "follow and comment to be pick for the next video" sur plusieurs lignes
    bottom_lines = TEXT_BOTTOM
    bottom_font = small_font
    rendered_lines = [bottom_font.render(line, True, (0, 0, 0)) for line in bottom_lines]
    line_height = rendered_lines[0].get_height()
    total_text_height = line_height * len(rendered_lines) + 10 * (len(rendered_lines) - 1)
    bottom_bg_width = max(r.get_width() for r in rendered_lines) + 64
    bottom_bg_height = total_text_height + 32

    bottom_bg = pygame.Rect(
        (SCREEN_WIDTH - bottom_bg_width) // 2,
        SCREEN_HEIGHT - bottom_bg_height - 40,
        bottom_bg_width,
        bottom_bg_height
    )
    pygame.draw.rect(screen, (255, 255, 255), bottom_bg, border_radius=18)
    pygame.draw.rect(screen, (0, 0, 0), bottom_bg, border_radius=18, width=4)

    y = bottom_bg.top + 16
    for r in rendered_lines:
        r_rect = r.get_rect(centerx=SCREEN_WIDTH // 2, top=y)
        screen.blit(r, r_rect)
        y += line_height + 10

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
