import time
import random

class MACLayer:
    """Distributed Coordination Function (DCF) using CSMA/CA."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.cw_min = 15      # Minimum Contention Window
        self.cw_max = 1023    # Maximum Contention Window
        self.cw_current = self.cw_min
        self.sifs = 0.000016  # Short Inter-Frame Space (16us for 802.11ac)
        self.difs = 0.000034  # DCF Inter-Frame Space
        self.slot_time = 0.000009
        
    def carrier_sense(self, medium_busy):
        """Implements Physical and Virtual Carrier Sensing."""
        if medium_busy:
            # Increment Backoff (Binary Exponential Backoff)
            self.cw_current = min(self.cw_max, (self.cw_current + 1) * 2 - 1)
            backoff_slots = random.randint(0, self.cw_current)
            return False, backoff_slots * self.slot_time
        
        self.cw_current = self.cw_min # Reset on success
        return True, self.difs

    def solve_hidden_terminal(self):
        """Generates Virtual Carrier Sensing (NAV) values."""
        # Returns duration for Request-to-Send (RTS) handshake
        pass
