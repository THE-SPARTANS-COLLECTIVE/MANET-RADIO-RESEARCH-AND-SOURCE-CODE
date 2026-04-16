# 2. Medium Access Control (MAC) & Distributed Coordination

## 2.1 The Hidden Terminal Problem & RTS/CTS
To prevent collisions in a decentralized mesh, we implement a four-way handshake. The probability of a successful handshake depends on the **Vulnerable Period** ($V_p$):

1. **RTS (Request to Send):** Duration $T_{RTS}$.
2. **CTS (Clear to Send):** Duration $T_{CTS}$.
3. **DATA:** Duration $T_{DATA}$.
4. **ACK:** Duration $T_{ACK}$.

## 2.2 Binary Exponential Backoff (BEB) Analysis
The contention window ($CW$) is a discrete-time Markov chain. The probability $\tau$ that a node transmits in a randomly chosen slot is:

$$\tau = \frac{2(1-2p)}{(1-2p)(W+1) + pW(1-(2p)^m)}$$

Where $W$ is the minimum contention window and $p$ is the conditional collision probability.

## 2.3 Time Division Multiple Access (TDMA) Synchronization
For deterministic latency, we research **Global Positioning System (GPS)** disciplined clock synchronization, allowing for Guard Bands ($G$) to account for clock drift ($\Delta t$):

$$G \ge 2 \cdot \Delta t + \frac{d_{max}}{c}$$
