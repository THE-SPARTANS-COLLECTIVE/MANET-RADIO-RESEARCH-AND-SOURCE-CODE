class IntegrityMonitor:
    """IDS to detect Blackhole attacks."""
    def __init__(self):
        self.trust_scores = {} # {node_id: score}

    def audit_node(self, node_id, packets_sent, packets_forwarded):
        """Analyzes forwarding behavior."""
        if packets_sent == 0: return 1.0
        ratio = packets_forwarded / packets_sent
        self.trust_scores[node_id] = ratio
        return "THREAT" if ratio < 0.4 else "SECURE"
