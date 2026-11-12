
# Assignment 8: Treasure Hunt Adventure
# The player explores an island and collects treasure.
import random

def play_game():
    treasures = []
    treasure_values = {
        "Golden Crown": 100,
        "Ruby": 75,
        "Emerald": 60,
        "Magic Sword": 40,
        "Diamond": 50
    }
    playing = True

    print("Welcome to Treasure Island!")
    print("Your mission is to collect treasure and escape!")

    # Keep showing choices until the player exits.
    while playing:
        print("\nWhat would you like to do?")
        print("1. Explore the jungle")
        print("2. Search the cave")
        print("3. Check your treasure")
        print("4. Escape the island")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nYou enter the jungle...")

            possible_treasures = ["Golden Crown", "Ruby", "Emerald", "Magic Sword"]
            found_treasure = random.choice(possible_treasures)

            print("You discovered a", found_treasure + "!")
            treasures.append(found_treasure)


        elif choice == "2":
            print("\nYou enter a dark cave...")
            print("You found a sparkling diamond!")
            treasures.append("Diamond")

        elif choice == "3":
            print("\nYour collected treasures:")
            if len(treasures) == 0:
                print("You haven't collected anything yet!")
            else:
                for treasure in treasures:
                    print("-", treasure)
            total_score = 0
            for treasure in treasures:
                total_score += treasure_values [treasure]
            print("Total score", total_score)

        elif choice == "4":
            print("\nYou escaped Treasure Island!")
            print("Total treasures collected:", len(treasures))

            total_score = 0
            for treasure in treasures:
                total_score += treasure_values [treasure]

            print("Total score:", total_score)
            print("Thanks for playing!")
            playing = False

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


play_game()
