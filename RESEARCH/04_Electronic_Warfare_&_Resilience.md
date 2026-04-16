# 4. Survivability: Anti-Jamming & Cryptographic Integrity

## 4.1 Frequency Hopping Spread Spectrum (FHSS)
To mitigate narrow-band jamming, the system utilizes a pseudo-random hop sequence $H_s$. The processing gain ($G_p$) is defined by:

$$G_p = 10 \log_{10} \left( \frac{B_{ss}}{B_i} \right)$$

Where $B_{ss}$ is the spread-spectrum bandwidth and $B_i$ is the information bandwidth.

## 4.2 Byzantine Fault Tolerance in MANETs
We analyze "Selfish Node" behavior where nodes refuse to forward packets to save power. We implement a **Generous Tit-for-Tat** strategy within the routing logic to enforce cooperation.

## 4.3 Elliptic Curve Cryptography (ECC) for Identity
Each node identity is verified using **Ed25519** signatures. The computational overhead is minimized for embedded radio processors while maintaining a 128-bit security level.
