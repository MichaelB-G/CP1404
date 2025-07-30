"""
CP1404 Practical 09 - Test SilverServiceTaxi
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi fares."""
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)  # fanciness multiplier 4
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(f"Fare for 18km: ${fancy_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
