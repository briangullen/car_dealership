import vehicles

trucks = [vehicles.Truck('Ford', 10000, 25000),
          vehicles.Truck('Dodge', 20000, 20000),
          vehicles.Truck('Chevy', 30000, 15000)]
motorcycles = [vehicles.Motorcycle('Ducati', 5000, 15000, 250),
               vehicles.Motorcycle('Honda', 7000, 8000, 200),
               vehicles.Motorcycle('Yamaha', 10000, 5000, 150)]


def get_trucks():
    for i, truck in enumerate(trucks):
        print(f'{i + 1}: {vehicles.Truck.get_info(truck)}')


def get_bikes():
    for i, moto in enumerate(motorcycles):
        print(f'{i + 1}: {vehicles.Motorcycle.get_info(moto)}')


def hello_message():
    print('Welcome to GC Bikes & Trucks!')


def main():
    hello_message()
    vehicles_to_compare = list[vehicles.Vehicle]()
    while True:
        while True:
            vehicle_type = input('Which type of vehicle would you like to see? trucks or motorcycles: ')
            if vehicle_type == 'trucks':
                get_trucks()
                while True:
                    add_vehicle = input('Would you like to add a vehicle?: y/n: ')
                    if add_vehicle == 'y':
                        vehicle_choice = int(input('Which vehicle would you like to add?: '))
                        vehicle_id = trucks[vehicle_choice - 1]
                        vehicles_to_compare.append(vehicle_id)
                        print(f'Vehicle {vehicle_id.make} added to list.')
                    else:
                        break
                break
            if vehicle_type == 'motorcycles':
                get_bikes()
                while True:
                    add_vehicle = input('Would you like to add a vehicle?: y/n: ')
                    if add_vehicle == 'y':
                        vehicle_choice = int(input('Which vehicle would you like to add?: '))
                        vehicle_id = motorcycles[vehicle_choice - 1]
                        vehicles_to_compare.append(vehicle_id)
                        print(f'Vehicle {vehicle_id.make} added to list.')
                    else:
                        break
                break
            else:
                print("Sorry your choice wasn't valid. Please try again.")
        keep_going = input('Would you like to look at more vehicles? y/n: ')
        if keep_going != 'y':
            break

    print('Your vehicles to compare are:')
    for vehicle in vehicles_to_compare:
        print(f'> {vehicle.get_info()}')
        vehicle.make_noise()


if __name__ == '__main__':
    main()
