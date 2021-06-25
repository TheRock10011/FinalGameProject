"""
  2Sprite Move With Walls
  3
  4Simple program to show basic sprite usage.
  5
  6Artwork from http://kenney.nl
  7
  8If Python and Arcade are installed, this example can be run from the command line with:
  9python -m arcade.examples.sprite_move_walls
"""

from tkinter.constants import NONE
import arcade
import os
from CreateLevel import CreatingLevel
from Goal import Goal
from PitTile import PitTile

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 568
SCREEN_TITLE = "Escape Artist"

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.LevelIn = 0
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.pit_list = None

        # Set up the player
        self.player_sprite = None
        self.pit_sprite = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        
        self.goal_sprite = arcade.Sprite(":resources:images/items/gold_1.png", 
                                            SPRITE_SCALING)
        
        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/enemies/slimeBlock.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0

        
        self.goal_list.append(self.goal_sprite)


        #Make like this to make new tile
        self.pit_list = arcade.SpriteList()
       
        #Make like this to make new tile



        self.player_list.append(self.player_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list, )
       


        # -- Set up the walls
        # Create a row of boxes
        self.LoadLevel(1)
        

        

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        self.goal_list.draw()
        # Draw all the sprites.
        self.wall_list.draw()
        self.pit_list.draw()
        self.player_list.draw()
        
        

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
           self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
           self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
           self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
           self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
          self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.CheckGameObjects()
       # Call update on all sprites (The sprites don't do much in this
       # example though.)
        self.physics_engine.update()

    def LoadLevel(self , LevelNumberToAdd):
        newLevel = CreatingLevel.WhichLevelToLoad(self.LevelIn)
        self.MakeLevel(newLevel)
        self.LevelIn += LevelNumberToAdd
        #if(self.LevelIn == 3):
        #   self.LevelIn = 1
    #Will Load next level

    def DeleteLevel(self):
        for i in range(len(self.wall_list)):
            self.wall_list.pop()
        for i in range(len(self.pit_list)):
            self.pit_list.pop()


    
    def MakeLevel(self, theLevel):
        self.DeleteLevel()
        #Takes a [] to make level.
        #0 for nothing, 1 for wall, 2 for goal, and 3 for player. 
        TheX = 0 # 20
        TheY = SCREEN_HEIGHT # 14
        
        
        for x in range(len(theLevel)):#130 should be he number
            
            #Makes a wall
            if theLevel[x] == 1:
                wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
                wall.center_x = TheX
                wall.center_y = TheY
                self.wall_list.append(wall)
            #Makes the goal
            if theLevel[x] == 2:
                self.goal_sprite.center_x = TheX
                self.goal_sprite.center_y = TheY
            
                
            if theLevel[x] == 3:
                #Moves The player to the correct location
                self.player_sprite.center_x = TheX
                self.player_sprite.center_y = TheY
            if theLevel[x] == 4:
                pit = arcade.Sprite(":resources:images/items/gold_1.png", 
                                            SPRITE_SCALING)
                pit.center_x = TheX
                pit.center_y = TheY
                self.pit_list.append(pit)
                #self.scene.add_sprite("Pit", pit)
                print("yes")
                
               

            
            TheX += 64
            if TheX > SCREEN_WIDTH :
                TheY -=64
                TheX = 0


    #Will Do this every frame
    def CheckGameObjects(self):
        hitGoal = Goal.checkGoalCollission(self, self.player_sprite.center_x, self.player_sprite.center_y,
        self.goal_sprite.center_x,self.goal_sprite.center_y)

        #hitPit = arcade.check_for_collision_with_list(
        #    self.player_sprite, self.scene.get_sprite_list("Coins")
        #)

        # Loop through each coin we hit (if any) and remove it
        #for coin in coin_hit_list:
            # Remove the coin
         #   coin.remove_from_sprite_lists()
            # Play a sound
          #  arcade.play_sound(self.collect_coin_sound)
       # hitPit = PitTile.CheckIfHitPitTile(self, self.player_sprite.center_x, self.player_sprite.center_y,
        #self.pit_list, self.pit_list.draw_hit_boxes)
        
        #if hitPit:
         #   self.LoadLevel(0)

        if hitGoal:
            self.LoadLevel(1)
        




def main():
   """ Main method """
window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()

if __name__ == "__main__":
   main()