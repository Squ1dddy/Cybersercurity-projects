<h1 align="center">🧙‍♂️ Year 11 Assessment Task 2 – Text-Based RPG Adventure Game</h1>
<h3 align="center">Developed using Object-Oriented Programming principles to simulate a dynamic, interactive game environment.</h3>

---

## 🧩 Overview

This project demonstrates a modular, class-driven architecture to build a fully interactive console-based RPG. The game features a multi-room map, character interactions, combat mechanics, inventory management, and puzzle-solving — all designed to showcase core software engineering principles such as encapsulation, inheritance, and polymorphism.

---

## 🧮 Key Systems

- 📁 **Modular File Structure**  
  All classes (Room, Character, Item, Weapon, etc.) are stored in separate files and imported into a clean, readable mainline. This promotes maintainability and separation of concerns.

- 🎒 **Inventory Management**  
  Items are automatically sorted and displayed with relevant attributes (e.g., damage, healing, durability). The system supports equipping weapons and armour, consuming healing items, and inspecting item stats.

- 🧝‍♂️ **Character System**  
  Includes both friendly and hostile characters with custom dialogue, unique items, and combat logic. Enemies have health, damage, and loot; friends can be spoken to, stolen from, or warned about dangers.

- 🕹 **Movement & Map Navigation**  
  Players navigate a multi-room map using directional commands. Rooms are linked logically and include locked areas, puzzles, and hidden items. The system supports dynamic room transitions and state changes.

- 🧠 **Combat & Equipment Mechanics**  
  Implements turn-based combat with weapon durability, damage reduction from armour, and health tracking. Healing items restore HP up to a capped maximum, and weapons degrade over time.

- 🧩 **Puzzle Integration**  
  Puzzle rooms present riddles that must be solved to unlock rewards. Correct answers trigger item drops and room state changes.

- 🧾 **Command System**  
  Players interact using typed commands (e.g., `talk`, `fight`, `inv`, `guess`, `steal`, `help`). Each command triggers a corresponding subroutine, simulating a responsive game loop.

---

## 🧠 Technical Highlights

- **Object-Oriented Design**: Classes for rooms, characters, items, and interactions encapsulate behavior and state.  
- **State Management**: Global variables track health, inventory, equipped items, and game progression.  
- **Input Validation**: All user inputs are sanitized and error-handled to prevent crashes or invalid states.  
- **Dynamic Interactions**: Game logic adapts based on player choices, item usage, and room conditions.  
- **Terminal UX**: Includes spacing, clearing, and formatting to simulate a clean console interface.

---

## 🛠️ Language & Tools

<p align="left">
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
</p>

---

## 🎯 Purpose

This game was developed as part of a Year 11 Software Engineering assessment task. It demonstrates proficiency in Python, object-oriented design, and interactive system development — aligning with the technical expectations of early entry engineering programs and showcasing initiative, creativity, and problem-solving.

---
