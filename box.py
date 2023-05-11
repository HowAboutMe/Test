# 导入必要的库
import pygame

# 定义游戏中用到的颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 0)
RED = (213, 50, 80)

# 定义方格的大小和游戏界面的大小
BLOCK_SIZE = 50
SCREEN_WIDTH = 16 * BLOCK_SIZE
SCREEN_HEIGHT = 12 * BLOCK_SIZE

# 定义游戏地图
MAP = [
    "wwwwwwwwwwwwwwww",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "w              w",
    "wwwwwwwwwwwwwwww",
]

# 定义游戏中的角色


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if MAP[self.y+dy][self.x+dx] == " ":
            self.x += dx
            self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x*BLOCK_SIZE,
                         self.y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


class Box():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if MAP[self.y+dy][self.x+dx] == " ":
            self.x += dx
            self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x*BLOCK_SIZE,
                         self.y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


# 初始化 Pygame
pygame.init()

# 创建游戏窗口和标题
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Push Box Game")

# 创建游戏时钟
clock = pygame.time.Clock()

# 创建角色和箱子
player = Player(2, 2)
box = Box(3, 3)

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-1, 0)
                if player.x == box.x & player.y == box.y:
                    box.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)
                if player.x == box.x & player.y == box.y:
                    box.move(1, 0)
            elif event.key == pygame.K_UP:
                player.move(0, -1)
                if player.x == box.x & player.y == box.y:
                    box.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
                if player.x == box.x & player.y == box.y:
                    box.move(0, 1)

    # 绘制游戏界面
    screen.fill(WHITE)
    for y, row in enumerate(MAP):
        for x, col in enumerate(row):
            if col == "w":
                pygame.draw.rect(screen, BLUE, (x*BLOCK_SIZE,
                                 y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    player.draw(screen)
    box.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()
