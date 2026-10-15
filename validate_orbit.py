
import math

# Physical and orbital parameters
earth_mu = 3.986004418e14  # m^3/s^2
earth_radius = 6371         # km
orbit_radius = 7000         # km

# Calculate orbital properties
radius_m = orbit_radius * 1000
orbital_speed = math.sqrt(earth_mu / radius_m)
orbital_period = 2 * math.pi * math.sqrt(
    radius_m**3 / earth_mu
)
acceleration = earth_mu / radius_m**2

# Position after 10 minutes
time_seconds = 600
angular_velocity = math.sqrt(earth_mu / radius_m**3)
angle = angular_velocity * time_seconds

x = orbit_radius * math.cos(angle)
y = orbit_radius * math.sin(angle)

calculated_radius = math.sqrt(x**2 + y**2)

# Validation tests
print("=== ORBIT VALIDATION REPORT ===")

print(f"Orbital radius: {orbit_radius:.2f} km")
print(f"Calculated radius: {calculated_radius:.2f} km")
print(f"Orbital speed: {orbital_speed / 1000:.3f} km/s")
print(f"Orbital period: {orbital_period / 60:.2f} minutes")
print(f"Acceleration: {acceleration:.3f} m/s^2")
print(f"Position after 10 min: X={x:.2f} km, Y={y:.2f} km")

print("\n=== TEST RESULTS ===")

assert math.isclose(
    calculated_radius, orbit_radius, abs_tol=1e-6
), "FAIL: Orbital radius mismatch"

assert 7.5 < orbital_speed / 1000 < 7.6, (
    "FAIL: Orbital speed outside expected range"
)

assert 97 < orbital_period / 60 < 98, (
    "FAIL: Orbital period outside expected range"
)

assert 8.0 < acceleration < 8.3, (
    "FAIL: Acceleration outside expected range"
)

print("PASS: Orbital radius")
print("PASS: Orbital speed")
print("PASS: Orbital period")
print("PASS: Centripetal acceleration")
print("\nAll validation tests passed!")
