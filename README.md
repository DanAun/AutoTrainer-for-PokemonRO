# AutoTrainer for Pokemon Revolution Online (PRO)

## Purpose & Features  
This project automates the repetitive leveling process in *Pokemon Revolution Online (PRO)* with a simple AutoTrainer. It offers two training modes:

- **Normal Mode**: Battles wild Pokémon until the primary Pokémon's PP (Power Points) is depleted. PP is defined in `config.ini`.  
- **Switch Mode**: Switches Pokémon upon entering battle. The Pokémon to switch to is specified in the `switch_pokemon` setting in `config.ini`.

---

## Installation & Running  
**Windows:**  
1. Download the latest release for windows from the GitHub release page.  
2. Run the executable to start the AutoTrainer.  

**Linux:**  
1. Download the latest release for linux from the GitHub release page.  
2. Run the executable to start the AutoTrainer.

## Configuration  
The behavior of the AutoTrainer can be customized using the `config.ini` file. Ensure the following variables are set according to your preferences:  
- `power_point`: Determines how many times to use certain moves before stopping training.  
- `switch_pokemon`: Sets the Pokémon to switch to in Switch Training. For example a value of `2` would switch to secondary pokemon.

---
