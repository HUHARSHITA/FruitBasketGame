import pygame
import math
import random
import os
import time
# Constants
HIGHSCORE_FILE = "highscore.txt"
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FRUIT_FALL_SPEED = 5
FRUIT_RADIUS = 15
NUM_FRUITS = 3
BOMB_FALL_SPEED = 5
BOMB_RADIUS = 15

class Fruit:
    def __init__(self, screen, x, y, img):
        self.parentScreen = screen
        self.img = pygame.image.load(img)
        self.fruitX = x
        self.fruitY = y
        self.fruitXcenter = self.fruitX + self.img.get_width() // 2
        self.fruitYcenter = self.fruitY + self.img.get_height() // 2

    def draw(self):
        self.parentScreen.blit(self.img, (self.fruitX, self.fruitY))

    def moveDown(self):
        if self.fruitY <= SCREEN_HEIGHT - self.img.get_height():
            self.fruitY += FRUIT_FALL_SPEED
        else:
            self.fruitY = 0
            self.fruitX = random.randint(0, SCREEN_WIDTH - self.img.get_width())
        self.fruitXcenter = self.fruitX + self.img.get_width() // 2
        self.fruitYcenter = self.fruitY + self.img.get_height() // 2
        self.draw()

class Bomb:
    def __init__(self, screen, x, y, img):
        self.parentScreen = screen
        self.img = pygame.image.load(img)
        self.bombX = x
        self.bombY = y
        self.bombXcenter = self.bombX + self.img.get_width() // 2
        self.bombYcenter = self.bombY + self.img.get_height() // 2

    def draw(self):
        self.parentScreen.blit(self.img, (self.bombX, self.bombY))

    def moveDown(self):
        if self.bombY <= SCREEN_HEIGHT - self.img.get_height():
            self.bombY += BOMB_FALL_SPEED
        else:
            self.bombY = 0
            self.bombX = random.randint(0, SCREEN_WIDTH - self.img.get_width())
        self.bombXcenter = self.bombX + self.img.get_width() // 2
        self.bombYcenter = self.bombY + self.img.get_height() // 2
        self.draw()

class Basket:
    def __init__(self, screen, x, y):
        self.parentScreen = screen
        self.img = pygame.image.load("resources/basket.png")
        self.x = x
        self.y = y
        self.xCenter = self.x + self.img.get_width() // 2
        self.yCenter = self.y + self.img.get_height() // 2

    def draw(self):
        self.parentScreen.blit(self.img, (self.x, self.y))

    def moveRight(self):
        if self.x <= SCREEN_WIDTH - self.img.get_width():
            self.x += 50
            self.xCenter = self.x + self.img.get_width() // 2
            self.draw()

    def moveLeft(self):
        if self.x >= 50:
            self.x -= 50
            self.xCenter = self.x + self.img.get_width() // 2
            self.draw()

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((200, 250, 180))
        pygame.display.update()
        self.playBackGround()
        self.basket = Basket(self.screen, 0, SCREEN_HEIGHT - 100)
        self.basket.draw()

        fruit_images = random.sample(["resources/fruit2.png", "resources/fruit3.png", "resources/fruit4.png", "resources/fruit5.png"], NUM_FRUITS)
        self.fruits = [Fruit(self.screen, random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), img) for img in fruit_images]

        self.bomb = Bomb(self.screen, random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), "resources/block.jpg")

        self.score = 0
        self.high_score = self.load_high_score()
        self.game_over = False

    def load_high_score(self):
        if os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        with open(HIGHSCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def reset(self):
        self.basket = Basket(self.screen, 0, SCREEN_HEIGHT - 100)
        fruit_images = random.sample(["resources/fruit2.png", "resources/fruit3.png", "resources/fruit4.png", "resources/fruit5.png"], NUM_FRUITS)
        self.fruits = [Fruit(self.screen, random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), img) for img in fruit_images]
        self.bomb = Bomb(self.screen, random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), "resources/block.jpg")
        self.score = 0
        self.game_over = False

    def displayScore(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score, (10, 10))
        high_score = font.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        self.screen.blit(high_score, (10, 50))
        pygame.display.flip()

    def playBackGround(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)  # Play endlessly from the beginning

    def playSound(self, sound):
        if sound == "ding":
            sound = pygame.mixer.Sound("resources/ding.mp3")
            pygame.mixer.Sound.play(sound)
        elif sound == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
            pygame.mixer.Sound.play(sound)

    def showGameOver(self):
        font = pygame.font.SysFont('arial', 40)
        text = font.render("GAME OVER!", True, (100, 90, 200))
        self.screen.blit(text, (50, 100))
        
    # Clear instructions for restarting or exiting
        text = font.render("Press Enter to play", True, (0, 0, 0))
        self.screen.blit(text, (20, 200))  # Improved positioning for better visibility
        text1=font.render("Press Esc to exit", True, (0, 0, 0))
        self.screen.blit(text1, (20, 300))
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
        self.displayHighScore()  # Separate function for displaying high score
        
        pygame.display.flip()
        pygame.mixer.music.pause()

    def displayHighScore(self):
        font = pygame.font.SysFont('arial', 30)
        high_score_text = font.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        self.screen.blit(high_score_text, (50, 250))

    def isCollide(self, obj):
        distance = math.sqrt((self.basket.xCenter - obj.fruitXcenter) ** 2 + (self.basket.yCenter - obj.fruitYcenter) ** 2)
        return distance < (FRUIT_RADIUS + self.basket.img.get_width() // 2)

    def isBombCollide(self):
        distance = math.sqrt((self.basket.xCenter - self.bomb.bombXcenter) ** 2 + (self.basket.yCenter - self.bomb.bombYcenter) ** 2)
        return distance < (BOMB_RADIUS + self.basket.img.get_width() // 2)

    def increaseScore(self):
        for fruit in self.fruits:
            if self.isCollide(fruit):
                self.score += 1
                self.playSound("ding")
                print("Score:", self.score)
                fruit.fruitY = 0
                fruit.fruitX = random.randint(0, SCREEN_WIDTH - fruit.img.get_width())

    def render(self):
        self.screen.fill((200, 250, 180))
        self.basket.draw()
        for fruit in self.fruits:
            fruit.draw()
        self.bomb.draw()
        self.displayScore()
        pygame.display.update()

    def moveFruitsDown(self):
        for fruit in self.fruits:
            fruit.moveDown()
        self.bomb.moveDown()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
                if event.key == pygame.K_RIGHT:
                    self.basket.moveRight()
                if event.key == pygame.K_LEFT:
                    self.basket.moveLeft()
                if self.game_over:
                    if event.key == pygame.K_RETURN:
                        self.reset()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.handleEvents()
            if not self.game_over:
                self.moveFruitsDown()
                self.increaseScore()
                if self.isBombCollide():
                    self.playSound("crash")
                    self.showGameOver()
                    pygame.display.flip()
                    time.sleep(5)
                    self.game_over = True
            self.render()
            clock.tick(30)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
