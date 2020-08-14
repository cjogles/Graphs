from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import os

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

# Load world
world = World()
# You may uncomment the smaller graphs for development and testing purposes.
dirpath = os.path.dirname(os.path.abspath(__file__))
map_file = dirpath + "/maps/main_maze.txt"
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# visited room dict
visited = {} 
# add first key:value pair to visited as room and its exits
visited[player.current_room.id] = player.current_room.get_exits()  
# inverse directions
inverse_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'} 
# inverse path
inverse_path = [] 

# this makes sense because we don't want to stop working until the traversal path is full of directions to each room
while len(visited) < len(world.rooms): 
    # if room has not been visited, do the following:
    if player.current_room.id not in visited:
        # add {key: value} pair to visited -> {current room: its exits}
        # Access direction from inverse path last spot
        # Remove the inverse direction from current rooms exits
        visited.update({player.current_room.id: player.current_room.get_exits()})
        inverse_direction = inverse_path[-1]  
        visited[player.current_room.id].remove(inverse_direction)

    # if all paths have been explored, do the following:
    if len(visited[player.current_room.id]) == 0: 
        # get inverse direction from inverse path
        # remove inverse direction from path now that you have it as a variable
        # append inverse direction to traversal path to show you traveled there
        # Move the bot in the inverse direction, because all other paths have been explored
        inverse_direction = inverse_path[-1] 
        inverse_path.pop()
        traversal_path.append(inverse_direction) 
        player.travel(inverse_direction) 

    # else there are other paths to explore, so do the following:
    else: 
        # grab last exit direction from current room
        # remove that room from visited
        # append the last exit direction to the traversal path
        # move the inverse direction to the inverse path
        # move the bot towards the last chosen direction
        direction = visited[player.current_room.id][-1] 
        visited[player.current_room.id].pop()
        traversal_path.append(direction)
        inverse_path.append(inverse_directions[direction])
        player.travel(direction) 

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
