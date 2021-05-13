from constants import *
from ui import *

LifeSpan = TextUI(f"lifeSpan : {0}/400", (Width-180, 80), (255, 255, 255))
LifeSpan.fontSize = 20

maxFit = TextUI(f"Fitness: {0}", (Width-180, 120), (255, 255, 255))
maxFit.fontSize = 20

Generation = TextUI(f"Generation: {1}", (Width-180, 160), (255, 255, 255))
Generation.fontSize = 20
