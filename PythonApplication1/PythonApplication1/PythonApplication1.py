import pygame
import sys
import math

# ������������� Pygame
pygame.init()

# ������� ������
screen_width = 800
screen_height = 600

# �����
WHITE = (255, 255, 255)

# �������� ����
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("�����, �������� �� �����")

# ��������� ��������� ��������� ����
eye_radius = 30
left_eye = [200, 300]
right_eye = [400, 300]

# �������� ���� ����
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ��������� ����
    screen.fill(WHITE)

    # ��������� ��������� ����
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # ������������ ���� ������� ������������ ����
    angle_left = math.atan2(mouse_y - left_eye[1], mouse_x - left_eye[0])
    angle_right = math.atan2(mouse_y - right_eye[1], mouse_x - right_eye[0])

    # ������ ��������� ��� ������ ����
    left_pupil = (left_eye[0] + eye_radius * math.cos(angle_left), left_eye[1] + eye_radius * math.sin(angle_left))
    right_pupil = (right_eye[0] + eye_radius * math.cos(angle_right), right_eye[1] + eye_radius * math.sin(angle_right))

    # ��������� ����� � ������ ����
    pygame.draw.circle(screen, (0, 0, 0), left_eye, eye_radius)  # �����
    pygame.draw.circle(screen, (0, 0, 255), left_pupil, 10)  # ������
    pygame.draw.circle(screen, (0, 0, 0), right_eye, eye_radius)
    pygame.draw.circle(screen, (0, 0, 255), right_pupil, 10)

    # ���������� ������
    pygame.display.flip()
