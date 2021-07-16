import pygame
import time
# mais informações:https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.get_pos
try:
    tempo = int(input("\ndigite o tempo da musica em segundos\n"))
    if(tempo <= 5):
        print("Digite um tempo maior que 5 segundos")
        exit()

except (ValueError):
    print("Ocorreu um erro ao digitar os segundos por favor digite um numero")
    exit()

pygame.init()
pygame.mixer.music.load('harrypotterbugado.mp3')
pygame.mixer.music.play()
time.sleep(tempo)