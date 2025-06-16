# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def teleport():
    agent.teleport_to_player()

player.on_chat("tp", teleport)

def turnleft():
    agent.turn(LEFT)
player.on_chat("left", turnleft)


def turnright():
    agent.turn(RIGHT)
player.on_chat("right", turnright)

def moveforward(steps):
    agent.move(FORWARD, steps)
player.on_chat("forward", moveforward)

def movebackwards(steps):
    agent.move(BACK, steps)
player.on_chat("backward", movebackwards)

def attack():
    agent.attack(FORWARD)
player.on_chat("attack", attack)

def jump(steps):
    agent.move(UP, steps)
player.on_chat("jump", jump)

def down(steps):
    agent.move(DOWN, steps)
player.on_chat("down", down)

def attackback():
    agent.attack(BACK)
player.on_chat("attackback", attackback)

def destroyblock():
    agent.destroy(FORWARD)
player.on_chat("break", destroyblock)


def MoveSteps():
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 6)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 3)
    agent.turn_left()
    agent.move(FORWARD, 4)
    agent.turn_right()
    agent.move(FORWARD, 4)

player.on_chat("go", MoveSteps)

def SPAWN():
    player.teleport(pos(0, 0, 0))
player.on_chat("spawn", SPAWN)
