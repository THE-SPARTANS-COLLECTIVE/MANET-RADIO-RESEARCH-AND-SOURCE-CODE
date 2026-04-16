# MANET Radio Research and Source Code Documentation
### Technical Analysis of Decentralized Wireless Mesh Architectures

---

## 1. RESEARCH SUMMARY
The research contained in this repository focuses on the optimization of Mobile Ad hoc Networks (MANETs) in high-mobility, spectrum-congested environments. By analyzing the intersection of stochastic radio propagation and algorithmic graph theory, this body of work establishes a framework for resilient, autonomous communication without fixed infrastructure. 

### 1.1 Signal Propagation Determinants
The core research (located in `01_PHY_Propagation_Determinants.md`) derives the mathematical foundations for signal integrity. We utilize the Log-Distance Path Loss model to predict signal decay:
$$PL = PL(d_0) + 10n \log_{10} \left( \frac{d}{d_0} \right) + X_\sigma$$
This allows the radio stack to calculate the Signal-to-Interference-plus-Noise Ratio (SINR) dynamically. Research further investigates Rayleigh and Rician fading to account for multipath interference in non-line-of-sight (NLOS) conditions.

### 1.2 MAC Layer and Temporal Coordination
The research in `02_MAC_State_Machine_Logic.md` addresses the Distributed Coordination Function (DCF). This involves the microsecond-level timing of SIFS (Short Inter-Frame Space) and DIFS (DCF Inter-Frame Space) to manage medium access. The study focuses on Binary Exponential Backoff (BEB) algorithms to mitigate the "Hidden Terminal Problem" and prevent packet collisions in dense node clusters.

### 1.3 Routing and Topology Optimization
Our routing research (`03_Algorithmic_Routing_Graph_Theory.md`) evaluates the trade-offs between reactive protocols (AODV) and proactive protocols (OLSR).
* **AODV:** Focuses on reducing control overhead by initiating route discovery only when a path is required.
* **OLSR:** Utilizes Multi-Point Relays (MPRs) to minimize broadcast flooding. The research provides a greedy heuristic for MPR selection, significantly reducing the "Forwarding Set" required to cover 2-hop neighbors.

---

## 2. TECHNOLOGICAL CAPABILITIES
The source code provided in the `SOURCE-CODE/` directory implements the findings from the research into a functional, modular radio stack.

### 2.1 Adaptive Link Integrity
The radio employs real-time Link Expiration Time (LET) prediction. By processing velocity and heading data from the `utils/gps_sim.py` module, the radio anticipates link failure before it occurs, triggering proactive route handovers. This ensures continuous connectivity for nodes moving at tactical speeds.

### 2.2 Spectrum Awareness and Power Control
Leveraging the `core/physical_layer.py` logic, the system monitors the noise floor and interference levels. This allows the radio to:
* **Minimize Detectability:** Adjust transmission power to the minimum level required for successful reception by the next hop.
* **Maximize Throughput:** Dynamically switch modulation schemes based on the Shannon-Hartley capacity limit:
  $$C = B \log_2 (1 + \text{SINR})$$

### 2.3 Security and Trust-Based Networking
The `security/` modules provide a two-tier defense mechanism:
* **Cryptographic Integrity:** Every packet is signed using HMAC-SHA256 via `security/ecc_encryptor.py`, ensuring routing tables cannot be poisoned by unauthorized nodes.
* **Behavioral Auditing:** The `security/integrity_check.py` module monitors neighbor behavior. If a node accepts packets but fails to forward them (a Blackhole attack), its "Trust Score" is downgraded, and the network automatically routes around the threat.

### 2.4 Telemetry and Post-Mission Analysis
The system includes a high-fidelity logging utility (`utils/logger.py`) that captures every state change, packet drop, and SINR fluctuation. This data is critical for refining propagation models and evaluating network performance metrics such as Packet Delivery Ratio (PDR) and End-to-End Latency.

---

**Institutional Author:** THE SPARTANS COLLECTIVE™

**Subject:** Advanced Wireless Communications and Tactical Networking Research

**License**: GNU GPL v.3.0
