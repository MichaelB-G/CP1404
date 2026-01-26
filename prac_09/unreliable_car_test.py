"""
CP1404 Practical 09 - Test UnreliableCar
"""

from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar behaviour."""
    # Create two cars: one very reliable and one very unreliable
    reliable_car = UnreliableCar("Reliable", 100, 90)  # 90% chance to drive
    unreliable_car = UnreliableCar("Unreliable", 100, 10)  # 10% chance to drive

    print("Testing Reliable Car:")
    for i in range(5):
        print(f"Attempt {i+1}: drove {reliable_car.drive(10)}km")

    print("\nTesting Unreliable Car:")
    for i in range(5):
        print(f"Attempt {i+1}: drove {unreliable_car.drive(10)}km")

if __name__ == "__main__":
    main()
