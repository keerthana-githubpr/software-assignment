import random
import pygame

def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    print(f"Now playing: {file_name}")

# List of all available audio file names
file_names = [f"{i}.mp3" for i in range(1, 20)]

# Shuffle the file names to generate a random order
random.shuffle(file_names)

# Initialize pygame
pygame.init()

# Play the first audio file
current_file = file_names[0]
play_audio(current_file)

# Current playback state
is_paused = False

# Main loop for audio playback control
while True:
    # Wait for user input
    user_input = input("Enter 'p' to pause, 'r' to resume, or 'n' to skip to the next audio and q to exit playlist: ")

    # Handle user input
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
        # Stop playing the current audio
        pygame.mixer.music.stop()

        # Increment the current index
        current_index = (file_names.index(current_file) + 1) % len(file_names)

        # Play the next audio file
        current_file = file_names[current_index]
        play_audio(current_file)
        is_paused = False
    else:
        print("Invalid input")
    

