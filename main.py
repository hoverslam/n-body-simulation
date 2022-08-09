# Libraries
import numpy as np

# Custom modules
import sys
sys.path.append("modules")
from vector import Vector3
from simulation import BruteForce
from celestial import Body


def inner_planets() -> list[Body]:
     bodies =  [Body(Vector3(), Vector3(),
                     1.98847e30, 6.957e8, color="yellow"),
                Body(Vector3(-2.565786669256473e10, 1.459776345868732e11, -1.548952074754238e7),
                     Vector3(-2.984330713107311e4, -5.272844521387671e3, 9.256858421500258e-1),
                     5.97219e24, 6.371e6, name="Earth", color="cornflowerblue"),
                Body(Vector3(1.629806212726895e11, 1.449170333840721e11, -9.972368219362050e8),
                     Vector3(-1.511758798465740e4, 2.024466077262084e4, 7.950950455491554e2),
                     6.41693e23, 3.390e6, name="Mars", color="orangered"),
                Body(Vector3(-8.238126961879626e10, 7.005400357447663e10, 5.684910758346014e9),
                     Vector3(-2.263904820538244e4, -2.701728799104976e4, 9.352522537487609e2),
                     4.86732e24, 6.051e6, name="Venus", color="navajowhite"),
                Body(Vector3(-4.726172010176350e10, -4.671443491995941e10, 4.087355549094304e9),
                     Vector3(2.476489737911525e4, -3.197373466563876e4, -4.885743869363329e3),
                     3.30104e23, 2.439e6, name="Mercury", color="gray"),
                Body(Vector3(-3.250173761375654e11, -2.203419016964185e11, 5.291759744142130e10),
                     Vector3(9.165639992762751e3, -1.610304458359491e4, -2.199191038589312e3),
                     9.38350e20, 4.697e5, name="Ceres"),
                Body(Vector3(-3.453585004297552e11, 2.151464493938778e10, 1.484082838948810e10),
                     Vector3(-3.944259837966826e3, -1.692743937506040e4, 1.202778577972903e4),
                     2.11000e20, 2.700e5, name="Pallas"),
                Body(Vector3(2.896729116971705e11, -1.781911555651397e11, -2.990483159764896e10),
                     Vector3(1.170943386515238e4, 1.610135702679393e4, -1.907600473100395e3),
                     2.59000e20, 2.627e5, name="Vesta")]
     
     return bodies


def random_planets(n: int, overall_mass: float) -> list[Body]:
     AU = 149_597_870_700
     rng = np.random.default_rng()
     
     bodies = []
     for i in range(n):
          position = Vector3(
               0.5 * rng.standard_normal() * AU,
               0.5 * rng.standard_normal() * AU,
               0.5 * rng.standard_normal() * AU
          )
          velocity = Vector3(
               0.0 * rng.standard_normal() * AU,
               0.0 * rng.standard_normal() * AU,
               0.0 * rng.standard_normal() * AU
          )
          mass = abs(rng.normal()) * overall_mass / n
          radius = rng.normal(1e7)
          bodies.append(Body(position, velocity, mass, radius))
          
     return bodies


if __name__ == "__main__":
     # Simulate inner planets of our solar System: Mercury, Venus, Earth, and Mars
     bodies = inner_planets()
     
     # Uncomment to simulate random planets
     """bodies = random_planets(10, 1e30)"""

     # Run simulation
     sim = BruteForce(bodies, 2, True)
     sim.run()