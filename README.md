# Doom-like Game using Ray Casting and Ray Marching

This project is a Doom-like game where I studied the principles of ray casting and ray marching. The game is built using Python and Pygame, with a focus on rendering a 3D environment using 2D techniques.

## Features
- **Ray Casting**: Utilized to render walls and create the illusion of a 3D environment.
- **Ray Marching**: Techniques for optimizing the distance calculations in the rendering process.
- **Mini-map**: Displays the player's position and view direction in a top-down map format.
- **FPS Display**: Real-time display of the game's frame rate.

## Technologies Used
- **Python**
- **Pygame**: Used for game development, graphics, and handling player input.
- **Ray Casting Techniques**: Core method for creating the 3D visuals in a 2D plane.

## Game Structure
The project is divided into the following files:
- **main.py**: The main game loop that handles player movement, drawing, and screen updates.
- **map.py**: Contains the map data and processes it into a format suitable for rendering.
- **ray_casting.py**: Handles the ray casting logic to calculate distances and render the game environment.
- **drawing.py**: Manages the rendering of the game world, mini-map, and FPS display.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame library

You can install Pygame using pip:
```bash
pip install pygame
