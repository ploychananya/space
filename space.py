import arcade
from model import Ship
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
 
        self.ship = Ship(100,100)
        #self.ship_sprite = arcade.Sprite('images/ship.png')
        self.ship_sprite = ModelSprite('images/ship.png',model=self.ship)
 
 
    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()
 
    def update(self, delta):
        ship = self.ship
 
        ship.update(delta)
        #-------self.ship_sprite.set_position(ship.x, ship.y)
 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()