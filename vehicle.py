class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

    def stop(self):
        print(f"{self.brand} is stopping...")


class Car(Vehicle):
    def play_music(self):
        print(f"{self.brand} is playing music 🎶")

    def turn_on_ac(self):
        print(f"{self.brand}'s AC is now ON ❄️")

    def open_sunroof(self):
        print(f"{self.brand}'s sunroof is open 🌞")

    def drive(self):
        print(f"{self.brand} is driving smoothly 🚗💨")


class Bike(Vehicle):
    def wheelie(self):
        print(f"{self.brand} is doing a wheelie! 🏍️🔥")

    def kick_start(self):
        print(f"{self.brand} is being kick-started 🔧")

    def rev_engine(self):
        print(f"{self.brand} revs its engine: VROOOM! 💥")

    def park(self):
        print(f"{self.brand} is parked using the side stand 🛑")


class Truck(Vehicle):
    def load_cargo(self):
        print(f"{self.brand} is loading cargo 📦")

    def unload_cargo(self):
        print(f"{self.brand} has unloaded the cargo 🛻")

    def attach_trailer(self):
        print(f"{self.brand}'s trailer is now attached 🔗")

    def detach_trailer(self):
        print(f"{self.brand}'s trailer has been detached ❌")

    def blow_horn(self):
        print(f"{self.brand} is blowing its horn: HONK HONK! 🚚📣")


# Object Instantiation
car = Car("Mercedes")
bike = Bike("BMW")
truck = Truck("Cadillac")

# Car Features
print("\n--- Car Actions ---")
car.play_music()
car.turn_on_ac()
car.open_sunroof()
car.drive()

# Bike Features
print("\n--- Bike Actions ---")
bike.wheelie()
bike.kick_start()
bike.rev_engine()
bike.park()

# Truck Features
print("\n--- Truck Actions ---")
truck.load_cargo()
truck.unload_cargo()
truck.attach_trailer()
truck.detach_trailer()
truck.blow_horn()
