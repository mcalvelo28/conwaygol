import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 600))

Clock = pygame.time.Clock()



class MAIN():
    def __init__(self):
        self.screenspace = []

        for x in range(40):
            self.templ = []

            for j in range(40):
                self.templ.append(0)
            
            self.screenspace.append(self.templ)
        self.active = False

    def changecoords(self, x, y):
        self.screenspace[y][x] = 1

    def screenprint(self):
        for x in range(40):
            for j in range(40):
                if self.screenspace[j][x] == 1:
                    pygame.draw.rect(screen, (255,255,255), (x * (600/40), j * (600/40), 15, 15))        

    def GOL(self):
        self.copy = self.screenspace.copy()

        for z in range(39):
            for k in range(39):
                neighbors = 0

                
                if self.copy[z - 1][k - 1] == 1:
                    neighbors += 1
                else:
                    pass
                
                if self.copy[z - 1][k] == 1:
                    neighbors += 1
                else:
                    pass

                if self.copy[z - 1][k + 1] == 1:
                    neighbors += 1
                else:
                    pass

                if self.copy[z][k - 1] == 1:
                    neighbors += 1
                else:
                    pass

                if self.copy[z][k + 1] == 1:
                    neighbors += 1
                else:
                    pass

                if self.copy[z + 1][k - 1] == 1:
                    neighbors += 1
                else:
                    pass
                
                if self.copy[z + 1][k] == 1:
                    neighbors += 1
                else:
                    pass

                if self.copy[z + 1][k + 1] == 1:
                    neighbors += 1
                else:
                    pass


                if self.copy[z][k] == 0:
                    if neighbors == 3:
                        self.copy[z][k] = 1
                    else:
                        pass
                elif self.copy[z][k] == 1:
                    if neighbors <= 1:
                        self.copy[z][k] = 0
                    elif 2 <= neighbors <= 3:
                        pass
                    elif neighbors >= 4:
                        self.copy[z][k] = 0
                    else:
                        pass
        
        self.screenspace = self.copy.copy()


main = MAIN()

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            main.changecoords(int(mouse[0] // (600/40)), int(mouse[1] // (600/40)))

            # print(int(mouse[0] // (600/40)))

        if event.type == pygame.KEYDOWN:
            if main.active == False:
                main.active = True
            else:
                main.active = False


    screen.fill((0,0,0))

    if main.active == True:
        main.GOL()
    else:
        pass

    main.screenprint()

    Clock.tick(10)


    pygame.display.update()