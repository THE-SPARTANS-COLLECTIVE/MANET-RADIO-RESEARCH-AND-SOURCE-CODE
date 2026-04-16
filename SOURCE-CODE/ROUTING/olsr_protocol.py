class OLSRProtocol:
    """Proactive Mesh Logic using Multi-Point Relays (MPR)."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.mpr_set = set()
        self.topology_map = {}

    def calculate_mpr(self, neighbors_1_hop, neighbors_2_hop):
        """Heuristic for MPR selection to minimize broadcast flooding."""
        selected_mpr = set()
        # Logic: Find 1-hop nodes that provide max coverage of 2-hop nodes
        for n2 in neighbors_2_hop:
            # Simplified greedy selection
            for n1 in neighbors_1_hop:
                if n2 in n1.visible_nodes:
                    selected_mpr.add(n1.id)
                    break
        self.mpr_set = selected_mpr
        return list(self.mpr_set)
