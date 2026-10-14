
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Simplified circular orbit parameters
orbit_radius = 7_000_000       # meters from Earth's center
earth_radius = 6_371_000       # meters
earth_mu = 3.986004418e14      # m^3/s^2

# Orbital calculations
orbital_speed = math.sqrt(earth_mu / orbit_radius)
angular_velocity = orbital_speed / orbit_radius
orbital_period = 2 * math.pi / angular_velocity

# Simulation state
elapsed_seconds = 0
time_step = 10

fig, ax = plt.subplots(figsize=(9, 8))
fig.subplots_adjust(left=0.12, right=0.97, top=0.92, bottom=0.10)
ax.set_aspect("equal")
ax.set_xlim(-8_000, 8_000)
ax.set_ylim(-8_000, 8_000)
ax.set_xlabel("X Position (km)")
ax.set_ylabel("Y Position (km)")
ax.set_title("Satellite Orbit - Live Telemetry")
ax.grid(True, alpha=0.3)

# Earth
earth = plt.Circle(
    (0, 0),
    earth_radius / 1000,
    color="royalblue",
    alpha=0.85,
    label="Earth"
)
ax.add_patch(earth)

# Orbit
theta = [i * 2 * math.pi / 360 for i in range(361)]
orbit_x = [
    orbit_radius * math.cos(a) / 1000 for a in theta
]
orbit_y = [
    orbit_radius * math.sin(a) / 1000 for a in theta
]
ax.plot(orbit_x, orbit_y, "--", color="gray",
        label="Satellite Orbit")

# Satellite and trail
satellite, = ax.plot([], [], "ro", markersize=11,
                     label="Satellite")
trail, = ax.plot(
    [], [],
    color="orange",
    linewidth=2.0,
    alpha=0.75,
    label="Trajectory"
)



# Velocity direction arrow
velocity_arrow = ax.quiver(
    [0], [0], [0], [0],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="limegreen",
    width=0.006,
    label="Velocity direction"
)

# Acceleration direction arrow
acceleration_arrow = ax.quiver(
    [0], [0], [0], [0],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="deepskyblue",
    width=0.006,
    label="Acceleration direction"
)






telemetry = ax.text(
    0.02, 0.98, "",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    color="white",
    bbox=dict(
        boxstyle="round,pad=0.6",
        facecolor="#172033",
        edgecolor="#38bdf8",
        linewidth=1.5,
        alpha=0.92
    )
)



trail_x = []
trail_y = []

def update(frame):
    global elapsed_seconds

    elapsed_seconds += time_step
    angle = angular_velocity * elapsed_seconds

    x = orbit_radius * math.cos(angle) / 1000
    y = orbit_radius * math.sin(angle) / 1000

    # Velocity components (km/s)
    vx = -orbital_speed * math.sin(angle) / 1000
    vy = orbital_speed * math.cos(angle) / 1000

    # Centripetal acceleration components (m/s^2)
    ax_acc = -(orbital_speed ** 2 / orbit_radius) * math.cos(angle)
    ay_acc = -(orbital_speed ** 2 / orbit_radius) * math.sin(angle)

    # Acceleration magnitude (m/s^2)
    acceleration_magnitude = math.sqrt(
        ax_acc ** 2 + ay_acc ** 2
    )

    altitude = (orbit_radius - earth_radius) / 1000

    # Keep only the most recent 150 trajectory points
    trail_x.append(x)
    trail_y.append(y)

    max_trail_points = 100

    if len(trail_x) > max_trail_points:
        trail_x.pop(0)
        trail_y.pop(0)

    satellite.set_data([x], [y])

    velocity_arrow.set_offsets([[x, y]])
    velocity_arrow.set_UVC(vx * 300, vy * 300)

    # Update acceleration arrow
    acceleration_arrow.set_offsets([[x, y]])

    arrow_scale = 500
    acceleration_arrow.set_UVC(
        ax_acc * arrow_scale,
        ay_acc * arrow_scale
    )

    trail.set_data(trail_x, trail_y)

    telemetry.set_text(
        f"SATELLITE TELEMETRY\n"
        f"────────────────────\n"
        f"Elapsed time: {elapsed_seconds / 60:.1f} min\n"
        f"X position: {x:.2f} km\n"
        f"Y position: {y:.2f} km\n"
        f"Altitude: {altitude:.2f} km\n"
        f"Orbital speed: {orbital_speed / 1000:.2f} km/s\n"
        f"Orbital period: {orbital_period / 60:.2f} min\n"
        f"Acceleration: {acceleration_magnitude:.2f} m/s²"
    )

    return satellite, trail, telemetry, velocity_arrow, acceleration_arrow

ax.legend(loc="lower left")

animation = FuncAnimation(
    fig, update, interval=100, blit=False,
    cache_frame_data=False
)

plt.tight_layout()
plt.show()
