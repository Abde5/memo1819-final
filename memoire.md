# Intersection graphs

## Kind of intersection graphs
 - Intersection graph
 - Arrangement graph
 - Unit disk graphs

# Disk Graphs
**Definition:** Disk graphs are graphs that represent a set of disks on a plane that intersect. $D$ being the set of disks, the graph $G$ is constructed by mapping every disk to a node on the graph and 2 nodes are connected if the 2 corresponding disks intersect.

**Definition:** Unit disk graph is a disk graph such that $\exists uv \in E(G)$ iff $d(u,v) \leq 1$.

**Definition:** Coin (or penny) graph is a disk graph such that $\exists uv \in E(G)$ iff $d(u,v) = 1$.

**Definition:** Unit disk graph is a disk graph such that $\exists uv \in E(G)$ iff $d(u,v) \leq \frac{\phi(u)}{2} + \frac{\phi(v)}{2}$.

**Lemma:** $G$ planar $\to$ $G$ is $CG$.

## Unit Disk Graphs reductions
### Maximum Independent Set (MIS)
$MIS$ is a problem that is classed $NP$-hard and $NC$-complete (Nick's Class) -> continue checking at home


# References

- (Data Structures & Algorithms[Springer page 253] -> APSP: https://link.springer.com/content/pdf/10.1007%2F978-3-319-62127-2.pdf)
- (Unit Disk Graphs: https://link.springer.com/content/pdf/10.1007%2Fb95598.pdf)
- Unit disk graphs definition: https://ac.els-cdn.com/S0167506008710471/1-s2.0-S0167506008710471-main.pdf?_tid=b07e3020-4087-40c7-9865-319328cd3cc5&acdnat=1524491200_ed8b55d390abddcce09c1db8f9139c6e
- (Algorithm for maximum clique): https://arxiv.org/abs/1712.05010
