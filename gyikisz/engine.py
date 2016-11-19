# - *- coding: utf- 8 - *-
import scene
from maaap import Map
from player import Player, Inventory
from sys import exit

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        player.set_attributes()
        print """
A sors kockái döntöttek!\nÜgyesség:%r\nÉleterő:%r\nSzerencse:%r\n
""" % (player.base_attributes['ugyesseg'],player.base_attributes['eletero'],player.base_attributes['szerencse'])
        player_inventory.set_bottle()
        raw_input("Készen állsz kalandor?\n> ") # just for fun and to give a feeling of starting something
        current_scene = self.scene_map.opening_scene() #
        turn = 0 # counting the turns, I need this for debugging and testing
        while player.actual_attributes['eletero'] > 0:
            turn += 1 #adds one to turn every cicle
            print "\n[turn%r]" % (turn) # prints out the turn
            print "\n--------------------------------------------------------------------------------"
            print "Ügyesség: %r/%r Életerő: %r/%r Szerencse: %r/%r " % (player.actual_attributes['ugyesseg'],player.base_attributes['ugyesseg'],player.actual_attributes['eletero'],player.base_attributes['eletero'],player.actual_attributes['szerencse'],player.base_attributes['szerencse'])
            print "Zsákod tartalma: %s %s %s" % (player_inventory.bottle[0:2], player_inventory.dict_sack, player_inventory.list_sack) #weird displaying
            print "Tested %s fedi, nyakadban %s lóg, kezedben %s leng." % (player_inventory.equipped['páncél'],player_inventory.equipped['nyakék'],player_inventory.equipped['fegyver']) #weird displaying
            print "--------------------------------------------------------------------------------"
            next_scene_name = current_scene.enter()
            player.check_ugyesseg()
            player.check_szerencse()
            player.check_eletero()
            current_scene = self.scene_map.next_scene(next_scene_name)
        x = Death()
        x.kampec()

class Death(object):

    def kampec(self):
        x = scene.Scene_X()
        return x.enter()

player = Player()
player_inventory = Inventory()
a_map = Map('0')
a_game = Engine(a_map)
a_game.play()
