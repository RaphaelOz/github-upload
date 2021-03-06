from defs import *

def run_spawn(spawn):
    if not spawn.spawning:
        # Get the number of our creeps in the room.
        num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)
        # If there are no creeps, spawn a creep once energy is at 250 or more
        if num_creeps < 0 and spawn.room.energyAvailable >= 250:
            spawn.createCreep([WORK, CARRY, MOVE, MOVE])
        # If there are less than 15 creeps but at least one, wait until all spawns and extensions are full before
        # spawning.
        elif num_creeps < 30 and spawn.room.energyAvailable >= spawn.room.energyCapacityAvailable:
            # If we have more energy, spawn a bigger creep.
            if spawn.room.energyCapacityAvailable >= 350:
                spawn.createCreep([WORK, CARRY, CARRY, MOVE, MOVE, MOVE])
            else:
                spawn.createCreep([WORK, CARRY, MOVE, MOVE])


