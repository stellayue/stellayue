import random
import time


class Hero:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = 100
        self.internal_energy = 5
        self.strength = 3
        self.morality = 5
        self.intelligence = 5
        self.money = 500
        self.skills = []
        self.round = 1
        self.sect = None
        self.house = None
    
    def hunt(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(3,7)
        else:
            gain = random.randint(8,12)
            print("You've met a lot of prey this month.")
        self.strength += gain
        print(f"Strength +{gain} from hunting.")
    def study(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(3,7)
        else:
            gain = random.randint(8,12)
            print("You had a flash of brilliance.")
        self.intelligence += gain
        print(f" Intelligence +{gain} from studying.")
    def help(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(3,7)
        else:
            gain = random.randint(8,12)
            print("You met a monk in the city and he gave you some scriptures to study.")
        self.morality += gain
        print(f"Morality +{gain} from helping others.")
    def work(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(300,600)
        else:
            gain = random.randint(700,900)
            print("Your boss rewarded you for your honesty!")
        self.money += gain
        print(f"Money +{gain} from working.")
    def cultivate(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(3,7)
        else:
            gain = random.randint(8,12)
            print("You've come to your senses.")
        self.internal_energy += gain
        print(f"Internal Energy +{gain} from cultivating.")
    def wudang(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(8,12)
        else:
            gain = random.randint(13,16)
            print("You've gained a lot of internal strength at Wudang Mountain!")
        self.internal_energy += gain
        print(f"Internal Energy +{gain} from Wudang.")
    def kunlun(self):
        chance = random.random()
        if chance < 0.7:
            gain = random.randint(8,12)
        else:
            gain = random.randint(13,16)
            print("You've gained a lot of strength at Kunlun Mountain!")
        self.strength += gain
        print(f"Strength +{gain} from Kunlun")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def sect_attack(self):
        if self.sect == 'Wudang':
            damage = self.strength * 0.7 + self.morality * 0.15
        elif self.sect == 'Kunlun':
            damage = self.strength * 0.8 + self.intelligence * 0.2
        else:
            damage = self.strength * 0.5
        return damage

    def sect_defense(self):
        if self.sect == 'Wudang':
            defense = self.internal_energy * 0.6
        elif self.sect == 'Kunlun':
            defense = self.internal_energy * 0.3
        else:
            defense = self.internal_energy * 0.1
        return defense
    
    def miss(self):
        if "Lingbo_weibu" in self.skills:
            if random.random()< 0.3:
                time.sleep(1)
                print(f"{self.name} used Lingbo Weibu and dodged the attack!")
                damage = 0
                return True  
        return False
    def unlock_skills(self):
        if self.sect == 'Kunlun':
            if self.internal_energy > 30 and "Lingbo_weibu" not in self.skills:
                time.sleep(1)
                print("You stand quietly by the water's edge, gazing inwardly, only to realize that your internal energy flows quietly through your body")
                time.sleep(1.5)
                print("As if a light wind is blowing on your face and water waves are rippling.")
                time.sleep(1)
                print("You've realized the ultimate lightness of being-- [Ling Bo Wei Bu].")
                self.skills.append("Lingbo_weibu")
        if self.sect == "Wudang":
            if self.internal_energy > 40 and self.morality > 30 and "Taiji_Shinkong" not in self.skills:
                time.sleep(1)
                print("The two qi of yin and yang intertwined and flowed between the meridians, rigidity and flexibility, emptiness and reality.")
                time.sleep(1.5)
                print("As you breathe in and out, your body seems to be dancing and quiet, and your mind gradually enters the realm of selflessness.")
                time.sleep(1)
                print("You've realized the ultimate power-- [Taiji Shinkong].")
                self.skills.append("Taiji_Shinkong")




    
    def show(self):
        print("\nCurrent Status:")
        print(f"Name: {self.name}")
        print(f"Sect: {self.sect}")
        print(f"HP: {self.hp:.2f}")
        print(f"Strength: {self.strength}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Morality: {self.morality}")
        print(f"Internal Energy: {self.internal_energy}")
        print(f"Money: {self.money}")
        print(f"Month: {self.round}/24")

partners = []
clues = []

class House:
    def __init__(self):
        self.farm = 0
        self.book_room = 0
        self.money = 0
        self.internal_energy = 0
        self.intelligence = 0

    def option1(self):
        self.farm = 2
        self.book_room = 1
        self.money = 400
        self.internal_energy = 2
        self.intelligence = 2

    def option2(self):
        self.farm = 1
        self.book_room = 2
        self.money = 400
        self.internal_energy = 4
        self.intelligence = 4

class Boss:
    def __init__(self,name,hp,strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self,target):
        damage = self.strength * 1.2
        target.hp -= damage
        print(f"{self.name} hits {target.name} for {damage} damage!")


def onevsone(player,boss):
    round_num = 1
    while player.hp > 0 and boss.hp > 0:
        time.sleep(1)
        print(f"\n--- Round {round_num} ---")
        print(f"{player.name}: HP {player.hp:.2f}")
        print(f"{boss.name}: HP {boss.hp:.2f}")
        selection = input("Choose action:\n1. Basic Attack\n2. Use Skill\n ").strip()
        damage = 0
        if selection == '1':
            damage = player.sect_attack()
            print(f"{player.name} attacks {boss.name} for {damage} damage!")
        elif selection == '2':
            if player.sect == "Wudang" and "taiji_fist" in player.skills:
                damage = 8 + player.strength * 0.7 + player.internal_energy * 0.2
                time.sleep(1)
                print("You used Taiji Fist!")
            elif player.sect == "Kunlun" and "kunlun_sword" in player.skills:
                damage = 10 + player.strength * 0.9 + player.intelligence * 0.1
                time.sleep(1)
                print("You used Kunlun Sword!")

        boss.hp -= damage
        if boss.hp < 0:
            boss.hp = 0
            print(f"You dealt {damage:.1f} damage to {boss.name}!")
            print(f"You defeated {boss.name}!")
            break

        damage = boss.strength
        if player.miss():
            actual_damage = 0
            print("You dodged the boss attack!")
        else:
            actual_damage = damage - player.sect_defense()
            if actual_damage < 0:
                actual_damage = 0
        player.hp -= actual_damage
        time.sleep(1)
        print(f"{boss.name} hits back and deals {actual_damage} damage to you!")

        if player.hp <= 0:
            print("You are defeated. Game Over.")
            break

        round_num += 1



    



def main():
    print("Welcome to the martial arts world!\nPlease enjoy your time on the world!")
    name = input("What' your name? ")
    time.sleep(0.8)
    print("A vision suddenly appeared in the sky, with auspicious clouds churning up, like a haze of fire. ")
    time.sleep(0.8)
    print("Some say it is auspicious; others say it is a sign of the coming chaos.")
    time.sleep(0.8)
    print("Are you, a nobody who has just stepped into the jianghu, a person chosen by fate, or a variable that stirs up the wind and clouds?")

    hero = Hero(name)
    boss1 = Boss("brigand_leader",50,22)
    while True:
        cho = input("There are two main sects to choose from here, choose Wudang to gain internal energy faster, choose Kunlun to gain strength faster, Which sect do you want to choose?[Wudang/Kunlun] ")
        if cho.lower() == 'wudang':
            hero.sect = 'Wudang'
            time.sleep(1)
            print("Your master taught you the basic Wudang moves.")
            hero.skills.append('taiji_fist')
            time.sleep(0.2)
            print("You have learned [Taiji Fist]!\n")
            break
        elif cho.lower() == 'kunlun':
            hero.sect = 'Kunlun'
            time.sleep(1)
            print("Your master taught you the basic Kunlun moves.")
            hero.skills.append('kunlun_sword')
            time.sleep(0.2)
            print("You have learned [Kunlun Sword]!\n")
            break
        else:
            print('Please choose either Wudang or Kunlun')

    

    while hero.round <= 24:

        if hero.round == 5:
            time.sleep(1.5)
            print("\n\n\nOne day you were walking in the countryside.")
            time.sleep(1.2)
            print("Suddenly you see a group of bandits in the distance, and they're tying up a handsome gentleman.")
            time.sleep(1.5)
            if hero.internal_energy > 10:
                print("You focus your internal energy and manage to overhear their sinister conversation.")
                time.sleep(1.2)
                print("They're planning to sell him to a distant warlord!")
            else:
                print("You can't hear clearly, but you know something's wrong.")
            time.sleep(1.2)
            print("You grit your teeth and decide to rescue him.")
            time.sleep(1)
            print("You're the first to catch a thief, and you're right next to him in a flash.")
            time.sleep(1)
            print("The mountain bandit: \nWhere's the kid from who doesn't know what he's doing?")
            time.sleep(2)
            print("You don't panic. You speak slowly.")
            time.sleep(1)
            print(f"You:\n I'm {hero.name}, I'm going to teach you a lesson today. ")
            time.sleep(2)
            print("The bandits laughed and didn't take it seriously")
            time.sleep(1)
            print("Only see the leader coming at you fast.")
            onevsone(hero, boss1)
            if boss1.hp == 0:
                print("You fought valiantly and managed to save the partner!")
                print("During this event, you boosted a lot of attributes\n\n\n")
                hero.intelligence += 3
                hero.morality += 5
                hero.money += 200
                time.sleep(1.2)
                print("This teenager, looking at you gratefully\n Watched you for a long time")
                time.sleep(1)
                print("You also notice his gaze. The boy's gaze is clear.Slender and graceful.")
                time.sleep(1)
                print("Zephyr:\nThank you for saving my life. ")
                time.sleep(1)
                print("To tell you the truth, I've left home and I'm ready to go out to make a name for myself.")
                time.sleep(1.5)
                print("I think you're a good man. Can I join you in the world?")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("You saw him and you thought he was a good match.")
                time.sleep(0.5)
                print("So you agreed.")
                time.sleep(1)
                print("This teenager is obviously happy, he takes out the wine from his backpack and you all drink together")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("Wine into the proud gas, sword light cold shadow shine sky high.")
                time.sleep(2.5)
                print("The road to the jianghu is long, and the heroes share this night.")
                partners.append("Zephyr")
                print("You have a new partner on your team.")
            else:
                print("You attempted a rescue, but failed due to lack of strength. You have suffered some injuries.\n\n\n")



        if hero.round == 8:
            time.sleep(1.2)
            print("\n\n\nYou stumble upon a treasure merchant in the mountains who sells you several magical secret books:")
            time.sleep(0.5)
            print("1. Nine Chapters of Arithmetic - Raising Intelligence (Costs 800)")
            print("2. Tao Te Ching - raising morality (cost 800)")
            print("3. The Nine Deadly Wonders - raise internal_energy (cost 800)")
            print("4. Hammering - Increase Strength (Costs 800)")
            print("5. Don't buy\n\n\n")

            answer = input("which book do want to buy? ").strip()
            if hero.money < 800 and answer != '5':
                print("You don't have any money. The businessman gave you a blank stare and left.")
            else:
                if answer == "1":
                    hero.intelligence += 12
                    hero.money -= 800
                    print("You feel so much smarter!")
                elif answer == "2":
                    hero.money -= 800
                    hero.morality += 12
                    print("You've had an epiphany.")
                elif answer == "3":
                    hero.money -= 800
                    hero.internal_energy += 12
                    print("You've gained a lot of internal strength.")
                elif answer == "4":
                    hero.money -= 800
                    hero.strength += 12
                    print("You've gained strength.")
                else:
                    print("You chose not to buy anything.")

        if hero.round == 10:
            time.sleep(2)
            print("You've been in the jungle for a while now, and you've got a sudden urge to buy a house.")
            time.sleep(2)
            print("Home traders do a double take when they see you coming.")
            time.sleep(1)
            print("Home traders:\nWhat kind of house do you want to buy?")
            time.sleep(1)
            print("You followed him around and asked him for a price")
            time.sleep(1)
            print("Home traders:\nWe've got a deal. It's only 3,000.It's a great value for the location. ")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            print("You left when he wasn't looking.")
            if "Zephyr" in partners:
                time.sleep(2)
                print("On a moonlit night, you're drinking alone.")
                time.sleep(2)
                print("Suddenly, you feel someone approaching. It's him. Zephyr")
                time.sleep(2)
                print("Zephyr:\nWhy are you drinking alone, brother?\nWe drink together.")
                time.sleep(2)
                print("Sensing your plight, the boy quietly purchases a cozy home for you.")
                time.sleep(1)
                print("Zephyr:\nThis is my gift to you, now we have a place to rest as we roam the martial world together.")
                time.sleep(2)
                print("he says with a smile, and signals a toast. It's all in the wine.")
                time.sleep(2)
                print("in the vast world of heroes, friendship lights the way forward.")
                time.sleep(1)
                print("You get a house.The house will spawn every turn and will restore your maximum blood value.")
                hero.house = House()
                while True:
                    time.sleep(1)
                    print("Please choose the extra construction of the house:")
                    print("1. 2 farms + 1 study_room, 400 gold per turn, 2 internal strength and 2 intelligence.")
                    print("2. 1 farm + 2 study_room, 200 gold per turn, 4 internal strength and 4 intelligence.")
                    answer1 = input("Please enter 1 or 2: ").strip()
                    if answer1 == '1':
                        hero.house.option1()
                        print("You chose option 1: 2 Farmland + 1 Study.")
                        break
                    elif answer1 == '2':
                        hero.house.option2()
                        print("You chose option 2: 1 Farmland + 2 Study.")
                        break
                    else:
                        print("Invalid input, please re-select")

        if hero.round == 14:
            time.sleep(1.2)
            print("\n\n\nOn this day you meet a beggar on the road who asks you for food")
            print("What do you want to do?")
            time.sleep(1)
            print("1.Give him some money. Well, he's a man of discriminating tastes.(money - 500)")
            print("2.You've got some catching up to do.")
            answer2 = input("Enter 1 or 2: ").strip()
            if hero.money > 500:
                if answer2 == '1':
                    clues.append("Mystery_Treasure")
                    hero.money -= 500
                    time.sleep(0.5)
                    print("He thanks you and tells you some clues about the treasure.")
                if answer2 == '2':
                    time.sleep(0.5)
                    print("After a short while, you find that face seems to have seen it somewhere, as if he is an elder of the Beggar's Association")
            else:
                print("You can only look at your wallet and apologize to him.")

        if hero.round == 16:
            if "Mystery_Treasure" in clues:
                time.sleep(1.5)
                print("\n\n\nYou follow the beggar's lead to the treasure site, where a man has already found it first")
                answer3 = input("1. Fighting, 2. Don't want it: (enter 1 or 2)").strip()
                if answer3 == '1':
                    boss1 = Boss("mystery_man",120,40)
                    print("You're about to go into battle.")
                    onevsone(hero, boss1)
                    if boss1.hp == 0:
                        time.sleep(1.5)
                        print("You took the treasure from him.")
                        time.sleep(1.5)
                        print("You open the package and obtain the Miracle Ring!")
                        print("With the ring on, you feel stronger, and your inner strength is increased by +10.")
                        hero.internal_energy += 10
                elif answer3 == "2":
                    print("Everything is on a first come, first served basis, so give it to him if he's first. Morality +2")
                    hero.morality += 2
                else:
                    print("please re-select")  

        if hero.round == 20:
            time.sleep(1.5)
            print("\n\n\nThis day you go to the biggest casino in town.")
            time.sleep(1.2)
            print("The Grand Casino was super crowded. All kinds of people.")
            time.sleep(1)
            print("You've come to the most crowded table.")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You've got a lot of inner strength. So you know the dealer is cheating.")
            time.sleep(1)
            print("A lot of people have been fooled by him, and it just so happens that he's noticed you and asked you to play a game.")
            print("What will you do?")
            print("1.play with him")
            if "Lingbo_weibu" in hero.skills:
                print("2. Use Lingbo_weibu")
                skill = "Lingbo_weibu"
            elif "Taiji_Shinkong" in hero.skills:
                print("2. Use Taiji_Shinkong")
                skill = "Taiji_Shinkong"
            else:
                skill = None
            answer4 = input("enter 1 or 2: ").strip()
            if answer4 == '1':
                chance = random.random()
                if chance < 0.95:
                    print("You made a bet. You lost. money- 200")
                    hero.money -= 200
                else:
                    print("You win, but it feel like the dealer let you win on purpose. money +200")
                    hero.money += 200
            elif answer4 == '2' and skill:
                if skill == "Lingbo_weibu":
                    time.sleep(2)
                    print("You just smiled. Walking past the dealer.")
                    time.sleep(1)
                    print("You got the dealer's bag of money so fast, the dealer didn't even notice. money +5000")
                    hero.money += 5000
                elif skill == "Taiji_Shinkong":
                    time.sleep(2)
                    print("You decided to teach this dealer a lesson.")
                    time.sleep(1)
                    print("You:\nDo you want to make a big bet with me?")
                    time.sleep(1)
                    print("The dealer smiles, thinking that this brother is going to lose a lot of money today。")
                    print("Dealer:\nI've got a good hand today. Don't be a liar if you lose.")
                    time.sleep(1)
                    print("You:\nThat's settled then.")
                    time.sleep(2)
                    print("The dealer starts rolling the dice.")
                    time.sleep(1)
                    print("You listen carefully to the state of the dice with your inner strength.")
                    time.sleep(1.5)
                    print("Pop!The dealer stopped shaking the dice.asking you to guess the size.")
                    time.sleep(1)
                    print("You've heard that the dice are small, so you said small.")
                    time.sleep(2)
                    print("You suddenly realized that the dice were big, and you used your inner strength to make it small again.")
                    time.sleep(2)
                    print("The moment it opened everyone was stunned. It's small. You win! money + 5000")
                    time.sleep(1.5)
                    print("The dealer was furious. He kept saying it was impossible. And come at you.")
                    time.sleep(1)
                    print("You used your powerful inner strength to send him flying 5 meters into the wall.")
                    time.sleep(2)
                    print("You:\nIf you come out and cheat again, you won't just fall on the wall.")
                    hero.money += 5000

        if hero.round == 22:
            time.sleep(2)
            print("\n\n\nThat day a merchant came to the town.")
            print("He sold some equipment.")
            print("Do you want to buy one?")
            print("1.Clouded Golden Armor +20 internal_energy\n2.Gilt Footwear +20 strength")
            answer5 = input("Enter 1 or 2:").strip()
            if hero.money > 3000:

                if answer5 == '1':
                    print("Your internal strength has increased by 20")
                    hero.internal_energy += 20
                    hero.money -= 3000
                elif answer5 == "2":
                    print("Your strength has increased by 20")
                    hero.strength += 20
                    hero.money -= 3000
            else:
                print("You don't have enough money!")


            



        if hero.round == 24:
            print("\n\n\nYour sect has decided to run a test.You need to defeat the evil people who are doing all the bad things.")
            print("You're about to go into battle.")
            boss2 = Boss("big_boss",300,70)
            onevsone(hero, boss2)
            if boss2.hp == 0:
                time.sleep(1)
                print("After many rounds, you defeated the big boss.")
                print("The rivers and lakes remain the same, and the wind and moon are boundless.")
                time.sleep(2)
                print("But you just know that the next time you make a move, it won't be for the world, it will be for the first time.")
                time.sleep(2)
                print("A dream of the jungle, a pot of turbid wine to thank the spring breeze. ")
                time.sleep(2)
                print("End")
            else:
                print("Try again~")
            break


        time.sleep(1)
        hero.show()
        time.sleep(1)
        print("") 
        print(f"------ the {hero.round} month ------")
        print("What do you want to do this month?")
        print("1.Hunting in the forest.")
        print("2.Studying at the Super school")
        print("3.Helping others in the towns.")
        print("4.Working at the No. 1 Restaurant.")
        print("5.Cultivating in the practice room")
        if cho.lower() == "wudang":
            print("6. You're practicing at Wudang Mountain.")
        if cho.lower() == "kunlun":
            print("6. You're practicing at Kunlun Mountain.")

        action = input("Enter the number of your choice (1-6): ").strip()
        if action == '1':
            hero.hunt()
        elif action == '2':
            hero.study()
        elif action == '3':
            hero.help()
        elif action == '4':
            hero.work()
        elif action == '5':
            hero.cultivate()
        elif action == '6':
            if hero.sect == "Wudang":
                hero.wudang()
            elif hero.sect == "Kunlun":
                hero.kunlun()
        
        else:
            print("You haven't done anything this month.")
        
        
        hero.unlock_skills()
        if hero.house is not None:
            hero.money += hero.house.money
            hero.internal_energy += hero.house.internal_energy
            hero.intelligence += hero.house.intelligence
            hero.hp = hero.max_hp

        hero.round += 1


if __name__ == "__main__":
    main()




