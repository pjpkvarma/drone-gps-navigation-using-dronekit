
# reference : github.com/dronekit/dronekit-python

from dronekit import connect, VehicleMode, LocationGlobalRelative
import math
import time


drone = connect('/dev/ttyACM0', baud=115200, wait_ready=True)

target_altitude = 2 # 2 meters
speed = 0.5 # 0.5m/s

# check if drone is armable and arming the drone
if drone.is_armable:
    print("drone is armable")

print("Arming....")
print("Changing to Guuided mode")

drone.mode = VehicleMode("GUIDED")
drone.armed = True

print("Armed")

# checking if the drone is armed before taking off
while not drone.armed:
    print("waiting to arm")
    time.sleep()

print("Taking off")
drone.simple_takeoff(target_altitude)

# we have to wait until drone reaches the required altitude
while True:
    print(f"Altitude : {drone.location.global_relative_frame.alt}")

    if drone.location.global_relative_frame.alt >= target_altitude * 0.95 :
        print(" Reached target altitude ")
        break
    time.sleep()


"""
give a gps waypont here
-- this will be changed to get this gps waypoint as an argument
"""
lat = None
lon = None
alt = None

location1 = LocationGlobalRelative(lat, lon, alt)
drone.simple_goto(location1, groundspeed=speed)

time.sleep(20)

# make the drone come back to launch location
drone.mode = VehicleMode("RTL")
drone.close()

