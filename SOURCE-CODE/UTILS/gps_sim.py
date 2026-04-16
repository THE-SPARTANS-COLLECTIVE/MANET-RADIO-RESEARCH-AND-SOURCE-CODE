import math

class GPSUnit:
    """Simulates node kinematics: Velocity, Heading, and Position."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, velocity_mps, heading_deg, dt=1.0):
        """Update coordinates based on vector movement."""
        rad = math.radians(heading_deg)
        self.x += velocity_mps * math.cos(rad) * dt
        self.y += velocity_mps * math.sin(rad) * dt
        return self.x, self.y

    def get_distance(self, other_gps):
        return math.sqrt((self.x - other_gps.x)**2 + (self.y - other_gps.y)**2)
