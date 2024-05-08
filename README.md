[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.


Analysis:
% python3 game_driver.py "human" "minimax"
Enter depth for Minimax player: 4
--------
. . . . 
. X O . 
. O X . 
. . . . 
--------
Player 1( X ) move:
Enter col:2
Enter row:3
Invalid move
Enter col:2
Enter row:0
Move: [2, 0] 

--------
. . X . 
. X X . 
. O X . 
. . . . 
--------
Player 2( O ) move:
Move: [1, 0] 

--------
. O X . 
. O X . 
. O X . 
. . . . 
--------
Player 1( X ) move:
Enter col:0
Enter row:0
Move: [0, 0] 

--------
X X X . 
. X X . 
. O X . 
. . . . 
--------
Player 2( O ) move:
Move: [3, 0] 

--------
X X X O 
. X O . 
. O X . 
. . . . 
--------
Player 1( X ) move:
Enter col:3
Enter row:2
Move: [3, 2] 

--------
X X X O 
. X X . 
. O X X 
. . . . 
--------
Player 2( O ) move:
Can't move
Player 1( X ) move:
Enter col:0
Enter row:3
Move: [0, 3] 

--------
X X X O 
. X X . 
. X X X 
X . . . 
--------
Player 2( O ) move:
Can't move
Player 1( X ) move:
Can't move
Player 1 Wins!

1. Simulate four games between yourself and the minimax player on a 4x4 board, with the
depth parameter set to 5, 3, 2, and 1, respectively. I was player 1, minimax was player 2
for all games.
    a. What were the results of each game?
        Depth = 5: I won
                4: I won
                3: I won
                2: I won
                1: I won

    b. Did the minimax player’s moves change when the depth was limited to smaller
    and smaller values?
        No, playing first I made the same 4 moves and the ai reacted the same way everytime.
        Not sure if that is supposed to happen? Feels like player 1 can win every time

    c. What was the average time per move for each of the games? Comment on why
    there is or is not a difference.
        Depth = 5: 0.039
                4: 0.019
                3: 0.008
                2: 0.003
                1: 0.001
        Its faster with a shallower depth because there less tree traversal/simulation
        taking place.


2. Simulate two games between yourself and the minimax player on an 8x8 board, with the
depth parameter set to 5 and 2.
    a. What were the results of each game?
        Depth = 5: I won
                2: I won

    b. Did the minimax player’s moves change when the depth changed?
        Not that I could really tell...

    c. What was the average time per move for each of the games? Comment on why
    there is or is not a difference.
        Depth = 5: 3.5
                2: 0.01


This won every game...

% python3 game_driver.py "human" "minimax"
--------
. . . . 
. X O . 
. O X . 
. . . . 
--------
Player 1( X ) move:
Enter col:2
Enter row:3
Invalid move
Enter col:2
Enter row:0
Move: [2, 0] 

--------
. . X . 
. X X . 
. O X . 
. . . . 
--------
Player 2( O ) move:
Move: [1, 0] 

--------
. O X . 
. O X . 
. O X . 
. . . . 
--------
Player 1( X ) move:
Enter col:0
Enter row:0
Move: [0, 0] 

--------
X X X . 
. X X . 
. O X . 
. . . . 
--------
Player 2( O ) move:
Move: [3, 0] 

--------
X X X O 
. X O . 
. O X . 
. . . . 
--------
Player 1( X ) move:
Enter col:3
Enter row:2
Move: [3, 2] 

--------
X X X O 
. X X . 
. O X X 
. . . . 
--------
Player 2( O ) move:
Can't move
Player 1( X ) move:
Enter col:0
Enter row:3
Move: [0, 3] 

--------
X X X O 
. X X . 
. X X X 
X . . . 
--------
Player 2( O ) move:
Can't move
Player 1( X ) move:
Can't move
Player 1 Wins!