# Car Racing Game with GPIO Integration 🏎️

A thrilling multiplayer car racing game built using Python, Pygame, and GPIO integration. Compete against a friend, collect coins, avoid obstacles, and race to victory with arcade-style controls powered by GPIO buttons.

---

## Features 🚀
- **Multiplayer Gameplay**: Two-player racing action with GPIO button controls.
- **Dynamic Interactions**:
  - Collect coins to increase your score.
  - Avoid obstacles to maintain speed.
  - Grab power-ups to boost your performance!
- **Real-Time Feedback**: Collision detection, scoring updates, and time-based gameplay.
- **Engaging Menus**:
  - Main Menu
  - Instructions Screen
  - Game Time Selector
  - Pause Menu
- **Sound Effects and Background Music**: Immerse yourself with custom audio for collisions, coin collection, and power-ups.
- **Arcade Feel**: Use GPIO buttons for car control to recreate the classic arcade gaming experience.

---

## Components Used 🛠️
- **Python**: Core game logic and GPIO management.
- **Pygame**: Graphics rendering, animations, and sound effects.
- **GPIO Buttons**: Hardware input for car controls.
- **Assets**: Custom images and sound effects for an engaging experience.

---

## How to Play 🎮
1. **Game Objective**:
   - Control your car using GPIO buttons to move up, down, left, or right.
   - Collect coins for points, avoid obstacles, and grab power-ups to gain an edge.
   - The player with the highest score at the end of the game wins.

2. **Controls**:
   - Player 1: GPIO Buttons (UP, DOWN, LEFT, RIGHT).
   - Player 2: GPIO Buttons (UP, DOWN, LEFT, RIGHT).

3. **Winning**:
   - The player with the highest score when the time runs out is declared the winner.
   - If scores are tied, the game goes into extra time.

---

## Installation and Setup 💻
### Prerequisites
- Python 3.7 or higher
- Pygame library
- GPIOZero library
- Raspberry Pi with GPIO buttons connected

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/car-racing-game-gpio.git
