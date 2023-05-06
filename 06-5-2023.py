def distance_ran(speed, run_time, rest_time, total_time):
    # Calculate the distance covered by each runner
    distance = 0
    time_elapsed = 0
    while time_elapsed < total_time:
        if time_elapsed % (run_time + rest_time) < run_time:
            distance += speed
        time_elapsed += 1
    return distance

print("At the end of 1234th seconds:")
print("John has run a total of {}m".format(distance_ran(10, 6, 20, 1234)))
print("James has run a total of {}m".format(distance_ran(8, 8, 25, 1234)))
print("Jenna has run a total of {}m".format(distance_ran(12, 5, 16, 1234)))
print("Josh has run a total of {}m".format(distance_ran(7, 7, 23, 1234)))
print("Jacob has run a total of {}m".format(distance_ran(9, 4, 32, 1234)))
print("Jerry has run a total of {}m".format(distance_ran(5, 9, 18, 1234)))
print("Therefore, the winning runner is Jenna with a distance of 3540m")


