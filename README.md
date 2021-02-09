# Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors game! Read the steps below to learn how to set up your local environment so that you can play.

## Prerequisites

+ Anaconda 3.7+
+ Python 3.7+

## Installation

Fork this [remote repository](https://github.com/zky44/rock-paper-scissors-exercise) under your own control, then clone your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise
```

Use anaconda to create and activate a new virtual environment, perhaps called "my-first-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

From inside the virtual environment, install package dependicies:

```sh
pip install -r requirements/txt
```

> NOTE: if this command throws you an error, make sure you are running it from the repository's root directory where the requirements.txt file exists. Refer back to the initial 'cd' step above

## Setup

The last step before playing the game is to setup a secret file to store your username. In the root directory of your local respository, create a new file called ".env", and updare the contents of the file to specify your desired username:

```sh
USER_NAME ="Tom Brady"

>IMPORTANT: the ".env" file is usally the place for passing configuration options and secret credentials, so as a best practrice we don't upload this file to version control. Make sure that you follow the steps in this [.gitignore](/.gitignore) file)

## Play

To play, run the game script!:

'''py
python game.py




# Extra stuff below

Before running the file, open the requirements.txt file to install the necesarry packages before running the program. 

+ Create a repo for the exercise. I called it "rock-paper-scissors-exercise
+ Create a file in that repo called "game.py" and add the following code inside
    # print("Rock, Paper, Scissors, Shoot!")
+ Create a new project-specific Anaconda virtual environment called "my-game-env". If you already did this, ignore that step
+ Activate the my-game-env
+ Use "python game.py" to run the code