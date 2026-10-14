
import math

print("=== SATELLITE POSITION CALCULATION ===")

# Orbital parameters
orbit_radius = 7_000_000  # meters
earth_mu = 3.986004418e14  # m^3/s^2

# Calculate orbital angular velocity
angular_velocity = math.sqrt(earth_mu / orbit_radius**3)

# Time after starting the simulation
time_seconds = 600  # 10 minutes

# Calculate satellite position
angle = angular_velocity * time_seconds

x = orbit_radius * math.cos(angle)
y = orbit_radius * math.sin(angle)

print(f"Time: {time_seconds / 60:.1f} minutes")
print(f"X position: {x / 1000:.2f} km")
print(f"Y position: {y / 1000:.2f} km")
print(f"Orbital angle: {math.degrees(angle):.2f} degrees")
