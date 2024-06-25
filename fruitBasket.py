import pygame
import time
import random
class Fruit:
    def __init__(self,screen,x,y):
        self.parentScreen=screen
        fruits=["resources/fruit1.png","resources/fruit2.png","resources/fruit3.png","resources/fruit4.png","resources/fruit5.png"]
        self.img=pygame.image.load(random.choice(fruits))
        self.x=x
        self.y=y

    def draw(self):
        self.parentScreen.blit(self.img,(self.x,self.y))
        #pygame.display.update()

    def moveDown(self):
        if self.y<=533:
            self.y+=5
            #self.posUpdate()
            self.draw()
        else:
            self.y=0
            #self.posUpdate()
            self.draw()


    

class Basket:
    def __init__(self,screen,x,y):
        self.parentScreen=screen
        self.img=pygame.image.load("resources/basket.png")
        self.x=x
        self.y=y

    def draw(self):
        self.parentScreen.blit(self.img,(self.x,self.y))
        pygame.display.update() 

    def moveRight(self):
        if self.x<=215:
            self.x+=50
            #self.posUpdate()
            self.draw()

    def moveLeft(self):
        if self.x>=5:
            self.x-=50
            #self.posUpdate()
            self.draw()

        

class Game:
    def __init__(self):
        pygame.init()
        print("init entered")
        self.screen=pygame.display.set_mode((400,600))
        self.screen.fill((200,250,180))
        pygame.display.update()
        x=0
        y=500
        self.basket=Basket(self.screen,x,y)
        self.basket.draw()
        print("basket")

        fruitList=[]
        x=self.setX()
        y=self.setY()
        self.fruit1=Fruit(self.screen,x,y)
        self.fruit1.draw()
        if self.fruit1 not in fruitList:
            fruitList.append(self.fruit1)

        # x=self.setX()
        # y=self.setY()
        # self.fruit2=Fruit(self.screen,x,y)
        # self.fruit2.draw()
        # fruitList.append(self.fruit2)

        # x=self.setX()
        # y=self.setY()
        # self.fruit3=Fruit(self.screen,x,y)
        # self.fruit3.draw()
        # fruitList.append(self.fruit3)

        # x=self.setX()
        # y=self.setY()
        # self.fruit4=Fruit(self.screen,x,y)
        # self.fruit4.draw()
        # fruitList.append(self.fruit4)

        # x=self.setX()
        # y=self.setY()
        # self.fruit5=Fruit(self.screen,x,y)
        # self.fruit5.draw()
        # fruitList.append(self.fruit5)

        self.score=0
        #time.sleep(2)
    def setX(self):
        x=random.randint(0,400)
        return x
    def setY(self):
        y=random.randint(0,250)
        return y
    
    def IncreaseScore(self,score):
        if self.isCollide() is True:
            self.score=(self.score+1)
            print(score)

    def isCollide(self):
    # Calculate the center coordinates of the basket and each fruit
        basket_center_x = self.basket.x + self.basket.img.get_width() // 2
        basket_center_y = self.basket.y + self.basket.img.get_height() // 2
        fruit_center_x_list = [
            self.fruit1.x + self.fruit1.img.get_width() // 2,
            # self.fruit2.x + self.fruit2.img.get_width() // 2,
            # self.fruit3.x + self.fruit3.img.get_width() // 2,
            # self.fruit4.x + self.fruit4.img.get_width() // 2,
            # self.fruit5.x + self.fruit5.img.get_width() // 2,
        ]
        fruit_center_y_list = [
            self.fruit1.y + self.fruit1.img.get_height() // 2,
            # self.fruit2.y + self.fruit2.img.get_height() // 2,
            # self.fruit3.y + self.fruit3.img.get_height() // 2,
            # self.fruit4.y + self.fruit4.img.get_height() // 2,
            # self.fruit5.y + self.fruit5.img.get_height() // 2,
        ]

        # Check for distance between centers within a threshold
        collision_threshold = 30  # Adjust this value based on image sizes
        for i in range(len(fruit_center_x_list)):
            distance_x = abs(basket_center_x - fruit_center_x_list[i])
            distance_y = abs(basket_center_y - fruit_center_y_list[i])
            if distance_x < collision_threshold and distance_y < collision_threshold:
                return True

        return False

        
    def posUpdate(self):
        self.parentScreen.blit(self.img,(self.x,self.y))
        pygame.display.update()
    
    def render(self):
        self.screen.fill((200,250,180))
        self.basket.draw()
        self.fruit1.draw()
        # self.fruit2.draw()
        # self.fruit3.draw()
        # self.fruit4.draw()
        # self.fruit5.draw()
        pygame.display.update()
        self.clock = pygame.time.Clock()

       
    def run(self):
        print("Run entered")
        running=True
        while running:
            self.screen.fill((200,250,180))
            self.fruit1.moveDown()
            # self.fruit2.moveDown()
            # self.fruit3.moveDown()
            # self.fruit4.moveDown()
            # self.fruit5.moveDown()
            
            #if pygame.event()==pygame.KEYDOWN():
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()            
                    exit(1)
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        running=False
                    if event.key==pygame.K_RETURN:
                        running=True
                    if event.key==pygame.K_RIGHT:
                        self.basket.moveRight()
                    if event.key==pygame.K_LEFT:
                        self.basket.moveLeft()
            self.fruit1.moveDown()
            # self.fruit2.moveDown()
            # self.fruit3.moveDown()
            # self.fruit4.moveDown()
            # self.fruit5.moveDown()
            self.IncreaseScore(self.score)
            self.render()
            self.clock.tick(30)
def main():
    game=Game()
    game.run()
if __name__=="__main__":
    main()