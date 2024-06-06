import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600

# Цвета
WHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Глаза, следящие за мышью")

# Настройка начальных координат глаз
eye_radius = 30
left_eye = [200, 300]
right_eye = [400, 300]

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фона
    screen.fill(WHITE)

    # Получение координат мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Рассчитываем угол курсора относительно глаз
    angle_left = math.atan2(mouse_y - left_eye[1], mouse_x - left_eye[0])
    angle_right = math.atan2(mouse_y - right_eye[1], mouse_x - right_eye[0])

    # Расчет координат для центра глаз
    left_pupil = (left_eye[0] + eye_radius * math.cos(angle_left), left_eye[1] + eye_radius * math.sin(angle_left))
    right_pupil = (right_eye[0] + eye_radius * math.cos(angle_right), right_eye[1] + eye_radius * math.sin(angle_right))

    # Отрисовка белка и зрачка глаз
    pygame.draw.circle(screen, (0, 0, 0), left_eye, eye_radius)  # глаза
    pygame.draw.circle(screen, (0, 0, 255), left_pupil, 10)  # зрачок
    pygame.draw.circle(screen, (0, 0, 0), right_eye, eye_radius)
    pygame.draw.circle(screen, (0, 0, 255), right_pupil, 10)

    # Обновление экрана
    pygame.display.flip()
