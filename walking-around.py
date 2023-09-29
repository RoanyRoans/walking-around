person = "stillwalking"
print ("you are the circle walking you cant walk over spikes the forest has lots of retracting spikes. get to the cave")
print ("- - -")
print ("- o -")
print ("- - -")
place = "middle"
while person == "stillwalking" :
    move = str(input("move "))
    if move == "a" and place == "middle":
        print ("- - -")
        print ("o - -")
        print ("^ - -")
        place = "left"
    if move == "w" and place == "middle":
        print ("^ o -")
        print ("- - -")
        print ("- - -")
        place = "up"
    if move == "d" and place == "middle":
        print ("- - ^")
        print ("- - o")
        print ("- - -")
        place = "right"
        move = str(input("move "))
    if move == "s" and place == "middle":
        print ("- - -")
        print ("- - - cave")
        print ("- o ^")
        print ("there is a map encarved in the ground")
        place = "down"
        map = "true"
    if move == "d" and place == "left":
        print ("- - -")
        print ("- o -")
        print ("- - -")
        place = "middle"
    if move == "s" and place == "up":
        print ("- - -")
        print ("- o -")
        print ("- - -")
        place = "middle"
    if move == "a" and place == "right":
        print ("- - -")
        print ("- o -")
        print ("- - -")
        place = "middle"
    if move == "w" and place == "down":
        print ("- - -")
        print ("- o -")
        print ("- - -")
        place = "middle"
    if move == "w" and place == "left":
        print ("o ^ -")
        print ("- - -")
        print ("- - -")
        place = "ul"
    if move == "s" and place == "ul":
        print ("- - -")
        print ("o - -")
        print ("^ - -")
        place = "left"
    if move == "a" and place == "down":
        print ("- - -")
        print ("^ ^ -")
        print ("o - ^")
        place = "dl"
    if move == "d" and place == "dl":
        print ("- - -")
        print ("^ ^ -")
        print ("- o ^")
        place == "down"
    if move == "s" and place == "right":
        print ("- - -")
        print ("- - -")
        print ("- ^ o")
        place = "dr"
    if move == "w" and place == "dr":
        print ("- - ^")
        print ("- - o")
        print ("- - -")
        place = "right"
    if move == "d" and place == "up":
        print ("^ - o")
        print ("- ^ ^")
        print ("- - -")
        place = "ur"
    if move == "a" and place == "ur":
        print ("^ o -")
        print ("- ^ ^")
        print ("- - -")
        place == "up"
    if place == "right" and move == "d" and map == "true":
        person = "foundthecave"
print ("congrats you finished ""'Walking Around' the prequel to GOBLINS!")
print("bye bye game over")