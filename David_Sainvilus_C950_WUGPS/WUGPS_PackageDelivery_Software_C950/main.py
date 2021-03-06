# David Sainvilus
# Student ID #: 001049272

from csv_data_reader import get_hash_map
from packages import total_distance
import datetime


class Main:
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('++++++++++++++++++++++++++++')
    print('Welcome to WGUPS Package delivery Program!')
    print('++++++++++++++++++++++++++++++\n')
    print(f'Delivery Route was completed in {total_distance():.2f} miles.\n')

    user_entry = input("""
Please select an number below to begin or type 'end' to end the program:
    0. Displays info for all packages at a particular time
    1. Displays info for a single package at a particular time
""")

    while user_entry != 'end':
        # Case if user selects Option #1
        # Get info for all packages at a particular time -> O(n)
        if user_entry == '0':
            try:
                user_input_time = input('Please enter a time (HH:MM:SS): ')
                (hrs, mins, secs) = user_input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Big O Complexity ->  O(n^2)
                for count in range(1, 41):
                    try:
                        first_time = get_hash_map().get_value(str(count))[9]
                        second_time = get_hash_map().get_value(str(count))[10]
                        (hrs, mins, secs) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass

                    # Shows user which packages left the hub
                    if convert_first_time >= convert_user_time:
                        get_hash_map().get_value(str(count))[10] = 'At Hub'
                        get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time

                        # Prints out package's current info
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                        )

                    # Shows user  which packages have left but have not been delivered
                    elif convert_first_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            get_hash_map().get_value(str(count))[10] = 'In transit'
                            get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                            # Prints out package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                            )

                        # Shows user which packages have already been delivered
                        else:
                            get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
                            get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                            # Prints out package's current info
                            print(
                                f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
                                f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
                            )
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()

        # Case if user selects Option #2
        # Get info for a single package at a particular time -> O(n)
        elif user_entry == '1':
            try:
                count = input('Enter a valid package ID: ')
                first_time = get_hash_map().get_value(str(count))[9]
                second_time = get_hash_map().get_value(str(count))[10]
                user_input_time = input('Enter a time (HH:MM:SS): ')
                (hrs, mins, secs) = user_input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Shows user  which packages have left the hub
                if convert_first_time >= convert_user_time:

                    get_hash_map().get_value(str(count))[10] = 'At Hub'
                    get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time

                    # Print package's current info
                    print(
                        f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                        f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                        f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                        f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                        f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
                    )

                # Shows user  which packages have left but have not been delivered
                elif convert_first_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        get_hash_map().get_value(str(count))[10] = 'In transit'
                        get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                            f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                            f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                            f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                            f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
                        )

                    # Shows user  which packages have already been delivered
                    else:
                        get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
                        get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time

                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
                            f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
                            f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
                            f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
                            f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
                            f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
                        )

            except ValueError:
                print('Invalid entry')
                exit()

        # Exit
        # This exits the program
        elif user_entry == 'end':
            exit()

        # Error
        # Print Invalid Entry and end the program
        else:
            print('Invalid entry!')
            exit()