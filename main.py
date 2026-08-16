class Robot():
    def __init__(self,name,battery,status):
        self.name = name
        self.battery = battery
        self.status = status
        
    def report(self):
        print(f"Robot: {self.name}")
        print(f"Battery_Level🔋: {self.battery}")
        print(f"Status: {self.status}")
        
    def charge(self):
        self.battery = 100
        print(f"{self.name} Fully Charged.")
        
    def shutdown(self):
        self.status = "Offline😑"
        print(f"{self.name} Currently {self.status}.")  
        
    def battery_check(self):
        if self.battery >= 70:
            print(f"Battery Level {self.battery} Excellent🔋") 
        elif self.battery >= 40:
            print(f"Battery Level {self.battery} Good✅")
        elif self.battery >= 20:
            print(f"Battery Level {self.battery} Low⚠️")
        else:
            print(f"Battery Level {self.battery} Recharge ")    

class CombatRobot(Robot):
    def __init__(self, name, battery, status, weapon):
        super().__init__(name, battery, status)
        self.weapon = weapon
    def report(self):
        super().report()
        print(f"weapon: {self.weapon}")
    def attack(self):
        print(f"{self.name} attacks with {self.weapon}!")    

class MedicalRobot(Robot):
    def __init__(self, name, battery, status, medicine_level):
        super().__init__(name, battery, status)
        self.medicine_level = medicine_level
    def report(self):
        super().report()
        print(f"medicine_level: {self.medicine_level}")
    def heal(self):
        print(f"{self.name} heals")    
        
class ScoutRobot(Robot):
    def __init__(self, name, battery, status, range_km):
        super().__init__(name, battery, status)
        self.range_km = range_km
    def report(self):
        super().report()    
        print(f"range_km: {self.range_km}")
    def scout(self):
        print(f"{self.name} Scouts {self.range_km}Km")   
                    

fleet = []

number = int(input("How many robots do u want to register?"))

for i in range(number):
    print(f"--------Register {i +1}--------")
    
    robot_type = input("Enter robot type(Combat,Medicine,Scout):").lower()
    
    name = input("Enter robot name:")
    battery = int(input("Enter robot battery level:"))
    status = input("Enter robot current status:")
    
    if robot_type == "combat":
        weapon = input("Enter weapon:")
        robot = CombatRobot(name, battery, status, weapon)
    elif robot_type == "medicine":
        medicine_level = int(input("Enter Medicine level:"))
        robot = MedicalRobot(name, battery, status, medicine_level)
    elif robot_type == "scout":
        range_km = float(input("Enter the scouting range_km:")) 
        robot = ScoutRobot(name, battery, status, range_km)
    else:
        print ("Invalid robot_type!!") 
        continue
    fleet.append(robot)          


#combat_1 = CombatRobot("Mark-1",23,"Online😐","Laser_Canon") 
#combat_2 = CombatRobot("Mark-2",78,"Online😐","Machine_Gun")
#Medical_1 = MedicineRobot("Mark-M",12,"Online😐",78)
#Medical_2 = MedicineRobot("Mark-3",50,"Online😐",12)
#Scout_1 = ScoutRobot("Mark-X",45,"Online😐",125.4)

#fleet = [ combat_1, combat_2, Medical_1, Medical_2, Scout_1]

print("\n===== FLEET REPORT =====")
for i, robot in enumerate(fleet, start=1):
    print(f"\n--- Robot {i} ---")
    if isinstance(robot, CombatRobot):
        print(type(robot).__name__)
        robot.battery_check()
        robot.report()
        robot.attack()
    elif isinstance(robot, MedicalRobot):
        print(type(robot).__name__)  
        robot.battery_check()
        robot.report()
        robot.heal()
    elif isinstance(robot, ScoutRobot):
        print(type(robot).__name__)  
        robot.battery_check()
        robot.report()   
        robot.scout()
        