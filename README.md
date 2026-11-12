# Treasure Hunt Adventure Game

## Project Description
This is a beginner-friendly Python adventure game where players explore a mysterious island, collect treasures, and try to escape.

## Initial Version
- Players can explore the jungle and discover a golden crown.
- Players can search a cave and find a diamond.
- Players can view their collected treasures.
- Players can escape the island and see their total treasure count.
- The game uses functions, loops, lists, and user input.

## How to Run the Program
1. Download or clone this GitHub repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Type `python3 main.py`.
5. Follow the instructions displayed in the game.



## AI Tool Used
ChatGPT (OpenAI)

## AI Assistance
I used ChatGPT to help improve my Treasure Hunt Adventure game by adding a random treasure feature. I wanted players to discover different treasures instead of finding the same item every time.

## New or Modified Features
- Added the Python random module.
- Created a list of possible treasures.
- Used random.choice() to select a random treasure.
- Updated the game to add the randomly selected treasure to the player's collection.

## Evaluation of AI Output
I accepted ChatGPT's suggestion because it made the game more fun and less predictable. I reviewed the code and tested the new feature by exploring the jungle multiple times. The game worked correctly, and different treasures appeared.

## Assignment 9: Feature Specifications

### Feature 1: Treasure Score System (Manual Development)

**Purpose:** Add a scoring system so players can see the value of their collected treasures.

**Expected Behavior:** Each treasure has a point value. The game calculates the player's total score and displays it when checking treasures or escaping the island.

**Test Cases:**
1. Collect one Diamond worth 50 points. The total score should be 50.
2. Collect two Diamonds. The total score should be 100.

### Feature 2: Mystery Treasure Chest (AI Development)

**Purpose:** Add a mystery chest to make the game more exciting.

**Expected Behavior:** Players can open a mystery chest and randomly receive a treasure or find an empty chest. Any treasure found is added to their collection.

**Test Cases:**
1. If the chest contains treasure, the item should be added to the player's collection.
2. If the chest is empty, the game should display a message and leave the collection unchanged.

## Feature Development Comparison

For Assignment 9, I added two features to my Treasure Hunt Adventure game using two separate GitHub branches.

The first feature was a Treasure Scoring System on the manual-feature branch. I wanted players to see the value of their treasures instead of only seeing how many they collected. I defined point values for five treasures and added calculations that display the total score when checking the collection or escaping the island. I used ChatGPT for coding guidance and implementation examples, then integrated the code and tested it. I confirmed that collecting two Diamonds produced 100 points.

The second feature was a Mystery Treasure Chest on the ai-feature branch. For this feature, ChatGPT generated the code that added a fifth menu option and randomly selected a treasure or an empty chest. The code worked on the first attempt. I tested both outcomes and confirmed that treasures were added correctly while empty chests did not change the collection. I did not need to reject or modify the AI-generated chest logic.

Both approaches helped me understand the game better. I felt more confident about the scoring feature because I worked through its calculations and tested them. The AI feature was faster to implement, but reviewing and testing the code was still important. After merging both branches, I tested the combined game successfully.