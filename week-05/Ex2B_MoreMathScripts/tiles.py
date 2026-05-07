# You are going to tile a room whose dimensions are length by width feet. 
# There are twelve tiles per box, each 1 foot by 1 foot.
# How many boxes of tiles do you need? You can only buy full boxes, not a partial box. 
# You also want to buy at least 10% more tiles than you need in order to handle chips, 
# breakage, and mess-ups. How many total boxes will you buy?

#TILES
import math
#Room dimensions
Length = 10
Width = 10

#Total Area
Area = Length * Width

# adding 10%
Tiles_needed = Area * 1.10

# each box has 12
boxes_needed = math.ceil(Tiles_needed / 12)

#RESULTS
print(f"You will need to buy {boxes_needed} boxes of tiles.")