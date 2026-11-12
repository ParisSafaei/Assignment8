
# Assignment 8: Treasure Hunt Adventure
# The player explores an island and collects treasure.
import random

def play_game():
    treasures = []
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
        print("5. Open a mystery treasure chest")

        choice = input("Enter your choice (1-5): ")

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

        elif choice == "4":
            print("\nYou escaped Treasure Island!")
            print("Total treasures collected:", len(treasures))
            print("Thanks for playing!")
            playing = False

        elif choice == "5":
            print("\nYou found a mysterious treasure chest!")

            chest_rewards = ["Golden Crown", "Ruby", "Emerald", None]
            reward = random.choice(chest_rewards)

            if reward is None:
                print("Oh no! The chest is empty!")
            else:
                treasures.append(reward)
                print("You opened the chest and found a", reward + "!")

        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")


play_game()
