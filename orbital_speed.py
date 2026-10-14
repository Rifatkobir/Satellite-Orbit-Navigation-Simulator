
import math

print("=== SATELLITE ORBITAL SPEED ===")

# Simplified illustrative model
orbit_radius = 7_000_000  # meters from Earth's center
earth_mu = 3.986004418e14  # Earth's gravitational parameter, m^3/s^2

# Circular orbital speed
orbital_speed = math.sqrt(earth_mu / orbit_radius)

# Circular orbital period
orbital_period = (
    2 * math.pi
    * math.sqrt(orbit_radius**3 / earth_mu)
)

print(f"Orbital radius: {orbit_radius / 1000:.0f} km")
print(f"Orbital speed: {orbital_speed / 1000:.2f} km/s")
print(f"Orbital period: {orbital_period / 60:.2f} minutes")
