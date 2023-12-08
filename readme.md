# Unnamed Jeopardy Game
A Jeopardy inspired game built on top of [The Trivia Api](https://the-trivia-api.com/).<br>
This is the [Planning Doc](https://docs.google.com/document/d/1NCdnIhhZvRXedCvAYOJ4_kEHXMFeGlRLU2YLS3yziU0/edit?usp=sharing).

# The Project
We made a Jeopardy inspired but also legally distinct trivia game that has a board of each question sorted into with the harder questions worth more points. It is designed to be a local, same device multiplayer game, (although it does work as a single player trivia game) where players get to pick a question on their turn and then the first person to “buzz in” gets to answer it. If they get it right they get the point value of the question, if they get it wrong they get that point value subtracted from them. Point values also can go into the negatives for an extra bit of risk. The game ends when all questions on the board have been answered, crowning the player with the most points as the winner.
# The Api
We used [The Trivia Api](https://the-trivia-api.com/) in order to get the questions necessary for our game. We sent requests for questions of certain categories and certain difficulties. We also sent requests for all category names to make our game.
# The Library
We used Flask as our Library in order to make the front end web environment. We learned additional skills when it came to web development like skills with CSS. 
# How we used searching and sorting
We used sorting to sort the players in order of score to make a functional leaderboard. We also had a separate list sorted alphabetically of the players to make the turn order. For searching we searched through all the questions for questions of certain point values and category names. We also searched for players by name.
# How we used functional programming
We used functional programming with python’s inbuilt sorting and searching functions in order to search through Objects with keys. Also we used other inbuilt functions like filter to make our job easier. 
# 

