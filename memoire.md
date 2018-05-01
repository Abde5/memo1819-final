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

**Definition:** A unit disk graph is a $c$-strip graph if it has a unit disk representation in which all centers of the unit disks lie between two parallel lines at distance $c$. [7]

## Main UD problems:

**Channel Assignment Problem**: (To explain)

**UD graph recognition**: "Is graph $G$ a UD?" or "Can graph $G$ be represented with disk intersections on a plane?" [6]

**Chomatic number**: What is the chromatic number of UDGs (lower/upper bound)? [6]

**Clique number**: Computing clique number of UDGs. [6]

**Independence number**: Computing or approximating the independence number of UDGs. [6]

**Smallest independent set**: finding or approximating a smallest dominating set. [6]

**Bisection on UID**: https://community.dur.ac.uk/george.mertzios/papers/Conf/Conf_Bisection-Unit-Disk.pdf

**Clique with UD "percer"**: Transversal number, cmb de points besoin pour percer une clique d'un UD. TRANSVERSAL NUMBER. Stabbing (check).

**Clique dans ro-disk graph$**





****


## Unit Disk Graphs reductions
### Maximum Independent Set (MIS)
$MIS$ is a problem that is classed $NP$-hard and $NC$-complete (Nick's Class) -> continue checking at home


# References

- [1] (Data Structures & Algorithms[Springer page 253] -> APSP: https://link.springer.com/content/pdf/10.1007%2F978-3-319-62127-2.pdf)
- [2] (Unit Disk Graphs: https://link.springer.com/content/pdf/10.1007%2Fb95598.pdf)
- [3] (Unit disk graphs definition): https://ac.els-cdn.com/S0167506008710471/1-s2.0-S0167506008710471-main.pdf?_tid=b07e3020-4087-40c7-9865-319328cd3cc5&acdnat=1524491200_ed8b55d390abddcce09c1db8f9139c6e
- [4] (Algorithm for maximum clique): https://arxiv.org/abs/1712.05010
- [5] (On coloring unit disk graphs): https://link.springer.com/content/pdf/10.1007%2FPL00009196.pdf
- [6] (The number of disk graphs): http://www.math.rug.nl/~tobias/Papers/countingDGsFinal.pdf
- [7] (c-Strip graphs): https://www.sciencedirect.com/science/article/pii/S0166218X15000207
- [8] (graphclasses): https://graphclasses.org
