
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("=== SATELLITE POSITION ANIMATION ===")

# Orbital parameters
orbit_radius = 7000  # km
earth_radius = 1000  # illustrative size, km
earth_mu = 3.986004418e14  # m^3/s^2

# Calculate angular velocity
orbit_radius_m = orbit_radius * 1000
angular_velocity = math.sqrt(
    earth_mu / orbit_radius_m**3
)

# Create circular orbit
angles = [
    math.radians(degree)
    for degree in range(361)
]

orbit_x = [
    orbit_radius * math.cos(angle)
    for angle in angles
]
orbit_y = [
    orbit_radius * math.sin(angle)
    for angle in angles
]

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Draw Earth
earth = plt.Circle(
    (0, 0),
    earth_radius,
    color="royalblue",
    label="Earth"
)
ax.add_patch(earth)

# Draw orbit
ax.plot(
    orbit_x,
    orbit_y,
    "--",
    color="gray",
    label="Satellite Orbit"
)

# Satellite marker and trail
satellite, = ax.plot(
    [], [],
    "ro",
    markersize=9,
    label="Satellite"
)

trail, = ax.plot(
    [], [],
    color="orange",
    linewidth=1.5,
    label="Trail"
)

# Time display
time_text = ax.text(
    0.02, 0.95, "",
    transform=ax.transAxes
)

ax.set_title("Satellite Orbit Animation")
ax.set_xlabel("X Position (km)")
ax.set_ylabel("Y Position (km)")
ax.set_xlim(-8000, 8000)
ax.set_ylim(-8000, 8000)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
ax.legend()

# Store satellite trail
trail_x = []
trail_y = []

def update(frame):
    # Simulated elapsed time in seconds
    time_seconds = frame * 30

    # Calculate satellite position
    angle = angular_velocity * time_seconds

    x = orbit_radius * math.cos(angle)
    y = orbit_radius * math.sin(angle)

    trail_x.append(x)
    trail_y.append(y)

    satellite.set_data([x], [y])
    trail.set_data(trail_x, trail_y)

    time_text.set_text(
        f"Elapsed time: {time_seconds / 60:.1f} minutes"
    )

    return satellite, trail, time_text

animation = FuncAnimation(
    fig,
    update,
    frames=range(1000),
    interval=50,
    blit=False
)

print("Animation started. Close the figure to stop.")
plt.show()
