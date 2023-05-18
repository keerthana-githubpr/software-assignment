import random
import pygame

def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    print(f"Now playing: {file_name}")


file_names = [f"{i}.mp3" for i in range(1, 20)]


random.shuffle(file_names)


pygame.init()

current_file = file_names[0]
play_audio(current_file)

is_paused = False


while True:
    
    user_input = input("Enter 'p' to pause, 'r' to resume, or 'n' to skip to the next audio and q to exit playlist: ")

    
    if user_input == "p":
        if not is_paused:
            pygame.mixer.music.pause()
            is_paused = True
            print("Audio paused")
        else:
            print("Audio is already paused")
    elif user_input == "r":
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
            print("Audio resumed")
        else:
            print("Audio is already playing")
    elif user_input == "q":
        exit(0)
    elif user_input == "n":
        
        pygame.mixer.music.stop()

        
        current_index = (file_names.index(current_file) + 1) % len(file_names)

        current_file = file_names[current_index]
        play_audio(current_file)
        is_paused = False
    else:
        print("Invalid input")
    

