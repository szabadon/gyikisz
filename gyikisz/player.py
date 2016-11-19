# - *- coding: utf- 8 - *-
from random import randint


class Player(object):
    def set_attributes(self):
        Player.base_attributes['ugyesseg'] = randint(1,6) + 6
        Player.base_attributes['eletero'] = randint(2,12) + 12
        Player.base_attributes['szerencse'] = randint(1,6) + 6
        Player.actual_attributes['ugyesseg'] = Player.base_attributes['ugyesseg']
        Player.actual_attributes['eletero'] = Player.base_attributes['eletero']
        Player.actual_attributes['szerencse'] = Player.base_attributes['szerencse']

    def check_ugyesseg(self):
        if Player.actual_attributes['ugyesseg']  > Player.base_attributes['ugyesseg']:
            Player.actual_attributes['ugyesseg'] = Player.base_attributes['ugyesseg']
            return "\n "

    def check_eletero(self):
        if Player.actual_attributes['eletero']  > Player.base_attributes['eletero']:
            Player.actual_attributes['eletero'] = Player.base_attributes['eletero']
            return "\n "
        elif Player.actual_attributes['eletero'] <= 0:
            return False

    def check_szerencse(self):
        if Player.actual_attributes['szerencse']  > Player.base_attributes['szerencse']:
            Player.actual_attributes['szerencse'] = Player.base_attributes['szerencse']
            return "\n "
        elif Player.actual_attributes['szerencse'] <= 0:
            return False

    def check_attributes(self): # it doesn't work and I don't understand why
        Player.check_eletero(self)
        Player.check_ugyesseg(self)
        Player.check_szerencse(self)


    base_attributes = {
    'ugyesseg':0,
    'eletero':1,
    'szerencse':0,
    }
    actual_attributes = {
    'ugyesseg':0,
    'eletero':1,
    'szerencse':0,
    }
    bonus_attributes = []

    proba_l = []
    proba_k = {'2': 'Szerencse',
    '75': 'Felelem',
    '151': 'Fajdalom',
    '183': 'Atalakulas',
    '220': 'Ero',
    '335': 'Ugyesseg'}

class Inventory(object):

    bottle =    [] # for storing magic bottle
    dict_sack = {'Kaja':10} # for storing dict format items
    list_sack = ['Lampas']  # for storing items I can put in a list
    equipped = {'páncél': 'Bőrpáncél',
    'fegyver':'Kard',
    'nyakék': 'semmi sem',
    'csizma':'Bőrcsizma',
    'gyűrű':'nincs',
    'sisak':'nincs'} #equipped items

    def set_bottle(self):
        while True:
            print "Melyik tulajdonságodat szeretnéd támogatni egy palack varázsitallal?"
            print "1. Ügyesség\n2. Életerő\n3. Szerencse"
            bottle = raw_input('> ')
            if bottle == '1':
                Inventory.bottle = ['Ugyesseg varazsitala:',2,'ugyesseg']
                break
            elif bottle == '2':
                Inventory.bottle= ['Eletero varazsitala:',2,'eletero']
                break
            elif bottle == '3':
                Inventory.bottle = ['Szerencse varazsitala:', 2, 'szerencse']
                break
            else:
                pass
