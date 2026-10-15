
import math

# Orbital parameters
EARTH_MU = 3.986004418e14  # m^3/s^2
ORBIT_RADIUS = 7_000_000   # meters
TIME_SECONDS = 600         # 10 minutes

# Calculate orbital motion
angular_velocity = math.sqrt(EARTH_MU / ORBIT_RADIUS**3)
angle = angular_velocity * TIME_SECONDS

# Calculate satellite position
x = ORBIT_RADIUS * math.cos(angle)
y = ORBIT_RADIUS * math.sin(angle)

# Calculate distance from Earth's center
calculated_radius = math.sqrt(x**2 + y**2)

# Automated validation tests
assert math.isclose(
    calculated_radius, ORBIT_RADIUS, rel_tol=1e-12
), "FAIL: Satellite is not on the expected orbit"

assert math.isclose(
    x, 5_586_090, rel_tol=0.001
), "FAIL: X position differs from the expected value"

assert math.isclose(
    y, 4_218_480, rel_tol=0.001
), "FAIL: Y position differs from the expected value"

print("=== SATELLITE POSITION TEST REPORT ===")
print(f"Time: {TIME_SECONDS / 60:.1f} minutes")
print(f"X position: {x / 1000:.2f} km")
print(f"Y position: {y / 1000:.2f} km")
print(f"Calculated orbital radius: {calculated_radius / 1000:.2f} km")
print("\nAll satellite position tests passed!")
