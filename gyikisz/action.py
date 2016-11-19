# - *- coding: utf- 8 - *-
from random import randint
from player import Player, Inventory


class Action(object):

    def end_turn(a):
        y = raw_input('> ')
        return a

    def dice_3(self,a,b,c):
        x = raw_input('> ')
        y = randint(1,6)
        if y < 3:
            return a
        elif y < 5:
            return b
        else:
            return c

    def act_att_change(self,a,b):
        Player.actual_attributes[a] += int(b)

    def base_att_change(self,a,b):
        Player.base_attributes[a] += int(b)

    def bonus_att_change(self,a):
        x = Player.bonus_attributes
        x.append(a)
        y = raw_input('> ')

    def bonus_att_change_rem(self,a):
        x = Player.bonus_attributes
        x.remove(a)

    def check_att(self,a,b,c,d):
        x = raw_input('> ')
        if Player.actual_attributes[a] > int(b):
            return c
        else:
            return d

    def check_equipped(self,item_type,item,yeah,nope):
        x = raw_input('> ')
        if Inventory.equipped[item_type] == item:
            return yeah
        else:
            return nope

    def check_bonus_att(self,bonus,yeah,nope):
        x = raw_input('> ')
        if bonus in Player.bonus_attributes:
            return yeah
        else:
            return nope

    def check_item_list_sack(self,item,yeah,nope):
        x = raw_input('> ')
        if item in Inventory.list_sack:
            return yeah
        else:
            return nope

    def check_item_dict_sack(self,item,yeah,nope):
        x = raw_input('> ')
        if item in Inventory.dict_sack:
            if Inventory[item] > 0:
                return yeah
        else:
            return nope

    def item_equipped(self,type,item):
        Inventory.equipped[type] == item
        y = raw_input('> ')

    def item_dict_sack(self,item_type,amount):
        Invenory.dict_sack[item_type] == amount
        print "\nZsákodban most %r %s van!\n" %(amount,item_type)
        y = raw_input('> ')

    def item_dict_sack_neg(self,item_type,amount_to_subtract):
        Inventory.dict_sack[item_type] -= int(amount_to_subtract)

    def item_list_sack(self,item):
        x = Inventory.list_sack
        x.append(item)
        print "\nEgy %s került a zsákodba!\n" % (item)
        y = raw_input('> ')

    def rem_item_list_sack(self,item):
        x = Inventory.list_sack
        x.remove(item)

    def life(self,a,b):
        x = raw_input('> ')
        if randint(2,12) > Player.actual_attributes['eletero']:
            return b
        else:
            return a

    def luck(self,a,b):
        x = raw_input('> ')
        if randint(2,12) > Player.actual_attributes['szerencse']:
            print "Balszerencse ért!"
            y = raw_input('> ')
            return b
        else:
            print "Most melléd állt a szerencse!"
            y = raw_input('> ')
            return a

    def agi(self,a,b):
        x = raw_input('> ')
        if randint(2,12) > Player.actual_attributes['ugyesseg']:
            print "Nem voltál elég ügyes!"
            y = raw_input('> ')
            return b
        else:
            print "Ezaz! Sikerült!"
            y = raw_input('> ')
            return a

    def choice(self,a,b):
        while True:
            answer = raw_input('> ')
            if answer == a:
                break
            elif answer == b:
                break
            elif answer == 'help':
                print """
kilepes: Kilépés a játékból\neszem: Bekapsz pár falatot
iszom: Meghúzod a varázsitalos palackot
                """
            elif answer == 'kilepes':
                print "Viszlát kalandor!"
                exit(0)
            elif answer == 'eszem':
                if Inventory.dict_sack['Kaja'] > 0:
                    Inventory.dict_sack['Kaja'] -= 1
                    if Player.actual_attributes['eletero'] < Player.base_attributes['eletero']:
                        Player.actual_attributes['eletero'] += 1
                        print "Egy kicsit életre kaptál... (Életerő +1)"
                    else:
                        print "Ez a falat jól esett!"
                else:
                    print "Nincs mit enned..."
            elif answer == 'iszom': #ha ez működik, akkor erre nagyon büszke leszek!
                if Inventory.bottle[1] > 0:
                    x = Inventory.bottle[2]
                    print "Nagyokat kortyolsz a varázsitalodból..."
                    Player.actual_attributes[x] += 1
                    Inventory.bottle[1] -= 1
                else:
                    print "Varázsitalod elfogyott!"
            else:
                print "Írd be a választásodhoz tartozó kódot!"
                pass
        return answer

    def choice_3(self,a,b,c):
        while True:
            answer = raw_input('> ')
            if answer == a:
                break
            elif answer == b:
                break
            elif answer == c:
                break
            else:
                print "Írd be a választásodhoz tartozó kódot!"
                pass

    def choice_4(self,a,b,c,d):
        while True:
            answer = raw_input('> ')
            if answer == a:
                break
            elif answer == b:
                break
            elif answer == c:
                break
            elif answer == d:
                break
            else:
                print "Írd be a választásodhoz tartozó kódot!"
                pass

    def battle(self,a,b,enemy_name, enemy_left, next):
        Enemy = {'ugyesseg':a,'eletero':b}
        if Inventory.equipped['sisak']=='Sog':
            Enemy['eletero'] -= 2
        while Enemy['eletero'] > 0 or Player.actual_attributes['eletero'] > 0:
            print "Életerőd: %r\n%s életereje:%r\n" % (Player.actual_attributes['eletero'],
                                                        enemy_name,
                                                        Enemy['eletero'])
            y = raw_input('> ')
            e_attack = Enemy['ugyesseg'] + randint(2,12)
            p_attack = Player.actual_attributes['ugyesseg'] + randint(2,12)
            print "Támadás!"
            if e_attack < p_attack:
                print "Megsebezted ellenfeled!"
                Enemy['eletero'] -= 1
                if Enemy['eletero'] <= 0:
                    if enemy_left > 0:
                        break
                    else:
                        return next
            elif e_attack > p_attack:
                print "%s megsebzett téged!" % (enemy_name)
                Player.actual_attributes['eletero'] -= 1
                if Player.actual_attributes['eletero'] <= 0:
                    return 'x'
            else:
                print "Döntetlen!"


    def add_saman_proba(self,a):
        Player.proba_l.append(a)

    def print_saman_proba_k(self):
        y = raw_input('> ')
        if len(Player.proba_l) < 3:
            for i in Player.proba_k:
                if Player.proba_k[i] not in Player.proba_l:
                    print Player.proba_k[i],' próbája: ',i
        elif len(Player.proba_l) >= 3:
            print "Sikerült teljesítened a Sámán feltételeit!\n\t\t 214"

    def saman_felajanlas(self,next):
        while y not in Inventory.list_sack:
             for i in Inventory.list_sack:
                 print i
             print "Válassz valamit a fenti listából..."
             y = raw_input('> ')
        Inventory.list_sack.remove(y)
        return next

    def empty_sack():
        Inventory.list_sack = []
        Inventory.dict_sack = {}
        Inventory.bottle = []

    def battle_sting(self,a,b,enemy_name,sting_t,sting_f):
        Enemy = {'ugyesseg':a,'eletero':b}
        sting = False
        if Inventory.equipped['sisak']=='Sog':
            Enemy['eletero'] -= 2
        while Enemy['eletero'] > 0 or Player.actual_attributes['eletero'] > 0:
            print "Életerőd: %r\n%s életereje:%r\n" % (Player.actual_attributes['eletero'],
                                                        enemy_name,
                                                        Enemy['eletero'])
            y = raw_input('> ')
            e_attack = Enemy['ugyesseg'] + randint(2,12)
            p_attack = Player.actual_attributes['ugyesseg'] + randint(2,12)
            print "Támadás!"
            if e_attack < p_attack:
                print "Megsebezted ellenfeled!"
                Enemy['eletero'] -= 1
                if Enemy['eletero'] <= 0:
                    if sting == True:
                        return sting_t
                    else:
                        return sting_f
            elif e_attack > p_attack:
                print "%s megsebzett téged!" % (enemy_name)
                Player.actual_attributes['eletero'] -= 1
                sting = True
                if Player.actual_attributes['eletero'] <= 0:
                    return 'x'
            else:
                print "Döntetlen!"
