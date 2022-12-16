import random
import tkinter as tk



findmg = None





class Pokemon():
    def __init__(self, name, type, hp, defe, atk, res, weak):
        self.name = name
        self.type = type
        self.hp = hp
        self.defe = defe
        self.atk = atk
        self.res = res
        self.weak = weak


class pokemon_moves():
    def __init__(self):
        pass

    def enemyatk(self):
        global findmg
        findmg = enemy.dmg * enemy.atk / char.defe * 0.4
        if enemy.typev in char.weak:
            findmg *= 1.3

        if enemy.typev in char.res:
            findmg *= 0.7
        round(char.hp, 2)
        print(char.hp)
        char.hp = char.hp - findmg
        round(char.hp, 2)
        print(char.hp)


    def charatk(self):
        global findmg
        findmg = char.dmg * char.atk / enemy.defe * 0.4
        if char.typev in enemy.weak:
            findmg *= 1.3

        if char.typev in enemy.res:
            findmg *= 0.7
        round(enemy.hp, 2)
        print(enemy.hp)
        enemy.hp = enemy.hp - findmg
        round(enemy.hp, 2)
        print(enemy.hp)

    def tackle(self):
        self.typev = "normal"
        self.dmg = 30

    def grasswhip(self):
        # grasswhip
        self.typev = "grass"
        self.dmg = 40

    def bubblebeam(self):
        # bubblebeam
        self.typev = "water"
        self.dmg = 40

    def ember(self):
        # ember
        self.typev = "fire"
        self.dmg = 40

    def atklist(self, move, user):
        atkmove = move
        usemover = user

        '''
        pokemon_moves.run_attack(attack:string)
        
        def run_attack(attack: str):
            match attack:
                case "tackle":
                    -- tackle attacke --
                
                case  "weed":
                    -- weed attacke --
                
                case _:
                    alle anderen faelle
        '''
        if atkmove == "tackle":
            pokemon_moves.tackle(self)
            if usemover == "char":
                pokemon_moves.charatk(self)
            elif usemover == "enemy":
                pokemon_moves.enemyatk(self)
            print(self.name + " used Tackle")
        if atkmove == "grasswhip":
            pokemon_moves.grasswhip(self)
            if usemover == "char":
                pokemon_moves.charatk(self)
            elif usemover == "enemy":
                pokemon_moves.enemyatk(self)
            print(self.name + " used Grasswhip")
        if atkmove == "bubblebeam":
            pokemon_moves.bubblebeam(self)
            if usemover == "char":
                pokemon_moves.charatk(self)
            elif usemover == "enemy":
                pokemon_moves.enemyatk(self)
            print(self.name + " used Bubblebeam")
        if atkmove == "ember":
            pokemon_moves.ember(self)
            if usemover == "char":
                pokemon_moves.charatk(self)
            elif usemover == "enemy":
                pokemon_moves.enemyatk(self)
            print(self.name + " used Ember")


class Poke1(pokemon_moves, Pokemon):
    def __init__(self, name, type, hp, defe, atk, res, weak, moveone, movetwo, movethree, movefour):
        Pokemon.__init__(self, name, type, hp, defe, atk, res, weak)
        self.moveone = moveone
        self.movetwo = movetwo
        self.movethree = movethree
        self.movefour = movefour

    def move1(self, move=None, user="char"):
        if move is None:
            move = self.moveone
        pokemon_moves.atklist(self, move=move, user=user)

    def move2(self, move=None, user="char"):
        if move is None:
            move = self.movetwo
        pokemon_moves.atklist(self, move=move, user=user)

    def move1enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.moveone
        pokemon_moves.atklist(self, move=move, user=user)

    def move2enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.movetwo
        pokemon_moves.atklist(self, move=move, user=user)
    
    def move3(self, move=None, user="char"):
        if move is None:
            move = self.movethree
        pokemon_moves.atklist(self, move=move, user=user)

    def move4(self, move=None, user="char"):
        if move is None:
            move = self.movefour
        pokemon_moves.atklist(self, move=move, user=user)

    def move3enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.movethree
        pokemon_moves.atklist(self, move=move, user=user)

    def move4enemy(self, move=None, user="enemy"):
        if move is None:
            move = self.movefour
        pokemon_moves.atklist(self, move=move, user=user)

    def moveinf(self):
        print("1: " + self.moveone[0].upper() + self.moveone[1:] + ",2: " + self.movetwo[0].upper() + self.movetwo[1:])


def enemymovex():
    enemymove = random.randrange(1, 3)
    if enemymove == 1:
        print("Enemy has choosen move 1")
        enemy.move1enemy()

    if enemymove == 2:
        print("Enemy has choosen move 2")
        enemy.move2enemy()

def create_mons():
    global enemy, char
    if starter == "bulbasaur":
        enemy = Poke1("Squirtle", "water", 75, 80, 60, ["fire", "test"], ["grass", "test"], "tackle", "bubblebeam", None, None)
        char = Poke1("Bulbasaur", "grass", 80, 60, 75, ["water", "test"], ["fire", "test"], "tackle", "grasswhip", "bubblebeam", None)

    if starter == "squirtle":
        enemy = Poke1("Charmander", "fire", 70, 75, 80, ["grass", "test"], ["water", "test"], "tackle", "ember", None, None)
        char = Poke1("Squirtle", "water", 75, 80, 60, ["fire", "test"], ["grass", "test"], "tackle", "bubblebeam", None, None)

    if starter == "charmander":
        enemy = Poke1("Bulbasaur", "grass", 80, 80, 80, ["water", "test"], ["fire", "test"], "tackle", "grasswhip", None, None)
        char = Poke1("Charmander", "fire", 80, 80, 80, ["grass", "test"], ["water", "test"], "tackle", "ember", None, None)



window = tk.Tk()

spritedict = {
    "charmander" : tk.PhotoImage(file="charmander.png", height=150, width=150),
    "bulbasaur" : tk.PhotoImage(file="bulbasaur.png", height=150, width=150),
    "squirtle" : tk.PhotoImage(file="squirtle.png", height=150, width=150),
}


window.title("Pokemon auf Wish")
window.resizable(False, False)

screen = tk.Canvas(window, width=1600, height=900)
screen.grid(columnspan=3, rowspan=3)

instructions = tk.Label(window, text="Choose your Starter", font="Raleway")
instructions.grid(columnspan=1, column=1, row=0)


def game():

    print("Game started")

    def updatehp():

        charhp = tk.Label(window, text=char.name + "  " + str(int(char.hp)), font="Raleway")
        charhp.grid(columnspan=2, column=0, row=1)

        enemyhp = tk.Label(window, text=enemy.name + "  " + str(int(enemy.hp)), font="Raleway")
        enemyhp.grid(columnspan=2, column=2, row=3)

    def choosemove1():
        if not enemy.hp < 1 and not char.hp < 1:
            print("You have choosen move 1")
            char.move1()
            enemymovex()
            updatehp()

        if enemy.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Won"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)

        if char.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Lost"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)




    def choosemove2():
        if not enemy.hp < 1 and not char.hp < 1:
            print("You have choosen move 2")
            char.move2()
            enemymovex()
            updatehp()

        if enemy.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Won"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)
        if char.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Lost"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)
    
    def choosemove3():
        if not enemy.hp < 1 and not char.hp < 1:
            print("You have choosen move 3")
            char.move3()
            enemymovex()
            updatehp()

        if enemy.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Won"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)
        if char.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Lost"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)
    
    def choosemove4():
        if not enemy.hp < 1 and not char.hp < 1:
            print("You have choosen move 4")
            char.move4()
            enemymovex()
            updatehp()

        if enemy.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Won"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)
        if char.hp < 1:
            clear_frame()
            game.text = tk.Label(window, text=("You´ve Lost"), font=('consolas', 40))
            game.text.grid(columnspan=4, column=2, row=2)






    screen = tk.Canvas(window, width=1600, height=900)
    screen.grid(columnspan=4, rowspan=4)

    charsprite = tk.Label(window, image=spritedict[f"{char.name.lower()}"])
    charsprite.grid(columnspan=2, column=0, row=0)

    enemysprite = tk.Label(window, image=spritedict[f"{enemy.name.lower()}"])
    enemysprite.grid(columnspan=2, column=2, row=2)

    updatehp()

    move1_text = tk.StringVar()
    move1button = tk.Button(window, textvariable=move1_text, command=lambda: choosemove1(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move1_text.set(char.moveone[0].upper() + char.moveone[1:])
    move1button.grid(columnspan=2, column=4, row=0)

    move2_text = tk.StringVar()
    move2button = tk.Button(window, textvariable=move2_text, command=lambda: choosemove2(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move2_text.set(char.movetwo[0].upper() + char.movetwo[1:])
    move2button.grid(columnspan=2, column=4, row=1)

    move3_text = tk.StringVar()
    move3button = tk.Button(window, textvariable=move3_text, command=lambda: choosemove3(), font="Raleway",
                            bg="yellow", fg="black", height=2, width=15)
    move3_text.set(char.movethree[0].upper() + char.movethree[1:])
    move3button.grid(columnspan=2, column=4, row=2)

    move4_text = tk.StringVar()
    move4button = tk.Button(window, textvariable=move4_text, command=lambda: choosemove4(), font="Raleway",
                            bg="yellow", fg="black", height=4, width=15)
    move4_text.set(char.movefour[0].upper() + char.movefour[1:])
    move4button.grid(columnspan=4, column=4, row=3)



    if enemy.hp <= 0:
        print("You´ve won")

    if char.hp <= 0:
        print("You´ve lost")


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





window.mainloop()



