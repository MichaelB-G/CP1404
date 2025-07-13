from prac_06.car import Car

def main():
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel after adding 20: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Drove: {distance_driven}km")
    print(limo)

main()
