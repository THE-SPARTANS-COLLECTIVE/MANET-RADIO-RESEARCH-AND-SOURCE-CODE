import time

class AODVRouteManager:
    """Ad-hoc On-Demand Distance Vector logic."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.sequence_number = 0
        self.routing_table = {}  # {dest: (next_hop, hops, seq, expiry)}
        self.rreq_id = 0

    def discover_route(self, destination):
        """Initiates a Route Request (RREQ)."""
        self.rreq_id += 1
        packet = {
            "type": "RREQ",
            "source": self.node_id,
            "dest": destination,
            "src_seq": self.sequence_number,
            "rreq_id": self.rreq_id
        }
        return packet

    def update_table(self, dest, next_hop, hops, seq):
        """Maintains the routing graph based on incoming RREPs."""
        if dest not in self.routing_table or seq > self.routing_table[dest][2]:
            self.routing_table[dest] = (next_hop, hops, seq, time.time() + 10)
            return True
        return False
