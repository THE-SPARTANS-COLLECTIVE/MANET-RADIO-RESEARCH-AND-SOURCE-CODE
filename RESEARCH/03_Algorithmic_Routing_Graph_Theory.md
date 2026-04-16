# 3. Network Layer: Graph Theory & Reactive Pathfinding

## 3.1 Graph Representation
A MANET is modeled as a time-varying directed graph $G_t = (V, E_t)$, where $V$ is the set of nodes and $E_t$ is the set of active bi-directional links at time $t$. A link $(u, v) \in E_t$ exists if and only if $SINR_{u \to v} \ge \gamma_{threshold}$.

## 3.2 Optimized Link State Routing (OLSR) & MPRs
The selection of **Multi-Point Relays (MPRs)** is an NP-hard problem. We use a heuristic where node $u$ selects a minimum subset of 1-hop neighbors $N^1(u)$ such that all 2-hop neighbors $N^2(u)$ are reachable.

## 3.3 Route Stability Metric
We introduce the **Link Expiration Time (LET)** prediction. Given two nodes at $(x_1, y_1)$ and $(x_2, y_2)$ with velocities $v_1, v_2$ and headings $\theta_1, \theta_2$, the LET is:

$$LET = \frac{-(ab + cd) + \sqrt{(a^2+c^2)r^2 - (ad-bc)^2}}{a^2 + c^2}$$

* $a = v_1 \cos \theta_1 - v_2 \cos \theta_2$
* $b = x_1 - x_2$
* $c = v_1 \sin \theta_1 - v_2 \sin \theta_2$
* $d = y_1 - y_2$
