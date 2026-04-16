# 1. Physical Layer: Electromagnetic Wave Propagation & Stochastic Fading

## 1.1 Large-Scale Path Loss Models
The fundamental link budget for a MANET node is governed by the **Log-Normal Shadowing Model**. We define the received power $P_r(d)$ at distance $d$ as:

$$P_r(d)[dBm] = P_t[dBm] + G_t[dBi] + G_r[dBi] - PL(d_0) - 10n \log_{10}\left(\frac{d}{d_0}\right) + X_\sigma$$

Where:
* $n$: Path loss exponent ($n=2$ for vacuum, $n=4$ for obstructed urban).
* $X_\sigma$: Zero-mean Gaussian random variable with standard deviation $\sigma$ (Shadowing).

## 1.2 Small-Scale Fading Dynamics
In high-mobility MANETs, the coherence time ($T_c$) of the channel must be shorter than the packet duration. The Doppler spread ($B_d$) is derived from the node velocity $v$ and carrier frequency $f_c$:

$$B_d = \frac{v \cdot f_c}{c}$$

The channel is considered **Fast Fading** if $T_s > T_c$, where $T_s$ is the symbol period. We utilize the **Jakes' Spectrum model** to simulate the Rayleigh fading process in a Rayleigh-distributed multi-path environment.

## 1.3 Signal-to-Interference-plus-Noise Ratio (SINR)
The capacity of a single radio link is bounded by the Shannon-Hartley Theorem, modified for interference:

$$C = B \log_2 \left( 1 + \frac{S}{N + \sum_{i=1}^{k} I_i} \right)$$

Where $I_i$ represents the co-channel interference from the $k^{th}$ neighboring node.
