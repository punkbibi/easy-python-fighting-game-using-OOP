
import random

class Story:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
       return ("""
        მოგესალმებით ესა არის მინი 'Fighting' თამაში. მოგაწვდით მცირედ ინსტრუქციას:
        გექნებათ 2 'Game mode' PvP და PvE. დასაწყისში გთხოვთ ჩაწეროთ გმირის სახელი და მაქსიმალური ძალა.
        მაქსიმალური ძალა არ შეიძლება იყოს 50 ზე მეტი, ის განსაზღვრავს რა range ში იქნება ალბათობით ამორჩეული დარტყმის damage
        გაქვთ შესაძლებლობა ჩაწეროთ კრიტიკული damage ს ალბათობა, გაითვალისწინეთ რომ არც ეს მნიშვნელობა შეიძლება იყოს 50 ზე მეტი.
        crit. damage დაგაკლებთ HP ს მაგრამ სანაცვლოდ იმდენივეს მოგიმატებთ damage ში. თუ არ გსურთ crit. damage ჩაწერეთ  0
        """)

class Fighter:
    def __init__(self, name, power=None, crit=None, health=100):
        self.__name = name
        self.power = power
        self.health = health
        self.crit = crit
        
    def get_name(self):
        return self.__name
    
    def attack(self, other, krit):
        damage1 = random.randrange(0, self.power + 1)
        krit = self.crit
        if krit is None: pass 
        else:
            crit_1 = random.randrange(0, 101)
            if self.crit is not None and crit_1 in range(0, krit+1):
            
                print(f"{self.get_name()}'s basic power:{damage1}")
                damage1 += crit_1
                print(f"{self.get_name()} got crit. damage")
                new_health1 = self.health - crit_1
                self.health = new_health1
                print(f"{self.get_name()}'s crit: {crit_1}")
                print(f"{self.get_name()}'s new damage: {damage1}")
                print(f"{self.get_name()}'snew health: {self.health}")
                print("************")
                if self.health <= 0:
                    print(f"{self.get_name()} is dead because of crit. damage\n {other.get_name()} won with HP: {other.health}")
                    return True
                else: pass
        
            else:
                print(f"{self.get_name()} doesn't got crit. damage") 
                print("************") 
        
        other.health -= damage1
        print(f"{self.get_name()}, damaged {other.get_name()} for {damage1} ")
        print(f"{self.get_name()}'s health: {self.health}\n{other.get_name()}'s health: {other.health}")
        print("************")
        return False    
       
            
class Game:
    def __init__(self):
        self.enemy = [Fighter("Goblin", 25),
                      Fighter("ბესო", 35),
                      Fighter("Dragon", 100),
                      Fighter("წავი", 1, 50),
                      Fighter("ქაიხოსრო", 35, 5),
                      Fighter("ვაშლი",0),
                      Fighter("კრიტიკოსი", 0, 100),
                      Fighter("ცეცხლი", 5),
                      Fighter("მობამბა", 90)
                      ] 
    
    
    def __str__(self) -> str:
        return "თამაში დაიწყო"
    
    
        
    def start(self):
        
        ga = int(input("1) PvP\n2)PvE: "))
        print("************")
        a = input(f"შეიყვანეთ სახეილი: ")
        b  = int(input(f"შეიყვანეთ ძალა: "))
        while b > 50:
            g  = int(input(f"შეიყვანეთ ძალა ახლიდან: "))
            b = g


        c = int(input(f"შეიყვანეთ crit. damage ს ალბათობა: "))
        if c == 0 :
            c_input = None
            c = c_input
        else:
                
            while c > 50:
                j = int(input(f"შეიყვანეთ crit. damage ახლიდან: "))
                c = j   
                    
        fi1 = Fighter(a,b,c)
        
        if ga ==1 :
            
            
            print("************")
            
            
            aa = input(f"შეიყვანეთ მეორე პერსონაჟის სახელი: ")
            bb = int(input(f"შეიყვანეთ ძალა: "))
            while bb > 50:
                gg  = int(input(f"შეიყვანეთ ძალა ახლიდან: "))
                bb = gg
                   
            cc = int(input(f"შეიყვანეთ crit. damage ს ალბათობაa: "))
            
            if cc == 0 :
                cc_input = None
                cc = cc_input
            else:
            
                while cc > 50:
                    jj = int(input(f"შეიყვანეთ crit. damage ახლიდან: "))
                    cc = jj  
                    
           
            
            fi2 = Fighter(aa, bb, cc)
            
            
            
            while True:
                print(f"{fi1.get_name()}'s health: {fi1.health}\n{fi2.get_name()}'s health: {fi2.health}")
                print("************")
                
                fi1.attack(fi2, fi1.crit)
                if fi1.health <= 0:
                    # print(f"{fi1.get_name()} is dead because of crit. damage\n {fi2.get_name()} won with HP: {fi2.health}")
                    break
                elif fi2.health <= 0:
                        print(f"{fi2.get_name()} is dead and {fi1.get_name()} won with HP: {fi1.health}")
                        break
                
                fi2.attack(fi1, fi2.crit)
                if fi2.health <= 0:
                    break
                        
                if fi1.health <= 0:
                    print(f"{fi1.get_name()} is dead and {fi2.get_name()} won with HP: {fi2.health}")
                    break
        elif ga == 2:
            print("************")
            rand_enemy = random.choice(self.enemy)
            
            while True:
                print(f"{fi1.get_name()}'s health: {fi1.health}\n{rand_enemy.get_name()}'s health: {rand_enemy.health}")
                print("************")
                
                fi1.attack(rand_enemy, fi1.crit)
                if fi1.health <= 0:
                    # print(f"{fi1.get_name()} is dead because of crit. damage\n {fi2.get_name()} won with HP: {fi2.health}")
                    break
                elif rand_enemy.health <= 0:
                        print(f"{rand_enemy.get_name()} is dead and {fi1.get_name()} won with HP: {fi1.health}")
                        break
                
                rand_enemy.attack(fi1, rand_enemy.crit)
                if rand_enemy.health <= 0:
                    break
                        
                if fi1.health <= 0:
                    print(f"{fi1.get_name()} is dead and {rand_enemy.get_name()} won with HP: {rand_enemy.health}")
                    break
        else:
            print(f"უნდა შეიყვანოთ ან 1 ან 2")
        
story = Story()
print(story)                   
game = Game()
print(game)
game.start()



