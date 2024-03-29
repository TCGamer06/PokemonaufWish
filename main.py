import random
import tkinter as tk
from pygame import mixer



findmg = None
musplay = 0
game_over = 0


attackdict = {}


def music(x):
    global musvar
    global musplay

    if musplay == 1:
        mixer.init()
        mixer.music.load(x)
        mixer.music.play()


def add_attack(name, damage, typev):
    attackdict[name] = {"damage": damage, "typev": typev}


add_attack("tackle", 30, "normal")
add_attack("grasswhip", 40, "grass")
add_attack("bubblebeam", 40, "water")
add_attack("ember", 40, "fire")
add_attack("electro_ball", 40, "electro")


weakdict = {
    "normal": ["fighting"],
    "grass": ["fire", "poison", "flying", "bug", "ice"],
    "fire": ["ground", "rock", "water"],
    "water": ["electro", "grass"],
    "fighting": ["flying", "psychic", "fairy"],
    "flying": ["rock", "electro", "ice"],
    "poison": ["ground", "psychic"],
    "ground": ["water", "grass", "ice"],
    "rock": ["fighting", "ground", "steel", "water", "grass"],
    "bug": ["flying", "rock", "fire"],
    "ghost": ["ghost", "dark"],
    "steel": ["fighting", "ground", "fire"],
    "electro": ["ground"],
    "psychic": ["bug", "ghost", "dark"],
    "ice": ["fighting", "rock", "steel", "fire"],
    "dragon": ["ice", "dragon", "fairy"],
    "dark": ["fighting", "bug", "fairy"],
    "fairy": ["poison", "steel"]
}

resdict = {
    "normal": ["ghost"],
    "grass": ["ground", "water", "grass", "electro"],
    "fire": ["bug", "steel", "fire", "grass", "ice", "fairy"],
    "water": ["steel", "fire", "water", "ice"],
    "fighting": ["rock", "bug", "dark"],
    "flying": ["ground", "fighting", "bug", "grass"],
    "poison": ["fighting", "poison", "bug", "grass", "fairy"],
    "ground": ["electro", "poison", "rock"],
    "rock": ["normal", "flying", "poison", "fire"],
    "bug": ["fighting", "ground", "grass"],
    "ghost": ["normal", "fighting", "poison", "bug"],
    "steel": ["poison", "normal", "flying", "rock", "steel", "grass", "psychic", "ice", "dragon", "fairy"],
    "electro": ["flying", "steel", "electro"],
    "psychic": ["fighting", "psychic"],
    "ice": ["ice"],
    "dragon": ["fire", "water", "grass", "electro"],
    "dark": ["psychic", "ghost", "dark"],
    "fairy": ["dragon", "fighting", "bug", "dark"]
}


class Pokemon:
    def __init__(self, name, type, hp, defe, atk):
        self.name = name
        self.type = type
        self.hp = hp
        self.defe = defe
        self.atk = atk
        self.res = resdict[f"{self.type}"]
        self.weak = weakdict[f"{self.type}"]


class pokemon_moves:
    def __init__(self):
        pass

    def enemyatk(self):
        global findmg
        findmg = enemy.dmg * enemy.atk / char.defe * 0.4
        if enemy.typev in char.weak:
            findmg *= 1.3

        if enemy.typev in char.res:
            findmg *= 0.7
        findmg = findmg * (round(random.uniform(0.85, 1.15), 2))

        print(char.hp)
        char.hp = char.hp - findmg
        print(char.hp)


    def charatk(self):
        global findmg
        findmg = char.dmg * char.atk / enemy.defe * 0.4
        if char.typev in enemy.weak:
            findmg *= 1.3

        if char.typev in enemy.res:
            findmg *= 0.7
        findmg = findmg * (round(random.uniform(0.85, 1.15), 2))
        round(enemy.hp, 2)
        print(enemy.hp)
        enemy.hp = enemy.hp - findmg
        round(enemy.hp, 2)
        print(enemy.hp)

    def run_attack(self, move, user):

        self.dmg = attackdict[f"{move}"]["damage"]
        self.typev = attackdict[f"{move}"]["typev"]
        if user == "char":
            pokemon_moves.charatk(self)
        elif user == "enemy":
            pokemon_moves.enemyatk(self)



class Poke1(pokemon_moves, Pokemon):
    def __init__(self, name, type, hp, defe, atk, moveone, movetwo, movethree, movefour):
        Pokemon.__init__(self, name, type, hp, defe, atk,)
        self.moveone = moveone
        self.movetwo = movetwo
        self.movethree = movethree
        self.movefour = movefour

    def move1(self, move=None, user="char"):
        if move is None:
            move = self.moveone
        pokemon_moves.run_attack(self, move=move, user=user)

    def move2(self, move=None, user="char"):
        if move is None:
            move = self.movetwo
        pokemon_moves.run_attack(self, move=move, user=user)

    def move1enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.moveone
        pokemon_moves.run_attack(self, move=move, user=user)

    def move2enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.movetwo
        pokemon_moves.run_attack(self, move=move, user=user)
    
    def move3(self, move=None, user="char"):
        if move is None:
            move = self.movethree
        pokemon_moves.run_attack(self, move=move, user=user)

    def move4(self, move=None, user="char"):
        if move is None:
            move = self.movefour
        pokemon_moves.run_attack(self, move=move, user=user)

    def move3enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.movethree
        pokemon_moves.run_attack(self, move=move, user=user)

    def move4enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.movefour
        pokemon_moves.run_attack(self, move=move, user=user)


def create_mons():
    global enemy, char
    if starter == "bulbasaur":
        enemy = Poke1("Squirtle", "water", 75, 80, 60, "tackle", "bubblebeam", "tackle", "bubblebeam")
        char = Poke1("Bulbasaur", "grass", 80, 60, 75, "tackle", "grasswhip", None, None)

    if starter == "squirtle":
        enemy = Poke1("Charmander", "fire", 70, 75, 80, "tackle", "ember", "tackle", "ember")
        char = Poke1("Squirtle", "water", 75, 80, 60, "tackle", "bubblebeam", None, None)

    if starter == "charmander":
        enemy = Poke1("Bulbasaur", "grass", 80, 80, 80, "tackle", "grasswhip", "tackle", "grasswhip")
        char = Poke1("Charmander", "fire", 80, 80, 80, "tackle", "ember", None, None)


window = tk.Tk()

spritedict = {
    "charmander": tk.PhotoImage(file="charmander.png", height=150, width=150),
    "bulbasaur": tk.PhotoImage(file="bulbasaur.png", height=150, width=150),
    "squirtle": tk.PhotoImage(file="squirtle.png", height=150, width=150),
    "pikachu": tk.PhotoImage(file="pikachu.png", height=150, width=150)
}


window.title("Pokemon auf Wish")
window.resizable(False, False)

screen = tk.Canvas(window, width=1600, height=900)
screen.grid(columnspan=3, rowspan=3)

instructions = tk.Label(window, text="Choose your Starter", font="Raleway")
instructions.grid(columnspan=1, column=1, row=0)


def game():

    print("Game started")
    global musplay
    musplay = 1
    music("standart.mp3")

    def check_effect(list):

        vars = list
        seff = []
        neff = []
        res = []

        i = 0
        for var in vars:
            i += 1
            if var in weakdict[f"{char.type}"]:
                seff.append(i)
            elif var in resdict[f"{char.type}"]:
                res.append(i)
            else:
                neff.append(i)

        if len(seff) > 0:
            return_var = random.choice(seff)
        elif len(neff) > 0:
            return_var = random.choice(neff)
        else:
            return_var = random.choice(res)

        return return_var

    def enemymovex():

        avtypes = [attackdict[f"{enemy.moveone}"]["typev"], attackdict[f"{enemy.movetwo}"]["typev"], attackdict[f"{enemy.movethree}"]["typev"], attackdict[f"{enemy.movefour}"]["typev"]]
        enemymove = check_effect(avtypes)

        if enemymove == 1:
            logging(f"\n {enemy.name} has used {enemy.moveone}", "enemy")
            enemy.move1enemy()

        if enemymove == 2:
            logging(f"\n {enemy.name} has used {enemy.movetwo}", "enemy")
            enemy.move2enemy()

        if enemymove == 3:
            logging(f"\n {enemy.name} has used {enemy.movethree}", "enemy")
            enemy.move3enemy()

        if enemymove == 4:
            logging(f"\n {enemy.name} has used {enemy.movefour}", "enemy")
            enemy.move4enemy()

    def updatehp():

        charhp = tk.Label(window, text=char.name + "  " + str(int(char.hp)), font="Raleway")
        charhp.grid(columnspan=2, column=0, row=2)

        enemyhp = tk.Label(window, text=enemy.name + "  " + str(int(enemy.hp)), font="Raleway")
        enemyhp.grid(columnspan=2, column=2, row=4)

    def game_done():
        global game_over
        if enemy.hp < 1:
            #mixer.music.pause()
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Won"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)
        if char.hp < 1:
            #mixer.music.pause()
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Lost"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)

    def choosemove1():
        if not enemy.hp < 1 and not char.hp < 1:
            logging(f"\n {char.name} has used {char.moveone}", "char")
            char.move1()
            enemymovex()
            updatehp()

        game_done()

    def choosemove2():
        if not enemy.hp < 1 and not char.hp < 1:
            logging(f"\n {char.name} has used {char.movetwo}", "char")
            char.move2()
            enemymovex()
            updatehp()

        game_done()
    
    def choosemove3():
        if not enemy.hp < 1 and not char.hp < 1:
            logging(f"\n {char.name} has used {char.movethree}", "char")
            char.move3()
            enemymovex()
            updatehp()

        game_done()
    
    def choosemove4():
        if not enemy.hp < 1 and not char.hp < 1:
            logging(f"\n {char.name} has used {char.movefour}", "char")
            char.move4()
            enemymovex()
            updatehp()

        game_done()

    def logging(logged, tag):
        log.insert(tk.END, "\n" + str(logged), tag)
        log.see("end")


    screen = tk.Canvas(window, width=1600, height=900)
    screen.grid(columnspan=4, rowspan=5)

    log = tk.Text(window, height=5, background="black", foreground="white")
    log.grid(columnspan=4, column=0, row=0)
    log.tag_config("N", foreground="white")
    log.tag_config("enemy", foreground="red")
    log.tag_config("char", foreground="cyan")


    logging("Game started", "N")

    charsprite = tk.Label(window, image=spritedict[f"{char.name.lower()}"])
    charsprite.grid(columnspan=2, column=0, row=1)

    enemysprite = tk.Label(window, image=spritedict[f"{enemy.name.lower()}"])
    enemysprite.grid(columnspan=2, column=2, row=3)

    updatehp()

    move1_text = tk.StringVar()
    move1button = tk.Button(window, textvariable=move1_text, command=lambda: choosemove1(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move1_text.set(char.moveone[0].upper() + char.moveone[1:])
    move1button.grid(columnspan=2, column=4, row=1)

    move2_text = tk.StringVar()
    move2button = tk.Button(window, textvariable=move2_text, command=lambda: choosemove2(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move2_text.set(char.movetwo[0].upper() + char.movetwo[1:])
    move2button.grid(columnspan=2, column=4, row=2)

    move3_text = tk.StringVar()
    move3button = tk.Button(window, textvariable=move3_text, command=lambda: choosemove3(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move3_text.set(char.movethree[0].upper() + char.movethree[1:])
    move3button.grid(columnspan=2, column=4, row=3)

    move4_text = tk.StringVar()
    move4button = tk.Button(window, textvariable=move4_text, command=lambda: choosemove4(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move4_text.set(char.movefour[0].upper() + char.movefour[1:])
    move4button.grid(columnspan=4, column=4, row=4)



    if enemy.hp <= 0:
        print("You´ve won")

    if char.hp <= 0:
        print("You´ve lost")

def charchoose(stats):
    global char
    char = Poke1(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7], stats[8])
    clear_frame()
    custombuttonenemy(
        ["Squirtle", "water", 75, 80, 60, "tackle", "bubblebeam", None, None], 0,
        0)
    custombuttonenemy(
        ["Charmander", "fire", 70, 65, 80, "tackle", "ember", None, None], 0, 1)
    custombuttonenemy(
        ["Bulbasaur", "grass", 80, 60, 75, "tackle", "grasswhip", None, None], 0,
        2)
    custombuttonenemy(["Pikachu", "electro", 90, 55, 82, "tackle", "electro_ball", "grasswhip", None], 0, 3)


    

def custombuttonchar(stats , loc1, loc2):
    poke = tk.Button(window, text=stats[0], command=lambda: charchoose(stats), font="Raleway", bg="violet", fg="white",
                    height=2, width=15)
    poke.grid(column=loc1, row=loc2)


def enemychoose(stats):
    global enemy
    if stats[7] == None:
        stats[7] = stats[5]
    if stats[8] == None:
        stats[8] = stats[6]
    enemy = Poke1(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7], stats[8])
    clear_frame()
    game()



def custombuttonenemy(stats, loc1, loc2):
    poke = tk.Button(window, text=stats[0], command=lambda: enemychoose(stats), font="Raleway", bg="yellow", fg="black",
                     height=2, width=15)
    poke.grid(column=loc1, row=loc2)
    
    

def customgame():
    status = 0
    customg_text.set("Custom choosen")

    clear_frame()
    custombuttonchar(["Squirtle", "water", 75, 80, 60, "tackle", "bubblebeam", None, None],
                     0, 0)
    custombuttonchar(["Charmander", "fire", 70, 75, 80, "tackle", "ember", None, None], 0, 1)
    custombuttonchar(["Bulbasaur", "grass", 80, 60, 75, "tackle", "grasswhip", None, None], 0, 2)
    custombuttonchar(["Pikachu", "electro", 90, 55, 82, "tackle", "electro_ball", "grasswhip", None], 0, 3)












def clear_frame():
   for widgets in window.winfo_children():
      widgets.destroy()

def charm():
    charm_text.set("Charmander choosen")
    global starter
    starter = "charmander"
    clear_frame()
    create_mons()
    game()


charm_text = tk.StringVar()
charm_btn = tk.Button(window, textvariable=charm_text, command=lambda:charm(), font="Raleway", bg="red", fg="black", height=2, width=15)
charm_text.set("Charmander")
charm_btn.grid(column=0, row=1)

def bisa():
    bisa_text.set("Bulbasaur choosen")
    global starter
    starter = "bulbasaur"
    clear_frame()
    create_mons()
    game()

bisa_text = tk.StringVar()
bisa_btn = tk.Button(window, textvariable=bisa_text, command=lambda:bisa(), font="Raleway", bg="green", fg="black", height=2, width=15)
bisa_text.set("Bulbasaur")
bisa_btn.grid(column=1, row=1)

def squirt():
    squirt_text.set("Squirtle choosen")
    global starter
    starter = "squirtle"
    clear_frame()
    create_mons()
    game()

squirt_text = tk.StringVar()
squirt_btn = tk.Button(window, textvariable=squirt_text, command=lambda:squirt(), font="Raleway", bg="blue", fg="black", height=2, width=15)
squirt_text.set("Squirtle")
squirt_btn.grid(column=2, row=1)


customg_text = tk.StringVar()
customg_button = tk.Button(window, textvariable=customg_text, command=lambda:customgame(), font="Raleway", bg="violet", fg="white",
                           height=2, width=15)
customg_text.set("Fight Custom")
customg_button.grid(column=1, row=2)




window.mainloop()
















