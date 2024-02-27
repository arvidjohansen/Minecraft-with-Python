# Install Ursina before using this "pip install ursina"
# Tutorial https://www.youtube.com/watch?v=DHSRaVeQxIk
# What are you doing here?!

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Variables
grass_texture = load_texture("Assets/Textures/Grass_Block.png")
punch_sound = Audio("Assets/SFX/Punch_Sound.wav", loop = False, autoplay = False)
window.exit_button.visible = False
block_pick = 1

# Updates every frame



# Voxel (block) properties
class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = "Assets/Models/Block",
            origin_y = 0.5,
            texture = texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.light_gray,
            scale = 0.5
        )
    
    # What happens to blocks on inputs
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
            
            if key == "right mouse down":
                punch_sound.play()
                destroy(self)


# Increase the numbers for more cubes. For exapmle: for z in range(20)
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))


player = FirstPersonController()
sky = Sky()



app.run()