while True:
    print("Song 1: Für Elise - Beethoven")
    print("Song 2: Moonlight Sonata - Beethoven")
    print("Song 3: Symphony No. 5 - Beethoven")
    print("Song 4: Clair De Lune - Debussy")
    print("Song 5: Spring” from The Four Seasons - Vivaldi")
    print("Song 6: Nutcracker Suite - Tchaikovsky")

    Quismundo_choice = int(input("\nEnter your song choice: "))

    found = False

    for Quismundo_song in range(1,6):
        if  Quismundo_song == Quismundo_choice:
            found = True
            break

    if found:
        if Quismundo_choice == 1:
            print("Playing Für Elise by Beethoven")
    elif Quismundo_choice == 2:
        print("Playing Moonlight Sonata by Beethoven")
    elif Quismundo_choice == 3:
        print("Playing Symphony No. 5 by Beethoven")
    elif Quismundo_choice == 4:
        print("Playing Clair De Lune by Debussy")
    elif Quismundo_choice == 5:
        print("Playing Spring from The Four Seasons by Vivaldi")
    elif Quismundo_choice == 6:
        print("Playing Nutcracker Suite by Tchaikovsky")
    else:
        print("Failed to play!")

    Quismundo_again = input("\nTry again? (Y/N): ")

    if Quismundo_again.upper() != "Y":
        break