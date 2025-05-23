def show_movement(vehicle):
    vehicle.move()  # Demonstrates polymorphism

def main():
    my_car = Car("Toyota", "Corolla")
    my_plane = Plane("Boeing", "747")
    my_boat = Boat("Yamaha", "WaveRunner")

    # List of different vehicle types
    vehicles = [my_car, my_plane, my_boat]

    for v in vehicles:
        show_movement(v)

if __name__ == "__main__":
    main()
