import time
import pygame

def main():
    pygame.init()

    ##VARIABLES##
    _work = 25; _break = 5; _cycles = 4


    print("Welcome to Customizable Pomodoro Timer!\n")
    print("Default values;")
    print(f"Work: {_work} min")
    print(f"Break: {_break} min")
    print(f"cycles: {_cycles} times\n")
    _change = str(input("Would you like to change durations?[y/n] "))
    
    if _change == 'y':
        _work = int(input("Work duration: "))
        _break = int(input("Break duration: "))
    
    sound_file = input("Enter the notification sound you want(leave blank for default): ").strip()
    if not sound_file:
    	sound_file = "notification.mp3"
    
    print(f"Pomodoro Timer is going to start with {_work} minutes of work & {_break} minutes of break.")
    
    for cycle in range(_cycles):
    	timer(_work,"Work")
    	notification(sound_file)
    	if cycle < _cycles-1:
            input("\nPress Enter to start break...")
            timer(_break, "break")
            notification(sound_file)

    print("Pomodoro Timer Completed!")


def timer(duration, timer_type):
    print(f"{timer_type} duration started!")
    _duration = duration - 1
    for minute in range(_duration, -1, -1):
        for second in range(59, -1, -1):
            time.sleep(1)
            print(f"\r{timer_type} - {minute:02}:{second:02}", end='', flush=True)
    print(f"\r{timer_type} - 00:00\n")

def notification(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()