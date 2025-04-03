# Maze Game: Maze Runner

**Team Members:**  
- Muhammad  
- Harshika  

## Introduction
The Maze Game, titled “Maze Runner,” is an interactive educational game designed for children aged 8-10. The game introduces players to problem-solving and critical thinking through an engaging maze navigation activity. The main objective is to navigate through a grid-based maze using directional commands. As players anticipate, plan, and execute strategies, they enhance their critical thinking and sequential reasoning skills.

This project leverages the Django framework for hosting the game as a web application, integrating HTML, CSS, and JavaScript for the game logic and visuals. The game aims to provide a user-friendly interface, captivating visuals, and progressively challenging levels to sustain interest and promote learning.

## Features and Inclusions

### 1. Game Mechanics:
- **Grid-Based Maze:** A visual maze where players control a robot's movements.
- **Command Inputs:** Options to input commands such as “Move Forward,” “Turn Left,” “Turn Right,” and “Execute.”
- **Real-Time Feedback:** The robot’s movements will update on the maze as commands are executed.
- **Collision Detection:** Ensures the robot cannot move into walls or go beyond maze boundaries.

### 2. Game Levels:
- Players must reach a specific endpoint, represented by a flag or treasure, to complete each maze.

### 3. Score and Rewards:
- **Efficiency-Based Scoring:** Points are awarded for completing levels in fewer steps or commands.
- **Achievement System:** Badges or rewards for completing levels or accomplishing specific tasks.

### 4. Interactive Interface:
- **Frontend Design:** Incorporates engaging visuals like colorful grids, animations for robot movement, and sound effects for actions.
- **Hints and Tutorials:** Provides instructions and tips for new players.

## Implementation Plan
The project will be developed in the following stages:

### 1. Backend Development:
- Establish a Django framework to manage web pages, user profiles, and levels.
- Create APIs for efficient communication between the front end and back end.

### 2. Frontend Development:
- Design a responsive and interactive interface using HTML, CSS, and JavaScript.
- Develop the grid-based maze and command input system.

### Further Dreams:
- **User Management:** Allow players to create profiles to track their progress and scores.

## Conclusion
“Maze Runner” is a unique and educational game that combines entertainment with learning, offering children an engaging introduction to coding concepts. By navigating a robot through challenging mazes, players will develop logical thinking, spatial awareness, and problem-solving abilities. The game’s progressive levels and reward system will keep players motivated and entertained throughout their journey.

## Research and Study

### Research Questions
- **RQ1:** How can maze navigation games enhance children’s problem-solving and critical thinking skills?
- **RQ2:** Does a progressive difficulty system improve the learning outcomes in educational games for children?

### Hypothesis
After playing the game for a few rounds, children will improve their ability to navigate complex environments, develop sequential reasoning skills, and boost their spatial awareness.

### Methodology
- **Learning Activity:** Players will interact with the game, using directional commands to guide a robot through a maze.
- **Learning Goals:** Improve spatial awareness, problem-solving, and critical thinking.
- **Learning Skills Supported:** Cognitive development, strategic planning, and basic coding logic.
- **Pre-Post Test:** Players take a pre-test on basic navigation skills and a post-test afterward to measure improvement.
- **Data Collection:** The game will track performance, including time taken to complete levels and the number of steps used.

## References:
1. **Aprily et al. (2023):**
   - **Summary:** The Maze Game supports early childhood writing skills, such as copying symbol shapes, imitating simple words, practicing name writing, and developing fine motor skills. A study highlights that children aged 5-6 who participated in maze activities showed improved literacy skills compared to those who did not. This reinforces the effectiveness of playful learning methods like the Maze Game in fostering writing and literacy skills among young learners.

2. **Wang et al. (2011):**
   - **Summary:** The paper "T-Maze: A Tangible Programming Tool for Children" presents a tool for 5-9-year-olds to create maze maps using tangible programming blocks and sensors. User studies showed that T-Maze is engaging and effectively teaches programming concepts while enhancing logical thinking skills. This supports the maze game concept by demonstrating how gameplay can aid in understanding complex ideas through interactive play.

3. **Blades and Spencer (1987):**
   - **Summary:** This study explored how children aged 4 to 6 navigate mazes using maps. The findings indicate that children can effectively enhance their navigation skills through engaging and fun use of maps.

4. **Levine et al. (2012):**
   - **Summary:** Research examined the connection between puzzle play and spatial skills in 2-year-olds, revealing that early puzzle play has a significant impact on spatial reasoning and problem-solving development.

## Installation

To set up Maze Runner on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mola73/Maze-Game.git

2. ## Activate the Virtual envioronmnet
   environmentname\Scripts\activate.bat
3. ## move to the directory of the app
   cd maze_game

4. ## Run server
 py manange.py runserver

## How to Play
Start the game: Launch the game by running main.py.

Input commands: The game will prompt you to enter commands such as “Move Forward,” “Turn Left,” “Turn Right,” and “Execute.”

Navigate the maze: Use the available commands to move your robot through the maze and reach the endpoint.

Complete levels: Try to complete each level in fewer steps for a higher score.

## Implementation
Game Structure
The game is executed through main.py, which serves as the entry point.

It uses a loop-based gameplay system where players receive commands and navigate a robot through the maze.

Backend Logic
The game is powered by Django to handle the backend, including user profiles, game state, and levels.

Frontend Logic
The game is rendered using HTML, CSS, and JavaScript. The maze and robot’s movements are visually updated in real-time.


Maze-Game/<br>
│<br>
├── main.py                # Main entry point for the game logic.<br>
<br>
├── requirements.txt       # List of Python dependencies required to run the game.<br>
<br>
├── README.md              # Documentation file (this one).<br>
<br>
├── static/                # Directory for static files like CSS, images, and client-side assets.<br>
│   ├── audio/             # Audio files for game sounds.<br>
│   └── images/            # Image files such as robot graphics and other assets.<br>
<br>
├── templates/             # Directory for HTML templates.<br>
│   ├── index.html         # template for displaying the start game interface.<br>
│   └── leaderboard.html    # Template for showing the results after each game.<br>
│   └── myfirst.html       # Main game page in the game<br>
│   └── gamestart.html     # Start page of the game.<br>
<br>
├── maze_runner/           # Core game logic and Django setup.<br>
│   ├── __init__.py        # Game logic functions like generating mazes and handling commands.<br>
│   ├── admin.py           # Admin interface setup for managing game data.<br>
│   ├── apps.py            # App configuration.<br>
│   ├── models.py          # Game models are used to store data, like player scores.<br>
│   ├── urls.py            # URL routing for Django views.<br>
│   ├── utils.py           # Utility functions like handling robot movements.<br>
│   ├── views.py           # Methods for rendering HTML templates and handling game actions.<br>
│   ├── requirements.txt   #List of dependencies for the project<br>
<br>
<br>
└── manage.py              # Django project management script.<br>

