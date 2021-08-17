import random
enemy_name_list = ["Stormtroopers", "Tusken Raiders", "Bounty Hunters", "Jawas"]
enemy_intro_list = [" this is going to hurt! ", " they are watching you... ", " Critical Hit! ", " beams of destruction! "]

class Adventurer:
    def __init__(self, name, beskar, health_points):
        self.name = name
        self.position = 0
        self.beskar = beskar
        self.health_points = health_points
    def __str__(self):
        ret = "---------------------------------------------------------------\n"
        ret += "Adventurer : " + self.name + "\n"
        ret += "Galaxy : " + str(self.position) + "\n"
        ret += "Beskar : " + str(self.beskar) + "\n"
        ret += "HP : " + str(self.health_points) + "\n"
        ret += "---------------------------------------------------------------\n"
        return ret

class Enemy:
    def __init__(self, name, position, introduction, damage):
        self.name = name
        self.position = position
        self.introduction = introduction
        self.damage = damage
    def __str__(self):
        ret = "---------------------------------------------------------------\n"
        ret += "Enemy : " + self.name + "\n"
        ret += "Position : " + str(self.position)
        ret += "Introduction : " + str(self.introduction) + "\n"
        ret += "Damage : " + str(self.damage) + "\n"
        ret += "---------------------------------------------------------------\n"
        return ret

def play(adventurer, enemies, path_length):
    print("*Initialization Complete*")
    print()
    print("It was a nice peaceful day in a Galaxy Far Far away, but the imperial forces stormed your ship and took baby yoda")
    print("Your mission is clear, We have reason to believe baby yoda is somewhere on Galaxy 10")
    print()
    print("Along the way you will come across some tough enemies so BEWARE!")
    print()
    print("Find the Baby.... It is the WAY!")
    for i in range(1, path_length+1): 
        input("\nPress RETURN to move forward.\n") # Wait for keypress
        adventurer.position = i 
        print(adventurer.name + " is at Galaxy " + str(adventurer.position))
        for enemy in enemies:
            if adventurer.position == enemy.position: 
                adventurer.health_points -= enemy.damage 
                print(enemy.introduction)
                print("Got attacked by " + enemy.name + " and lost " + str(enemy.damage) + " HP")
                break
        else: 
            pickup = random.randint(10, 50)
            adventurer.beskar += pickup
            print("Recieved " + str(pickup) + " beskar")
        if adventurer.health_points <= 0: # If the adventurer has died
            print("\n\n" + adventurer.name + " lost")
            break
    else:
        print("You Did it! " + adventurer.name + " Baby Yoda is saved!") # If adventurer reached the end
        print("This is the Way....")
        
def main():
    path_length = 10
    adventurer = Adventurer("Mandalorian", 0, 100)
    num_enemies = random.randint(int(0.3*path_length), int(0.7*path_length)) 
    enemies = []
    for _ in range(num_enemies):
        enemy_name, enemy_intro = random.choice(enemy_name_list), random.choice(enemy_intro_list)
        enemy_position, enemy_damage = random.randint(1, path_length), random.randint(20, 50)
        enemies.append(Enemy(enemy_name, enemy_position, "It's " + enemy_name + enemy_intro, enemy_damage))
    play(adventurer, enemies, path_length) 
    print("\n\nAt the end of the game:") 
    print(adventurer)

if __name__ == "__main__":
    main()