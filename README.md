# Software-Engineering-Project

-----------------------------------------
|     Team members    |  Github         |
-----------------------------------------
| Parker Sutterfield  |  psutterf       |
-----------------------------------------
| Cade Melton         |  caderade-r     |
-----------------------------------------
| Jayden Blair        |  Jaybobjr       |
-----------------------------------------
| Garrett Hernandez   |  garretth1098   |
-----------------------------------------



Install script found in install directory; in order to run:

```
$bash setup.bash
```

another script is found to verify install and check if VM is ready


Python Depandancies used: 
-   Pillow; Python Imaging Library(PIL)        main.py
-   psycopg2                                   db.py
-   tkinter                                    playerAction.py, PlayerEntry.py
-   pygame                                     AudioManager.py 



HOW TO RUN:

```
python3 main.py
```

- This will open the player entry screen where you will enter the hardware ID and player names 
- in a second terminal window run the command:

```
python3 trafficGenerator.py
```

- this will prompt you to manually enter the hardware IDs again of two players from each team
- it will then print the message "waiting for start from game_software"
- this needs to be done BEFORE pressing start game
- when the player action screen appears it will send a start code to the traffic generator which then simulate the gameplay
