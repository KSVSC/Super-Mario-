# SuperMario
This is a terminal based Mario game implemented using python. The Libraries used can be found in [Requirements.txt](../master/Requirements.txt)
![Screenshot](demo.png)
## Usage
`Python3 level2.py`

### Game Controls:
a-move left
<br>d-move right
<br>w-jump
<br>q-quit the game

### Game has two levels
##### Level 1: 
There are Two kinds of enemies *(turtle and mushroom)* move linearly with different speeds and characteristics. Also coin_bricks where mario collect coins.
##### Level 2: 
Additionally introduced Boss enemy *(goomba)* which move randomly in air. Can't be killled at one go.Once killed they re-appear at aonther position untill their lives become zero.

#### Scoring:
For collecting coins from coin_bricks: 10.
<br>Killing mushroom: 20
<br>Killing turtle:50
<br>Killing goomba:100

#### Game Objects:
living
<br>|__mario
<br>|__turtle
<br>|__mushroom
<br>|__goomba
<br>|__coin_bricks

#### Extras:
1. Different colors for various objects using colorama.
2. Different sounds for various movements/actions of mario.
3. Enemies with different speeds.

This was implemented as part of SSAD course at IIIT-Hyderabad.
