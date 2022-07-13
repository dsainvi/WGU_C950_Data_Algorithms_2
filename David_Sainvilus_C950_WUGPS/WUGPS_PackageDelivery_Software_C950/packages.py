
import distances
import csv_data_reader

# Empty lists created
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distances = []
second_truck_distances = []
third_truck_distances = []

# Times the trucks leave the hub
first_leave_times = ['8:00:00']
second_leave_times = ['9:10:00']
third_leave_times = ['11:00:00']

# Set delivery_start to first_leave_time for all truck one packages -> O(n)
for index, value in enumerate(csv_data_reader.get_first_delivery()):
    csv_data_reader.get_first_delivery()[index][9] = first_leave_times[0]
    first_delivery.append(csv_data_reader.get_first_delivery()[index])

# Compare truck one addresses to address list -> O(n^2)
for index, outer in enumerate(first_delivery):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            first_truck_distances.append(outer[0])
            first_delivery[index][1] = inner[0]

# Call algorithm to sort packages for first truck
distances.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0

# Calculate total distance of the first truck and distance of each package -> O(n)
for index in range(len(distances.first_truck_index())):
    try:
        total_distance_1 = distances.get_distance(int(distances.first_truck_index()[index]),
                                                  int(distances.first_truck_index()[index + 1]), total_distance_1)

        deliver_package = distances.get_time(distances.get_current_distance(int(distances.first_truck_index()[index]),
                                                                            int(distances.first_truck_index()[index + 1])),
                                             first_leave_times)
        distances.first_truck_list()[index][10] = (str(deliver_package))
        csv_data_reader.get_hash_map().update(int(distances.first_truck_list()[index][0]), first_delivery)
    except IndexError:
        pass

# Set delivery_start to second_leave_time for all truck two packages -> O(n)
for index, value in enumerate(csv_data_reader.get_second_delivery()):
    csv_data_reader.get_second_delivery()[index][9] = second_leave_times[0]
    second_delivery.append(csv_data_reader.get_second_delivery()[index])

# Compare truck two addresses to address list -> O(n^2)
for index, outer in enumerate(second_delivery):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            second_truck_distances.append(outer[0])
            second_delivery[index][1] = inner[0]

# Call algorithm to sort packages for second truck
distances.get_shortest_route(second_delivery, 2, 0)
total_distance_2 = 0

# Calculate total distance of the second truck and distance of each package -> O(n)
for index in range(len(distances.second_truck_index())):
    try:
        total_distance_2 = distances.get_distance(int(distances.second_truck_index()[index]), int(distances.second_truck_index()[index + 1]), total_distance_2)

        deliver_package = distances.get_time(distances.get_current_distance(int(distances.second_truck_index()[index]), int(distances.second_truck_index()[index + 1])), second_leave_times)


        distances.second_truck_list()[index][10] = (str(deliver_package))
        csv_data_reader.get_hash_map().update(int(distances.second_truck_list()[index][0]), second_delivery)
    except IndexError:
        pass

# Set delivery_start to third_leave_time for all truck three packages -> O(n)
for index, value in enumerate(csv_data_reader.get_final_delivery()):
    csv_data_reader.get_final_delivery()[index][9] = third_leave_times[0]
    third_delivery.append(csv_data_reader.get_final_delivery()[index])

# Compare truck three addresses to address list -> O(n^2)
for index, outer in enumerate(third_delivery):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            third_truck_distances.append(outer[0])
            third_delivery[index][1] = inner[0]

# Call algorithm to sort packages for third truck
distances.get_shortest_route(third_delivery, 3, 0)
total_distance_3 = 0

# Calculate total distance of the third truck and distance of each package -> O(n)
for index in range(len(distances.third_truck_index())):
    try:
        total_distance_3 = distances.get_distance(int(distances.third_truck_index()[index]), int(distances.third_truck_index()[index + 1]), total_distance_3)


        deliver_package = distances.get_time(distances.get_current_distance(int(distances.third_truck_index()[index]), int(distances.third_truck_index()[index + 1])),  third_leave_times)


        distances.third_truck_list()[index][10] = (str(deliver_package))
        csv_data_reader.get_hash_map().update(int(distances.third_truck_list()[index][0]), third_delivery)
    except IndexError:
        pass


# Get distance of all packages -> O(1)
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3