
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

print("=== SATELLITE ORBIT SIMULATOR ===")
print("Day 2: Satellite Orbit Animation")

# Simplified illustrative model
orbit_radius = 5.0
earth_radius = 1.0
orbit_period = 20.0
time_step = 0.1

# Calculate the circular orbit
angles = [
    2 * math.pi * i / 360
    for i in range(361)
]

orbit_x = [orbit_radius * math.cos(a) for a in angles]
orbit_y = [orbit_radius * math.sin(a) for a in angles]

# Create the figure
fig, ax = plt.subplots(figsize=(8, 8))

earth = plt.Circle(
    (0, 0),
    earth_radius,
    color="royalblue",
    label="Earth"
)
ax.add_patch(earth)

ax.plot(
    orbit_x,
    orbit_y,
    "--",
    color="gray",
    label="Satellite Orbit"
)

satellite, = ax.plot(
    [orbit_radius],
    [0],
    "ro",
    markersize=9,
    label="Satellite"
)

# Display the trail behind the satellite
trail, = ax.plot([], [], color="orange", linewidth=1.5, label="Trail")

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("X Position (illustrative units)")
ax.set_ylabel("Y Position (illustrative units)")
ax.set_title("Satellite Orbit Animation - Day 2")
ax.grid(True, alpha=0.3)
ax.legend()

# Store positions for the trail
trail_x = []
trail_y = []

def update(frame):
    angle = 2 * math.pi * frame / 200

    x = orbit_radius * math.cos(angle)
    y = orbit_radius * math.sin(angle)

    satellite.set_data([x], [y])

    trail_x.append(x)
    trail_y.append(y)

    trail.set_data(trail_x, trail_y)

    return satellite, trail

animation = FuncAnimation(
    fig,
    update,
    frames=range(201),
    interval=50,
    blit=False,
    repeat=True
)

plt.show()
