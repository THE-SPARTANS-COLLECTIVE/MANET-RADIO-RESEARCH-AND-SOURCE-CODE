# MANET Radio Research & Source Code
### High-Fidelity Tactical Wireless Mesh Stack for Contested Electronic Environments

---

## 1. STRATEGIC MISSION & RESEARCH OVERVIEW
The **MANET Radio Research Framework** is a multi-disciplinary initiative designed to architect command-and-control (C2) resilience in denied, degraded, and disrupted environments (D3E). Traditional centralized communication architectures represent single points of failure; this framework provides a sovereign, self-healing alternative through decentralized, autonomous mesh topology.

### 1.1 Stochastic Waveform Modeling & Propagation Determinants
The framework initiates at the Physical Layer (PHY), treating the wireless medium as a non-deterministic, time-varying environment. Our research transitions beyond simple Free Space Path Loss (FSPL) to account for atmospheric and topographical variables that define tactical operational theaters.

#### 1.1.1 Log-Distance Path Loss and Shadowing
In contested environments, signal decay is non-linear. We implement a rigorous path loss model where the path loss exponent ($n$) is dynamically adjusted based on the environment (Urban: $n=3.5$ to $4.5$, Rural: $n=2.0$). 

$$PL(d) = PL(d_0) + 10n \log_{10}\left(\frac{d}{d_0}\right) + X_{\sigma}$$

The variable $X_{\sigma}$ represents **Log-Normal Shadowing**, a Gaussian distribution used to simulate signal obstruction by massive objects (buildings, terrain), ensuring that the "Rocket Physics" of signal obstruction are accurately reflected in the source code's `physical_layer.py`.

#### 1.1.2 Multipath Fading: Rayleigh vs. Rician
To support high-reliability communication in Non-Line-of-Sight (NLOS) scenarios, the research investigates the distribution of received signal power.
* **Rayleigh Fading:** Employed when the radio environment lacks a dominant line-of-sight component, resulting in a signal envelope characterized by the probability density function:
    $$p(r) = \frac{r}{\sigma^2} e^{-\frac{r^2}{2\sigma^2}}$$
* **Rician Fading:** Utilized in drone-to-ground or open-field tactical links where a primary signal component exists, modeled using the $K$-factor to determine the ratio of the dominant path to the scattered paths.

---

## 2. MAC LAYER ARCHITECTURE: TEMPORAL COORDINATION

### 2.1 DCF State Machine & Inter-Frame Spacing
The Medium Access Control (MAC) layer governs the "Listen Before Talk" (LBT) mechanism. Research in `02_MAC_State_Machine_Logic.md` details the exact microsecond timings required for synchronization across a distributed mesh:
* **SIFS (Short Inter-Frame Space):** Prioritizes high-priority control frames (ACK, CTS).
* **DIFS (DCF Inter-Frame Space):** The mandatory delay for standard data frames.
* **NAV (Network Allocation Vector):** A virtual carrier-sensing mechanism that reserves the airwaves, preventing the **Hidden Terminal Problem**.

### 2.2 Binary Exponential Backoff (BEB) Markov Chain
When a collision occurs, the system utilizes a Markov Chain analysis to determine the Contention Window ($CW$).
1.  On first failure: $CW = 15$.
2.  On subsequent failure: $CW = 2^{k}-1$ (up to $1023$).
This ensures that as node density increases, the probability of simultaneous re-transmission decreases exponentially, maintaining network stability during "high-intensity traffic" events.

---

## 3. NETWORK LAYER: TOPOLOGY & GRAPH THEORY

### 3.1 Proactive vs. Reactive Paradigms
The system supports dual-mode routing to adapt to mission-specific requirements.
* **Reactive (AODV):** Employs the **Reverse Path Setup** method. Route Request (RREQ) packets create temporary "breadbox" paths in node caches, minimizing idle control traffic.
* **Proactive (OLSR):** Utilizes **Multi-Point Relays (MPR)**. The research identifies the set-cover problem inherent in MPR selection, providing a greedy algorithm that ensures 100% 2-hop coverage while reducing broadcast overhead by up to 70%.

### 3.2 Predictive Link Expiration Time (LET)
By integrating the `utils/gps_sim.py` kinematics engine, the routing logic calculates the **Link Expiration Time**. If two nodes are moving at specific velocities and headings, the system predicts the exact timestamp when the distance $d$ will exceed the radio range $R$:

$$LET = \frac{-(ab + cd) + \sqrt{(a^2+c^2)r^2 - (ad-bc)^2}}{a^2 + c^2}$$

This allows for **Proactive Handovers**, where the network reroutes traffic *before* the physical link breaks, a necessity for tactical vehicle-to-vehicle (V2V) communications.

---

## 4. ELECTRONIC WARFARE & SYSTEM SURVIVABILITY

### 4.1 Anti-Jamming and Spectrum Agility
The research in `04_Electronic_Warfare_&_Resilience.md` addresses the impact of intentional narrow-band and wide-band jamming.
* **Processing Gain ($G_p$):** Our signal processing research implements pseudo-random frequency hopping logic to maximize the ratio between information bandwidth and spread bandwidth.
* **Automatic Power Control (APC):** By calculating path loss in real-time, nodes reduce their transmission power to the absolute minimum required to hit the next hop, shrinking the network's **LPI/LPD (Low Probability of Intercept/Detection)** footprint.

### 4.2 Security: Cryptographic Integrity & Trust
* **Asymmetric Identity:** Utilizing Elliptic Curve Cryptography (ECC) for identity verification without the overhead of heavy RSA keys. Every packet header is hashed with HMAC-SHA256 to prevent "packet spoofing."
* **Behavioral Auditing:** The `integrity_check.py` module tracks the **Packet Delivery Ratio (PDR)** of neighboring nodes. If a neighbor accepts packets but fails to forward them (the "Blackhole" attack profile), the system initiates a "Topology Poisoning Defense," blacklisting that node across the entire collective mesh.

---

## 5. REPOSITORY MODULARITY

### [RESEARCH/](./RESEARCH)
The academic foundation. Each module follows a rigorous scientific derivation format.
* **01_PHY_Propagation_Determinants.md**: Exhaustive math on the Log-Distance model, Friis transmission equations, and thermal noise floors.
* **02_MAC_State_Machine_Logic.md**: Logic for the Distributed Coordination Function (DCF). Covers SIFS, DIFS, and the BEB Markov Chain.
* **03_Algorithmic_Routing_Graph_Theory.md**: Detailed analysis of pathfinding and loop-prevention mechanisms.
* **04_Electronic_Warfare_&_Resilience.md**: Theoretical defense against Blackhole, Sybil, and Jamming attacks.

### [SOURCE-CODE/](./SOURCE-CODE)
The production-ready Python implementation.
* **CORE/**: Physical and MAC layer implementations (The physics and timing engine).
* **ROUTING/**: Logic for AODV (Reactive) and OLSR (Proactive) mesh protocols.
* **SECURITY/**: HMAC-based integrity monitoring and ECC utilities.
* **UTILS/**: Kinematic movement simulators, GPS coordinate tracking, and telemetry logging.
* **main.py**: The central ignition system for node simulation and stack initialization.

---

## 6. PERFORMANCE METRICS
The framework measures success through three high-fidelity KPIs:
1.  **Packet Delivery Ratio (PDR):** Percentage of packets reaching destination successfully.
2.  **End-to-End Latency ($\tau$):** Cumulative delay across $N$ hops, accounting for processing and propagation.
3.  **Control Overhead:** Ratio of management traffic to actual payload, optimized via MPR research.

---
**Institutional Author:** THE SPARTANS COLLECTIVE™

**Subject:** Advanced Wireless Communications and Tactical Networking Research (MANET)

**License**: GNU GPL v.3.0
