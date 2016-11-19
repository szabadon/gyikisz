# - *- coding: utf- 8 - *-
from sys import exit
from action import Action

class Scene(object):

    def enter(self):
        print "Ez az alap "
        exit(1)

class Scene_X(Scene):

    def enter(self):
        print "\n\t\t\t**************\n\t\t\t**Meghaltál!**\n\t\t\t**************\n"
        exit(1)

class Hattertortenet(Scene):

    def enter(self):
        print """
Az Osztriga-öböl nyugodt kis halászfalu úgy harminc kilométernyire a hírhedt
Feketehomok Kikötőtől délre, a tengerpart mentén. Mivel ez a hely egy hosszú
félsziget végében található, melyet csupán egy meredek, kanyargós ösvényen lehet
elérni, a halászok és asszonyaik arra kényszerültek, hogy az egyszerű emberek
életét éljék itt, távol az ország szörnyekkel és varázslatokkal teli életétől.
Fangtól déli irányban elindulva úgy döntesz, hogy néhány napos pihenőt tartasz,
és mivel nem ismersz nyugalmasabb helyet az Osztriga-öbölnél, lovadat gyorsabb
ügetésre ösztökéled a part mentén.
A faluban lakik régi barátod, Mungo, akit évek óta nem láttál. Két nap múlva egy
sziklaszirthez érsz, ahonnan rálátni az Osztriga-öbölre. Gyönyörű, napfényes
reggel van, körös-körül minden nyugodt. Azóta, hogy utoljára itt jártál, semmi
sem változott. A kőházak kis csoportja a sziklák lába és a móló közé ágyazódott
be, ahol tucatnyi halászhajó ring a vízen. Leszállsz a lovadról, elindulsz
a kanyargós ösvényen, le a faluba. Először síró asszonyokkal találkozol. Amint
közelebb akarsz menni hozzájuk, férfiak ugranak elő a házakból, és feléd
tartanak. Egyikük régi jó barátod, Mungo. Széltől cserzett arca haragos..."""
        y = raw_input('> ')
        print """
Meglepetten néz rád, de nem köszönt. Elmeséli, milyen szomorúság érte a faluját.
Mivel nincs aranyuk, sem egyéb kincsük, az Osztriga-öböl lakói soha nem
érdekelték igazán a külső támadókat. Néhány hete azonban, amikor a férfiak kint
voltak a vízen, a Tűzszigeti Gyíkemberek zsákmányul ejtették néhány hajójukat,
és több fiatalembert elraboltak. Mungo szerint a foglyok biztosan a Tűz-szigeten
raboskodnak, és vasra verve dolgoznak az aranybányában. Az emberrablás óta két
ember őrködik a faluban, míg a többiek halásznak. Ennek ellenére a Gyíkemberek
ma reggel ismét támadtak, lefegyverezték az őröket, és magukkal vittek még egy
csapat fiatalembert. Mungo közli veled, hogy nekivág a tengernek, egyedül megy a
Tűz-szigetre, mivel a többiek félnek. Némán figyel, hogy vele tartasz. Hátba
vereget, és hálája jeléül kezet ráz veled. A szegény halászfalu lakói egy
pillanatra elfelejtik a bánatukat, és köréd sereglenek, hogy köszönetet
mondjanak neked. Mungo ezután meghív, hogy vacsorázz vele, és pihenj egy keveset,
mert az út a Tűz-szigetre órákig tar majd... """
        y = raw_input('> ')
        print """
A fenséges lakoma közben, ahol főtt homárt és salátát szolgálnak fel nektek,
megbeszélitek a haditervet.
Mungo elmondja, nem hiszi, hogy laknának emberek a Tűz-szigeten, bár ismeretei
elég hiányosak. Amit tud, az mind a partvidék többi településének halászai
között terjengő szóbeszéd. Azt is tudni vélik, hogy a Tűz-sziget annak idején
börtönsziget volt, amelyet fizetett Gyíkemberek őriztek. Az Olaf herceg eléggé
hiábavaló kísérlete volt annak érdekében, hogy megszabadítsa országát a nem-
kívánatos elemektől. A jó herceg azonban hamarosan rájött, hogy egyszerűbb lenne
áttelepíteni hűséges alattvalóit a Tűz-szigetre, és a szárazföldön hagyni
a gazembereket - ugyanis túl sok volt belőlük. Feladta hát eredeti tervét, és
felszámolta a börtöntelepet. Amikor a Gyíkemberek nem kaptak fizetést, bosszút
álltak a foglyokon, és a sziget egy királynak kikiáltott Gyíkember-börtönőr
rémuralma alá került. A foglyoknak megparancsolták, hogy kutassanak arany után
a föld mélyében a Gyíkkirály számára. Éheztették őket, és kegyetlenül bántak
velük... """
        y = raw_input('> ')
        print """
Sokan közülük meghaltak, és ez lehet az oka, hogy a Gyíkkirály most újabb
rabszolgák után küldi az embereit. Tudni vélik azt is, hogy a király, hatalmát
megerősítendő, voodoo-val (törzsi varázslatokkal) és fekete mágiával kezdett
foglalkozni. Genetikai kísérleteket is folytat, hogy kifejlesszen egy új
Gyíkember-fajt, amely legyőzhetetlen lesz. A legtöbb kísérlet azonban balul sült
el. Torzszülöttek láttak napvilágot, és veszélyes folyadékok kerültek
a csatornarendszerbe. Ez rettenetes következményekkel járt. A sziget növényzete
és állatvilága megváltozott: emberevő növények és óriás szörnyek fejlődtek ki.
Néhány fogolynak sikerült tutajon elmenekülnie a szigetről - ezeket a halászok
mentették meg és vitték ki a szárazföldre. De hogy mi történt az elmúlt néhány
év során, azt senki sem tudja. A minapi támadásokig a Tűz-szigetről már-már meg
is feledkeztek. Kétséges, hogy sikerül-e megölnöd a Gyíkkirályt és megmentened
az elrabolt áldozatokat, de meg kell próbálnod a lehetetlent.
Felállsz, és lesétálsz Mungóval a kikötőbe, ahol beszálltok barátod kis halász-
bárkájába. Eloldod a csónakot, és az éljenző tömeget nézve azon gondolkozol,
vajon visszatérsz-e ide valaha is?"""
        y = raw_input('> ')
        return '1'

class Scene_1(Scene):

    def enter(self):
    	print """
Nem múltak el nyomtalanul azok az évek, amelyeket Mungo az Osztriga-öböl halászai
között töltött - bátor hajós vált belőle. Ügyesen felhúzza a vitorlát, és nyugat
felé kormányozza a kis bárkát az ezüstkék tengeren. A szárazföld hamarosan elmarad
mögöttetek a távolban. Hátradőlsz a fedélzeten, és nyugodtan sütkérezel a délutáni
napsütésben. A bárka fara felől éles füttyentést hallasz, mintha a kormánylapát
csikorogna - Mungo füttyentett egy sirálynak. A régi szép időkre gondolsz,
amelyeket Mungóval töltöttél, ezzel a jókedvű, mindig segítőkész baráttal. Hinni
sem akarod, hogy annyi rossz van azon a földön, ahol olyan ember él, mint Mungo.
Ahogy múlnak az órák, beszélgetéssel és nevetgéléssel próbálod meg elhessegetni
a közelgő veszélyt. Mungo mindig is nagy mesélő hírében állt, most is arról kezd
beszélni neked, milyen is volt az, amikor az apja vándorcirkusszal járta a
vidéket. - Hatalmas ember volt, akár egy hegy - mondja nevetve-, a nézőközösségért
mindenre képes volt. Trollokkal birkózott, engedte, hogy elefántok tapossanak rá,
sőt még a Gyilkos Méhnek is hagyta, hogy megcsípje! Kemény fickó volt; végül is
északon lelte halálát. A cirkusszal Fangban léptek fel a Bajnokok Próbája
ünnepségein, és az apám elhatározta, hogy ő is benevez. Elindult a Halállabirintusban,
ahonnan sajnos sohasem került elő. Túl öreg volt már az ilyesmihez, de nem akadt
senki, aki ezt megmondta volna neki. De hát végül is megpróbálta! """
        y = raw_input('> ')
        print """
Mungo már éppen belekezdene a következő történetbe, de felugrik, és
torkaszakadtából elordítja magát: - Föld! - Úgy hangzik ez, mintha egy hajó
legénységével akarná közölni az örömhírt. Oda nézel, ahová a barátod mutat, és a
távolban a Tűz-szigetet pillantod meg. Hatalmas zöld párnaként lebeg a víz színén,
amelyből egy hegy nyúlik a magasba. Lágyan gomolygó füst száll fel a tetejéből.
Tűzhányó ez, és haragosan kitörni készül.
Mungo a bárkát egy keskeny kis öbölbe irányítja a sziget keleti csücskében,
abban reménykedve, hogy meg tud bújni a magas sziklák között. Mindketten
felveszitek a hátizsákotokat, és kiugrotok a bárkából, hogy elinduljatok
felkutatni a Gyíkkirályt.

Ha végig akarod cserkészni a balra lévő parti sziklákat a kis öbölben: 24

Ha át akarsz mászni a jobbra magasodó parti sziklákon az öböl másik oldalára: 33

"""
        this_scene = Action()
        return this_scene.choice('24','33')

class Scene_2(Scene):
    def enter(self):
        print """
A Sámán három dióhéjat tesz le eléd a földre, és közli, hogy az egyik alatt egy
gyöngyszemet rejtett el. Meg kell mondanod, melyik alatt van.
\nTedd próbára a Szerencsédet!\n"""
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.luck('358','326')

class Scene_3(Scene):
    def enter(self):
        print"""
A törpék, felbátorodva a lehetőségtől, hogy esetleg kiszabadulhatnak,
kalapácsaikkal a segítségedre sietnek, hogy végezni tudj az őrrel.
Az ütések zuhatagától a Gyíkember a Törpék éljenzése közepette a földre rogy.
A Törpék leverik a lábukról béklyóikat, köréd sereglenek, hogy köszönetet
mondjanak neked, és isznak a vödörből, hogy szomjukat oltsák.
Elmondod nekik, hogy meg akarod ölni a Gyíkkirályt, ők pedig valamennyien
felajánlják segítségüket. Megkérdezed, hol van a többi fogoly; erre ők azt
válaszolják, hogy valamennyien egy mélyebben fekvő tárnában vannak. Megkéred
a Törpéket, hogy vezessenek oda, amilyen gyorsan csak lehet."""
        answer = raw_input('> ')
        return '161'


class Scene_4(Scene):

    def enter(self):
        print """
A vágat fokozatosan kiszélesedik, és klausztrofóbiád csökken.
Nemsokára útelágazáshoz érsz.

Ha balra akarsz menni: 101

Ha jobbra akarsz menni: 44
"""
        this_scene = Action()
        return this_scene.choice('101','44')

class Scene_5(Scene):

    def enter(self):
        print """
Kardodat beledöföd a Csörgőkígyó sötét fészkébe, és fémesen csengő hangot hallasz.
Teljesen megfeledkezel a Csörgőkígyóról, és kardoddal megpróbálod kipiszkálni a
lyukból azt a fémtárgyat, amelybe kardod beleütközött. A nap fényében megcsillan
egy csodálatos, aranyló szárnyú sisak.

Ha a sisakot a fejedre akarod tenni: 292

Ha inkább nem nyúlsz a sisakhoz,
és óvatosan elindulsz lefelé a szurdokban, nyugati irányban: 119
"""
        this_scene = Action()
        return this_scene.choice('292','119')

class Scene_6(Scene):

    def enter(self):
        print """
Amint megiszod az italt, szédülni kezdesz, de tested erővel telik meg.

Nyertél 1 Ügyesség és 2 Életerő pontot, mert ittál a varázspatak vizéből.

Felfrissülve továbbmész a legtávolabbi ajtóhoz... """
        this_scene = Action()
        this_scene.act_att_change('eletero','2')
        this_scene.act_att_change('ugyesseg','1')
        return '353'

class Scene_7(Scene):

    def enter(self):
        print """
Amint nyugat felé haladsz, észreveszed, hogy a talaj egyre nedvesebb, süppe-
dősebb lesz. Nemsokára bokáig gázolsz a vízben. A fák egyre ritkulnak, és
egyszer csak azon veszed észre magad, hogy sűrű, fekete ingoványban gázolsz.
Amerre a szem ellát, mocsár vesz körül. Hirtelen cuppogó hangot hallasz a há-
tad mögül, és meglepetten látod, hogy egy furcsa teremtmény rohan el melletted.
Kicsiny testét zöld hüllőpikkelyek borítják. Két karja hosszú, a földet verdesi,
úszóhártyás lábával fürgén mozog a mocsár felszínén. Ügyet sem vet rád.

Ha meg akarod szólítani ezt a teremtményt: 317

Ha inkább folytatod fárasztó utadat nyugati irányba: 158
"""
        this_scene = Action()
        return this_scene.choice('317','158')

class Scene_8(Scene):

    def enter(self):
        print """
Elérsz a kanyarig és lenézel a folyosóra, melyet egy ajtó zár le.
Ösztönöd azt súgja, hogy felmenj a csigalépcsőn... """
        y = raw_input('> ')
        return '82'

class Scene_9(Scene):

    def enter(self):
        print """
Előkapod a vasrudat a hátizsákodból, és beledöföd a félelmetes krokodil pofájába.
Felpeckelt szájával a vadállat tehetetlen, így nyugodtan elhajózhatsz a tutajodon.
"""
        y = raw_input('> ')
        return '390'

class Scene_10(Scene):

    def enter(self):
        print """
Olyan sötét van a fúrólyukban, hogy még a kinyújtott kezedet sem látod.

Ha továbbra is erre akarsz lefelé kúszni: 34

Ha inkább visszafordulsz és
a vájatban mész tovább a kézikocsi mellett elhaladva: 321
"""
        this_scene = Action()
        return this_scene.choice('34','321')

class Scene_11(Scene):

    def enter(self):
        print """
A Törpék már elintézték a másik Orkot, és most a segítségedre sietnek.
Az Orkot egykettőre ártalmatlanná teszik. """
        y = raw_input('> ')
        return '121'

class Scene_12(Scene):

    def enter(self):
        print """
Sűrű dzsungelen hatolsz át, amikor hirtelen egy emberi csontvázba botlasz.
A kukacok és férgek már rég felfalták a testet, de a megmaradt ruhákból arra
következtetsz, hogy menekülő fogoly volt az illető férfi vagy nő. Kíváncsi vagy,
vajon hogyan halt meg. Egy kisbalta és egy tekercs kötél hever a csontváz mellett.
Ezeket a tárgyakat magadhoz veszed, mielőtt folytatnád utadat északnyugat felé.
"""
        this_scene = Action()
        this_scene.item_list_sack('Balta')
        this_scene.item_list_sack('Tekercskötél')
        return '105'

class Scene_13(Scene):

    def enter(self):
        print """
A szürkületben nem veszed észre a Mérges Pókot, amint a banánfa törzsén
mászik lefelé. Rátenyerelsz dagadt, szőrös testére, és még mielőtt ráesz-
mélnél mi történt, a pók megmar.\nVesztesz 3 Életerő pontot.\n
A sokkhatástól összecsuklasz. """
        this_scene = Action()
        return this_scene.agi('381','118')

class Scene_14(Scene):

    def enter(self):
        print """
A folyó lágyan hömpölyög az alacsony hegyek között. Amint kijutsz a következő
kanyarból, a bal part közelében néhány sárkunyhót látsz. A part felé veszed az
irányt, de gondosan ügyelsz rá, hogy senki se vegyen észre a kunyhók lakói közül.
A partra ugrasz, és a fák között kúszva megközelíted a kunyhókat. Amíg az egyik
kunyhó mögött lapulsz, két magas, páncélt viselő, hüllőhöz hasonló lényt látsz,
kezükben korbács és görbe kard; ők a Gyíkemberek! """
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.check_bonus_att('uzenet','63','270')

class Scene_15(Scene):

    def enter(self):
        print """
Szervezeted elég erős, hogy legyőzze a betegséget, és lázad nemsokára elmúlik.
Eloldod tutajodat, és elindulsz a folyón fölfelé... """
        y = raw_input('> ')
        return '379'

class Scene_16(Scene):

    def enter(self):
        print """
Leveszed a hátizsákodat, és ledobod a fa üregébe. Gyorsan bemászol, és vérezve,
kimerülten nyúlsz el a földön. Meg sem moccansz. 1 Életerő pontot vesztesz."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-1')
        y = raw_input('> ')
        print """
A következő pillanatban meghallod a melletted elfutó Fejvadászok dübörgő lépteit.

Tedd próbára a Szerencsédet!"""
        return this_scene.luck('380','313')

class Scene_17(Scene):

    def enter(self):
        print """
Lefelé indulsz a dombról és balra fordulsz, a tűzhányó irányába... """
        y = raw_input('> ')
        return '303'

class Scene_18(Scene):

    def enter(self):
        print """
A dió és a szamóca kitűnő. A pigmeusok tudják, mi a finom eledel a dzsungelban.
\nNyertél 2 Ügyesség pontot.\n
Az egyik hirtelen élesen felordít, erre valamennyien eltűnnek a buja bozótban.
Megkönnyebbülten sóhajtasz fel, és folytatod utadat nyugat felé..."""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg','2')
        y = raw_input('> ')
        return '7'

class Scene_19(Scene):

    def enter(self):
        print """
A vágatnak ez a része olyan, mintha rég nem használták volna. A mennyezetet
tartó gerendák megrepedeztek, és úgy látod, életveszélyesek. Egy függőlegesen
lefelé haladó tárna széléhez érsz, mely mögött nem sokkal véget ér a vágat.
Nincs létra, amelyen lemászhatnál. """
        y = raw_input('> ')
        this_scene = Action()
        this_scene.check_equipped('csizma','Vörös bőrcsizma','392','246')

class Scene_20(Scene):

    def enter(self):
        print """
Csizmáddal széttaposod a másik tojást, mielőtt elindulnál felfelé a tűzhányó
oldalában, mert a kénmedencén nem tudsz keresztülmenni."""
        y = raw_input('> ')
        return '178'

class Scene_21(Scene):

    def enter(self):
        print """
Visszadugod kardodat a hüvelyébe, és lesétálsz a tópartra.
\nHa még most is inni akarsz a vízből: 92

 \nHa inkább továbbmész nyugatnak: 222
 """
        this_scene = Action()
        return this_scene.choice('92','222')

class Scene_22(Scene):

    def enter(self):
        print """
A Gyíkkirály úgy megijed, hogy eldobja a lángpallosát. Odaugrasz és felkapod,
hogy saját pusztító fegyverével támadj rá. \nNyertél 2 Ügyesség pontot.\n
A Király képtelen védekezni, de a Goncsong végül is arra kényszeríti, hogy harcoljon...
"""
        this_scene = Action()
        return this_scene.battle(10,15,'Gyíkkirály',0,'153')

class Scene_23(Scene):

    def enter(self):
        print """
Felkapod a Gyíkember vízzel teli vödrét, hogy elvidd a szomjazó raboknak.
A vágatban addig mész, míg az kamrává nem szélesedik...
"""
        y = raw_input('> ')
        return '223'

class Scene_24(Scene):

    def enter(self):
        print """
Egykettőre az aranysárga homokparton teremsz. Néhány szikla áll ki a tengerből,
és a part végében egy kis fehér kőházikót pillantasz meg. Elhagyatottnak látszik.
A teteje beszakadt, a ház roskadozik. A homokban cikcakkban egymást keresztező
hosszú nyomokat fedezel fel.

Ha a part mentén el akarsz menni a házhoz: 211

Ha inkább visszamászol a sziklákon az öbölbe,
és azon át a parton keresztül a másik öbölbe: 33
"""
        this_scene = Action()
        return this_scene.choice('211','33')

class Scene_25(Scene):

    def enter(self):
        print """
Három újabb Grannitusz rohamoz meg, hogy a lábadba mélyessze a fogát. Át tudod
ugrani őket, de az elsőt már nem tudod lerázni - fogával a lábszáradba csimpasz-
kodik. Rácsapsz a kardoddal... """
        this_scene = Action()
        return this_scene.battle(4,3,'Grannitusz',0,'85')

class Scene_26(Scene):

    def enter(self):
        print """
Kinyitod a zsákot, de az üres; koromfekete belül. Úgy döntesz, hogy egy követ
dobsz bele, aztán meglátod, mi történik. A kő eltűnik a zsákban, és az egyáltalán
nem lesz nehezebb tőle. A Feneketlen Zsákot tartod a kezedben.
\nNyertél 1 Szerencse pontot!\n
A zsák birtokában nagy, nehéz tárgyakat is magaddal vihetsz majd anélkül, hogy
súlyukat megéreznéd. Ezek a tárgyak egy másik dimenzióba kerülnek át, így súly-
talanná válnak, de bármikor elővehetők. Ha még nem tetted volna:
\nFelpróbálhatod a csizmát: 94\n
\nFelhúzhatod a gyűrűt az ujjadra: 297\n
\nHa a fent említett dolgok egyikéhez sincs kedved,
folytathatod utadat nyugat felé, a tisztáson át: 222"""
        this_scene = Action()
        this_scene.act_att_change('szerencse','+1')
        this_scene.bonus_att_change('feneketlen_zsak')
        return this_scene.choice_3('94','297','222')

class Scene_27(Scene):

    def enter(self):
        print """
Közeledik az este, a nap fokozatosan lenyugszik a láthatáron. Olyan, mintha egy
nagy vörös léggömb tűnne el a szemed elől a tűzhányó tövében. Rózsaszín és vörös
napsugarak jelennek meg az égbolton, és hamarosan ezer és ezer apró rovar hangjá-
tól lesz zajos a környék. Úgy döntesz, hogy két bokor között letáborozol, s abban
reménykedsz, hogy kellőképpen rejtve leszel itt az esetleges éjszakai ragadozók
elől. \nTedd próbára a Szerencsédet!\n """
        this_scene = Action()
        return this_scene.luck('388','348')

class Scene_28(Scene):

    def enter(self):
        print """
A vágat egyszer csak elágazik...
\nHa balra indulsz: 226
\nHa egyenesen előre folytatod ez utadat: 101 """
        this_scene = Action()
        return this_scene.choice("226","101")

class Scene_29(Scene):

    def enter(self):
        print """
Amint a Hidra a közeledbe ér, a kardodért nyúlsz, hogy felkészülj a csatára...
"""
        this_scene = Action()
        this_scene.battle(9,9,'Hidra jobb feje',1,'389')
        return this_scene.battle(9,9,'Hidra bal feje',0,'389')

class Scene_30(Scene):

    def enter(self):
        print """
Madártollat keresve mész a tűzhányó felé, amikor egy hatalmas teremtmény ugrik
eléd a sziklák mögül. Groteszk testét bibircsókok borítják és hosszú álláról
nyál csorog. Egy Hegyi Troll támadott meg!"""
        this_scene = Action()
        if not this_scene.check_equipped('sisak','Sog'):
            this_scene.act_att_change('eletero','-2')
        return this_scene.battle(9,9,'Hegyi Troll',0,'65')

class Scene_31(Scene):

    def enter(self):
        print """
Felkapod a rudat, és ellököd a tutajt a Krokodil úszó tetemétől.
Ha nincs a birtokodban a Feneketlen Zsák, amelybe beletehetted őket,
dárdád és baltád (ha egyáltalán van ilyen harci eszközöd) a tutajról
beleesik a vízbe, miközben a Krokodillal viaskodsz. Káromkodsz a vesz-
teség miatt, de tovább hajózol a folyón fölfelé... """
        y = raw_input('> ')
        this_scene = Action()
        if this_scene.check_bonus_att('feneketlen_zsak',True,False) == True:
            return '390'
        else:
            this_scene.rem_item_list_sack('Balta')
            this_scene.rem_item_list_sack('Dárda')
            return '390'

class Scene_32(Scene):

    def enter(self):
        print """
Mire megtalálod és kiszabadítod az összes foglyot,
hatvanhárom bosszúra elszánt hű követőd vezére vagy. """
        y = raw_input('> ')
        return '201'

class Scene_33(Scene):

    def enter(self):
        print """
Hamarosan eléred a tengerpartot, de amint meglátod, mi történik ott, gyorsan
visszaugrasz a sziklák mögé. Hat Kalózt láttok egy evezős csónak körül, amelyet
valószínűleg ők húztak partra. Ránézel Mungóra, és megbeszélitek, mit tegyetek.

Ha meg akarjátok támadni a Kalózokat: 340

Ha inkább visszamentek az öbölbe,
majd onnan a tengerparton át a másik kis öbölbe: 24
"""
        this_scene = Action()
        return this_scene.choice('24','340')

class Scene_34(Scene):

    def enter(self):
        print """
Tovább kúszol lefelé a vágatban, de csakhamar rájössz, hogy az nem vezet sehová.
Alig van hely, hogy megfordulj, így aztán fejedet két lábad közé dugva hátrabuk-
fencezel. Visszamászol a fúrólyukon, ahonnan szabadon eléred a fővágatot...
\n1 Szerencse pontot vesztesz.\n
Kimászol a fúrólyukból, és balra fordulsz a vágatban."""
        this_scene = Action()
        this_scene.act_att_change('szerencse','-1')
        y=raw_input('> ')
        return '321'

class Scene_35(Scene):

    def enter(self):
        print """
A sziklába vésve ez olvasható: "Fordulj vissza, vagy meghalsz!"
Ez komoly figyelmeztetés, de nem tudod, hogy azoknak szól-e, akik belépnek a
szurdokba, vagy azoknak, akik kifelé igyekeznek onnan, ugyanis a szikla mindkét
iránnyal pontosan szemben áll. Bár nem akarod az életedet kockáztatni, mégis m
egragadod a kardod markolatát, és lelopakodsz a szurdokba... """
        y=raw_input('> ')
        return '119'

class Scene_36(Scene):

    def enter(self):
        print """
A Gyíkkirály egyre jobban közeledik feléd..."""
        this_scene = Action()
        return this_scene.check_equipped('fegyver','Tűzpallos','111','346')

class Scene_37(Scene):

    def enter(self):
        print """
Habár arra számítasz, hogy valamilyen szörnyű vadállat bukkan fel a vízből,
körülötted mégis minden nyugodt. A lábad alatt fokozatosan szilárdulni kezd
a talaj, és csakhamar kiérsz a vízből. Sűrű iszapban haladsz. Figyelmesen
szemléled a terepet meg az eget, de valahogy nem érzékeled azokat az undo-
rító puha testeket, melyek a lábadhoz tapadnak. Csak amikor valami furcsát
érzel, akkor nézel le, és látod, hogy Óriás Piócák tekeredtek a lábadra..."""
        y = randint(1,6) + 1
        this_scene = Action()
        this_scene.act_att_change('eletero','-y')
        this_scene.item_dict_sack_neg('Kaja','y')
        return '280'

class Scene_38(Scene):

    def enter(self):
        print """
Úgy látszik, a Gyíkember süket, mert nem hallotta meg leejtett kardod csörrenését,
és továbbmegy a vágatban. Felkapod a kardodat, és utána lopakodsz..."""
        y=raw_input('> ')
        return '51'

class Scene_39(Scene):

    def enter(self):
        print """
A vágat aljában kókusz nagyságú szikladarabok hevernek. A felületük meglepően
sima. Némelyik mintha mozogna kissé, de te arra gyanakszol, hogy ez nem más,
mint a fény és az árnyék játéka. Ekkor aztán az egyik szikladarab életre kel,
és parányi lábain feléd iramodik. Hasító fájdalmat érzel lábadban, mintha éles
fogak vájtak volna a húsodba.
\n1 Életerő pontot veszítesz.\n
Rémülten veszed észre, hogy Grannituszok, tatuhoz hasonló
gonosz emberevő állatok vettek körül..."""
        this_scene = Action()
        return this_scene.check_bonus_att('csörgőkígyómarás','207','25')

class Scene_40(Scene):

    def enter(self):
        print """
Az árnyas szurdokban haladsz lefelé. A déli oldalon emelkedő hegyek elfogják
a nap fényét. A szurdok egyszerre szürkülni kezd. Föntről hatalmas morajlást
hallani. Sziklaomlás van! Óriási szikladarabok és kövek zuhannak rád."""
        this_scene = Action()
        return this_scene.luck('253','107')

class Scene_41(Scene):

    def enter(self):
        print '''
A tubákosszelencében kicsiny aranyrögöt találsz, meg egy szelet papírt, melyre
faszénnel a következőket írták:
"Ha a kezedbe kerül ez az írás, az azt jelenti,
hogy nem sikerült megszabadulnom a Gyíkkirály
rabszolgabányájából. Tutajom a szurdok mögött
van elrejtve, a folyóparton. Ha azért jöttél a
szigetre, hogy segíts nekünk, kérlek, hajózz
fölfelé a folyón egészen addig, míg meg nem
pillantod sárkunyhóinkat. A rabszolgabányák
közel vannak, de óvakodj a Gyíkember őreitől."

Összehajtogatod a kis cédulát, és az aranyröggel együtt zsebre vágod.
Folytatod utadat a lábnyomokat követve...'''
        this_scene = Action()
        this_scene.bonus_att_change('uzenet')
        this_scene.item_list_sack('Aranyrog')
        y = raw_input('> ')
        return '325'

class Scene_42(Scene):

    def enter(self):
        print """
Magasba emelt kardoddal rátámadsz a hozzád legközelebb álló ellenfélre, egy Hobgoblinra.
"""
        this_scene = Action()
        return this_scene.battle(6,5,'Hobgoblin',0,'341')

class Scene_43(Scene):

    def enter(self):
        print """
A Gyíkemberek észrevesznek és gyorsan reagálnak! """
        this_scene = Action()
        this_scene.battle(9,8,'Első Gyíkember',1,'284')
        return this_scene.battle(8,8,'Első Gyíkember',0,'284')

class Scene_44(Scene):

    def enter(self):
        print """
Hamarosan egy újabb elágazáshoz érsz. Amint balra tekintesz, a vágat
végében megpillantod a napfényt, és eszedbe jut, hogy ott van a bejárat.
Úgy döntesz, hogy egyenesen odamész..."""
        y = raw_input('> ')
        return '274'

class Scene_45(Scene):

    def enter(self):
        print """
Kardod lepattan a Gyíkember páncélzatáról. Az szembefordul veled,
aki orvul meg akartad gyilkolni, és görbe kardjával rád támad.
"""
        this_scene = Action()
        return this_scene.battle(9,9,'Kétfejű Gyíkember',0,'173')

class Scene_46(Scene):

    def enter(self):
        print """
Az étel láttán a férfi szeme felcsillan; leteszi a rudat, és int, hogy ülj le.
Amikor bekebelezi mindazt, amit adtál neki (veszítesz 1 Élelmiszeradagot), el-
mondod, mi járatban vagy. Elmeséli, hogy valamikor régen tolvaj volt az anyaor-
szágban, de elfogták, és Olaf hercege büntetésként ötévi rabságra ítélte, amit
a Tűz-szigeten kellett letöltenie. Miután a Gyíkemberek vették át a hatalmat a
szigeten, rákényszerítették, hogy az aranybányákban dolgozzék. Egy szép napon
azonban sikerült megmenekülnie, és azóta rejtőzik a dzsungelben. Úgy gondolja,
már túl öreg ahhoz, hogy a tutajútra vállalkozzék, és így jusson el a szárazföldre.
 Egyébként is jól érzi magát itt a fa odvában. Megkérdezed tőle, vajon tud-e neked
 valami hasznos információval szolgálni. Azt válaszolja, hogy szívesen megteszi,
 ha adsz neki még egy kis ennivaló.
\nHa adsz neki még egy adagot Élelmiszerkészletedből: 149\n
\nHa inkább mérgesen ráförmedsz: 69\n
"""
        this_scene = Action()
        return this_scene.choice('149','69')

class Scene_47(Scene):

    def enter(self):
        print """
Amint lefelé haladsz a fővágatban, jobbról egy elágazás mellett mész el,
balról meg egy másik vágat bejáratát látod. Egy függőlegesen lefelé haladó
akna széléhez érsz, melynek oldalához egy falétrát támasztottak. Lenézel az
akna mélyére. Bár nem látod a fenekét, mégis úgy döntesz, hogy lemászol a létrán.
"""
        y = raw_input('> ')
        return '315'

class Scene_48(Scene):

    def enter(self):
        print """
Amikor lehajolsz, hogy megnézed a furcsa tojásokat, az egyik eltörik. Színtelen,
nyúlós folyadék buggyan ki belőle, majd egy lyuk támad a héjban. Tűhegyes fogú,
hosszú állkapocs jelenik meg a nyílásban, melyet parányi, sötétzöld, szem nélküli
fej követ. A vadállat beleszimatol a levegőbe, majd ösztönösen a torkodnak ugrik.
Szerencsétlenségedre épp egy szörnyű fenevad fészkébe botlottál bele:
a Borotvafogú arra termett, hogy más élőlényeket elpusztítson...
"""
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.check_equipped('sisak','Sog','56','304')

class Scene_49(Scene):

    def enter(self):
        print """
Visszadugod a kardodat a hüvelyébe, és folytatod megkezdett
utadat nyugat felé. Fokozatosan szilárdul a talaj a lábad
alatt, és nemsokára túljutsz a mocsáron. Veled szemben két
hegy emelkedik, és úgy döntesz, hogy a közöttük húzódó szur-
dokban mész tovább."""
        y = raw_input('> ')
        return '362'

class Scene_50(Scene):

    def enter(self):
        print """
Válladdal nekifeszülsz az ajtónak..."""
        this_scene = Action()
        return this_scene.agi('356','266')

class Scene_51(Scene):

    def enter(self):
        print """
Az énekhang és a kőhöz csapódó kalapács zaja igen erős; közel lehetsz ahhoz
a helyhez, ahol a foglyok dolgoznak. Elhatározod, hogy hátba támadod a Gyíkembert.
Fölemelsz egy nagy követ, és máris mögötte állsz. Az felfigyel rád - de már nem
tudja elkerülni, hogy a nehéz követ a fejéhez ne vágd. Amikor elterül a földön,
kiragadod a kezéből a vödröt, remélve, hogy abban víz van, amit odaadhatsz a
szomjazó foglyoknak. Addig mész a vágatban, amíg egy nagyobb terembe nem érkezel...
"""
        y = raw_input('> ')
        return '223'

class Scene_52(Scene):

    def enter(self):
        print """
Az Óriásdarázs fullánkjában lévő méreg bénítóan hat rád..."""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg','-1')
        return '141'

class Scene_53(Scene):

    def enter(self):
        print """
Édes illat száll alá a fa lombjai közül. Teljesen elbódulsz és elálmosodsz tőle.
Mivel a szemed lecsukódik, nem veszed észre, hogy a fejed felett lévő ágakról
egy vastag inda kúszik lefelé. Lassan a nyakad köré tekeredik, és fojtogatni kezd.
Fulladozva felébredsz, és a kardod után nyúlsz, mely a lábadnál hever.

Tedd próbára a Szerencsédet!"""
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.luck('256','132')

class Scene_54(Scene):

    def enter(self):
        print """
Amikor lehajolsz, hogy átkutasd a Gyíkkirály ruháját, észreveszed,
hogy a Goncsong már lábával elrugaszkodik, hogy a te fejeden landoljon. """
        this_scene = Action()
        return this_scene.agi('244','260')

class Scene_55(Scene):

    def enter(self):
        print """
Szervezeted erős, és így a kígyó mérge nem okoz nagyobb bajt.
\nVesztesz 2 Életerő pontot.\n
Egy ronggyal bekötözöd a sebedet, és pihensz egy keveset.
\nHa a kardoddal ki akarod csalogatni a Csörgőkígyót a fészkéből: 5\n
\nHa inkább óvatosan továbbmész a szurdokban nyugat felé: 119\n
"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        return this_scene.choice('5','119')

class Scene_56(Scene):

    def enter(self):
        print """
Elfordítod a fejedet, amikor rád támad a Borotvafogú, amely így sisakod
nyakvédőjén fennakad. Visszaugrik, te pedig kardot rántasz, hogy ledöfd
a gonosz teremtményt... """
        this_scene = Action()
        return this_scene.battle(6,5,'Borotvafogú',0,'20')

class Scene_57(Scene):

    def enter(self):
        print """
Az elágazáshoz visszatérve fordulhatsz balra: 361\n
Vagy folytathatod utadat egyenesen előre a vágatban: 19 """
        this_scene = Action()
        return this_scene.choice('361','19')

class Scene_58(Scene):

    def enter(self):
        print """
Térdig süppedve a nyálkás mocsárban azon igyekszel, hogy lépést tarts a fürge
Mocsári Szökdécselővel. Hirtelen délnek fordul, és megint int, hogy kövessed. \n
Ha még mindig követni akarod a Mocsári Szökdécselőt: 235 \n
Ha inkább továbbra is nyugat felé folytatod az utadat: 37 """
        this_scene = Action()
        return this_scene.choice('235','37')

class Scene_59(Scene):

    def enter(self):
        print """
Amint mászol felfelé a hegyen, belebotlasz egy rejtett zsinórba, melyet két
kis szikla között feszítettek ki. A sziklák elmozdulnak, és a hegy oldalán
végiggördülve figyelmeztetik a barlang lakóját a hívatlan látogató jelenlétére.
Egy ádáz tekintetű Barlangi Nő jelenik meg a barlang bejáratánál. Testét állat-
szőrök fedik, kezében egy dárda meg egy kőbalta van.
\nElőrelép, és feléd hajítja a dárdát.
\nTedd próbára a Szerencsédet! """
        this_scene = Action()
        return this_scene.luck('108','255')

class Scene_60(Scene):

    def enter(self):
        print """
Elhibázod mind a három fürge mozgású Grannituszt,
így tehát egyenként kell megküzdened velük!"""
        this_scene = Action()
        this_scene.battle(4,3,'Első Grannitusz',2,'192')
        this_scene.battle(3,2,'Második Grannitusz',1,'192')
        return this_scene.battle(4,3,'Harmadik Grannitusz',0,'192')

class Scene_61(Scene):

    def enter(self):
        print """
Körülnézel, és látod, hogy Mungó az utolsó kalózzal, a kapitánnyal csap össze!
De mielőtt a segítségére siethetnél, a kapitány hirtelen előrelendül, és átdöfi
szegény Mungó mellét. Az gyötrelmesen feljajdul, majd összeesik. A kapitány
feléd fordul, arcán torz mosoly ül, mely a bal orcáján végighúzódó hosszú fekete
sebhelytől származik. Rátámadsz a kapitányra, hogy bosszút állj Mungón. """
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.battle(10,6,'Kalózkapitány',0,'165')

class Scene_62(Scene):

    def enter(self):
        print """
A dárda elzúg melletted, és a Hobgoblin pánikszerűen elmenekül.
Átmész a hídon, a szakadék másik oldalára..."""
        y = raw_input('> ')
        return '139'

class Scene_63(Scene):

    def enter(self):
        print """
Sárkunyhók és Gyíkemberek - az aranybánya valahol itt van a közelben!
\nHa elindulsz, hogy megkeresd a bányát: 147 \n
\nHa előbb inkább elintézed a Gyíkembereket: 329
"""
        this_scene = Action()
        return this_scene.choice('147','329')

class Scene_64(Scene):

    def enter(self):
        print """
Még nem tudod, de a gyűrű is hasznodra válik. Aki viseli, annak segít kiállni
a próbát. A kukacok eltűnnek a szemed elől, a Sámán varázslata megtörik..."""
        this_scene = Action()
        this_scene.add_saman_proba('Atalakulas')
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_65(Scene):

    def enter(self):
        print """
Újra útnak indulsz, hogy mielőbb megtaláld a Sámánt. Ahogy mész, csomókba kötött
füvet látsz, és ebből arra következtetsz, hogy akit keresel, már nem lehet messze.
Kíváncsi vagy, vajon tudja-e, hogy itt jársz. Megállsz és körülnézel. Életnek
semmi nyoma, csupán egy döglött sirály fekszik jobbra egy sziklán."""
        this_scene = Action()
        return this_scene.check_bonus_att('sámán_kréta_üzenete','89','365')

class Scene_66(Scene):

    def enter(self):
        print """
Felkapod a Törzsfőnök dárdáját, és visszafutsz a dzsungelba, ahonnan jöttél.
Hamarosan messze kerülsz a Fejvadászok településétől. Lassítasz, már nem kell
rohannod. Ismét magadra maradtál"""
        y = raw_input('> ')
        return '113'

class Scene_67(Scene):

    def enter(self):
        print """
A Sámán elveszi tőled a csontokat, és fájdalmad azonnal megszűnik.
A próbán azonban megbuktál, és a Sámán nem fogja elárulni neked titkát.
\nInt, hogy indulj el délkeleti irányba, és közli veled, hogy a fogolytábor
arra van, valamint azt is, hogy a Goncsonggal az ő segítsége nélkül kell meg-
küzdened. Megfordulsz, és elindulsz lefelé a tűzhányó oldalában, a Gyíkkirály
erődítményéhez... """
        y = raw_input('> ')
        return '168'

class Scene_68(Scene):

    def enter(self):
        print """
A vágat igencsak összeszűkült, a mennyezetet tartó gerendák megrepedeztek és
helyenként elmozdulnak. A klausztrofóbia érzése kerít hatalmába a félhomályban,
de nem adod fel, tovább mész előre, miközben föld és egy csomó apró kő hullik rád.
A vágat egy újabb kereszteződésbe torkollik. Mit teszel?
\nElindulsz balra: 278\n
\nElindulsz jobbra: 70\n
\nVisszafordulsz: 172 """
        this_scene = Action()
        return this_scene.choice_3('278','70','172')

class Scene_69(Scene):

    def enter(self):
        print """
Az öreg tolvaj felpattan, és még magasabbra mászik a fán, miközben hangosan át-
kozódik. Nagyon fürge, így karddal a kezedben meg a hátizsákodat cipelve képte-
len vagy elérni. Úgy döntesz, hogy magára hagyod, lemászol az indán, és folyta-
tod az utadat északnyugati irányba..."""
        y = raw_input('> ')
        return '375'

class Scene_70(Scene):

    def enter(self):
        print """
A vágat élesen jobbra kanyarodik, majd egyenesen megy tovább, ameddig a szem
ellát. Elindulsz rajta, de hirtelen morajlást hallasz a fejed fölött. A tartó-
gerendák összetörnek, és az egész boltozat rád omlik... """
        this_scene = Action()
        this_scene.act_att_change('eletero','-5')
        return this_scene.luck('345','175')

class Scene_71(Scene):

    def enter(self):
        print """
Miközben nagy zajjal vágsz utat magadnak a buja növények között, nem veszed
észre, hogy hat pigmeus figyel fel rád, és követni kezd. Gyűrűbe zárnak, még
mielőtt megpillantanád őket, és fúvócsövükkel célba veszik testedet...
\nHa beszélni akarsz velük: 276\n
\nHa inkább harcolni akarsz ellenük: 359\n """
        this_scene = Action()
        return this_scene.choice('276','359')

class Scene_72(Scene):

    def enter(self):
        print """
Az írás egy kérés, mely a Sámántól származik, akit éppen keresel. Azt kéri,
hogy keress egy madártollat, és tűzd a hajadba, ha békés szándék vezet hozzá.
Kíváncsi vagy, vajon honnan tudja a Sámán, hogy őt keresed, de úgy döntesz,
szükséged lesz arra a tollra. Elindulsz, hogy keress egyet..."""
        y = raw_input()
        return '30'

class Scene_73(Scene):

    def enter(self):
        print """
Habár megpróbálod ledöfni a Köpködő Varangyot, az rád ugrik,
és a kardod célt téveszt. Megrémülsz, amikor a hatalmas állat
a földre dönt. Hegyes foga belefúródik az egyik karodba..."""
        this_scene = Action()
        return this_scene.choice('217','396')

class Scene_74(Scene):

    def enter(self):
        print """
A feléd tartó Gyíkember nem fog gyanút, és a
Törpék csapatával nyugodtan elvonulhatsz..."""
        y = raw_input('> ')
        return '114'

class Scene_75(Scene):

    def enter(self):
        print """
A Sámán odalép hozzád, és ujjával megérinti a fejedet.
Szörnyű, riasztó alakok jelennek meg előtted. Olyan valóságosnak
hatnak, hogy szinte ordítani szeretnél fájdalmadban..."""
        this_scene = Action()
        return this_scene.check_bonus_att('piros_por','155','131')

class Scene_76(Scene):

    def enter(self):
        print """
Az elhajított dárda a válladba fúródik, és a földre zuhansz...
\n3 Életerő pontot vesztesz!\n
Ha még életben vagy, látod, hogy az ember, akit megmentettél, odalép hozzád, és
kihúzza a dárdát a válladból. Felemel, odavonszol az egyik kunyhóba, hogy ott
elrejtőzz, ugyanis egy másik Fejvadász éppen rád akar támadni.
A kunyhóban megmentőd egy dárdát meg egy kőbaltát vesz magához. Rád mosolyog
hálája jeléül, majd hatalmas üvöltéssel kirohan a kunyhóból. Nézed, mint rohan
rá a Fejvadászokra fegyvereivel csapkodva. Hármat sikerül is leütnie, amikor
egy döfés végez vele. Kitámolyogsz a kunyhóból, és rátámadsz a megmaradt Fejva-
dászokra, de csak egyikük, a törzsfőnök veszi fel veled a harcot, a többiek meg-
fordulnak és elmenekülnek... """
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        return this_scene.battle(8,8,'Fejvadászok Törzsfőnöke',0,'66')

class Scene_77(Scene):

    def enter(self):
        print """
Az ajtó kinyílik, és megpillantod a bilincsbe vert Törpét, amint a furcsa
külsejű kétfejű Gyíkember a laboratóriumba tuszkolja. Átlökdösi egy ajtón,
amely a raktárba vezet...
\nHa előbújsz rejtekhelyedről, hogy megtámadd a mutánst (alakváltoztatót): 289\n
\nHa inkább megvárod, míg bemennek a raktárhelyiségbe: 91\n """
        this_scene = Action()
        return this_scene.choice('289','91')

class Scene_78(Scene):

    def enter(self):
        print """
Meglapulsz a fal legsötétebb zugában. A léptek egyre közelednek hozzád, amikor
megpillantasz egy Gyíkembert, kezében vödörrel. Elmegy melletted, anélkül hogy
észrevenne, és hangosan káromkodik, mert nehéz a vödör. Biztonságos távolságból
követed a vágatban..."""
        this_scene = Action()
        return this_scene.luck('184','154')

class Scene_79(Scene):

    def enter(self):
        print """
Felmész a dombtetőre, és belépsz a barlangba. Rothadó élelmiszer bűze és
izzadságszag terjeng a levegőben. Néhány tárgy hever szanaszét a földön,
mintha szemét volna. Már épp elhagyni készülsz a barlangot, amikor egy
Barlangi Nő ágya mögött egy kis zugban kicsinyke agyagtálat teszel észre.
Az agyagtálban vörös por van. Mit teszel?
\nRákensz belőle az arcodra: 332\n
\nLenyelsz belőle egy keveset: 97\n
\nNem nyúlsz hozzá, és kimész a barlangból: 17 """
        this_scene = Action()
        return this_scene.choice('332','97','17')

class Scene_80(Scene):

    def enter(self):
        print """
Levágsz egy fürt banánt, és lemászol a fáról. A banán édes, mint a méz.
\nNyersz 2 Életerő pontot.\n
Elégedetten mászol be a búvóhelyedre, hogy meghúzd magad éjszakára. Amint
felnézel az égre, gomolygó felhőket látsz az egyre sötétedő, vöröses égbolton.
Leszámítva az ezernyi rovar fülsiketítő zenéjét, élvezed a hűvös estét,
és hamarosan elalszol..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','2')
        return this_scene.luck('388','348')

class Scene_81(Scene):

    def enter(self):
        print """
Amint egyre előbbre haladsz a buja bozótban, ijedtedben feláll a hátadon a szőr,
mert érzed, hogy valaki figyel. Megállsz, karddal a kézben, körülnézel, lesed,
nem mozdul-e levél valahol. Ekkor három sötét bőrű férfi toppan eléd, mindegyiken
csupán egyszerű ágyékkötő van. Kőbaltával és hosszú dárdával vannak felfegyverezve,
de igazából csak akkor ijedsz meg tőlük, amikor észreveszed, hogy mindháromnak
az övét zsugorított emberfejek díszítik. A Fejvadászok veszekedni kezdenek, hogy
melyikük öljön meg és szerezze meg ezáltal a jogot arra, hogy fejedet az övére
tűzze. Végül az egyik előrelép."""
        y = raw_input('> ')
        this_scene = Action()
        this_scene.battle(6,6,'Első Fejvadász',2,'177')
        this_scene.battle(7,6,'Második fejvadász',1,'177')
        return this_scene.battle(6,7,'Harmadik fejvadász',0,'177')

class Scene_82(Scene):

    def enter(self):
        print """
Felrohansz a csigalépcsőn, s egy faajtó előtt állsz meg. Óvatosan lenyomod
a kilincset, és résnyire nyitod az ajtót. Az oromzati párkány mellett, lábát
szétvetve áll a gyalázatos Gyíkkirály; aki öklét rázva kiabál katonáinak.
Egy furcsa Fekete Oroszlán engedelmesen ül mellette, de nem ő, hanem a
Gyíkkirály feje búbján megtelepedett Goncsong látványa tölt el igazán
félelemmel. Nagy levegőt veszel, és odalépsz az oromzati párkányhoz.
Intesz saját harcosaidnak, és odakiáltasz a Gyíkkirálynak. Az rád se néz,
csak csettint egyet a Fekete Oroszlánnak, hogy vesse rád magát."""
        this_scene = Action()
        return this_scene.battle(11,11,'Fekete Oroszlán',0,'203')

class Scene_83(Scene):

    def enter(self):
        print """
A domboldal elég meredek, és megcsúszik a lábad. Elveszíted
az egyensúlyodat, és lecsúszol a hegyről..."""
        this_scene = Action()
        return this_scene.luck('334','281')

class Scene_84(Scene):

    def enter(self):
        print """
Az ajtó egy folyosóra nyílik, melyen jobbra is, balra is mehetsz.
Jobbra a folyosó csakhamar véget ér, úgyhogy balra indulsz el.
Egy újabb ajtót találsz a jobb oldali falban, amelyre a "Börtönőr"
feliratot festették. Továbbmész. A folyosó élesen balra kanyarodik,
és egy csigalépcsőbe torkollik...
\nHa be akarsz nyitni az ajtón: 195\n
\nHa inkább lemész a csigalépcsőn: 8\n"""
        this_scene = Action()
        return this_scene.choice('195','8')

class Scene_85(Scene):

    def enter(self):
        print """
Mivel a másik három Grannitusz is feléd rohan, megpróbálod széttaposni
csontpáncéljukat. Még mielőtt azok vájnák a lábadba éles fogukat..."""
        this_scene = Action()
        return this_scene.dice_3('60','239','112')

class Scene_86(Scene):

    def enter(self):
        print """
A Pigmeusok meglepődnek vakmerőséged láttán, és nevetésben törnek ki.
Egyikük odalép hozzád, és megkínál néhány szem dióval és szamócával.
\nHa úgy döntesz, hogy elfogadod és megeszed az ételt: 18\n
\nHa nem eszed meg: 295\n"""
        this_scene = Action()
        return this_scene.choice('18','295')

class Scene_87(Scene):

    def enter(self):
        print """
Amint a férfi közelébe érsz, az felugrik a tutajodra. Tekintete vad,
a teste csupa veríték. Félrebeszél a magas láztól, úgyhogy képtelen
vagy vele szót érteni. Hirtelen előhúzza a tőrét a ruhája redőiből,
és rád támad. Nincs már időd, hogy a kardodat előrántsd, így puszta
kézzel kell megküzdened vele..."""
        this_scene = Action()
        return this_scene.battle(9,4,'Őrjöngő Fogoly',0,'130')

class Scene_88(Scene):

    def enter(self):
        print """
Elhatározod, hogy tutajt építesz magadnak, és elindulsz a folyón fölfelé.
A folyó elég sekély, így minden nehézség nélkül átgázolhatsz rajta; hogy
a túlsó partjáról néhány kisebb fát szerezz..."""
        y = raw_input()
        this_scene = Action()
        return this_scene.check_item_list_sack('Balta','179','305')

class Scene_89(Scene):

    def enter(self):
        print """
Odamész a sirályhoz, és kihúzol egy tollat a szárnyából. Hátizsákodból
egy darab spárgát veszel elő, s ezzel kötöd a tollat hátul a hajadhoz.
Óvatosan, kissé szorongva mész tovább..."""
        y = raw_input('> ')
        this_scene = Action()
        this_scene.bonus_att_change('siraly_toll')
        return '269'

class Scene_90(Scene):

    def enter(self):
        print """
Az öreg egy összetekert drótdarabkát vesz elő a zsebéből, és átnyújtja neked.
Észreveszi kíváncsi tekintetedet, és így szól: - Ez olyan drót, amit én tolvaj-
kulcsnak használtam, hogy megszabaduljak a bilincseimtől, mielőtt megszöktem
volna a bányából. Még hasznát veheted, ha fogságba kerülsz! - Megköszönöd az
öregnek az ajándékot, és az indán lekúszva tovább folytatod utadat északnyugati irányban..."""
        y = raw_input('> ')
        this_scene = Action()
        this_scene.item_dict_sack_neg('Kaja','3')
        this_scene.item_list_sack('Tolvajkulcs')
        return '375'

class Scene_91(Scene):

    def enter(self):
        print """
Amint a mutáns (alakváltoztató) és a fogoly elhagyták a laboratóriumot,
előmászol a lóca alól, és a nyitott ajtón át továbbmész..."""
        y = raw_input('> ')
        return '180'

class Scene_92(Scene):

    def enter(self):
        print """
A víz felfrissít...
\nNyertél 1 Életerő pontot!\n
Miközben iszol, egy faládikát pillantasz meg a tó fenekén...
\nHa alámerülsz, hogy felhozd: 259
\nHa inkább továbbmész nyugatnak: 222"""
        this_scene = Action()
        return this_scene.choice('259','222')

class Scene_93(Scene):

    def enter(self):
        print """
Célzol, és elhajítod a tőrt. Az elröpül, és egyenesen
beleáll a narancsba, amely legurul a szikláról..."""
        this_scene = Action()
        this_scene.add_saman_proba('Ugyesseg')
        this_scene.print_saman_proba_k()
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_94(Scene):

    def enter(self):
        print """
A csizma épp jó a lábadra. Körbefutsz benne, de semmi sem történik veled, így
hát úgy döntesz, hogy inkább nem kell. Ha még nem tetted volna:
\nKinyithatod a zsákot: 26\n
\nFelhúzhatod a gyűrűt az ujjadra: 297\n
\nHa egyikhez sincs kedved,
folytathatod utadat nyugat felé, a tisztáson át: 222"""
        this_scene = Action()
        this_scene.item_equipped('csizma','Vörös bőrcsizma')
        return this_scene.choice_3('26','297','222')

class Scene_95(Scene):

    def enter(self):
        print """
A mutáns Gyíkember leugrik a döglött Styracosaurus hátáról,
és alabárdját kinyújtott kezében tartva odacsörtet hozzád... """
        this_scene = Action()
        return this_scene.battle(9,9,'Mutáns Gyíkember',0,'133')

class Scene_96(Scene):

    def enter(self):
        print """
Várod a többi pigmeus támadását, de ők egyszerűen felkapják halott társukat, és
némán eltűnnek a dzsungel rengetegében.
\nIsmét egyedül maradtál, s folytatod utadat nyugat felé..."""
        y = raw_input('> ')
        return '7'

class Scene_97(Scene):

    def enter(self):
        print """
A port szinte lehetetlen lenyelni. Beszippantasz egy keveset, és köhögni kezdesz.
Úgy érzed, ég a tüdőd...
\nVeszítesz 2 Életerő pontot és 1 Szerencse pontot.\n
Végül a fájdalom megszűnik. Mit teszel?
\nRákensz egy kevés port az arcodra: 332\n
\nOtt hagyod a port a barlangban és távozol: 17"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        this_scene.act_att_change('szerencse','-1')
        return this_scene.choice('332','17')

class Scene_98(Scene):

    def enter(self):
        print """
Lassan, de biztosan fölemeled a hatalmas szikladarabot a földről.
A Sámán jelt ad, hogy leteheted. Elégedett az erőddel..."""
        this_scene = Action()
        this_scene.add_saman_proba('Ero')
        this_scene.print_saman_proba_k()
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_99(Scene):

    def enter(self):
        print """
Az Emberevő Óriásnál nincs semmi, aminek hasznát vennéd, így hát folytatod
tutajod építését. Körülbelül egy óra múlva elegendő fatörzs gyűlik össze ahhoz,
hogy egy kis tutajt eszkábálj magadnak. Indákkal kötözöd egymáshoz a fatörzseket,
majd a kész tutajt vízre bocsátod..."""
        y = raw_input('> ')
        print """
 Egy hosszú, vékony bottal lökve magadat fölfelé indulsz a folyón."""
        y = raw_input('> ')
        return '387'

class Scene_100(Scene):

    def enter(self):
        print """
A gyümölcs igazán finom. Nyersz 1 Életerő pontot. Felüdülve ismét útnak indulsz,
miközben egyfolytában nyalogatod a szád szélét a finom gyümölcs után..."""
        this_scene = Action()
        y = raw_input('> ')
        return this_scene.luck('352','160')

class Scene_101(Scene):

    def enter(self):
        print """
Egy oldalára dőlt fakerekű kézikocsit teszel észre a vágat közepén. Teljesen
elállja az utadat. Kicsiny, összetört csontváz fekszik mellette, valószínűleg
egy Törpéé. A vágatból kerek fúrólyuk nyílik. Arra gondolsz, vajon nem a Szikla-
hernyó támadta-e meg a szegény Törpét. A vágat hosszú, nem látod a végét, de
életnek semmi nyomát nem tapasztalod.
\nHa be akarsz mászni a fúrólyukba: 10\n
\nHa a kézikocsin átmászva folytatod az utadat a vágatban: 321"""
        this_scene = Action()
        return this_scene.choice('10','321')

class Scene_102(Scene):

    def enter(self):
        print """
Visszarohansz a buja bozótban, s közben megfeledkezel a szúrós ágakról és éles
tüskékről. Észreveszed egy fa üregét, amelyben, úgy gondolod, elrejtőzhetsz.

Ha megkockáztatod, hogy elbújj az üregben: 16

Ha inkább továbbfutsz: 169
"""
        this_scene = Action()
        return this_scene.choice('16','169')

class Scene_103(Scene):

    def enter(self):
        print """
Bár a viszketéstől majd megőrülsz, valami ennél is rosszabb történik. Elönt az
izzadság, és remegni kezdesz. Kezdődő maláriád van.
\n3 Életerő pontot veszítesz.\n
... """
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        return this_scene.life('15','316')

class Scene_104(Scene):

    def enter(self):
        print """
Felállsz, és belenézel a hátizsákodba. Élelmiszerkészleted (ha egyáltalán még
van belőle) tönkrement, ehetetlenné vált. A felszerelésed többi része viszont
nem sérült meg. Nincs más választásod, mint hogy gyalog folytasd utadat..."""
        this_scene = Action()
        this_scene.item_dict_sack('Kaja',0)
        return '197'

class Scene_105(Scene):

    def enter(self):
        print """
Óvatosan mászol fölfelé, éberen figyelve mindenre. Félúton egy fatörzsekből
összeeszkábált kis magaslest pillantasz meg, melyről egy inda lóg le.
\nHa fel akarsz mászni a magaslesre: 286\n
\nHa inkább továbbmész: 375
"""
        this_scene = Action()
        return this_scene.choice('286','375')

class Scene_106(Scene):

    def enter(self):
        print """
Néhány szó után észreveszed, hogy a lány nem érti, mit beszélsz. Lehet, hogy még
gyermekkorában hagyták itt a Tűz-szigeten, és vadon nevelkedett az állatokkal
együtt. A lány visszafogja a Tigrist, és furcsa hangokat hallatva nyugalomra
inti. Az láthatóan engedelmeskedik neki, úgyhogy lassan hátrálsz, nehogy meg-
riaszd. Mikor tisztes távolságba kerülsz tőlük, gyorsan a völgy felé indulsz,
hogy megkeresd a kiszabadított foglyokat..."""
        y = raw_input('> ')
        return '279'

class Scene_107(Scene):

    def enter(self):
        print """
A szikladarabok esőként zúdulnak alá, s az egyik eltalál..."""
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.dice_3('210','336','245')

class Scene_108(Scene):

    def enter(self):
        print """
A dárda elzúg a fejed mellett, és nagyot koppanva landol az egyik sziklán.
A Barlangi Nő mérgesen felmordul, és bunkósbotjával rád ront... """
        this_scene = Action()
        return this_scene.battle(5,5,'Barlangi Nő',0,'79')

class Scene_109(Scene):

    def enter(self):
        print """
Ajkadat rászorítod a kürt szélére, és belefújsz, amilyen erősen csak tudsz.
A csata kimenetele hirtelen megváltozik, amint bajtársaid meghallják a kürt
hangját. A Gyíkkirály katonái hátrálni kezdenek, s a köztük ütött résen át
eléred az erőd fakapuját. Átrohansz rajta, és beérsz a belső udvarba.
\nHa be akarsz menni a balra nyíló szárnyas ajtón: 268\n
\n Ha inkább a veled szemben lévő távoli ajtók egyikén mennél be: 84\n"""
        this_scene = Action()
        return this_scene.choice('268','84')

class Scene_110(Scene):

    def enter(self):
        print """
Nemcsak a bőröd nem bírja elviselni a gomba spóráit; a gyomrod is háborog.
Iszonyatosan rosszul érzed magad, ugyanis a gomba, amit megettél, mérges volt.
\nVeszítesz 3 Életerő és 1 Szerencse pontot.\n
Ha még mindig életben vagy, lassan egyre jobban érzed magad,
és ismét nekivágsz a dzsungelnak..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        this_scene.act_att_change('szerencse', '-1')
        return this_scene.end_turn('224')

class Scene_111(Scene):

    def enter(self):
        print """
A Gyíkkirály dühe, amellyel rád támadt, teljesen megdöbbent. Lángpallosával
egyik csapást a másik után méri rád, úgyhogy nem tudsz mást tenni, mint védekezni.
"""
        this_scene = Action()
        return this_scene.battle(12,15,'Gyíkkirály',0,'153')

class Scene_112(Scene):

    def enter(self):
        print """
Két fürge Grannituszt ártalmatlanná tettél, de még el kell bánnod a harmadikkal.
"""
        this_scene = Action()
        return this_scene.battle(4,3,'Grannitusz',0,'192')

class Scene_113(Scene):

    def enter(self):
        print """
Lassan törsz előre a sűrű dzsungelban, s nem tudod igazán, merre is mész.
Később egy pillanatra a fák között átvillan egy parányi napsugár, s ebből
megállapíthatod, merre is jársz. Nyugat felé indulsz el... """
        y = raw_input('> ')
        return '7'

class Scene_114(Scene):

    def enter(self):
        print """
A Törpék sietve ügetnek végig a vágatokon. A sok hónapos rabságban már jól
megtanultak tájékozódni a bánya labirintusában. Egyszer csak megállnak, és
egyikük odasúgja neked, hogy a következő kanyarnál dolgozik egy másik fog-
olycsoport. Hallod a sziklákhoz csapódó csákányok és kalapácsok tompa puf-
fanását. A Törpéknek azt mondod, hogy menjenek tovább, és ha jelt adsz,
támadják meg az őröket. A Törpék befordulnak a kanyarba, melyből kiérve
egy csapat férfit és Elfet látsz, amint a lábuknál egymáshoz láncolta a
sziklafallal szemben dolgoznak. Két Ork őr ordítva utasítja őket, hogy
dolgozzanak gyorsabban. Az őrök meglepődnek, amikor megpillantanak, de
csak akkor veszik észre, hogy álruhában vagy, amikor egészen a közelükbe
érsz. Elkiáltják magukat, és kardot rántanak."""
        this_scene = Action()
        return this_scene.luck('265','138')

class Scene_115(Scene):

    def enter(self):
        print """
A dárda belefúródik a malacba, és az elterül. Fát gyűjtesz, tüzet raksz, és neki-
látsz megsütni a pecsenyét. Amikor ropogósra sül, leülsz a földre lakomázni.
\nNyersz 3 Életerő pontot!\n
Újult erővel indulsz ismét nyugati irányba."""
        this_scene = Action()
        this_scene.act_att_change('eletero','3')
        return this_scene.end_turn('170')

class Scene_116(Scene):

    def enter(self):
        print """
Az étel nagyon ízlik, és leülsz lakmározni...
\nNyersz 2 Életerő pontot.\n
Épp akkor, amikor befejeznéd a táplálkozást, a hátad mögött lévő bokrok felől
zajt hallasz. Nem véletlenül akasztotta fel a fára az élelmet tulajdonosa,
ugyanis meg akarta védeni a Medve elől, amely most éppen arra készül, hogy rád
támadjon. Megpróbálsz elmenekülni...
"""
        this_scene = Action()
        this_scene.item_dict_sack_neg('Kaja',1)
        return this_scene.luck('27','247')

class Scene_116b(Scene):

    def enter(self):
        this_scene = Action()
        return this_scene.battle(10,9,'Medve',0,'247')


class Scene_117(Scene):

    def enter(self):
        print """
Amint fölfelé mászol, az öreg rád támad, kókuszzáport zúdít a fejedre. Hiába
mondod neki, hogy nem akarod bántani, egyre csak hajigálja rád mindazt, ami a
keze ügyébe kerül, és azt rikácsolja, hogy: „Takarodj!" Mire felérsz a magas-
lesre, jó néhány púp éktelenkedik a fejeden.
\nVeszítesz 1 Életerő pontot.\n
A magasles távoli végében megpillantod az öreget, akinek a kezében egy bambusz-
bot van, és rövid vászonnadrágot visel. Mit teszel?
\nFelajánlasz neki valamit az élelmiszerkészletedből: 46\n
\nOtthagyod, és inkább folytatod az utadat észak-
nyugat felé a dzsungelen át: 375\n
\nOdamész hozzá, és kiragadod a kezéből a bambuszbotot: 349\n """
        this_scene = Action()
        return this_scene.choice_3('46','375','349')

class Scene_118(Scene):

    def enter(self):
        print """
Hátrazuhansz, hiába markolásztad oly elkeseredetten a levegőt. Nagyot puffansz
a földön. Azonnal visszamászol a fára, miközben kardod hegyével lepöckölöd a Mérgespókot.
"""
        this_scene = Action()
        return this_scene.end_turn('80')

class Scene_119(Scene):

    def enter(self):
        print """
Lenn, a finom homokban a szurdokból kifelé tartó lábnyomokat veszel észre.
Ahogy előremész, a nyomok hirtelen megszakadnak, és dulakodás jeleit látod.
Az egyik pár lábnyom visszafelé vezet a szurdokba, mögötte két egyenes csík
húzódik a földön, mintha valakit a földön húztak volna. Amint követed a láb-
nyomokat, a homokban egy fényes tárgyon akad meg a szemed. Ekkor jössz rá, hogy
egy réz tubákosszelencét találtál. Fölemeled, és látod, hogy nyitható a teteje.
\nHa ki akarod nyitni a tubákosszelencét: 41\n
\nHa inkább visszadobod a homokba és a lábnyomokat követve folytatod utadat: 325
"""
        this_scene = Action()
        return this_scene.choice('41','325')

class Scene_120(Scene):

    def enter(self):
        print """
A „Goncsong" név hallatán a Hobgoblint félelem tölti el.
Rémülten felordít, és rád szegezi a dárdáját..."""
        this_scene = Action()
        return this_scene.luck('62','240')

class Scene_121(Scene):

    def enter(self):
        print """
Az Elfek és a férfiak arcán boldog mosoly jelenik meg, amikor a második Ork is
holtan terül el. A Törpék leoldják a foglyok láncait, és most már tizennégy ba-
rátod van, aki segít terved végrehajtásában. Egyikük az Osztriga-öbölből való.
Bár boldog, hogy esetleg kiszabadul, elszomorítja Mungo halálának híre. Munka-
eszközeikkel felfegyverezve a foglyok felkérnek, hogy légy a vezérük, és vezesd
őket a Gyíkkirály kőerődítményébe, ahol a király őrei és elit gárdája védelme
alatt lakik. Elfogadod az ajánlatukat, és ismét visszafordulsz a vágatokba, hogy
kiszabadítsd a többi bányászfoglyot.."""
        this_scene = Action()
        return this_scene.dice_3('251','293','32')

class Scene_122(Scene):

    def enter(self):
        print """
Letörlöd a sűrű vért kardod pengéjéről, és ismét nyugati irányba indulsz.
Útközben arra gondolsz, vajon miféle teremtmény leselkedhet még rád itt a mocsárvilágban?
"""
        this_scene = Action()
        return this_scene.end_turn('37')

class Scene_123(Scene):

    def enter(self):
        print """
Bár a Gyíkkirály iszonyatosan fél, a Goncsong arra kényszeríti, hogy támadjon
rád lángpallosával. A lángtól megriadva majmod leugrik a válladról, és eltűnik.
Ekkor a Gyíkkirály, akinek félelme elszállt, dühödt kegyetlenséggel támad rád.
"""
        this_scene = Action()
        return this_scene.end_turn('346')

class Scene_124(Scene):

    def enter(self):
        print """
A kígyó mérge túl erős ahhoz, hogy szervezeted legyőzze, így elájulsz..."""
        this_scene = Action()
        return this_scene.luck('156','357')

class Scene_125(Scene):

    def enter(self):
        print """
Majdnem belehalsz a fájdalomba, amikor a Sámán
odalép hozzád, és elveszi tőled a csontokat..."""
        this_scene = Action()
        this_scene.add_saman_proba('Fajdalom')
        this_scene.print_saman_proba_k()
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_126(Scene):

    def enter(self):
        print """
A hátizsákodból három adag Élelmet veszel elő, és elosztod a Pigmeusok között.
Mindegyik megszagolja, mielőtt belekóstolna. Hirtelen egymásra néznek, és hang-
osan utálkozva kiköpik a falatot a szájukból. Az egyik jelt ad a többieknek,
hogy támadjanak rád, de amint kihúzza kőbunkóját az övéből, a gyomrához kap
és elvágódik. A többiek is tántorogni kezdenek; a te ételedtől lettek rosszul.
Nem vesztegeted tovább az időt, és amilyen gyorsan csak tudsz, nekivágsz
a dzsungelnak nyugati irányba... """
        this_scene = Action()
        this_scene.item_dict_sack_neg('Kaja','-3')
        return this_scene.end_turn('7')

class Scene_127(Scene):

    def enter(self):
        print """
A Hobgoblin természetesen elég buta ahhoz, hogy elhiggye: te a Gyíkkirály
egyik őre vagy. Neked szegezi a dárdáját, és mély hangján a következőt kérdi:
- Jelszó? - Mit válaszolsz?
\n"Tessék?" 193\n
\n"Goncsong" 120\n
\n"Tűz-sziget" 287\n """
        this_scene = Action()
        return this_scene.choice_3('193','120','287')

class Scene_128(Scene):

    def enter(self):
        print """
A tó vize tisztának, frissnek látszik, bár kissé zavar az a zöld alga, ami a
felszínén úszik. Amikor lehajolsz, hogy igyál, a tó közepe felöl hirtelen fel-
bukkanó hatalmas zöld szájból jókora vízsugár tör elő..."""
        this_scene = Action()
        return this_scene.agi('248','351')

class Scene_129(Scene):

    def enter(self):
        print """
Elveszed a botot a varázslótól, de abban a pillanatban, amikor megérinted, tüzes
vasrúddá változik. Veszítesz 2 Életerő, 1 Ügyesség és 1 Szerencse pontot, amiért
oly meggondolatlanul rátámadtál a Sámánra. Eldobod a vasrudat, és még mindig nem
akarod elhinni, hogy mi történt.
\nHa beszélni akarsz a Sámánnal: 324\n
\nHa inkább megtámadod a kardoddal: 157\n"""
        this_scene = Action()
        return this_scene.choice('324','157')

class Scene_130(Scene):

    def enter(self):
        print """
Egy jól irányzott balhoroggal leteríted a férfit, majd belököd a folyóba. Ordít,
de nem próbál meg visszamászni a tutajodra. Lelkiismeret-furdalásod van, amiért
magára hagyod, de tovább kell menned, hogy teljesítsd küldetésedet..."""
        this_scene = Action()
        return this_scene.end_turn('14')

class Scene_131(Scene):

    def enter(self):
        print """
Nem vagy ura az akaratodnak, és üvölteni kezdesz. Megbuktál a próbán!
A Sámán ezek után nem árulja el neked a titkát. A gonosz, úgy látszik,
eltűnik, és a Sámán délkeleti irányba mutat, mondván, hogy arra van a
fogolytábor, továbbá közli, hogy a Goncsongot egyedül, az ő segítsége
nélkül kell legyőznöd. Megfordulsz és elindulsz lefelé a tűzhányó ol-
dalában, hogy megtaláld a Gyíkkirály erődítményét."""
        y = raw_input('> ')
        return '168'


class Scene_132(Scene):

    def enter(self):
        print """
Kinyújtod a kezedet, amennyire csak tudod, de képtelen vagy elérni a kardodat.
Az inda egyre szorosabban tekeredik a nyakad köré, és rövidesen elveszted az
eszméletedet. A húsevő fa zsákmánya lettél. """
        return 'x'

class Scene_133(Scene):

    def enter(self):
        print """
A mutáns pajzsát magadhoz veszed, mert az könnyű, de ugyanakkor erős is.
\nNyertél 1 Ügyesség pontot!\n
A fogolytábor már egészen közel lehet; nem vesztegeted tovább az időt, ismét útnak indulsz.
"""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg',1)
        return this_scene.end_turn('218')

class Scene_134(Scene):

    def enter(self):
        print """
Fokozatosan visszanyered a látásodat, és kardodat visszadugod a hüvelyébe.
\nHa továbbra is inni akarsz a tóból: 92\n
\nHa inkább továbbmész nyugati irányba: 222\n"""
        this_scene = Action()
        return this_scene.choice('92','222')

class Scene_135(Scene):

    def enter(self):
        print """
Ha a kereszteződéstől folytatod az utat egyenesen előre: 39\n
\nha jobbra: 361"""
        this_scene = Action()
        return this_scene.choice('39','361')

class Scene_136(Scene):

    def enter(self):
        print """
Korbácsodat beledugod az övedbe, és eldöntöd, mit csinálj.
\nHa fel akarod kapni a rozsdás kést: 275\n
\nHa inkább egyenesen odamész a legtávolabbi ajtóhoz: 312 """
        this_scene = Action()
        return this_scene.end_turn('275','312')

class Scene_137(Scene):

    def enter(self):
        print """
Kézzel-lábbal magyarázod a Pigmeusoknak, hogy semmit nem adsz nekik.
Azok mérgükben feléd hajítanak egy dárdát..."""
        b = 0 - int(randint(1,6))
        this_scene = Action()
        this_scene.act_att_change('eletero',b)
        return this_scene.end_turn('373')

class Scene_138(Scene):

    def enter(self):
        print """
Az egyik Ork kardjával rád támad, és meg kell küzdened vele!"""
        this_scene = Action()
        return this_scene.battle(7,7,'Ork Őr',0,'121')

class Scene_139(Scene):

    def enter(self):
        print """
Ismét elindulsz délkeleti irányba a homokon és sziklákon át. Egyszer csak egy
dinosaurushoz hasonló paripa hátán lovagló, állig felfegyverzett hüllő állja el
az utadat. Egy mutáns Gyíkemberrel van dolgod, aki egy Styracosaurus hátán köze-
lít feléd. A Gyíkember ügetésbe kezd, s rád támad."""
        this_scene = Action()
        return this_scene.battle(11,10,'Styracosaurus',0,'95')

class Scene_140(Scene):

    def enter(self):
        print """
A földre zuhansz, de nem sérülsz meg. Felállsz, de nem jutsz messzire, mert a vágat
csakhamar véget ér. Nincs más választásod, vissza kell térned az előző elágazáshoz.
"""
        this_scene = Action()
        return this_scene.end_turn('378')

class Scene_141(Scene):

    def enter(self):
        print """
Ismét útnak indulsz, hogy megkeresd a Sámánt..."""
        this_scene = Action()
        return this_scene.end_turn('399')

class Scene_142(Scene):

    def enter(self):
        print """
Futás közben hátranézel, hogy megtudd, követ-e a lány a Tigrissel. Szerencsére
sehol nem látod őket. Lassítasz, és leballagsz a szurdokba, hogy csatlakozz a
felszabadult foglyokhoz..."""
        this_scene = Action()
        return this_scene.end_turn('279')

class Scene_143(Scene):

    def enter(self):
        print """
Letépsz néhány levelet a tölcsér alakú növényről, és dühösen megdörzsölöd vele
feldagadt arcodat. Azonnal megkönnyebbülsz, a viszketés szerencsére elmúlik.
\nHa még mindig meg akarod enni a gombát: 110\n
\nHa inkább továbbmész a dzsungelban: 224\n """
        this_scene = Action()
        return this_scene.choice('110','224')

class Scene_144(Scene):

    def enter(self):
        print """
Kardod átdöfi a Gyíkember szívét, aki azonnal kimúlik..."""
        this_scene = Action()
        return this_scene.end_turn('173')

class Scene_145(Scene):

    def enter(self):
        print """
Lassan bedugod a kezedet a lyukon, és megdermedsz a félelemtől, amikor meghallod
az ismerős csörgő hangot. Megpróbálod kihúzni a kezedet, még mielőtt a Csörgőkígyó
méregfoga belevájna a karodba, de az fürgébb, mint te: mérge a véredbe kerül.
Amilyen gyorsan csak tudod, kardoddal felvágod a sebedet, hogy jól kivérezzen.
"""
        this_scene = Action()
        this_scene.bonus_att_change('csörgőkígyómarás')
        return this_scene.check_att('eletero',18,'55','264')

class Scene_146(Scene):

    def enter(self):
        print """
A bokor tüskéi mérgezőek. 3 Életerő pontot vesztesz!
Ha még életben vagy, továbbvonszolod magad a fogolytábor irányába."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        return this_scene.end_turn('291')

class Scene_147(Scene):

    def enter(self):
        print """
A kunyhók mögött ösvény vezet a fák között egy magas hegy sziklás falához.
A sziklafal közepén nyílik a bánya négyszögletes bejárata. Sok lábnyom vezet
be- és kifelé. Óvatosan belépsz a bányába, s a falhoz lapulva haladsz. A vágatot
fáklyák világítják meg, hátborzongató árnyakat vetítve a falakra. Érzed, hogy az
út lejt, és hamarosan egy elágazáshoz érsz.
\nHa balra mész: 274\n
\nHa jobbra indulsz: 28\n"""
        this_scene = Action()
        return this_scene.choice('274','28')

class Scene_148(Scene):

    def enter(self):
        print """
Búvóhelyedtől nem messze néhány banánfát találsz. A gyümölcsöt a földről nem
éred el, ezért fel kell másznod a fára..."""
        this_scene = Action()
        return this_scene.luck('80','13')

class Scene_149(Scene):

    def enter(self):
        print """
Az öregember elveszi az ételt, és szénnel lerajzolja a sziget térképét egy darab
rongyra. Megjelöli rajta azt a helyet, ahol most vagy, és azt is, hogy hol talál-
ható a bánya meg a fogolytábor, ahol a Gyíkkirály él. Összehajtogatod a térképet,
és a hátizsákodba teszed. Már épp le akarsz ereszkedni az indán, amikor az öreg
így szól: - Még egy kis ételért cserébe adok neked valami igazán hasznosat!
"""
        this_scene = Action()
        return this_scene.choice('90','375')

class Scene_150(Scene):

    def enter(self):
        print """
Valahogy sikerül megmenekülnöd a dühöngő zuhatag elől, és kifulladva terülsz el a jobb
parton. Miközben kimerülten fekszel a mocsárban, a Víziszörny dühe elcsitul mögötted."""
        this_scene = Action()
        return this_scene.luck('104','159')

class Scene_151(Scene):

    def enter(self):
        print """
A Sámán átnyújtja neked a két csontot, és megkér, hogy fogj egyet-egyet a jobb
és bal kezedbe. Izmaid megfeszülnek, és úgy érzed, belülről majd szétfeszít va-
lami, mindjárt szétrobbansz, és iszonyatos fájdalom kínoz..."""
        this_scene = Action()
        return this_scene.choice('67','125')

class Scene_152(Scene):

    def enter(self):
        print """
A ház mögött keskeny kis ösvény vezet fel a sziklához. Elindulsz felfelé, s mire
felérsz, jól kifulladsz. Nagyot húzol a kulacsodból, és megállapítod, hogy
nemsokára fogytán lesz az ivóvized. Nyugat felé nézel, és a fák mögött, ijesztően
közel, az alvó tűzhányót pillantod meg. Életnek semmi jelét nem tapasztalod -
tisztán hallod a madarak csivitelését és a bogarak zümmögését. A rohamosan le-
ereszkedő szürkületben úgy döntesz, letáborozol éjszakára az egyik szikla tövében.
Nem alszol valami jól, s a nap első sugarainak fényére azonnal felébredsz.
Máris útnak indulsz. Elhatározod, hogy egyenesen nyugati irányba mész, a fák felé.
"""
        y = raw_input('> ')
        return '391'

class Scene_153(Scene):

    def enter(self):
        print """
Utolsó, végzetes csapásod a földre kényszeríti a Gyíkkirályt. Mit teszel?
\nMegfordulsz és köszöntöd a seregedet: 188\n
\nLevágod a Goncsong fullánkját: 384\n
\nÁtkutatod a Gyíkkirály ruháját: 54"""
        this_scene = Action()
        return choice_3('188','384','54')

class Scene_154(Scene):

    def enter(self):
        print """
Megbotlasz egy kőben. Miközben megpróbálsz egyensúlyozni,
hogy fel ne bukj, elejted a kardodat..."""
        this_scene = Action()
        return this_scene.luck('38','319')

class Scene_155(Scene):

    def enter(self):
        print """
A vörös por mágikus ereje segít, hogy ura légy önmagadnak.
Lassan-lassan túljutsz a borzalmakon..."""
        this_scene = Action()
        this_scene.add_saman_proba('Felelem')
        this_scene.print_saman_proba_k()
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_156(Scene):

    def enter(self):
        print """
Bár már közel jártál a halálhoz, mégis sikerült legyőznöd a kígyó mérgét.
A méreg azonban igencsak legyengített. Végül is visszanyered az eszméletedet
és kipihened magad, de veszítesz 5 Ügyesség és 4 Életerő pontot.
\nHa ki akarod piszkálni a Csörgőkígyót a kardoddal: 5\n
\nHa inkább óvatosan leereszkedsz a szurdokba
és egyenesen nyugati irányba mész: 119"""
        this_scene = Action()
        return this_scene.choice('5','119')

class Scene_157(Scene):

    def enter(self):
        print """
Végzetes tévedés volt, hogy megtámadtad a hatalmas varázslót. Egy kicsiny dal,
mely ajkáról száll föl, kardodat tekergő kígyóvá változtatja. A kígyó a karodra
csavarodik. Felordítasz fájdalmadban, és megpróbálod lerázni az állatot. Igyeke-
zeted azonban hiábavalónak bizonyul, mert a kígyó mérge szinte azonnal végez veled.
"""
        this_scene = Action()
        return this_scene.end_turn('x')

class Scene_158(Scene):

    def enter(self):
        print """
Egyre puhább és puhább lesz a talaj a lábad alatt, mígnem egyszer csak térdig
süppedsz a fekete mocsárban. Csak nehezen tudsz lépkedni, és egyre jobban aggódsz:
az egész területet víz borítja, csupán itt-ott látni egy kicsinyke nádast. De azért
elszántan mész tovább, mígnem közvetlenül előtted egy tapogató kar nyúlik ki a feke-
te vízből, aztán egy másik követi, majd lassan egy rémes, poliphoz hasonló, rücskös
bőrű, sötétzöld színű vadállat emelkedik ki hat lábán a vízből. Ez nem más, mint az
undorító Iszapszívó, mellyel meg kell küzdened!"""
        this_scene = Action()
        return this_scene.check_item_list_sack('Dárda','394','158b')

class Scene_158b(Scene):
    def enter(self):
        this_scene = Action()
        return this_scene.battle(10,9,'Iszapszívó',0,'122')

class Scene_159(Scene):

    def enter(self):
        print """
Túlságosan is arra koncentráltál, hogy ne fulladj bele a habokba, így nem vetted
észre, hogy a vízsugár letépte a hátadról a hátizsákodat.
\nMinden élelmed, sőt a zsákodban tartott többi dolgod is elúszott.\n
\nVeszítesz 2 Szerencse pontot.\n
Hüvelyében pihenő kardod és viselt dolgaid szerencsédre megmaradtak.
Nincs más választásod, gyalog kell folytatnod az utat..."""
        this_scene = Action()
        this_scene.empty_sack()
        this_scene.act_att_change('szerencse','-2')
        return this_scene.end_turn('197')

class Scene_160(Scene):

    def enter(self):
        print """
Dongást hallasz a fejed fölött, és egy Óriásdarazsat pillantasz meg, amint épp
lecsapni készül rád, mivel a gyümölcs édes illata odacsalta. Az utolsó pillanat-
ban rántod elő a kardodat, hogy megvédd magad..."""
        this_scene = Action()
        return this_scene.battle_sting(6,6,'Óriásdarázs','52','141')

class Scene_161(Scene):

    def enter(self):
        print """
Felöltöd a Gyíkember páncélját, hogy álcázd magad, a Törpéket pedig libasorba
állítod, hagy azt a látszatot keltsék, mintha össze lennének láncolva. Mosolyogva
csapkodsz a levegőbe a korbáccsal, és hajtod a Törpéket a vágaton lefelé. Követed
őket a végeláthatatlan alagutakban, egyre lejjebb, a bánya mélyébe. Ahogy elhaladsz
egy másik vágatrendszer mellett, egy Gyíkembert pillantasz meg, amint feléd tart...
"""
        this_scene = Action()
        return this_scene.luck('74','262')

class Scene_162(Scene):

    def enter(self):
        print """
Hiába rángatod a kilincset, az ajtó nem nyílik.
\nHa be akarod törni: 50\n
\nHa inkább visszamész az erődítmény udvarára és más ajtókkal próbálkozol: 84
"""
        this_scene = Action()
        return this_scene.choice('50','84')

class Scene_163(Scene):

    def enter(self):
        print """
A Gyíkemberek észrevesznek, és gyorsan reagálnak..."""
        this_scene = Action()
        this_scene.battle(9,8,'Első Gyíkember',1,'368')
        return this_scene.battle(8,8,'Második Gyíkember',0,'368')

class Scene_164(Scene):

    def enter(self):
        print """
A Goblin mélyen alszik, és nem ébred fel. Szép csöndben elhagyod a szobát,
és magaddal viszed a mellvértjét. A folyosón magadra öltöd - épp hogy beleférsz.
\nNyersz 1 Ügyesség pontot.\n
Becsukod a Goblin ajtaját és elindulsz a csigalépcső felé..."""
        this_scene = Action()
        this_scene.item_equipped('páncél','Goblin Mellvért')
        this_scene.act_att_change('ugyesseg','1')
        return this_scene.end_turn('8')

class Scene_165(Scene):

    def enter(self):
        print """
Mungo körül a homok vörös a vértől. Letérdelsz mellé, és óvatosan a karodba
emeled a fejét. Kissé kinyitja a szemét. Bár haldoklik, halványan elmosolyodik.
Suttogva így szól: - Hát elfogtuk őket, de mi hasznom belőle? Fogadd meg, hogy
elkapod a Gyíkkirályt! Ugye megfogadod? - Ekkor lecsukódik a szeme, és holtan
esik össze. A parton, a szikla tövében temeted el, és sírját a homokba szúrt
kardjával jelölöd meg. Keskeny kis ösvényt veszel észre, amely a szikla oldalá-
ban visz fel a csúcsra, majd visszanézel, és megpillantod a ládát a parton.
\nHa úgy döntesz, hogy felmész az ösvényen: 200\n
\nHa inkább kinyitod a ládát: 398 """
        this_scene = Action()
        return this_scene.choice('398','200')

class Scene_166(Scene):

    def enter(self):
        print """
Amint belépsz a cellába, csodálkozva tapasztalod,
hogy az öregember meg se szólal..."""
        this_scene = Action()
        return this_scene.check_equipped('gyűrű','Varázsgyűrű','294','318')

class Scene_167(Scene):

    def enter(self):
        print """
Kardoddal hadonászva rohansz a disznó után, de az igencsak fürge. Átrohan a tisztáson,
és hamarosan eltűnik a szemed elől. Lassítasz, és nyugati irányba haladva még mindig
arra gondolsz, hogy milyen fenséges disznóvacsoráról kell lemondanod..."""
        this_scene = Action()
        return this_scene.end_turn('170')

class Scene_168(Scene):

    def enter(self):
        print """
Gyorsan haladsz délkelet felé, abban a reményben, hogy foglyokkal találkozol:
a kiszabadított foglyokkal. Hamarosan egy szakadék széléhez érsz, amely túl
széles ahhoz, hogy átugord. Kelet felé veszed az utadat, s dühöngsz, amiért
időt veszítesz. Egy kőhidat látsz magad előtt, mely összeköti a szakadék két
peremét, de egy felfegyverzett Hobgoblin áll őrt mellette. Mit teszel?
\nMegpróbálsz valamilyen csellel átjutni a kőhídon: 127\n
\nFelajánlasz a Hobgoblinnak egy aranyrögöt
(ha van ilyen a birtokodban), hogy átengedjen: 252\n
\nMegtámadod a kardoddal: 328"""
        this_scene = Action()
        return this_scene.choice_3('127','252','328')

class Scene_169(Scene):

    def enter(self):
        print """
A Fejvadászok sokkal otthonosabban mozognak a dzsungelban, mint te, és csakhamar
utolérnek. Szembefordulsz és megküzdesz velük. Szerencsére a bozótban túl keskeny
az ösvény ahhoz, hogy egyszerre egynél több Fejvadásszal kelljen összecsapnod.
"""
        this_scene = Action()
        this_scene.battle(7,6,'Első Fejvadász',2,'261')
        this_scene.battle(6,6,'Második Fejvadász',1,'261')
        return this_scene.battle(6,7,'Első Fejvadász',0,'261')

class Scene_170(Scene):

    def enter(self):
        print """
A távolban egy hegy magaslik, és mögötte északnyugatra megpillantod az alvó
tűzhányó ijesztő körvonalait. Kisvártatva eléred a délkeleti irányba hömpölygő
folyó bozótos partját. A túlpart elég meredek és erdő borítja..."""
        this_scene = Action()
        return this_scene.check_bonus_att('uzenet','288','88')

class Scene_171(Scene):

    def enter(self):
        print """
Odakúszol a tűzhöz abban reménykedve, hogy a Fejvadászok figyelmét túlságosan is
leköti rituális szertartásuk, és nem vesznek észre.
Tedd próbára a Szerencsédet!"""
        y = raw_input('> ')
        this_scene = Action()
        return this_scene.luck('215','302')

class Scene_172(Scene):

    def enter(self):
        print """
Hamarosan visszajutsz egy újabb elágazáshoz...
\nHa továbbra is egyenesen előre akarsz menni: 383\n
\nHa jobbra akarsz fordulni: 4\n"""
        this_scene = Action()
        return this_scene.choice('383','4')

class Scene_173(Scene):

    def enter(self):
        print """
A Törpe kegyelemért könyörög, amint a Gyíkember a földre rogy... """
        this_scene = Action()
        return this_scene.check_item_list_sack('Tolvajkulcs','393','216')

class Scene_174(Scene):

    def enter(self):
        print """
A pép keserű, és a szád zsibbadni kezd tőle. Verejtékezel, és úgy érzed, hogy a
tested erőtől duzzad. Nyersz 2 Életerő pontot. Felkapod a kardodat, és újult
erővel ismét nekivágsz az útnak nyugati irányba."""
        this_scene = Action()
        this_scene.act_att_change['eletero','2']
        y = raw_input('> ')
        return '113'

class Scene_175(Scene):

    def enter(self):
        print """
Sikerül hátrálva kimásznod a kőtörmelék alól. Leporolod a ruhádat, és visszatérsz
az utolsó elágazáshoz, ugyanis már nem tudsz továbbmenni, mert a vágat beomlott.
\nAmint visszaérsz az elágazáshoz, elindulhatsz balra: 172\n
\nVagy mehetsz egyenesen: 278"""
        this_scene = Action()
        return this_scene.choice('172','278')

class Scene_176(Scene):

    def enter(self):
        print """
A Sámán megrázza tollakkal díszített botját, mely kereplő hangot ad. Ellenségnek
tart, mert nem adtad jelét baráti érzelmeidnek. Mit teszel?
\nMegpróbálsz beszélni vele: 324\n
\nMegpróbálod kiütni a kezéből a tollas végű botot: 129\n
\nKarddal támadsz rá: 157\n"""
        this_scene = Action()
        return this_scene.choice_3('324','129','157')

class Scene_177(Scene):

    def enter(self):
        print """
A Fejvadászoknak a fegyverükön kívül más felszerelésük nem volt, viszont elrej-
tettek egy banánnal és kókusszal teli zsákot. Úgy döntesz, hogy nem a saját
Élelmiszerkészletedből fogyasztasz, hanem megeszed a Fejvadászok gyümölcsét.
\nNyersz 1 Életerő pontot!\n
Kíváncsi vagy, vajon milyen közel lehet a falu, ahonnan jöttek. Felmászol egy fa
tetejére, hogy jobban körülnézhess. A magasból látod, amint délnyugatra, elég
közel hozzád, füst száll a magasba. Valószínűleg az ő falujuk lehet ott. Nyugatra
egyre ritkulnak a fák, északnyugaton pedig a távolban megpillantod a tűzhányó
félelmetes körvonalát. Lemászol a fáról, és eldöntöd, merre menj tovább.
\nHa délnyugat felé folytatod az utadat: 229\n
\nHa inkább északnyugati irányba mész, hogy megkerüld a füstöt: 12
"""
        this_scene = Action()
        this_scene.act_att_change('eletero','1')
        return this_scene.choice('229','12')

class Scene_178(Scene):

    def enter(self):
        print """
Egy kis magaslaton, tükörfényesre csiszolt kövek gyűrűjében, különböző tárgyak
láthatók: egy karkötő, egy agyagbaba, egy vékony korsó meg egy csont, hogy csak
néhányat említsünk az ott heverő dolgok közül. Ezek valószínűleg a Sámánnak szánt
adományok.
\nHa te is szeretnél itt elhelyezni valamilyen tárgyat: 233\n
\nHa inkább elvennél valamit a tárgyak közül: 306"""
        this_scene = Action()
        return this_scene.choice('233','306')

class Scene_179(Scene):

    def enter(self):
        print """
Rövid idő alatt sikerül annyi fát kivágnod, amennyi egy kis tutaj elkészítéséhez
elegendő. A szálfákat indákkal erősíted egymáshoz, majd vízre bocsátod a tutajt.
Egy hosszú, vékony ággal kormányozva lököd előre magad, és elindulsz fölfelé a folyón...
"""
        this_scene = Action()
        return this_scene.end_turn('387')

class Scene_180(Scene):

    def enter(self):
        print """
A vágat élesen jobbra kanyarodik. A fordulóban egy csigalépcsőhöz érsz, amely a
toronyba vezet. Valami azt súgja, hogy menj fel a lépcsőn..."""
        this_scene = Action()
        return this_scene.end_turn('82')

class Scene_181(Scene):

    def enter(self):
        print """
Kevés reményed van rá, de mégis megpróbálod, hogy varázszsákoddal foglyul ejtsd
a Víziszörnyet. Kinyitod a zsák száját, amilyen nagyra csak tudod, és várod,
hogy a Víziszörny lecsapjon rád..."""
        this_scene = Action()
        return this_scene.luck('230','257')

class Scene_182(Scene):

    def enter(self):
        print """
Kivont karddal rárontasz az Óriásrákra. Az kiereszti szorításából Mungót, hogy
így mindkét ollójával rád támadjon."""
        this_scene = Action()
        return this_scene.battle(10,11,'Óriásrák',0,'366')

class Scene_183(Scene):

    def enter(self):
        print """
A Sámán rád csap a botjával, ettől testedet kukacok lepik el. A szádban és a füledben
nyüzsögnek..."""
        this_scene = Action()
        return this_scene.check_equipped('gyűrű','Varázsgyűrű','64','283')

class Scene_184(Scene):

    def enter(self):
        print """
Megbotlasz egy kőben, de nem esel el és nem csapsz zajt.
\nNyersz 1 Szerencse pontot.\n
Megkönnyebbülten felsóhajtasz, és követed a Gyíkembert..."""
        this_scene = Action()
        this_scene.act_att_change('szerencse','1')
        return this_scene.end_turn('51')

class Scene_185(Scene):

    def enter(self):
        print """
Magasba emelt kardoddal ráveted magad a hozzád
legközelebb álló ellenfélre, egy mutáns Gyíkemberre..."""
        this_scene = Action()
        return this_scene.battle(8,9,'Mutáns Gyíkember',0,'341')

class Scene_186(Scene):

    def enter(self):
        print """
Amikor előveszed a hátizsákodat, már szinte haldokolsz az éhségtől. Befalsz
egy adagot az Élelmiszerkészletedből, és bemászol a rejtekhelyedre. Az égen,
ahogy leszáll az este, fenyegető bíborvörös és mályvaszínű felhők gyülekeznek.
Bár ezernyi rovar fülsiketítő hangon zajong körülötted a kellemes, hűvös éjsza-
kában, te mégis gyorsan elalszol..."""
        this_scene = Action()
        this_scene.item_dict_sack_neg('Kaja','1')
        return this_scene.luck('388','348')

class Scene_187(Scene):

    def enter(self):
        print """
A zsákban csupán néhány összegöngyölt széles levél van. Amint összenyomod őket,
úgy érzed, mintha a belsejükben valamilyen pép vagy sűrű massza lenne. Kiteker-
geted a leveleket, és világoszöld masszát találsz bennük. Mit teszel?

Ha, megpróbálod mire jó a massza: 187b

Ha, nem nyúlsz a masszához, hanem továbbmész nyugati irányba: 113
"""
        this_scene = Action()
        return this_scene.choice('187b','113')

class Scene_187b(Scene):

    def enter(self):
        print """
Ha, masszából rákensz egy keveset a sebeidre: 377

Ha, eszel egy keveset a masszából: 174
"""
        this_scene = Action()
        return this_scene.choice('377','174')

class Scene_188(Scene):

    def enter(self):
        print """
Nagy könnyelműséget követsz el azzal, hogy hátat fordítasz a félelmetes Goncsongnak.
Harcosaidnak alig van idejük rá, hogy megünnepeljék a Gyíkkirály felett aratott győ-
zelmedet, ugyanis Goncsong, fullánkját kihúzva, átpattan a fejedre. Tűhegyes fullánk-
ja a homlokodba fúródik, és belemélyed az agyadba. Ettől a pillanattól kezdve a Gon-
csong uralkodik az akaratod felett, és csupán tehetetlenül szemlélheted, amint a
Gyíkkirály serege megsemmisíti demoralizált csapatodat. A csatát elvesztetted...
"""
        this_scene = Action()
        return this_scene.end_turn('x')

class Scene_189(Scene):

    def enter(self):
        print """
Mielőtt az eszméletét vesztett Gyíkember magához térne, átkutatod a zsebeit.
Három vaskulcsot találsz. Magadhoz veszed és zsebre vágod őket. Ezután hátrakötöd
mindkét kezét, és behúzod a kunyhóba. Amint magához tér, követeled, hogy árulja el,
mit tud a fogoly bányászokról? Elmondja, hogy a bánya bejárata nincs messze - vagy
százméternyire van a kunyhók mögött. Kikötöd a Gyíkembert egy póznához, és elhagyod
a kunyhót, hogy megkeresd a bányákat..."""
        this_scene = Action()
        this_scene.item_list_sack('Három Vaskulcs')
        return this_scene.end_turn('147')

class Scene_190(Scene):

    def enter(self):
        print """
Amikor megérinted a kardod markolatát, a bennszülött lány elengedi a fenevad
pórázát. A Tigris egy ugrással rád veti magát...
\nVesztettél 2 Életerő pontot!\n
Ha még mindig életben vagy, elő tudod rántani a kardodat, hogy megvédd magad...
"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        return this_scene.battle(11,8,'Kardfogú Tigris',0,'343')

class Scene_191(Scene):

    def enter(self):
        print """
A kezed csúszik az iszaptól: nem találod el a hatalmas Iszapszívót, dárdád
beleesik a vízbe. Most már a kardoddal kell legyőznöd az Iszapszívót!"""
        this_scene = Action()
        this_scene.rem_item_list_sack('Dárda')
        return this_scene.battle(10,9,'Iszapszívó',0,'122')

class Scene_192(Scene):

    def enter(self):
        print """
Úgy döntesz, hogy elindulsz a vágatban lefelé, de az csakhamar véget ér.
Nincs más választásod, vissza kell menned az elágazáshoz..."""
        this_scene = Action()
        return this_scene.end_turn('57')

class Scene_193(Scene):

    def enter(self):
        print """
A Hobgoblin bután rád mereszti a szemét és így szól: - Igen, helyes a válasz;
a „Tessék" a jelszó. Átkelhetsz a hídon. - Félreáll az útból, te pedig gyorsan
átmész a szakadék túloldalára..."""
        this_scene = Action()
        return this_scene.end_turn('139')

class Scene_194(Scene):

    def enter(self):
        print """
A hegy oldalában haladsz a szurdok mentén. Amint föltekintesz a magasba,
észreveszed, hogy a szurdok másik oldalán hegyomlás kezdődik: hatalmas
kövek és szikladarabok zuhannak a mélybe. Bár nincs ínyedre a hegymászás,
mégis megkönnyebbülsz, hogy nem vagy a szurdokban.
\nNyersz 1 Szerencse pontot!\n
\nHa továbbra is itt a hegy oldalában akarod folytatni az utadat: 83\n
\nHa viszont megkockáztatod, hogy lemenj a szurdokba: 382"""
        this_scene = Action()
        this_scene.act_att_change('szerencse','1')
        return this_scene.choice('83','382')

class Scene_195(Scene):

    def enter(self):
        print """
Az ajtó egy koszos, nyomorúságos szobába nyílik. A kis rácsos ablakon beszűrődő
napsugarak megvilágítják a szemközti falat. A szoba egyik sarkában lévő szalma-
matracon egy Goblin horkol. Az ágya fölött egy szögön vas mellvért lóg.
\nHa be akarsz osonni a szobába, hogy ellopd a mellvértet: 333\n
\nHa inkább becsukod az ajtót és visszamész a csigalépcsőhöz: 8\n"""
        this_scene = Action()
        return this_scene.choice('333','8')

class Scene_196(Scene):

    def enter(self):
        print """
Megkerülöd az Óriásgyík hatalmas testét, és sietve továbbmész a szurdokban,
amely végre szélesedni kezd, s egy füves réthez érsz. A hegyek lassan elma-
radnak mögötted. Balra, nem túl messze, talán tíz méterre, egy tavat látsz,
melyből madarak iszogatnak...
\nHa inni akarsz a tó vizéből: 128\n
\nHa inkább tovább folytatod az utat nyugati irányba: 222"""
        this_scene = Action()
        return this_scene.choice('222','128')

class Scene_197(Scene):

    def enter(self):
        print """
Látod, amint a nap lassan lemegy nyugaton. Olyan, mintha egy nagy piros léggömb
úszna a vízen. Hamarosan eltűnik, leszáll az este. Úgy döntesz, letáborozol két
szikla között. A sziklákra ágakat fektetsz, és leveleket szórsz rájuk. Igencsak
megéheztél a folyón átélt megpróbáltatások után, és sürgősen enni akarsz valamit...
"""
        this_scene = Action()
        this_scene.check_item_dict_sack('Kaja','186','148')
        return this_scene.end_turn()

class Scene_198(Scene):

    def enter(self):
        print """
Az elhagyatott ház telis-tele van ócska bútorral, törött cserépedénnyel és
mindenféle rongyos ruhával. Elrúgod a szőnyeget, és egy fogantyút veszel észre
a padlóban - csapóajtót találtál.

Ha fel akarod emelni a csapóajtót: 267

Ha inkább úgy döntesz, hogy elhagyod a házat: 152
"""
        this_scene = Action()
        return this_scene.choice('267','152')

class Scene_199(Scene):

    def enter(self):
        print """
A Sámán figyelmesen végighallgatja, amit a Gyíkkirályról és a vele kapcsolatos
tervedről elmondasz. Szeretnéd megtudni azt is, miként ölhetnéd meg a parazita
Goncsongot, hogy ezáltal csökkentsd a király erejét. A Sámán nagyot ugrik a
Goncsong név hallatán. Nyilvánvalóan fogalma sem volt róla, hogy akár egy is
akad belőle a szigeten. Akadozó nyelvvel közli, hogy elárulja neked a varázstitkokat,
de ezt ki kell érdemelned, bármily nemes is a küldetésed. A próba fájdalmas lesz és nehéz.
\nHa elfogadod a Sámán feltételeit: 397\n
\nHa nem akarod elsajátítani a Sámán tudományát,
és anélkül akarsz a Gyíkkirállyal megküzdeni: 237\n"""
        this_scene = Action()
        return this_scene.choice('397','237')

class Scene_200(Scene):

    def enter(self):
        print """
Fölfelé indulsz a keskeny ösvényen és alaposan kifulladsz, mire felérsz. Iszol
egy korty vizet a kulacsodból, és megállapítod, hogy nemsokára gondjaid lesznek
az ivóvízzel a szigeten. Nyugat felé nézve megpillantod a fák mögül kimagasló
alvó tűzhányó félelmetes körvonalait, de életnek semmi jelét nem tapasztalod -
bár hallod a madarak és rovarok kakofonikus zenéjét. Az egyre sötétebb alkonyat-
ban elhatározod, hogy letáborozol az egyik szikla tövében. Nem alszol valami jól,
és a nap első sugaraira felébredsz. Máris elindulsz. Egyenesen nyugat felé tar-
tasz, bemész a fák közé."""
        y = raw_input('> ')
        return '391'

class Scene_201(Scene):

    def enter(self):
        print """
Csapatadat kivezeted a bányából, és megtámadjátok a sárkunyhókat, ahol az örök
laknak. Miután az utolsóval is végeztek, a foglyok üdvrivalgásban törnek ki, és
énekelve ünneplik győzelmüket. Egy öreg Törpe táncra perdül, a boldog tömeg
tapsolva veszi körül. A szenvedést, fájdalmat most mindenki elfelejti. Míg a
többiek a szabadulásukat ünneplik, egy Elf lép oda hozzád, és közli, hogy négy-
szemközt szeretne veled beszélni. Távolabb húzódtok a többiektől, és figyelemmel
hallgatod, milyen mondanivalója van az Elfnek. Aggódva figyelmeztet, hogy a
Gyíkkirály erődje elleni támadás egyenlő az öngyilkossággal. A király hatalma
és élete védelmében engedélyezte, hogy egy förtelmes parazita, a Goncsong meg-
telepedjék a feje búbján. A Goncsongnak a király agyába szúrt fullánkja a Gyík-
király legyőzhetetlenné teszi, és a telepátia segítségével ellenőrzése alatt
tarthatja az összes mutáns (átváltozó) harcost. Ahhoz, hogy végezz a
Gyíkkirállyal, először a Goncsongot kell elpusztítanod. Tudnod kell azonban,
hogy csak a sziget Sámánja ismeri a Király varázserejének titkát. A Gyíkkirály
mindaddig sérthetetlen, amíg meg nem tudod, hogyan távolítható el a Goncsong a
fejéről. Sajnos az Elf, a szigeten töltött négy éve alatt még nem látta a Sámánt.
A sámánok általában magányosan élnek, távol a többi bennszülöttől, tudományuknak
szentelve életüket. Megköszönöd az Elf értékes információját, és visszamész a
többiekhez. Amikor odaérsz hozzájuk, a magasba emeled mindkét karodat, hogy
csöndre intsd őket. Elmondod, mit tudtál meg a Goncsongról, és közlöd, hogy
elindulsz megkeresni a Sámánt, mert csak te tudod kinyomozni, hol van. Megkéred
a többieket, hogy menjenek el az erődig, ahol majd egy-két nap múlva csatlakozol
hozzájuk, és elindítod a támadást. Nem szívesen, de beleegyeznek a tervedbe, te
pedig sietve elindulsz, hogy felkutasd a Sámánt."""
        this_scene = Action()
        return this_scene.end_turn('363')

class Scene_202(Scene):

    def enter(self):
        print """
A dárda talál, mélyen belefúródik az Iszapszívó puha, zöld testébe. Bár a sebe-
sülés legyengíti, az Iszapszívó mégis támadásra indul..."""
        this_scene = Action()
        return this_scene.battle(8,5,'Iszapszívó',0,'122')

class Scene_203(Scene):

    def enter(self):
        print """
A Gyíkkirály nem akar hinni a szemének, amikor az Oroszlán holtan terül el.
Ekkor végre feléd fordul, és lángpallosával hadonászva haragosan rád támad."""
        this_scene = Action()
        return this_scene.check_bonus_att('majom','314','36')

class Scene_204(Scene):

    def enter(self):
        print """
Az imbolygó tutajon egyensúlyozva kirántod a kardodat, hogy megtámadd a dühödt Krokodilt.
"""
        this_scene = Action()
        return this_scene.battle(6,7,'Krokodil',0,'31')

class Scene_205(Scene):

    def enter(self):
        print """
Hirtelen mozdulatod megijeszti a lányt, aki elengedi a Tigris pórázát.
Az egyetlen ugrással rád veti magát...
\nVeszítettél 2 Életerő pontot!\n
Ha még mindig életben vagy, kardot tudsz rántani, hogy védekezz..."""
        this_scene = Action()
        return this_scene.end_turn(11,8,'Kardfogú Tigris',0,"343")

class Scene_206(Scene):

    def enter(self):
        print """
Izgatottan kikapja a baltát a kezedből. A többiek körésereglenek, és énekelni
kezdenek. Szemmel láthatóan örülnek az új szerzeménynek, amit vallási kegy-
tárgynak tartanak. Mit teszel?
\nOtthagyod őket, és nyugati irányba haladva eltűnsz a dzsungelban: 7\n
\nKérsz tőlük valamit a baltáért cserébe: 86\n
\nRájuk támadsz a kardoddal: 359 """
        this_scene = Action()
        this_scene.rem_item_list_sack('Balta')
        return this_scene.choice_3('7','86','359')

class Scene_207(Scene):

    def enter(self):
        print """
A Grannitusz hirtelen elereszti a lábszáradat, és a földre zuhansz. Jókorát
rúgsz belé, és nézed, mint száll el a vágaton lefelé. A Csörgőkígyó mérge
ölte meg, ami a szervezetedben elraktározódott. A többi Grannitusz észreveszi,
hogy mi történt, és gyorsan visszahúzódik a vágat falának sötét mélyedéseibe.
"""
        this_scene = Action()
        this_scene.check_bonus_att('feneketlen_zsak','371','192')
        return this_scene.end_turn()

class Scene_208(Scene):

    def enter(self):
        print """
Bizalmatlanul néz rád, mondván, hogy észre kellett volna venned figyelmeztető
jelzését a vízből. De helyrehozhatod a hibát, és ismét barátok lehettek, ha a
hajában lévő tollért cserébe felajánlasz neki valamit a hátizsákodból. Nincs
más megoldás, eleget kell tenned a Sámán kívánságának.
Miután a tollat a hajadba tűzted, a Sámán hajlandó meghallgatni..."""
        this_scene = Action()
        return this_scene.saman_felajanlas('199')

class Scene_209(Scene):

    def enter(self):
        print """
Elhibáztad! A dárda átrepül a Hidra feje fölött, és a mocsárba fúródik.
Kardoddal kell megküzdened a Hidrával..."""
        this_scene = Action()
        this_scene.battle(9,9,'Hidra bal fej',1,'389')
        return this_scene.battle(9,9,'Hidra bal fej',0,'389')

class Scene_210(Scene):

    def enter(self):
        print """
Egy hatalmas sziklatömb rázuhan a kardforgató karodra.
\nVeszítesz 4 Életerő és 2 Ügyesség pontot.\n
Ha még mindig életben vagy, egészséges karoddal véded a fejedet, és amilyen
gyorsan csak tudsz, rohanni kezdesz lefelé a szurdokon..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-4')
        this_scene.act_att_change('ugyesseg','-2')
        return this_scene.end_turn('253')

class Scene_211(Scene):

    def enter(self):
        print """
Félúton a házhoz váratlanul észreveszed, hogy a parton hatalmas homokhalom kezd
a levegőbe emelkedni. Ebből hat nagy tüskés láb és egy pár olló bukkan elő, majd
hatalmas rákpáncél jelenik meg: az ijesztő méretű Óriásrák tornyosul előtted.
A Rák végigrohan a homokon, és egyik ollójával megragadja Mungót.
Barátod fájdalmasan felordít, de hiába minden, képtelen kiszabadulni a satuszerű
ollók fogságából.
\nHa segíteni akarsz Mungónak: 182\n
\nHa inkább visszarohansz a kőházba: 307
"""
        this_scene = Action()
        return this_scene.choice('182','307')

class Scene_212(Scene):

    def enter(self):
        print """
A nap egyre melegebben süt, és aggódni kezdesz, mert a kulacsod majdnem
teljesen üres. Vizet keresel. Végül találsz egy sziklamélyedést, melyben
összegyűlt az esővíz. Jócskán iszol belőle, majd megtöltöd a kulacsodat is.
Már éppen indulni készülsz, amikor a sziklamedence oldalában krétajeleket
fedezel fel...
\nHa el akarod olvasni, mi van odaírva: 72\n
\nHa inkább azonnal útnak indulsz: 30"""
        this_scene = Action()
        return this_scene.choice('72','30')

class Scene_213(Scene):

    def enter(self):
        print """
Hamarosan elérsz egy másik elágazáshoz...
\nHa balra akarsz fordulni: 68\n
\nHa jobbra akarsz menni: 383"""
        this_scene = Action()
        return this_scene.choice('68','383')

class Scene_214(Scene):

    def enter(self):
        print """
A Sámán örül, hogy most már elárulhatja neked a titkát. Tekintetét a magasba
emeli, s széttárt karral, mozdulatlanul áll. Teljes transzban van, amikor el-
meséli neked, hogyan is néz ki a parazita Goncsong. Olyan, mint egy aratópók,
és csupán a fullánkja mélyed bele a gazdája - jelen esetben a Gyíkkirály -
agyába. Ahhoz, hogy valaki megölje, először is a fullánkját kell megsemmisíteni,
különben képes és átugrik a támadójára, hogy új gazdát találjon. De amíg
irányítása alatt tartja a Gyíkkirályt, az szinte legyőzhetetlen, és az egyszerű
fegyverek nem tehetnek kárt benne. Csupán a lángpallos képes a Goncsong gazdáját
megsebesíteni. A Gyíkkirály maga is használ ilyen fegyvert, vagyis egy olyan
varázskardot, amit bármikor rozsdás késsé változtathat. Ezt aztán senki nem
akarja ellopni. A lángpallos birtokában és a Goncsong irányítása alatt a Gyík-
király halálos ellenfél. Csak egyetlenegy teremtmény képes megijeszteni - a majom!
A Gyíkemberek velük született majomfrászban élnek, s ezt még a Goncsong ereje
se tudja legyőzni. A Sámán lassan magához tér a transzból, és délkelet felé
mutatva közli, hogy a fogolytelep arra van. Elköszönsz tőle, és lemész a
tűzhányó aljába, hogy onnan menj tovább a Gyíkkirály erődítménye felé..."""
        this_scene = Action()
        return this_scene.end_turn('168')

class Scene_215(Scene):

    def enter(self):
        print """
Megmarkolsz egy lángoló faágat, az egyik kunyhó mögé rohansz és felgyújtod.
Aztán a másikhoz rohansz, és azt is felgyújtod. A kunyhók egy pillanat alatt
lángban állnak, te pedig a következő kunyhó mögül lesed, hogyan rohangálnak
ide-oda a kétségbeesetten ordítozó Fejvadászok a tisztáson. Az oszlophoz ki-
kötött férfi egy időre őrizetlenül marad. Odafutsz hozzá, hogy kiszabadítsd.
Egyetlen kardcsapással átvágod az indát, mellyel az oszlophoz kötözték, és
rohanni kezdesz vissza a dzsungelba. Futás közben odakiáltasz neki, hogy kö-
vessen. Az egyik Fejvadász észrevesz, és feléd hajítja a dárdáját...
\nA sors kockára teszi az életed!"""
        this_scene = Action()
        return this_scene.dice_3('76','250','323')

class Scene_216(Scene):

    def enter(self):
        print """
Közlöd a Törpével, hogy te vezeted a támadást az erődítmény ellen, és megkérdezed,
merre rejtőzik a Gyíkkirály. Elmondja, hogy a király az erődítmény oromzati lőréseinél
áll, onnan lelkesíti a seregét. Megmondod a Törpének, hogy elintézed a Gyíkkirályt,
aztán visszajössz, és őt is kiszabadítod. Elköszönsz tőle, és kirohansz a nyitott ajtón.
"""
        this_scene = Action()
        return this_scene.end_turn('180')

class Scene_217(Scene):

    def enter(self):
        print """
A Köpködő Varangy foga fájdalmasan váj bele a karodba, de szerencsére nem abba,
amelyikkel vívni szoktál.
\nVeszítesz 2 Életerő pontot!\n
Sikerül szétfeszítened a kardoddal a Köpködő Varangy pofáját, és ki tudsz mászni
hatalmas hasa alól. Felállsz, és vakon ráveted magad."""
        this_scene = Action()
        this_scene.a
        return this_scene.end_turn(8,6,'Köpködő Varangy',0,'134')

class Scene_218(Scene):

    def enter(self):
        print """
Beleakad a lábad egy tüskés bokorba, s kiserken a véred. Megittad az ánizsízű
folyadékot a tengerparti kunyhóban talált kancsóból? """
        this_scene = Action()
        return this_scene.check_bonus_att('ánizsízű_tejfehér_ital','258','146')

class Scene_219(Scene):

    def enter(self):
        print """
A dárda elzúg a disznó mellett, és beleáll a földbe. Szomorúan nézed, amint
reménybeli vacsorád eltűnik a távolban. Felkapod a dárdádat, és folytatod
az utadat nyugat felé..."""
        this_scene = Action()
        return this_scene.end_turn('170')

class Scene_220(Scene):

    def enter(self):
        print """
A Sámán rámutat a sziklatömbre, és kéri, hogy emeld azt föl.
Két karoddal átölelve fölemeled..."""
        this_scene = Action()
        return this_scene.life('98','369')

class Scene_221(Scene):

    def enter(self):
        print """
Annak a helynek a közelében, ahol az Óriás Sárkánylégy fekszik összezsugorodva,
kagyló alakú gombát veszel észre, amely egy korhadó fatönkhöz tapadt.
\nHa enni akarsz a gombából: 358\n
\nHa inkább ismét felkerekedsz és nekivágsz a dzsungelnak: 224"""
        this_scene = Action()
        return this_scene.choice('358','224')

class Scene_222(Scene):

    def enter(self):
        print """
Balra mozgást észlelsz; apró állat fut át a cisztáson. Amikor felbukkan, látod,
hogy egy kismalac. A sült malac gondolatára csorogni kezd a nyálad."""
        this_scene = Action()
        return this_scene.check_item_list_sack('Dárda','342','167')

class Scene_223(Scene):

    def enter(self):
        print """
A szemed elé táruló látvány mérhetetlenül feldühít. Hat félmeztelen Törpe,
akiket a lábuknál fogva egymáshoz láncoltak, akár a barmokat, kalapáccsal
a kezében a sziklafalat bontja. Egy fegyveres Gyíkember bikacsökkel ösztönzi
őket gyorsabb munkára. Leteszed a vödröt, és megtámadod a Gyíkembert..."""
        this_scene = Action()
        return this_scene.end_turn(5,3,'Gyíkember',0,'3')

class Scene_224(Scene):

    def enter(self):
        print """
Úgy döntesz, hogy eléggé eltávolodtál északnyugatra a Fejvadászok falujától;
már nem kell tartanod tőlük. Így aztán egyenesen átvágsz a dzsungelen nyugati
irányba. Alig teszel meg egy rövidke utat, amikor meglepetten látod, hogy tel-
jesen kopár tisztáshoz értél. Hatalmas zöld kristály fekszik a tisztás közepén,
és izzó meleget áraszt. Mit teszel?
\nMegkerülöd a kristályt, és folytatod az utadat nyugat felé: 71\n
\nMegérinted a kristályt: 232\n
\nMegpróbálsz lepattintani egy darabot a kristályból a kardoddal:	370"""
        this_scene = Action()
        return this_scene.choice_3('71','232','370')

class Scene_225(Scene):

    def enter(self):
        print """
A Sámán résnyire szűkült szemmel rád kiált: - Hazug! - Hirtelen remegni kezd a föld,
és hatalmas szakadék nyílik meg alattad. Gőz csap fel belőle, leforrázza a lábadat.
\nVesztesz 3 Életerő pontot.\n
Bocsánatot kérsz a Sámántól, amiért hazudtál neki, és megmagyarázod, hogy csak azért
tetted, mert el akartad nyerni beleegyezését. Nem tudtad, hogy a toll az ő békeszimbóluma.
A Sámán morogva megérinti botjával a lábadat, s a fájdalom azonnal elmúlik."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        return this_scene.end_turn('301')

class Scene_226(Scene):

    def enter(self):
        print """
A vágat szűkülni kezd. Mivel a mennyezet igen alacsony, le kell hajolnod.
A bánya használaton kívüli részébe jutottál...
\nHa ezen a vágaton akarsz továbbmenni: 213\n
\nHa inkább visszatérsz az előző elágazáshoz, és ott balra fordulsz: 101"""
        this_scene = Action()
        return this_scene.choice('213','101')

class Scene_227(Scene):

    def enter(self):
        this_scene = Action()
        return this_scene.check_item_list_sack('Három Vaskulcs','273','162')

class Scene_228(Scene):

    def enter(self):
        print """
Számos szikla áll ki a vízből, ki kell kerülnöd őket. Ez nehéz munka, és egyre
fáradtabb leszel. Úgy döntesz, hogy rövid időre kievezel a partra pihenni.
Lefekszel a fák árnyékában, és elalszol. Amikor felébredsz, látod, hogy a tested
telis-tele van szúnyogcsípéssel..."""
        this_scene = Action()
        return this_scene.luck('236','103')

class Scene_229(Scene):

    def enter(self):
        print """
Amint előrehatolsz a buja bozótban, távoli tamtamdob hangját hallod abból az
irányból, ahonnan a füstöt láttad felszállni.

Ha továbbra is délnyugatra tartasz: 337

Ha inkább nyugat felé mész: 113
"""
        this_scene = Action()
        return this_scene.choice('337','113')

class Scene_230(Scene):

    def enter(self):
        print """
A vízsugár olyan erővel tör rád, hogy kis híján lesodor a tutajról. Szerencsére
meg tudod tartani az egyensúlyodat, és nem esel le róla. A nyitott zsák elnyeli
a vizet, egyre több és több ömlik bele. A zsák olyan, mintha nagy darab, puha zselé lenne.
\nAz örvény olyan gyorsan tűnik el, amilyen gyorsan keletkezett,
mert a Víziszörny feneketlen zsákod foglya lett!
\nNyertél 2 Szerencse pontot!\n
Viszont szerencsétlenségedre a tutaj kettétörik, ezért úgy döntesz, hogy
átgázolsz a vízen a jobb partra. Nem kockáztatod meg, hogy megszökjön a
Víziszörny, ezért gödröt ásol, és betemeted a Feneketlen Zsákot.
Nincs más választásod, gyalog kell folytatnod az utadat."""
        this_scene = Action()
        this_scene.act_att_change('szerencse','2')
        this_scene.bonus_att_change_rem('feneketlen_zsak')
        return this_scene.end_turn('197')

class Scene_231(Scene):

    def enter(self):
        print """
A hordó tele van ananásszal; valamennyi rohadt, csak úgy hemzseg a muslicáktól.
De a hordó mögött eldugva egy vízzel teli üveget veszel észre a földön. Kihúzod
a dugót, és beleszagolsz. Lehet, hogy víz van benne, de iszonyatosan poshadt.
\nHa meg akarod inni a folyadékot: 6\n
\nHa inkább továbbmész a szemközti falon lévő ajtóhoz: 353"""
        this_scene = Action()
        return this_scene.choice('6','353')

class Scene_232(Scene):

    def enter(self):
        print """
Lassan, izgatottan érinted meg az izzó kristályt. Forróság árad szét a testedben,
igen nagy erőt érzel magadban.
\nNyersz 3 Életerő pontot, mert a kristály regeneráló hatással van rád.\n
\nHa eddig még nem tettad volna meg, most lepattinthatsz
a kardoddal egy darabot a kristályból: 370\n
\nVagy ha úgy gondolod, elhagyhatod a tisztást,
és folytathatod az utadat a dzsungelen át nyugatra: 71"""
        this_scene = Action()
        this_scene.act_att_change('eletero','3')
        return this_scene.choice('370','71')

class Scene_233(Scene):

    def enter(self):
        print """
Hirtelen vörösen izzani kezd egy sor kő, és mutatja a tűzhányó oldalában felfelé
vezető utat. Úgy döntesz, hogy követed a vörös kövek vonalát..."""
        this_scene = Action()
        return this_scene.end_turn('249')

class Scene_234(Scene):

    def enter(self):
        print """
Elkeseredetten harcolsz a dühöngő árral szemben, de nem tudsz megmenekülni
a Víziszörny örvényéből. Erőd egyre csökken, már nem bírsz tovább úszni.
Elveszted az eszméletedet, és elnyel a Szörny, hogy mindörökre az ő vízi
világában maradj..."""
        this_scene = Action()
        return this_scene.end_turn('x')

class Scene_235(Scene):

    def enter(self):
        print """
A Mocsári Szökdécselő rövidesen nyugatnak fordul. Kíváncsi vagy, vajon csapdába
akar-e csalni, vagy pedig biztonságosabb útvonalat választott a mocsáron át.
Kérdésedre hamarosan megkapod a választ, ugyanis váratlanul hatalmas állat
emelkedik ki a mocsárból. Ez a kétfejű Hidra. Hatalmas, meztelen csiga-teste
feléd siklik, s mindkét fejét támadásra készen feléd fordítja..."""
        this_scene = Action()
        return this_scene.check_item_list_sack('Dárda','272','29')

class Scene_236(Scene):

    def enter(self):
        print """
Kibírhatatlanul viszket a sok csípés, láznak még sincs semmi nyoma.
Visszaugrasz a tutajra, és ismét folytatod az utat a folyón felfelé..."""
        this_scene = Action()
        return this_scene.end_turn('379')

class Scene_237(Scene):

    def enter(self):
        print """
A Sámán vállat von, aztán felszólít, hogy azonnal távozz. Délkeleti irányba mutat,
és azt mondja, hogy a fogolytábor arra van. Megfordulsz, és a tűzhányó oldalában
lemész, hagy felkutasd a Gyíkkirály birodalmát..."""
        this_scene = Action()
        return this_scene.end_turn('168')

class Scene_238(Scene):

    def enter(self):
        print """
Az ital ánizsízű és tejfehér. Az utolsó cseppig kiiszod, de nem érzel semmit, így
csak sejtheted, hogy megvéd utad során. Leteszed a kancsót, és kilépsz a házból.
"""
        this_scene = Action()
        this_scene.bonus_att_change('ánizsízű_tejfehér_ital')
        return '152'

class Scene_239(Scene):

    def enter(self):
        print """
Csupán egyetlen fürge Grannituszt tudsz feltartóztatni, és még kettővel kell
megküzdened, méghozzá külön-külön..."""
        this_scene = Action()
        this_scene.battle(4,3,'Első Grannitusz',1,'192')
        return this_scene.end_turn(3,2,'Második Grannitusz',0,'192')

class Scene_240(Scene):

    def enter(self):
        print """
A dárda átdöfi a válladat, és a földre rogysz.
\nVeszítesz 2 Életerő és 1 Ügyesség pontot.\n
A Hobgoblin pánikszerűen elmenekül, ahelyett hogy végezne veled. Amikor már olyan
jól érzed magad, hogy lábra tudsz állni, átmész a kőhídon a szakadék túloldalára.
"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        this_scene.act_att_change('ugyesseg','-1')
        return this_scene.end_turn('139')

class Scene_241(Scene):

    def enter(self):
        print """
Mindkét Gyíkember háttal áll, amikor rájuk veted magad. Az egyiket sikerül
leütnöd a kardod markolatával, úgyhogy ez el is veszti az eszméletét,
de a másikkal meg kell küzdened..."""
        this_scene = Action()
        return this_scene.battle(9,8,'Gyíkember',0,'189')

class Scene_242(Scene):

    def enter(self):
        print """
A lány mozdulatlanul áll, amíg elfutsz tőle. """
        this_scene = Action()
        return this_scene.luck('142','205')

class Scene_243(Scene):

    def enter(self):
        print """
Az egyik Pigmeus előrelép, és kikapja a kezedből a baltát. A többiek körülveszik,
és énekelni kezdenek. Szemmel láthatólag igen elégedettek a zsákmánnyal, amelyet
vallásos kegytárgynak tartanak. Mit teszel?
\nOtthagyod őket, és eltűnsz a dzsungelban
nyugati irányban: 7
\nKérsz tőlük valamit a baltáért
cserébe: 86
\nRájuk támadsz a kardoddal: 359"""
        this_scene = Action()
        this_scene.rem_item_list_sack('Balta')
        return this_scene.choice_3('7','86','359')

class Scene_244(Scene):

    def enter(self):
        print """
Kardot rántasz az ugrásra kész Goncsongra, és átdöföd dagadt potrohát.
Legyőzted a Gyíkkirályt és a Goncsongot is!!!"""
        this_scene = Action()
        return this_scene.end_turn('400')

class Scene_245(Scene):

    def enter(self):
        print """
Egy szikladarab a válladat éri, de éppen csak megüt.
\nVesztesz 2 Életerő pontot!\n
Két karoddal véded a fejedet, és amilyen gyorsan csak tudsz, lerohansz a szurdokon.
"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        return this_scene.end_turn('253')

class Scene_246(Scene):

    def enter(self):
        print """
A mély tárnába nem tudsz másképp lejutni, csak ha leugrasz. Úgy döntesz,
hogy ezt nem kockáztatod meg, hanem inkább visszamész az elágazáshoz..."""
        this_scene = Action()
        return this_scene.end_turn('135')

class Scene_247(Scene):

    def enter(self):
        print """
A Medve nyakában bőr nyakörv van, amelyen rézsíp lóg. A sípot zsebre vágod
és elindulsz, hogy megkeresd a Sámánt."""
        this_scene = Action()
        this_scene.item_list_sack('Síp')
        return this_scene.end_turn('27')

class Scene_248(Scene):

    def enter(self):
        print """
Elkapod a fejed a vízsugár elől, és visszanyúlsz a kardodért. Készen állsz,
hogy félreugorj a következő adag kellemetlen sav elől, melyet a Köpködő Varangy
bocsát ki. Hirtelen kiugrik a vízből, hogy tűhegyes fogait beléd mélyessze..."""
        this_scene = Action()
        return this_scene.end_turn(5,6,'Köpködő Varangy',0,'21')

class Scene_249(Scene):

    def enter(self):
        print """
Az egyik szikla mögül hirtelen egy férfi feje bukkan elő; a haját színes
gyöngyök és tollak díszítik. Óvatosan lép elő a rejtekhelyéről. Az egyik
kezében tolldíszes bot van, a másikban meg két állatcsont. Ő a sziget va-
rázslója, a Sámán, akit keresel! Van a hajadban egy madártoll?
"""
        this_scene = Action()
        return this_scene.check_bonus_att('siraly_toll','199','176')


class Scene_250(Scene):

    def enter(self):
        print """
A dárda elsüvít és beleáll a szegény férfi hátába, akit az imént mentettél meg.
Kínjában felordít, majd a földre zuhan. Már nem segíthetsz rajta. Amint a többi
Fejvadász észreveszi, hogy mi történik, te gyorsan visszarohansz a dzsungelba,
de rikácsoló hangjuk közvetlenül mögötted zúg.
"""
        y = raw_input('> ')
        return '102'

class Scene_251(Scene):

    def enter(self):
        print """
Amíg megtalálod és kiszabadítod az összes foglyot, 4 Életerő pontot veszítesz a
csatákban. Ha még mindig életben vagy, úgy te vagy a vezére hatvanhárom elszánt,
bosszúra vágyó fogolynak..."""
        this_scene = Action()
        this_scene.act_att_change('eletero',"-4")
        return this_scene.end_turn('201')

class Scene_252(Scene):

    def enter(self):
        print """
A Hobgoblin szeme felcsillan az aranyrög láttán. Máris a markát tartja, mohón
várva, hogy megvesztegesd. Az aranyrögöt a kezébe nyomod, és átmész a kőhídon
a szakadék túloldalára..."""
        this_scene = Action()
        this_scene.rem_item_list_sack('Aranyrog')
        return this_scene.end_turn('139')

class Scene_253(Scene):

    def enter(self):
        print """
Minden erődet összeszedve rohansz előre a keskeny szurdokban, s csak abban
reménykedsz, hogy több sziklaomlás már nem lesz. A szurdok egyszer csak ki-
szélesedik, s végre lassíthatsz. Rettenetes klausztrofóbiád elmúlik..."""
        this_scene = Action()
        return this_scene.end_turn('382')

class Scene_254(Scene):

    def enter(self):
        print """
A csata nem a legkedvezőbben alakul a számodra, mert egyre több embered esik
áldozatul a Gyíkkirály megszállott seregének. Látod, hogy a vezérük a csatasor
mögött üvöltve buzdítja harcra az embereit. A vezér hatalmas Küklopsz; páncélruha
van rajta, a kezében kétélű balta. Le kell győznöd, hogy a saját embereiddel egyesülhess.
"""
        this_scene = Action()
        return this_scene.battle(10,10,'Küklopsz',0,"299")

class Scene_255(Scene):

    def enter(self):
        print """
Leversz néhány meglazult szikladarabot, amikor megpróbálsz elugrani a dárda elől,
de sajnos az fájdalmasan fúródik bele a combodba.
\n3 Életerő pontot veszítesz!\n
A Barlangi Nő elégedetten kiált fel, és bunkósbotját lengetve rohan le a dombról.
Összeszorított foggal kihúzod a dárdát a combodból, majd előrántod a kardodat, hogy védd magad.
"""
        this_scene = Action()
        return this_scene.end_turn(7,5,'Barlangi Nő',0,'79')

class Scene_256(Scene):

    def enter(self):
        print """
Kinyújtod a kezedet, és ujjaiddal épp hogy sikerül elérned a kardodat. Már nem
kapsz levegőt, és az arcod paprikavörös a nyakadon kidagadó erektől. Elkesere-
detten csapkodod a kardoddal az indát, míg végre sikerül átvágnod, és megszabad-
ulnod halálos szorításától. Köhögni kezdesz. Miközben a nyakadat masszírozod, a
förtelmes indát nézed, melyből bíborvörös lé csöpög. Bár szerencsés vagy, hogy
megmenekültél a húsevő fa fogságából, mégis megsérültél.
1 Ügyesség pontot és 2 Életerő pontot veszítesz!
Fáradt vagy, de úgy döntesz, jobb lesz, ha továbbmész. """
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        this_scene.act_att_change('ugyesseg', '-1')
        return '81'

class Scene_257(Scene):

    def enter(self):
        print """
Terved csődöt mond! A vízsugár olyan erővel zúdul rád, hogy kiveri kezedből a
varázszsákot, ami elsüllyed. A tutajod kettétörik, és a vízfüggöny mögül meg-
hallod a Víziszörny gurgulázó kacaját. Levegőért kapkodsz a víz alatt. Minden
erődet összeszedve megpróbálsz kiúszni a partra..."""
        this_scene = Action()
        return this_scene.agi('150','234')

class Scene_258(Scene):

    def enter(self):
        print """
Bár a bokor leveleinek hegye mérgezett, mégsem sérülsz meg.
Továbbmész, és tudod, hogy iszonyatos veszedelmet kerültél el...
"""
        this_scene = Action()
        return this_scene.end_turn('291')

class Scene_259(Scene):

    def enter(self):
        print """
Tudod, hogy a Köpködő Varangyok soha senkivel nem osztják meg vízi birodalmukat,
ezért sietve fejest ugrasz a vízbe, és kiemeled a faládikót. A parton kardod élé-
vel felfeszíted a tetejét, és a láda tartalmát a fűre szórod. Egy színes folyadé-
kkal teli üvegfiolát találsz benne, egy kis bársonyzsákot, egy pár piros bőrcsiz-
mát és egy aranygyűrűt. Mit teszel?
\nKinyitod a zsák száját: 26
\nFelpróbálod a csizmát: 94
\nFelhúzod a gyűrűt az ujjadra: 297 """
        this_scene = Action()
        return this_scene.choice_3('94','297','26')

class Scene_260(Scene):

    def enter(self):
        print """
Kardoddal akarod feltartóztatni a Goncsongot, de elhibázod: a fejed búbján landol,
és agyadba mélyeszti a fullánkját. Mostantól kezdve a Goncsong irányítja az akaratodat,
és csupán tehetetlenül szemlélheted, amint a Gyíkkirály serege megsemmisíti demoralizált
csapatodat. A csatát elvesztetted!"""
        this_scene = Action()
        return this_scene.end_turn('x')

class Scene_261(Scene):

    def enter(self):
        print """
A többi Fejvadász azt hiszi, hogy legyőzhetetlen, isteni erővel bíró
varázsló vagy. Sarkon fordulnak, és sipító fejhangon ordítva elmenekülnek.
\nHa ki akarod nyitni az egyik halott Fejvadász mellett heverő zsákot: 187\n
\nHa inkább továbbmész nyugatnak: 113\n
"""
        this_scene = Action()
        return this_scene.choice('113','187')

class Scene_262(Scene):

    def enter(self):
        print """
A feléd tartó Gyíkember rád kiált, és megkérdi, merre mész. Ilyen közelről nem
tudod eljátszania Gyíkember szerepét. Elő kell rántanod a kardodat..."""
        this_scene = Action()
        return this_scene.end_turn(7,8,'Gyíkember',0,'386')

class Scene_263(Scene):

    def enter(self):
        print """
Tudtad, hogy a kardforgató karodat nem szabad beledugnod a kőgyűrűbe, így aztán
sérült kezed nem okoz különösebb gondot.
\nVeszítesz 1 Ügyesség pontot!\n
Kelletlenül belehajítod a kőgyűrűbe Felszerelési Tárgyaid egyikét,
és várod, mi történik..."""
        this_scene = Action()
        return this_scene.saman_felajanlas('233')

class Scene_264(Scene):

    def enter(self):
        print """
Szervezeted gyenge és a méreg gyorsan hat. Lüktetni kezd a karod és elönt
a veríték. Ájulás környékez.
\nVeszítesz 5 Életerő pontot!\n """
        y = raw_input('> ')
        this_scene = Action()
        this_scene.act_att_change('eletero','-5')
        return this_scene.check_att('eletero',9,'364','124')

class Scene_265(Scene):

    def enter(self):
        print """
A Törpék gyűlölettől fűtve rátámadnak az Orkokra. A harc nem tart sokáig,
az elkeseredett Törpék gyorsan végeznek az Orkokkal..."""
        this_scene = Action()
        return this_scene.end_turn('121')

class Scene_266(Scene):

    def enter(self):
        print """
Az ajtó nem ereszt, képtelen vagy kinyitni. Nincs más választásod, mint hogy
visszamenj az erődítmény udvarára, és megpróbáld kinyitni az onnan nyíló többi ajtót.
"""
        this_scene = Action()
        return this_scene.end_turn('84')

class Scene_267(Scene):

    def enter(self):
        print """
Meghúzod a fogantyút és fölemeled a csapóajtót. Alatta egy kis üregben egy fa-
ládát találsz. Kiemeled, és leteszed a földre. A fedele viasszal van lezárva.
\nHa ki akarod nyitni a ládát: 354\n
\nHa inkább úgy döntesz, hogy elhagyod a házat: 152
"""
        this_scene = Action()
        return this_scene.choice('152','354')

class Scene_268(Scene):

    def enter(self):
        print """
Az ajtó egy keresztfolyosóra nyílik. A folyosó túloldalán vasráccsal védett
cellaajtók sorakoznak egymás mellett. Balra nézel, s látod, hogy a folyónak
itt vége szakad, tehát jobbra indulsz. Az utolsó cellában a faajtó mögött
törékeny öregembert látsz. Egy fapadon ül, bilincsbe vert lábát a falhoz
láncolták. Cellájának ajtaja nyitva van, de a folyosóra kivezető faajtót
erős lakattal zárták le. Mit teszel?
\nKiszabadítod az öreget: 166\n
\nMegpróbálod kinyitni a faajtót: 227"""
        this_scene = Action()
        return this_scene.choice('166','227')

class Scene_269(Scene):

    def enter(self):
        print """
Félúton, a hegy oldalában, bal kéz felől egy barlang bejáratát veszed észre,
melynek félkör alakban elhelyezkedő köveit sikító színűre festették, és mind-
egyiknek a tetejére egy koponyát tettek.
\nHa fel akarsz mászni a barlanghoz: 59\n
\nHa inkább továbbmész a tűzhányó irányába: 303"""
        this_scene = Action()
        return this_scene.choice('59','303')

class Scene_270(Scene):

    def enter(self):
        print """
Elhatározod, hogy megtámadod a Gyíkembereket. Abban reménykedsz, hogy élve
megúszod az összecsapást, és ki tudsz majd szedni belőlük valamit. Csöndben
kikúszol a fák rejtekéből egészen a kunyhó sarkáig. Körülnézel, és észreveszed,
hogy a Gyíkemberek még mindig beszélgetnek. Kivont karddal megvizsgálod a terepet,
hogy lásd, vajon sikerülhet-e a terved?"""
        this_scene = Action()
        return this_scene.luck('241','43')

class Scene_271(Scene):

    def enter(self):
        print """
A Gyíkkirály hirtelen megtorpan, amint észreveszi a majmodat. Remegni kezd
- szemmel láthatóan fél a majomtól."""
        this_scene = Action()
        return this_scene.luck('22','123')

class Scene_272(Scene):

    def enter(self):
        print """
Amint a Hidra a közeledbe ér, dárdáddal megcélzod az egyik fejét..."""
        this_scene = Action()
        return this_scene.dice_3('209','209','344')

class Scene_273(Scene):

    def enter(self):
        print """
Az egyik kulcs pontosan illik a zárba. Kinyitod az ajtót..."""
        this_scene = Action()
        return this_scene.end_turn('395')

class Scene_274(Scene):

    def enter(self):
        print """
A vágatban egyenesen mész előre, amíg egy függőlegesen lefelé haladó aknához nem
érsz. Belülről falétrát támasztottak az oldalához, de amint letekintesz a mélybe,
nem látod az akna végét...
\nHa le akarsz menni a létrán: 315\n
\nHa inkább visszamész az elágazáshoz,
majd onnan a vágat másik végébe indulsz: 28\n"""
        this_scene = Action()
        return this_scene.choice('315','28')

class Scene_275(Scene):

    def enter(self):
        print """
Amint megérinted a kést, az egy szemvillanás alatt átalakul. Az ócska,
régi kés csodálatos lángpallossá változik. Ez a Gyíkkirály egyik fegyvere!
\nNyertél 2 Ügyesség pontot és 2 Szerencse pontot!\n
Új kardoddal suhintasz egyet a levegőbe, aztán nekivágsz a folyosónak,
hogy eljuss a legtávolabbi ajtóhoz."""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg','2')
        this_scene.act_att_change('szerencse','2')
        this_scene.item_equipped('fegyver','Tűzpallos')
        return this_scene.end_turn('312')

class Scene_276(Scene):

    def enter(self):
        print """
A Pigmeusok valamit morognak, majd rád kiáltanak, de nem érted a nyelvüket.
Szemmel láthatóan akarnak valamit tőled, de nem tudod, hogy mit.
\nMit adnál oda nekik?\n
\nA kisbaltát: 243\n
\nA vasrudat: 327\n
\nÉlelmiszert: 126\n
\nA felsoroltak közül semmid sincs: 137"""
        this_scene = Action()
        return this_scene.choice_4('243','327','126','137')

class Scene_277(Scene):

    def enter(self):
        print """
A kardfogó kezed sérült meg.
\n3 Ügyesség pontot veszítettél!\n
Vonakodva bár, de mégis bedobsz egy tárgyat a kőgyűrűbe,
és várod, hogy mi történik..."""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg','3')
        return this_scene.end_turn('233')

class Scene_278(Scene):

    def enter(self):
        print """
A vágat hirtelen véget ér, és aggódni kezdesz, hogy eltévedtél.
\nVeszítesz 1 Szerencse pontot!\n
Megfordulsz, és visszatérsz az előző elágazáshoz.
\nHa egyenesen akarsz továbbmenni: 70\n
\nHa jobbra fordulsz: 172"""
        this_scene = Action()
        return this_scene.choice('70','172')

class Scene_279(Scene):

    def enter(self):
        print """
Lent a völgyben egy sűrű kis erdőhöz érsz. A fák közül hirtelen ismerős arcok
bukkannak elő. A Törpék, az Elfek és a bányából kiszabadított férfiak várnak
itt rád. Örülsz, hogy újra látod őket, és elmondod nekik, mi történt veled
azóta, hogy utoljára találkoztatok. Közlöd velük, hogy az erődítményt azonnal
meg kell támadni, és a Gyíkkirályt te fogod elintézni. Összegyűjtöd őket, és
az élükön haladva levezeted őket a völgybe. Amint a kőerődítmény felé futsz,
látod, hogy a fakapuja tárva-nyitva áll. A Gyíkkirály ellened küldött őrei
és mutánsai rontanak rátok. Kis csapatodnak össze kell csapnia a Gyíkkirály
katonáival..."""
        this_scene = Action()
        return this_scene.dice_3('185','308','42')

class Scene_280(Scene):

    def enter(self):
        print """
Miután alaposan átvizsgálod minden porcikádat, hogy végleg megszabadultál-e a
mocsári élősködőktől, nyugati irányban folytatod az utat a mocsáron át. Két hegy
előtted emelkedik, de te úgy döntesz, hogy a közöttük húzódó szurdokon mész tovább...
"""
        this_scene = Action()
        return this_scene.end_turn('362')

class Scene_281(Scene):

    def enter(self):
        print """
Nehéz helyzetben vagy! Nem tudsz megállni gurulás közben, és egyre csak
bukfencezel lefelé a szurdokba. Fájdalmas puffanással érsz földet...
\nVeszítesz 2 Életerő pontot!\n
Felállsz, leporolod magad, és úgy döntesz, a szurdokban mész tovább..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        return this_scene.end_turn('119')

class Scene_282(Scene):

    def enter(self):
        print """
Óvatosan nyitod ki a zsák száját; hátha mérges kígyó van benne, de meglepetten
tapasztalod, hogy élelmet rejt: lépes mézet, búzalepényt és gyümölcsöt.
\nHa meg akarod enni az élelmet: 116\n
\nHa nem eszed meg, hanem inkább elteszed későbbre, és továbbmész: 27"""
        this_scene = Action()
        this_scene.item_dict_sack_neg('Kaja','-3')
        return this_scene.choice('116','27')

class Scene_283(Scene):

    def enter(self):
        print """
Nem bírod a megpróbáltatást, ezért intesz a Sámánnak, hogy hagyja abba.
Megbuktál a próbán, így a Sámán nem fogja megosztani veled a titkát.
Délkeleti irányba mutat, azt állítja, hogy a fogolytábor arra van,
továbbá közli veled, hogy a Goncsonggal egyedül kell megbirkóznod.
Megfordulsz, és lefelé indulsz a tűzhányó oldalában, hogy megkeresd
a Gyíkkirály erődítményét..."""
        y = raw_input('> ')
        return '168'

class Scene_284(Scene):

    def enter(self):
        print """
Visszamész a sebesült Gyíkemberhez, és felszólítod, hogy adja meg magát.
Eldobja a kardját és a korbácsát, kétrét görnyed előtted, majd erősen
zihálva a földre bukik. Két karját a háta mögött összekötözöd a korbácsával,
és betuszkolod a kunyhóba. Követeled, hogy mondja meg, hol van a bánya.
Elárulja, hogy a bánya bejárata nincs messze; körülbelül száz méterre található
a kunyhó mögött. Odakötözöd a Gyíkembert egy oszlophoz és a kunyhót elhagyva
elindulsz, hogy megkeresd a bányát..."""
        this_scene = Action()
        return this_scene.end_turn('147')

class Scene_285(Scene):

    def enter(self):
        print """
A Goblin felriad álmából. Felnyúl, és két vézna kezével megpróbálja átfogni
a nyakadat."""
        this_scene = Action()
        return this_scene.end_turn('322')

class Scene_286(Scene):

    def enter(self):
        print """
Körülbelül félúton lehetsz az indán, amikor egy fejet pillantasz meg a magasles
egyik sarkában. Egy ősz öregember áll ott, aki szikrázó szemmel, dühösen így szól:
- Takarodj innét, vagy megbánod!
\nHa úgy döntesz, hogy tovább mászol az indán fölfelé: 117\n
\nHa engedelmeskedsz neki és az indán lecsúszva továbbmész északnyugatra: 375
"""
        this_scene = Action()
        return this_scene.choice('375','117')

class Scene_287(Scene):

    def enter(self):
        print """
Elég sokáig tart, míg a Hobgoblin rájön, hogy rossz jelszót mondtál. Végül
leesik neki a tantusz, és neked szegezi a dárdáját..."""
        this_scene = Action()
        return this_scene.end_turn('328')

class Scene_288(Scene):

    def enter(self):
        print """
Kutatni kezdesz a cserjében az elrejtett tutaj után. Hamarosan rátalálsz.
Behúzod a vízbe, és felugrasz rá. A folyó sekély, egy hosszú rúd segítségével
könnyűszerrel tudsz az árral szemben hajózni..."""
        this_scene = Action()
        return this_scene.end_turn('387')

class Scene_289(Scene):

    def enter(self):
        print """
A szörnyűséges mutáns mögé ugrasz és belevágod a kardodat a hátába..."""
        this_scene = Action()
        return this_scene.luck('144','45')

class Scene_290(Scene):

    def enter(self):
        print """
A viszketés szinte elviselhetetlen. Nem tudsz mást csinálni,
vakarod az arcodon lévő ragyákat...
\nVeszítesz 1 Életerő és 1 Szerencse pontot!\n
\nHa a melletted lévő bokor leveleivel be akarod dörzsölni az arcodat: 143\n
\nHa megpróbálod megenni a gombát: 110\n"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-1')
        this_scene.act_att_change('szerencse','-1')
        return this_scene.choice('143','110')

class Scene_291(Scene):

    def enter(self):
        print """
Egy halott tengerész fekszik a cserjésben. Valószínűleg a kalózhajó
legénységének egyik tagja, akit a mutáns Gyíkember megölt. Egy majom
igyekszik kiszabadulni a tengerész kezében lévő lánc fogságából.
\nHa magaddal akarod vinni a majmot: 330\n
\nHa ott hagyod, ahol van, és továbbmész: 350"""
        this_scene = Action()
        return this_scene.choice('330','350')

class Scene_292(Scene):

    def enter(self):
        print """
A sisak több mint százéves, és egykor egy Sog nevű legendás harcosé volt,
aki maga is foglalkozott varázslással. A sisak viselőjétől úgy megijed
minden ellenfele, hogy az automatikusan megnyeri bármely csatában az első
Fordulót. Az ellenfélnek csak annyi bátorsága marad, hogy védekezzen a
második Fordulóban. Büszkén a fejedre teszed új szerzeményedet, majd
óvatosan lemész a dombról a szurdokba. Nyugati irányba mész tovább."""
        this_scene = Action()
        this_scene.item_equipped('sisak','Sog')
        return '119'

class Scene_293(Scene):

    def enter(self):
        print """
Mire megleled és kiszabadítod az összes foglyot, 2 Életerő pontot veszítesz a
csatában. Ha még mindig élsz, te lehetsz a vezére hatvanhárom elszánt, bosszúra
vágyó harcosnak..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        return this_scene.end_turn('201')

class Scene_294(Scene):

    def enter(self):
        print """
A Varázsgyűrű ismeretlen ereje óvatosságra int: az sugallja, hogy az öreg csak
látomás; a rémséges Alakváltoztató műve. Kirohansz, a cellából, és becsapod
magad mögött az ajtót, éppen akkor, amikor az öreg vadállattá kezd átváltozni.
Zöld tüskék bújnak elő a ruháján át, és nyáladozó állkapcsát szélesre tátva
kivillantja pengeéles fogsorát. Az Alakváltoztatót ejtetted foglyul a cellában,
s most már megpróbálhatod kinyitni a faajtót..."""
        this_scene = Action()
        return this_scene.end_turn('227')

class Scene_295(Scene):

    def enter(self):
        print """
A Pigmeus megsértődik, hogy nem fogadtad el az ajándékát. Dobbant egyet a lábával
és eldobja a fúvócsövét. A többi Pigmeus körülfog benneteket:
csak akkor nyerheted vissza a becsületedet, ha megvívsz a Pigmeussal!
Előrántod a kardodat, hogy védekezz a felbőszült Pigmeussal szemben..."""
        this_scene = Action()
        return this_scene.battle(6,5,'Pigmeus',0,'96')

class Scene_296(Scene):

    def enter(self):
        print """
A Gyíkkirály hirtelen megdermed, amikor tekintete találkozik a majoméval.
Remegni kezd, hisz a majmoktól való félelme közismert. Úgy meg van rémülve,
hogy csak nehezen tudja felemelni a kardját, hogy védekezzen, amikor megtámadod.
Csupán a Goncsong kényszerítő befolyása alatt kezd amolyan látszatellenállásba.
"""
        this_scene = Action()
        return this_scene.battle(6,15,'Gyíkkirály',0,'153')

class Scene_297(Scene):

    def enter(self):
        print """
Abban a pillanatban, amikor az ujjadra húzod a gyűrűt, nagyon elszédülsz.
Meg akarsz szabadulni a gyűrűtől, de az nem mozdul. Varázsgyűrű van az
ujjadon. 2 Ügyesség pontot veszítesz. Ha még nem tetted volna:
\nKinyithatod a zsákot: 26\n
\nFelpróbálhatod a csizmát: 94\n
\nHa egyikhez sincs kedved,
folytathatod utadat nyugat felé, a tisztáson át: 222"""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg','-2')
        this_scene.item_equipped('gyűrű','Varázsgyűrű')
        return this_scene.choice_3('26','94','222')

class Scene_298(Scene):

    def enter(self):
        print """
Koromsötét van a fúrólyukban, amely akár több kilométer hosszú is lehet.
Úgy gondolod, hogy nem vezet sehova. Nincs sok helyed, hogy megfordulj,
így aztán fejedet két lábad közé hajtva bukfencezel. Visszamászol a fúrólyukon,
és megkönnyebbülsz, amikor eléred a fővágatot. De amikor bukfenceztél a
fúrólyukban, hogy meg tudj fordulni, valami kiesett a hátizsákodból.
\nHúzz ki egy tárgyat a Felszerelésedből.\n
\nVeszítesz 1 Szerencse pontot!\n
Kimászol a fúrólyukból, jobbra fordulsz, és lefelé mész a vágatban."""
        this_scene = Action()
        this_scene.act_att_change('szerencse','-1')
        return this_scene.saman_felajanlas('47')

class Scene_299(Scene):

    def enter(self):
        print """
Embereid fellelkesülnek a Küklopsz halálán, és újult erővel folytatják a harcot.
Amikor a Gyíkkirály serege kezd visszavonulni, átvágod az arcvonalukat, és oda-
rohansz az erődítmény fakapujához. Belépve a belső udvarba jutsz, ahonnan
egy-egy szárnyas ajtó vezet az épületbe.
\nHa a balra nyíló szárnyas ajtón akarsz bemenni: 268\n
\nHa inkább a veled szemben lévő ajtón kívánsz benyitni: 84"""
        this_scene = Action()
        return this_scene.choice('268','84')

class Scene_300(Scene):

    def enter(self):
        print """
A Víziszörny rázuhan a tutajodra és darabokra töri. Gurgulázó kacaja túlharsogja
a vízáradat moraját. Levegő után kapkodsz a rád zúduló víztömeg alatt. Összeszeded
minden erődet, és megpróbálsz kiúszni a partra..."""
        this_scene = Action()
        return this_scene.agi('150','234')

class Scene_301(Scene):

    def enter(self):
        print """
Bár a Sámán rosszul beszél anyanyelveden, mégis úgy látod, ragyogóan megért
mindent, amit mondasz neki, de mielőtt meghallgatna, ragaszkodik hozzá, hogy
tűzz a hajadba egy tollat. Saját tolldíszéből ajánl fel egyet, amit a hajából
vesz ki, és kéri, hogy adj érte valamit cserébe. Nincs más választásod, eleget
kell tenned az óhajának... Végül elmosolyodik, és várja, hogy beszélj."""
        this_scene = Action()
        return this_scene.saman_felajanlas('199')

class Scene_302(Scene):

    def enter(self):
        print """
Éppen le akarod törni az ágat, amikor egy ugató kutya szalad oda hozzád. A Fej-
vadászok, amint meglátnak, üvöltve köréd sereglenek. Lándzsáikkal és bunkósbot-
jaikkal hadonászva rohannak rád.

Ha harcolni akarsz ellenük: 331

Ha inkább visszarohansz a dzsungelba: 102
"""
        this_scene = Action()
        return this_scene.choice('331','102')

class Scene_303(Scene):

    def enter(self):
        print """
Végre elérsz a tűzhányó tövébe, de a Sámánnak még híre-hamva sincs. Felnézel, és
egy hatalmas fekete hegyet látsz, amelynek csúcsa az egekbe nyúlik. Arra gondolsz,
vajon mikor fog ismét kitörni a vulkán, hamutengert és forró lávazuhatagot okádva.
Elhessegeted ezeket a gondolatokat, és eldöntöd, merre menj.
\nHa egyenesen indulsz el a hegyen fölfelé: 178\n
\nHa inkább a tűzhányó tövében mész körbe: 355\n"""
        this_scene = Action()
        return this_scene.choice('178','355')

class Scene_304(Scene):

    def enter(self):
        print """
Éles fogak vájnak a nyakadba: a ravasz Borotvafogú őrjöngve támad rád, hogy megöljön.
\nVeszítesz 2 Életerő pontot!\n
Ha még mindig életben vagy, kardoddal megpróbálod levágni magadról a szörnyű teremtményt.
"""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        return this_scene.battle(6,5,'Borotvafogú',0,'20')

class Scene_305(Scene):

    def enter(self):
        print """
Karddal fát vágni lassú, fáradságos munka. Aggódni kezdesz, hogy a favágás zajára
felfigyelhet valaki. Félelmed hamarosan beigazolódik. A hátad mögött két fa között
egy Ogre jelenik meg. Álmából verted fel. Felmordul, és egy hatalmas faágat szoron-
gatva elindul feléd..."""
        this_scene = Action()
        return this_scene.battle(8,8,'Ogre',0,'99')

class Scene_306(Scene):

    def enter(self):
        print """
Amint a kőgyűrű fölé nyúlsz, olyan fájdalmat érzel, mintha egy kocsikerék küllői
kapták volna be a kezedet. Visszarántod, de látod, hogy az teljesen deformálódott.
"""
        this_scene = Action()
        return this_scene.dice_3('277','277','263')

class Scene_307(Scene):

    def enter(self):
        print """
Elkeseredett igyekezetedben, hogy elmenekülj az Óriásrák elől, nem számolsz a
homokkal, amelyen átfutsz. Hirtelen nedves és puha lesz a lábad alatt, ráadásul
süppedni kezdesz. Futóhomokra tévedtél, és miközben menekülni próbálsz, egyre
mélyebbre süppedsz. Rémülten ordítani kezdesz, mert a homok már a nyakadig ér.
Utolsó pillantásoddal Mungót látod, akit épp elnyel az Óriásrák."""
        y = raw_input('> ')
        return 'x'

class Scene_308(Scene):

    def enter(self):
        print """
Magasba emelt kardoddal rátámadsz a hozzád legközelebb álló ellenfélre.
Egy Gyíkemberre..."""
        this_scene = Action()
        return this_scene.battle(8,7,'Gyíkember',0,'341')

class Scene_309(Scene):

    def enter(self):
        print """
Mindkét Gyíkember háttal áll, amikor rájuk támadsz. Az egyiket foglyul tudod
ejteni, mielőtt észrevennék a támadást, de a másikkal meg kell küzdened!"""
        this_scene = Action()
        return this_scene.battle(9,8,'Gyíkember',0,'368')

class Scene_310(Scene):

    def enter(self):
        print """
Nekiesel az egyik korhadt tartógerendának, amely a súlyod alatt eltörik. A mennyezet
rád szakad. Majdnem megfulladsz a törmelék alatt, szinte élve vagy eltemetve.
\nVeszítesz 4 Életerő pontot!\n
Ha életben maradsz, sikerül kimásznod a homok és kőtörmelék alól,
de vissza kell menned az utolsó elágazásig..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-4')
        return this_scene.end_turn('378')

class Scene_312(Scene):

    def enter(self):
        print """
A következő ajtó egy kis raktárhelyiségbe nyílik,
amely hordókkal és zsákokkal van tele.
\nHa meg akarod nézni, mit rejt az egyik hordó: 231\n
\nHa inkább továbbmész a folyosó túloldalán lévő következő ajtóhoz: 353"""
        this_scene = Action()
        return this_scene.choice('231','353')

class Scene_313(Scene):

    def enter(self):
        print """
Vesztedre a csapatot vezető Fejvadász úgy dönt, hogy átkutatja a fa odvát, ahol
rejtőzöl. Bedugja a fejét az odú nyílásán, majd vidáman odakiált a többieknek.
Csapdába kerültél, és a fejed hamarosan ott fog díszelegni a fejvadászok skalpjai között!
"""
        y = raw_input('> ')
        return 'x'

class Scene_314(Scene):

    def enter(self):
        this_scene = Action()
        return this_scene.check_equipped('fegyver','Tűzpallos','296','271')

class Scene_315(Scene):

    def enter(self):
        print """
Óvatosan lépkedsz lefelé a létrán, és egyszer csak leérsz a tárna aljába.
A tompa fényben új vágatot fedezel fel, ahonnan énekhangok szüremlenek feléd.
A vágatban haladva az ének egyre hangosabb tesz, majd közelebb érve kőtörés
zaja vegyül bele. Hirtelen lépteket hallasz a hátad mögül. Mit teszel?
\nElrejtőzöl a félhomályban: 78\n
\nSzembefordulsz a jövevénnyel, bárki
legyen is az: 347"""
        this_scene = Action()
        return this_scene.choice('78','347')

class Scene_316(Scene):

    def enter(self):
        print """
Maláriás leszel, és magas láz gyötör.
\nVeszítesz újabb 3 Életerő és 1 Ügyesség pontot!\n
Az önkívületben teljesen elveszíted az időérzékedet. Amikor végre meggyógyulsz,
fogalmad sincs, meddig voltál beteg. Átkutatod a hátizsákodat, és szomorúan
tapasztalod, hogy eltűnt az összes Élelmed. Valószínűleg hangyák vagy bogarak
ették meg. Megmosdasz a folyóban, és tutajra szállsz, hogy folytasd utadat..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        this_scene.act_att_change('ugyesseg','-1')
        this_scene.item_dict_sack('Kaja',0)
        return this_scene.end_turn('379')

class Scene_317(Scene):

    def enter(self):
        print """
A teremtmény hirtelen megáll, és zavartan néz rád a válla fölött.
Széles ajka kinyílik, hosszú, vékony, rózsaszín villás nyelve kipattan,
majd ugyanolyan gyorsan vissza is húzódik. Hatalmas szeméből bánat sugárzik,
és ekkor rájössz, hogy ez nem más, mint egy ravasz Mocsári Szökdécselő.
Szánalmas külsejük ellenére ezek a teremtmények gyakran vonszolják be könnyelmű
áldozataikat a mocsári húsevő vadállatok búvóhelyeire, hogy jutalmul néhány
apró húscafatot kapjanak. Ennek ellenére nincs olyan teremtmény, amely nálánál
jobban közlekedne a veszélyes mocsárvilágban. A Mocsári Szökdécselő int a fejével,
hogy kövesd a mocsáron át...
\nHa követni akarod: 58\n
\nHa inkább egyedül mész tovább nyugat felé:158"""
        this_scene = Action()
        return this_scene.choice('58','158')

class Scene_318(Scene):

    def enter(self):
        print """
Amikor megérinted az öregembert, az a szemed láttára kezd átváltozni.
Zöld tüskék bújnak elő a ruháján keresztül, szája pedig borotvaéles
fogakkal szegélyezett nyáladzó pofává változik. Nem emberrel van dolgod,
hanem egy Alakváltoztatóval, akivel meg kell küzdened..."""
        this_scene = Action()
        return this_scene.battle(10,10,'Alakváltoztató',0,'372')

class Scene_319(Scene):

    def enter(self):
        print """
A Gyíkember megfordul, hogy megnézze, ki van a háta mögött. Észrevesz, amint a
földön elnyúlva fekszel. Leteszi a vödrét, és kardjával a kezében rád rohan.
Felpattansz, és megmarkolod a kardodat, hogy megvívj vele!"""
        this_scene = Action()
        return this_scene.battle(7,7,'Gyíkember',0,'23')

class Scene_320(Scene):

    def enter(self):
        print """
Gondosan célzol, és elhajítod a tőrt. """
        y = raw_input('> ')
        print """
Szerencsétlenségedre az épp a narancs fölött száll el...
\nMegbuktál a próbán, és a Sámán most már nem árulja el neked a titkát.
Délkelet felé mutat, és közli, hogy a fogolytábor arra van, majd figyelmeztet:
a Goncsonggal az ő segítsége nélkül kell megküzdened. Megfordulsz, és elindulsz
lefelé a tűzhányó oldalában, hogy megkeresd a Gyíkkirály erődítményét..."""
        y = raw_input('> ')
        return '168'

class Scene_321(Scene):

    def enter(self):
        print """
A vágat egy elágazásba torkollik...
\nHa balra akarsz fordulni: 19\n
\nHa jobbra akarsz menni: 39 """
        this_scene = Action()
        return this_scene.choice('19','39')

class Scene_322(Scene):

    def enter(self):
        print """
A Goblin szívós harcos, fegyverként használ mindent, ami a keze ügyébe kerül.
"""
        this_scene = Action()
        return this_scene.battle(5,6,'Goblin',0,'367')


class Scene_323(Scene):

    def enter(self):
        print """
A dárda elszáll, de egyikőtöket se találja el. Amilyen gyorsan csak tudsz, bero-
hansz a dzsungelbe a Fejvadászok elől. Átvágod magad a buja bozóton, de közben
megfeledkezel az éles ágakról és tüskékről. Végül teljesen kifulladva megállsz,
és zihálva nekidőlsz egy fának. A férfi, akit megmentettél, úgy kimerült, hogy
nem bír beszélni, de hálásan mosolyog rád. Amikor végre kifújja magát, elmondja,
hogy Sama a neve, és a Gyíkkirály aranybányájából szökött meg. Egy tutajt szeret-
ne összeeszkábálni, hogy áthajózhasson a szárazföldre. Elmondod neki, mi járatban
vagy. Azt tanácsolja, fordulj vissza, ugyanis a Gyíkkirály állítólag sebezhetet-
len. Közlöd vele, hogy nem félsz a Gyíkkirálytól, és elhatároztad, hogy megölöd.
Sama azt feleli, hogy kimondhatatlanul hálás neked, amiért megmentetted az élet-
ét, mégis képtelen rá, hogy ismét szembetalálkozzék a Gyíkkirállyal. Megnyugtatod,
hogy te nem kényszeríted semmi ilyesmire, és küldetésedet egyedül fogod teljesíteni.
Mielőtt búcsúzóul kezet fognátok, Sama egy csontamulettet ad át neked, amelyet
egy bőrszíjon a nyakában viselt. - Szerencsét hoz majd neked! - mondja kedvesen.
\nSzerencse pontjaid száma mostantól kezdve sosem csökken 7 alá.\n
Ezt követően Sama eltűnik a dzsungelban, te pedig ismét egyedül folytatod utadat.
"""
        this_scene = Action()
        this_scene.item_equipped('nyakék','csontamulett')
        return '113'

class Scene_324(Scene):

    def enter(self):
        print """
Közlöd a Sámánnal, hogy nem ellenségesek a szándékaid; segítségért jöttél hozzá.
Hűvösen végigmér, és így szól: - Miért nincs tolla hajadban, ha barát vagy? -
\nHa meg akarod mondani neki, hogy volt tollad, csak elvesztetted: 225\n
\nHa azt akarod mondani, hogy nem gondoltál rá,
hogy még fontos lehet számodra a toll:208"""
        this_scene = Action()
        return this_scene.choice('225','208')

class Scene_325(Scene):

    def enter(self):
        print """
Lábad alatt szilárdabbá válik a talaj, és a kövek között már nem látod a
lábnyomokat. A távolból halk morgást hallasz - lehet, hagy a tűzhányó ébredezik?
Lerohansz a szurdokba, ahol hirtelen hatalmas hüllő zárja el az utadat. Kővé
dermedten szemléled a páncéltestű hüllőt, amely legalább hat méter hosszú.
Óriásgyík áll előtted - zsákmányul akar ejteni. Küzdj meg vele!"""
        this_scene = Action()
        return this_scene.battle(8,9,'Óriásgyík',0,'196')

class Scene_326(Scene):

    def enter(self):
        print """
Rámutatsz az első dióhéjra. A Sámán fölemeli, de nincs alatta semmi... """
        y = raw_input('> ')
        print """
Megbuktál a próbán, és a Sámán nem fogja elárulni neked a titkát.
Délkelet felé mutatva közli veled, hogy a fogolytábor arra van,
és a Goncsonggal az ő segítsége nélkül, egyedül kell megbirkóznod.
Sarkon fordulsz, és elindulsz lefelé a tűzhányó oldalában,
hogy megkeresd a Gyíkkirály erődítményét."""
        y = raw_input('> ')
        return '168'

class Scene_327(Scene):

    def enter(self):
        print """
Az egyik Pigmeus előrelép, és kikapja a kezedből a vasrudat. Megszagolgatja
és megnyalogatja, de elégedettségnek nem sok jelét adja. Mutatja, hogy valami
mást kér. Mit adsz neki?
\nBaltát: 206
\nÉlelmet: 126
\nEgyiket sem: 137"""
        this_scene = Action()
        return this_scene.choice_3('206','126','137')

class Scene_328(Scene):

    def enter(self):
        print """
Gyorsan kirántod a kardodat, és odaugrasz a Hobgoblinhoz."""
        this_scene = Action()
        return this_scene.battle(6,6,'Hobgoblin',0,'338')

class Scene_329(Scene):

    def enter(self):
        print """
Óvatosan előbújsz a fák rejtekéből, és a kunyhóhoz osonsz. Körülnézel, és látod,
hogy a Gyíkemberek még mindig beszélgetnek. Kirántod a kardodat, és előrontasz
rejtekedből, hogy végrehajtsd a tervedet."""
        this_scene = Action()
        return this_scene.luck('309','163')

class Scene_330(Scene):

    def enter(self):
        print """
A majom boldogan ugrik a válladra, és új barátod társaságában ismét útnak indulsz.
"""
        this_scene = Action()
        this_scene.bonus_att_change('majom')
        return this_scene.end_turn('350')

class Scene_331(Scene):

    def enter(self):
        print """
Bár igen jó harcos vagy, a Fejvadászok túl sokan vannak ahhoz, hogy megbirkózz
velük. Négyet ártalmatlanná teszel, amikor egy dárda a hátadba fúródik, és kül-
detésed véget ért..."""
        y = raw_input('> ')
        return 'x'

class Scene_332(Scene):

    def enter(self):
        print """
A por nemcsak szép, de varázsereje is van. Egy varázslóé volt, akit arra
kényszerítettek, hogy a Gyíkkirály rabszolgája legyen, de mielőtt a varázsló
lement volna a bányába, elhajította a port tartalmazó üvegcsét, remélve, hogy
valaki majdcsak megtalálja. A Barlangi Nő találta meg, de csak annyit tett,
hogy a port az üvegből egy kis agyagtálkába öntötte át. A por megvéd minden
olyan embertől vagy élőlénytől, aki az akaratodat szeretné irányítani.
\nNyersz 2 Szerencse pontot!\n
A barlangban nincs egyéb figyelemre méltó dolog, úgyhogy továbbmész..."""
        this_scene = Action()
        this_scene.bonus_att_change('piros_por')
        return this_scene.end_turn('17')

class Scene_333(Scene):

    def enter(self):
        print """
Miközben a mellvértet leemeled a szögről, az nekiütközik a falnak..."""
        this_scene = Action()
        return this_scene.luck('164','285')

class Scene_334(Scene):

    def enter(self):
        print """
Kinyújtod a karodat, és sikerül elkapnod egy bokrot. Végre megállsz, nem gurulsz
tovább. A földön fekve egy üreget veszel észre az egyik szikla tövében, de túl
sötét van odabenn, úgyhogy nem látod, mit rejt...
\nHa be akarsz nyúlni az üregbe: 145\n
\nHa inkább óvatosan lemész a szurdokba,
hogy nyugat felé folytasd az utadat: 119"""
        this_scene = Action()
        return this_scene.choice('145','119')

class Scene_335(Scene):

    def enter(self):
        print """
A Sámán átnyújt neked egy tört, és azt mondja,
próbáld meg vele eltalálni a narancsot,
amit a szikla tetejére tett... """
        this_scene = Action()
        return this_scene.agi('93','320')

class Scene_336(Scene):

    def enter(self):
        print """
Egy nagy szikladarab zuhan a válladra, de szerencsédre nem a kardforgató karod
sérül meg. Veszítesz 3 Életerő és 1 Ügyesség pontot! Ha még mindig életben vagy,
úgy ép karoddal a fejedet védve, amilyen gyorsan csak tudsz, rohanni kezdesz le-
felé a szurdokon."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-3')
        this_scene.act_att_change('ugyesseg','-1')
        return '253'

class Scene_337(Scene):

    def enter(self):
        print """
A tamtam hangja egyre erősödik, ahogy befelé haladsz a sűrű dzsungelban.
Énekhangok és mély, dübörgő zaj üti meg a füledet. A lehető leghalkabban
lopakodsz előre, amíg egy kis tisztáshoz nem érsz. A tisztás szélén körben
bambuszkunyhók állnak. A tisztás közepén tizenkét Fejvadászt látsz, akik egy
oszlophoz kikötött félmeztelen férfit vesznek körül. Az egyik Fejvadász, akinek
az arcát és a fejét díszes maszk fedi, előrelép és karját a magasba emeli.
A tamtamszó hirtelen elhallgat...."""
        y = raw_input('> ')
        print """
Ekkor egy nő csontkést nyújt át neki - a Fejvadászok készen állnak, hogy új tró-
feát szerezzenek maguknak! Túl sokan vannak ahhoz, hogy megtámadd őket, egyedül
tehetetlen vagy. Egyféleképpen tudnád elterelni a Fejvadászok figyelmét, de ez
veszélyes.

Ha az előtted lobogó tábortűzből kiragadsz egy égő
fahusángot, és felgyújtasz vele néhány kunyhót: 171

Ha inkább visszahúzódsz a dzsungelba és kelet felé mész tovább: 113
"""
        this_scene = Action()
        return this_scene.choice('171','113')

class Scene_338(Scene):

    def enter(self):
        print """
Egy bőrzacskó csüng a Hobgoblin övén.
\nHa ki akarod nyitni: 374
\nHa inkább átrohansz a szakadék túloldalára: 139"""
        this_scene = Action()
        return this_scene.choice('374','139')

class Scene_339(Scene):

    def enter(self):
        print """
A Köpködő Varangy ugyanabban a pillanatban veti rád magát, amikor kardoddal
előredöfsz. A Varangy súlya a földre lök, de kardod célba talál; markolatig
mélyed a Varangy torkába. Haláltusájában vonaglik néhányat, te pedig kimászol
kövér hasa alól. Fokozatosan visszanyered a látásodat, és fölkapod a kardodat.
\nHa továbbra is inni akarsz a tó vizéből: 92\n
\nHa inkább továbbmész nyugat felé: 222"""
        this_scene = Action()
        return this_scene.choice('92','222')

class Scene_340(Scene):

    def enter(self):
        print """
Kirántod a kardodat, és lerohansz a partra, remélve, hogy a kalózok nem vesznek
észre. Kettőt sikerül ledöfnöd, mielőtt előránthatnák a késüket, de a másik két
kalózzal meg kell vívnod. """

        this_scene = Action()
        this_scene.battle(7,7,'Első Kalóz',1, '61')
        return this_scene.battle(8,6,'Második Kalóz',0, '61')

class Scene_341(Scene):

    def enter(self):
        print """
Körülnézel, hogy megszemléld, hogy áll a harc. Sok harcostársadat lemészárolták,
a többiek pedig hátrálnak..."""
        this_scene = Action()
        return this_scene.check_item_list_sack('Valhalla Kürtje','109','254')

class Scene_342(Scene):

    def enter(self):
        print """
A malac igen gyorsan fut, ezért a dárdát azonnal el kell hajítanod."""
        this_scene = Action()
        return this_scene.luck('115','219')

class Scene_343(Scene):

    def enter(self):
        print """
A lány sírni kezd, és hirtelen bűntudatot érzel, amiért megölted a Tigrisét.
Meg akarnád vigasztalni, de a lány gazellagyorsasággal elfut tőled, fel a hegyre.
Visszadugod a kardodat a hüvelyébe, és leereszkedsz a völgybe, hogy csatlakozz
a kiszabadított foglyokhoz..."""
        this_scene = Action()
        return this_scene.end_turn('279')

class Scene_344(Scene):

    def enter(self):
        print """
Ragyogó dobás! A dárda felszáll, és éppen a Hidra egyik nyitott pofájába áll bele,
sőt keresztüldöfi. A fej élettelenül bukik előre, de a Hidra még mindig támad az
ép fejével..."""
        this_scene = Action()
        return this_scene.battle(9,9,'Hidra',0,'389')

class Scene_345(Scene):

    def enter(self):
        print """
Hátrálva kimászol a törmelék alól. A kő- és szikladarabok között kis fadoboz
fekszik. Szétfeszíted a zárat a kardoddal, és boldogan kiáltasz fel, amikor
megpillantod, mit rejt. Egy vadászkürt van benne, méghozzá a belevésett írás
szerint nem közönséges kürt, hanem Valhalla híres kürtje. Hangjára erő és bá-
torság tölti el azt, aki belefújt, sőt a barátait is, akik hallják.
\nNyersz 2 Szerencse pontot!\n
Nyakadba akasztod a kürtöt, és visszamész az előző elágazáshoz...
\nHa innen jobbra akarsz elindulni: 172\n
\nHa egyenesen előre mész tovább: 278"""
        this_scene = Action()
        this_scene.act_att_change('szerencse','2')
        this_scene.item_list_sack('Valhalla Kürtje')
        return this_scene.end_turn()

class Scene_346(Scene):

    def enter(self):
        print """
Képtelen vagy ellenállni a Gyíkkirály támadásának. Lángpallosával egyik csapást
a másik után méri rád, és nem tudsz mást tenni, csak védekezni. Saját kardoddal
semmire sem mész, egy árva karcolást sem tudsz ejteni a Gyíkkirályon. Hátrálnod
kell, egyre jobban kifáradsz, így a Gyíkkirály azonnal lesújt. Lángpallosával
iszonyatos sebet ejt a karodon, úgyhogy kénytelen vagy eldobni a kardodat. Felkap,
és csapatainak üdvrivalgása közepette kihajít az oromzati lőrésen. Véged van.
A Tűz-sziget uralkodója mindörökre a Gyíkkirály marad!"""
        this_scene = Action()
        return this_scene.end_turn('x')

class Scene_347(Scene):

    def enter(self):
        print """
A vágatban egy Gyíkember közeledik feléd, kezében vödörrel. Meglepődik,
amikor meglát, és a földre dobja a vödröt. Öblös hangján felordít, majd
görbe kardjával rád veti magát..."""
        this_scene = Action()
        return this_scene.end_turn(7,7,'Gyíkember',0,'23')

class Scene_348(Scene):

    def enter(self):
        print """
Mialatt alszol, a Vámpír Denevér lecsap rád, hogy a véredből igyék.
Nem érzed, amint a fogát belevájja a karodba, és csak akkor veszed
észre a fogai nyomát a bőrödön, amikor felébredsz...
\nVeszítesz 2 Életerő pontot!\n
Beleborzongsz sebeid látványába, majd gyorsan összecsomagolsz, és ismét útnak indulsz.
"""
        this_scene = Action()
        return this_scene.end_turn('212')

class Scene_349(Scene):

    def enter(self):
        print """
Amikor felérsz a magasles tetejére, az öregember eldobja a botját, és följebb
mászik a fán. Igen fürge, és te a kardodat meg a hátizsákodat cipelve nem tudod
utolérni. Úgy döntesz, hogy otthagyod az öreget, lemászol az indán, és
északnyugat felé folytatod az utadat..."""
        this_scene = Action()
        return this_scene.end_turn('375')

class Scene_350(Scene):

    def enter(self):
        print """
Túljutsz a cserjésen meg egy dombon. Kiérsz egy platóra, ahonnan zöld völgy
tárul a szemed elé. A völgy közepén kőerődítmény áll; csíkos zászlaját a szél
lobogtatja. Végre megtaláltad a fogolytábort! Éppen le akarsz ereszkedni a
völgybe, amikor a hátad mögül morgást hallasz. Egy Kardfogú Tigris az, amelyet
egy vadmacskaszemű szőke lány vezet kötélen. Kérdőn tekint rád, közben alig
tudja visszafogni a Tigrist. Mit teszel?
\nMegpróbálsz beszélni vele: 106\n
\nRátámadsz a Tigrisre a kardoddal: 190\n
\nLemenekülsz a völgybe: 242"""
        this_scene = Action()
        return this_scene.choice_3('106','190','242')

class Scene_351(Scene):

    def enter(self):
        print """
A folyadék az arcodba fröccsen, és csípni kezdi a szemedet. Átmenetileg megvakít
a Köpködő Varangy ragacsos, savas nyála. Tisztában vagy azzal, hogy mi történik
veled, és kihúzod a kardodat. Tudod, hogy a Köpködő Varangy rád fogja vetni magát,
hogy megöljön hegyes fogaival. Vakon a levegőbe suhintasz a kardoddal, és hátralépsz
a tó szélétől, miközben szabad kezeddel megdörzsölöd a szemedet. Bár nem látsz,
tapasztalod, hogy a Köpködő Varangy rád ugrik..."""
        this_scene = Action()
        return this_scene.luck('339','73')

class Scene_352(Scene):

    def enter(self):
        print """
A tűzhányó oldalában fény villan; ez akár tükörből vagy fényes fémlemezről
visszatükröződő napfény is lehet. Talán a Sámán az, vagy a Gyíkkirály egyik
járőre? Azonnal útnak indulsz, hogy kiderítsd..."""
        this_scene = Action()
        return this_scene.end_turn('399')

class Scene_353(Scene):

    def enter(self):
        print """
Az ajtó nincs bezárva. Amint benyitsz, egy lócákkal és zsámolyokkal teli
szobában találod magad; üvegserlegek, flaskák és poharak sorakoznak a lócákon,
a falakon lévő polcokon meg furcsa keverékkel teli korsók állnak. A Gyíkkirály
laboratóriumában vagy. Hirtelen léptek zaja üti meg a füledet az ajtó túloldaláról.
\nHa ki akarod rántania kardodat, hogy azzal
fogadd a jövevényt, bárki légyen is az: 360\n
\nHa inkább elbújsz valamelyik lóca alá: 77"""
        this_scene = Action()
        return this_scene.choice('360','77')

class Scene_354(Scene):

    def enter(self):
        print '''
A láda fedele könnyen nyílik. Egy bedugaszolt cserépkancsót találsz benne, meg
egy cédulát, melyre ezt írta valaki:
\n"Sok évvel ezelőtt jöttem a Tűz-szigetre, hogy itt nyugalmat találjak.
De amióta a Gyíkember betette ide a lábát, nem élhetek itt tovább. Most
visszamegyek a szárazföldre. Sok mérgező növény és bokor van a szigeten;
egyetlen karcolásuk megölhet. Idd meg a kancsóban lévő italt, ez védett-
séget biztosít ellenük. Minden jót kívánok neked. bármi hozott is a szigetre.
Isten áldjon. Baskin."
\nHa meg akarod innia kancsóban lévő italt: 238\n
\nHa inkább ügy döntesz, hogy azonnal elhagyod a házat: 152\n
'''
        this_scene = Action()
        return this_scene.choice('238','152')

class Scene_355(Scene):

    def enter(self):
        print """
Menet közben erős kénszagot érzel a levegőben. Hamarosan hatalmas, sűrű sárga
iszappal teli tóhoz érsz. Felszínéről kellemetlen cuppogós hangot adó, nagy
gázbuborékok törnek elő. A tó iszapja igen meleg lehet; csak úgy forr körülötte
a levegő. Egy kövekből és botokból készült furcsa fészekben két óriási tojást
fedezel fel, amelyek jól fejlett dinnyéhez hasonlítanak. A héjuk sárga, rücskös.
Elképzelni sem tudod, miféle szerzet rakhatta le ide, a kénes tó partjára a
tojásait, hogy kikeltse őket.
\nHa közelebbről akarnád megszemlélni a tojásokat: 48\n
\nHa inkább felmászol a tűzhányó tetejére: 178"""
        this_scene = Action()
        return this_scene.end_turn()

class Scene_356(Scene):

    def enter(self):
        print "Az ajtó kinyílik..."
        this_scene = Action()
        return this_scene.end_turn('395')

class Scene_357(Scene):

    def enter(self):
        print """
A kígyómarás végzetes. Tehetetlen vagy a méreggel szemben, és senki sincs
melletted, aki segítene rajtad. Kalandod a Tűz-szigeten e kopár hegyén véget ér!
"""
        this_scene = Action()
        return this_scene.end_turn('x')

class Scene_358(Scene):

    def enter(self):
        print """
Rámutatsz a középső dióhéjra. A Sámán fölemeli, és megkönnyebbülten látod, hogy egy
üveggyöngy fekszik alatta."""
        this_scene = Action()
        this_scene.add_saman_proba('Szerencse')
        this_scene.print_saman_proba_k()
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_359(Scene):

    def enter(self):
        print """
Alig teszel meg két lépést, amikor a Pigmeusok szájukhoz emelik fúvócsövüket,
és hat nyilat lőnek ki rád."""
        ny = 0 - int(randint(1,6))
        this_scene = Action()
        this_scene.act_att_change('eletero',ny)
        return this_scene.end_turn('373')

class Scene_360(Scene):

    def enter(self):
        print """
Az ajtó feltárul, és egy mindkét lábán és kezén megbilincselt Törpe nyomul be
a laboratóriumba. Egy furcsa kétfejű Gyíkember tartja fogva. Félrelöki a szegény
Törpét, és görbe kardját a magasba emelve, támadásra készen feléd lép..."""
        this_scene = Action()
        return this_scene.battle(9,9,'Kétfejű Gyíkember',0,'173')

class Scene_361(Scene):

    def enter(self):
        print """
Visszaérsz a fúrólyukhoz, ahol a szerencsétlenül járt Törpe még mindig a
kézikocsi mellett fekszik...
\nHa be akarsz mászni a fúrólyukon: 298\n
\nHa inkább továbbmész: 47"""
        this_scene = Action()
        return this_scene.choice('298','47')

class Scene_362(Scene):

    def enter(self):
        print """
A talaj emelkedni kezd a lábad alatt, végre túljutottál a veszélyes vidéken,
a dzsungel és a mocsár már mögötted van. A buja fű és a sok-sok virág gyönyörűvé
varázsolja a szigetet, de tudod, hogy nincs időd pihenni. Nemrég értél a szurdokba,
mely a hegyek között nyugati irányba húzódik...
\nHa a szurdokon akarsz végigmenni: 40\n
\nHa inkább a jobbra emelkedő hegyre kapaszkodsz fel: 194"""
        this_scene = Action()
        return this_scene.choice('40','194')

class Scene_363(Scene):

    def enter(self):
        print """
Visszamész a folyóhoz, és felugrasz a tutajodra. Elég lassan haladsz az árral
szemben, amikor a folyó szűkülni kezd, a folyása egyre sebesebbé válik...
\nHa továbbra is a tutajjal akarod folytatni az utadat: 228\n
\nHa inkább a szárazföldön mész tovább: 376"""
        this_scene = Action()
        return this_scene.choice('228','376')

class Scene_364(Scene):

    def enter(self):
        print """
Nagyon legyengített a kígyóméreg, mégis életben maradsz.
Pihensz, amíg elég erősnek nem érzed magad ahhoz, hogy folytasd az utadat...
\nHa megpróbálod a kardoddal kipiszkálni a Csörgőkígyót a lyukból: 5\n
\nHa inkább óvatosan lemész a szurdokba és elindulsz nyugat felé: 119"""
        this_scene = Action()
        return this_scene.end_turn()

class Scene_365(Scene):

    def enter(self):
        print """
A Sámánnak nyoma sincs, úgyhogy továbbmész
a tűzhányó irányában, amerre az ösztönöd visz..."""
        this_scene = Action()
        return this_scene.end_turn('269')

class Scene_366(Scene):

    def enter(self):
        print """
Letérdelsz Mungo összezúzott teste mellé, és óvatosan a karodra fekteted a fejét.
Résnyire nyitja a szemét. Bár haldoklik, halványan elmosolyodik. Suttogva így szól:
- Látod, barátom, az én utam itt véget ér. Nagy hasznomat vetted, mondhatom.
Fogadd meg, hagy megölöd a Gyíkkirályt. Ugye megteszed? - Lecsukódik a szeme, és
holtan omlik a karjaidba. A parton temeted el egy szikla tövében, és sírját a ho-
mokba szúrt kardjával jelölöd, meg. Elszántabban, mint valaha, elindulsz a kőház felé.
"""
        y = raw_input('> ')
        return '198'

class Scene_367(Scene):

    def enter(self):
        print """
Leakasztod a mellvértet, és magadra öltöd.
\nNyersz 1 Ügyesség, pontot!\n
Elhagyod a Goblin szobáját, és a csigalépcsőhöz mész..."""
        this_scene = Action()
        this_scene.act_att_change('ugyesseg','1')
        this_scene.item_equipped('páncél','Goblin Mellvért')
        return this_scene.end_turn('8')

class Scene_368(Scene):

    def enter(self):
        print """
Gyorsan átkutatod a Gyíkemberek tetemét. Egyikük zsebében három vaskulcsot
találsz, amit zsebre vágsz. Nem vesztegeted tovább az időt, elindulsz,
hogy megkeresd a foglyokat..."""
        this_scene = Action()
        this_scene.item_list_sack('Három Vaskulcs')
        return this_scene.end_turn('147')

class Scene_369(Scene):

    def enter(self):
        print """
A szikla túl nehéz, hogy felemeld. Fel kell adnod a küzdelmet!
\nMegbuktál a próbán, a Sámán így nem osztja meg veled a titkát!
Délkelet felé mutat, mondván, hogy a fogolytábor arra van, és közli veled,
hogy a Goncsonggal az ő segítsége nélkül kell megküzdened. Sarkon fordulsz,
és lefelé indulsz a tűzhányó oldalában, hogy megkeresd a Gyíkkirály erődítményét....
"""
        y = raw_input('> ')
        return '168'

class Scene_370(Scene):

    def enter(self):
        print """
Meglendíted a kardodat, és hatalmasat csapsz vele a sziklára. Megrémülsz, amikor
látod, hogy a penge kettétörik és csak egy csonka karddarab marad a kezedben.
\nVeszítesz 2 Ügyesség pontot!\n
\nHa még nem tetted volna, megérintheted a kristályt: 232\n
\nHa úgy gondolod, hogy elhagyhatod a tisztást
és nyugat felé, a dzsungelen át folytathatod az utadat: 71"""
        this_scene = Action()
        return this_scene.end_turn()

class Scene_371(Scene):

    def enter(self):
        print """
Elhatározod, hogy egy Grannituszt magaddal viszel, hátha még később hasznát
veszed. Körbetapogatod a falat, leemelsz róla egy kőállatot, és beledobod a zsákba.
Ezután lefelé indulsz a vágaton, de az csakhamar véget ér. Nincs más választásod,
mint hogy megfordulj és visszamenj az előző elágazáshoz."""
        this_scene = Action()
        this_scene.item_list_sack('Grannitusz')
        return this_scene.end_turn('57')

class Scene_372(Scene):

    def enter(self):
        print """
Elhagyod a cellát és szörnyű lakóját. Megpróbálod kinyitni a faajtót."""
        this_scene = Action()
        return this_scene.end_turn('227')

class Scene_373(Scene):

    def enter(self):
        print """
A nyílvesszők hegyét a Pigmeusok altató folyadékba mártották, úgyhogy
eszméletlenül zuhansz a földre. Amikor felébredsz, a Pigmeusok már sehol sincsenek.
Kardod még mindig a kezedben van, de a hátizsákod üres. Az összes Felszerelési
Tárgyad és Élelmed eltűnt!
\nVeszítesz 2 Szerencse pontot!\n
A Pigmeusokat átkozva ismét nyugat felé indulsz..."""
        this_scene = Action()
        this_scene.empty_sack()
        this_scene.act_att_change('szerencse','-2')
        return this_scene.end_turn('7')

class Scene_374(Scene):

    def enter(self):
        print """
A zsákban egy kis agyagbabát találsz. Egy ördögűző készítette, és meg van átkozva.
\nVeszítesz 2 Szerencse pontot!\n
Lehajítod a babát a szurdokba, és átmész a hídon..."""
        this_scene = Action()
        this_scene.act_att_change('szerencse','-2')
        return this_scene.end_turn('139')

class Scene_375(Scene):

    def enter(self):
        print """
Miközben utat vágsz magadnak a sűrű bokrok és a buja növények között, zümmögő
hangra leszel figyelmes. Színpompás, de ijesztő külsejű Óriás Sárkánylégy lebeg
egy helyben a fejed fölött. Sebesen csapkod szivárványszínű szárnyaival. Hirtelen lecsap rád.
"""
        this_scene = Action()
        return this_scene.battle(8,4,'Óriás Sárkánylégy',0,'221')

class Scene_376(Scene):

    def enter(self):
        print """
A tutajt odakormányozod a jobb partra, és leugrasz. róla. Erdős domb emelkedik
előtted, sziklái és bokrai között csak nehezen lehet felkapaszkodni. Körülnézel,
és úgy döntesz, hogy továbbmész északnyugat felé, a tűzhányó irányába, mert úgy
gondolod, hogy a Sámán valahol ott rejtőzik. Miközben keresztülvágod magad a buja
bozóton, hirtelen egy furcsa bokron akad meg a szemed. Széles, karmazsinvörös végű
levelei vannak, és óriás málnához hasonló gyümölcsök csüngenek róla.
\nHa enni akarsz a gyümölcséből: 100\n
\nHa inkább továbbmész: 399\n"""
        this_scene = Action()
        return this_scene.end_turn()

class Scene_377(Scene):

    def enter(self):
        print """
A massza kissé büdös, de semmilyen hatással nincs rád. Itt semmi ehető nincs,
úgyhogy fogod a kardodat, és ismét útnak indulsz nyugat felé.
"""
        y = raw_input('> ')
        return '113'

class Scene_378(Scene):

    def enter(self):
        print """
Az elágazástól vagy egyenesen mész tovább: 68\n
\nVagy balra fordulsz: 4"""
        this_scene = Action()
        return this_scene.choice('68','4')

class Scene_379(Scene):

    def enter(self):
        print """
Nem tudni, mitől, a víz kavarogni kezd. Örvény képződik a tutajod orránál,
és minden erődet össze kell szedned, nehogy belekerülj. Váratlanul hatalmas
vízsugár tör fel az örvényből, és ember alakúvá formálódik. A Víziszörny le
akar csapni rád."""
        this_scene = Action()
        return this_scene.check_bonus_att('feneketlen_zsak','181','300')

class Scene_380(Scene):

    def enter(self):
        print """
Úgy tizenöt perc múlva megpróbálod elhagyni biztos rejtekhelyedet.
Szerencsédre a Fejvadászok eltűntek. Utat vágsz magadnak a kardoddal,
és azonnal elindulsz nyugat felé. """
        y = raw_input('> ')
        return '113'

class Scene_381(Scene):

    def enter(self):
        print """
Fél kézzel megkapaszkodsz a fában, és lelököd a Mérgespókot a fa törzséről.
Tovább mászol felfelé, és levágsz egy nagy fürt banánt. Lenn a földön megeszed,
aztán gyorsan visszaindulsz a rejtekhelyedre.
\nNyersz 2 Életerő pontot!\n
Bemászol a "sátradba", hogy ott töltsd az éjszakát, s közben az jár az eszedben,
vajon milyen meglepetéseket hoz a holnap. Felnézel az égre. Az egyre sötétedő
éjszakában rózsaszín és bíborszínű felhők gomolyognak. Az ezernyi rovar fülsiketítő
zaját leszámítva élvezed a hűvös éjszakát, és csakhamar elalszol..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','2')
        return this_scene.luck('388','348')

class Scene_382(Scene):

    def enter(self):
        print """
Jobbra, egy hatalmas szikla oldalában néhány szót látsz bevésve.
\nHa föl akarsz mászni a sziklához, hogy megnézd, mit véstek bele: 35\n
\nHa inkább folytatod az utat a szurdokban: 119"""
        this_scene = Action()
        return this_scene.choice('35','119')

class Scene_383(Scene):

    def enter(self):
        print """
A vágat igen keskeny. A mennyezetet tartó gerendák megrepedtek és helyenként
kilazultak. Klausztrofóbiád egyre nő a félhomályban, de továbbmész, miközben
föld és egy csomó apró kő hull a fejedre. Nem veszel észre a földön egy nagy
követ, és átesel rajta..."""
        this_scene = Action()
        return this_scene.luck('140','310')

class Scene_384(Scene):

    def enter(self):
        print """
Mielőtt a Goncsong kihúzná a fullánkját a Gyíkkirály fejéből, lekaszabolod
a kardoddal. A Gyíkkirályt is és a Goncsongot is megölted!"""
        this_scene = Action()
        return this_scene.end_turn('400')

class Scene_385(Scene):

    def enter(self):
        print """
Kinyújtod a kezedet, leszakítasz egy gombát, kagylókalapja kinyílik, és egy
csomó spóra lövell az arcodba. Viszketni kezd tőle a bőröd, és tele lesz kiütéssel.
A viszketéstől már a szemedet is alig bírod nyitva tartani. Mit teszel?
\nSemmit, abban reménykedve, hogy majdcsak elmúlik: 290\n
\nBedörzsölöd az arcodat a melletted lévő bokor leveleivel: 143\n
\nMegeszed a gombát: 110"""
        this_scene = Action()
        return this_scene.choice_3('290','143','110')

class Scene_386(Scene):

    def enter(self):
        print """
A Törpék a segítségedre sietnek, és ártalmatlanná teszitek a Gyíkembert.
Ismét felsorakoztatod a Törpéket, és továbbindultok a vágatban."""
        this_scene = Action()
        return this_scene.end_turn('114')

class Scene_387(Scene):

    def enter(self):
        print """
Alig indulsz el a folyón felfelé, máris rájössz, hogy még a tutaj tetején
sem vagy biztonságban. Egy szempár bukkan elő a vízből, majd egy éles fogakkal
szegélyezett óriási, szélesre tátott állkapocs köteti. Egy Krokodil nagy
lendülettel veti rá magát a tutajodra, csaknem ledönt róla. Körülötted csapkod
a vízben, elszántan csattogtatja az állkapcsát, hogy bekapjon."""
        this_scene = Action()
        return this_scene.check_item_list_sack('Vasrud','9','204')

class Scene_388(Scene):

    def enter(self):
        print """
Nyugodtan alszol, majd amikor korán reggel felébredsz, folytatod utadat."""
        this_scene = Action()
        return this_scene.end_turn('212')

class Scene_389(Scene):

    def enter(self):
        print """
Amikor a Hidra alámerül a fekete mocsárba, a Mocsári Szökdécselő elillan,
hiszen kiderült galád csele. Hatalmas ugrásokkal tűnik el a szemed elöl.
Nincs más választásod, folytatnod kell fárasztó utadat nyugat felé. Alig
teszel meg száz métert, amikor észreveszed, hogy jobbra kavarogni kezd a víz.
A gonosz Mocsári Szökdécselő a mocsárnak abba a részébe csalt el, amelyben
nyüzsögnek a húsevők. Szélsebesen feléd úszik egy Óriás Vízisikló, és ismét
meg kell küzdened az életedért..."""
        this_scene = Action()
        return this_scene.end_turn(8,5,'Óriás Vízisikló',0,'49')

class Scene_390(Scene):

    def enter(self):
        print """
A folyó jobb partján rongyokba öltözött férfit pillantasz meg. Eszeveszetten
integetve kiabál neked. Szökött fogolynak nézed...
\nHa a tutajodat odakormányozod hozzá: 87\n
\nHa inkább továbbhajózol fölfelé a folyón: 14"""
        this_scene = Action()
        return this_scene.choice('87','14')

class Scene_391(Scene):

    def enter(self):
        print """
A fák között buja a bozót: rengeteg a hosszú, széles, tüskés levél, de van itt
vadszőlő, mindenféle kúszónövény, gomba, gyökér és százféle nagyságú, fajtájú
és színű virág. Mind-mind a fény felé tör, helyet keresve magának a nyirkos
rengetegben. A kardoddal kell utat vágnod magadnak, ez pedig lassú, fáradságos
munka.
\nHa le akarsz ülni pihenni egy hatalmas fa tövében: 53\n
\nHa inkább folytatod megkezdett utadat nyugat felé: 81
"""
        this_scene = Action()
        return this_scene.choice('53','81')

class Scene_392(Scene):

    def enter(self):
        print """
Hirtelen átvillan az agyadon az a gondolat, hagy talán a csizma, amit a lábadon
viselsz, varázserejű lehet. Talpadat a falhoz nyomod, és megpróbálsz rajta fel-
menni. Csodák csodájára sikerül! A Mindentmászó Varázscsizma van a lábadon!
\nNyersz 1 Szerencse pontot!\n
Lemászol a falról, és kissé félénken odalépsz a tárna széléhez. Furcsa érzés
merőlegesen lemenni a falon, mint egy légy. A tárna mély, de végül is leérsz
az aljára. Lent koromsötét van. Végigtapogatod a falat, de nem találsz semmilyen
vágatot, ami kivezetne belőle. Már éppen visszaindulnál a tárna oldalfalán, amikor
belebotlasz valamibe. Lehajolsz, és egy kard élét tapintod ki. Visszamész a vágat-
ba, ahol megvizsgálod legújabb szerzeményedet. A fáklyák sárga fénye gyönyörűen
megmunkált kardot világít meg.
\nNyersz 2 Ügyesség pontot!\n
Ledobod a tárnába a régi kardodat, és visszatérsz az elágazáshoz..."""
        this_scene = Action()
        this_scene.act_att_change('szerencse','1')
        this_scene.act_att_change('ugyesseg','2')
        this_scene.item_equipped('fegyver','Gyönyörűen megmunkált kard')
        return this_scene.end_turn('135')

class Scene_393(Scene):

    def enter(self):
        print """
A kis drótdarab segítségével gyorsan leveszed a Törpe bilincsét.
\nNyersz 1 Szerencse pontot!\n
Közlöd a Törpével, hogy te vezeted a fogolytábor felszabadító harcát,
és megkérdezed tőle, hol rejtőzik a Gyíkkirály. Elmondja, hogy a Gyíkkirály
az erőd oromzati lőrésénél áll, onnan buzdítja harcra a csapatát. Megmondod
a Törpének, hogy vegye el a mutáns alakváltoztató, görbe kardját, és megkéred,
segítsen fogva tartott társainak. Szerencsét kívánsz neki, aztán kirohansz az ajtón.
"""
        this_scene = Action()
        this_scene.act_att_change('szerencse','1')
        return this_scene.end_turn('180')

class Scene_394(Scene):

    def enter(self):
        print """
Mielőtt az Iszapszívó túl közel kerülne hozzád, feléhajítod a dárdádat."""
        this_scene = Action()
        return this_scene.dice_3('191','202','202')

class Scene_395(Scene):

    def enter(self):
        print """
Mocskos kínzókamrában találod magad. Telis-tele van iszonyú kínzóeszközökkel;
kínpadokkal, hüvelykszorítókkal, vasszögekkel és korbácsokkal. Egy rozsdás
kést is észreveszel a kamra sarkában álló asztalon. Mit teszel?
\nFelkapsz egy korbácsot: 136\n
\nFelkapod a rozsdás kést: 275\n
\nNem nyúlsz hozzá semmihez, inkább a
legtávolabbi ajtóhoz mész: 312"""
        this_scene = Action()
        return this_scene.end_turn('136','275','312')

class Scene_396(Scene):

    def enter(self):
        print """
A Köpködő Varangy foga fájdalmasan belemélyed kardforgató karodba.
\nVeszítesz 2 Életerő és 2 Ügyesség pontot.\n
A másik kezedbe veszed a kardot; sikerül kifeszítened a Köpködő Varangy száját.
Kimászol hatalmas hasa alól, és vaktában belédöfsz..."""
        this_scene = Action()
        this_scene.act_att_change('eletero','-2')
        this_scene.act_att_change('szerencse','-2')
        return this_scene.end_turn(8,6,'Köpködő Varangy',0,'134')

class Scene_397(Scene):

    def enter(self):
        print """
A Sámán közli veled, hogy három próbának kell megfelelned a hat közül.
Megkérdezi, melyiket választod elsőnek..."""
        this_scene = Action()
        this_scene.print_saman_proba_k()
        ans = raw_input("Írd be melyik utat választod: ")
        return ans

class Scene_398(Scene):

    def enter(self):
        print """
Kinyitod a ládát, és meglepetten látod, hogy vasrudak vannak benne! A kapitány
valószínűleg becsapta a legénységet, amikor elhitette velük, hogy kincset ásnak
el. Az igazi kincs biztosan még mindig a hajó fedélzetén van, bár nem sok hasznát
veheti már. Úgy döntesz, hogy egy vasrudat elteszel a hátizsákodba. A kis ösvényen
felkapaszkodsz a sziklára."""
        add_item = Action()
        add_item.item_list_sack('Vasrud')
        return '200'

class Scene_399(Scene):

    def enter(self):
        print """
A fa ágáról kitömött zsák lóg le egy kötélen.
\nHa le akarod vágni a zsákot: 282\n
\nHa inkább továbbmész: 27"""
        this_scene = Action()
        return this_scene.choice('282','27')

class Scene_400(Scene):

    def enter(self):
        print """
Áthajítod a hitvány Goncsong tetemét az oromzati párkányon, majd felállsz a
párkányra, ahonnan embereid jól láthatnak. Lentről üdvrivalgás hallatszik.
Elégedetten szemléled, milyen könnyen győzik le embereid a Gyíkkirály demora-
lizált seregét. A csatának vége, te győztél! Az Elfek, a Törpék és az emberek
valamennyien visszatérhetnek a szárazföldön lévő otthonukba. A Tűz-sziget
rabszolgabányái örökre megszűnnek. Mungo biztosan büszke lenne rád, ha élne!
"""
