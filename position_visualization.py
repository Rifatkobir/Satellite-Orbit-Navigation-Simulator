
import math
import matplotlib.pyplot as plt

print("=== SATELLITE POSITION VISUALIZATION ===")

# Orbital parameters
orbit_radius = 7000  # km
earth_radius = 1000  # illustrative size, km

earth_mu = 3.986004418e14  # m^3/s^2
orbit_radius_m = orbit_radius * 1000

# Calculate angular velocity
angular_velocity = math.sqrt(
    earth_mu / orbit_radius_m**3
)

# Position after 10 minutes
time_seconds = 600
angle = angular_velocity * time_seconds

x = orbit_radius * math.cos(angle)
y = orbit_radius * math.sin(angle)

# Draw the orbit
orbit_x = []
orbit_y = []

for i in range(361):
    theta = math.radians(i)
    orbit_x.append(orbit_radius * math.cos(theta))
    orbit_y.append(orbit_radius * math.sin(theta))

plt.figure(figsize=(8, 8))

# Earth
earth = plt.Circle(
    (0, 0),
    earth_radius,
    color="royalblue",
    label="Earth"
)
plt.gca().add_patch(earth)

# Orbit and satellite
plt.plot(
    orbit_x, orbit_y,
    "--", color="gray",
    label="Satellite Orbit"
)

plt.scatter(
    x, y,
    color="red", s=100,
    label="Satellite Position"
)

plt.plot(
    [0, x], [0, y],
    "r:", alpha=0.7,
    label="Position Vector"
)

plt.title("Satellite Position After 10 Minutes")
plt.xlabel("X Position (km)")
plt.ylabel("Y Position (km)")
plt.axis("equal")
plt.xlim(-8000, 8000)
plt.ylim(-8000, 8000)
plt.grid(True, alpha=0.3)
plt.legend()

print(f"Time: {time_seconds / 60:.1f} minutes")
print(f"X position: {x:.2f} km")
print(f"Y position: {y:.2f} km")
print(f"Orbital angle: {math.degrees(angle):.2f} degrees")

plt.show()
