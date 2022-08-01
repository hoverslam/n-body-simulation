from vector import Vector3
from simulation import BruteForce
from celestial import Body

if __name__ == "__main__":
     bodies = [Body(Vector3(), Vector3(),
                    1.98847e30, 6.957e8, "Sun", "yellow"),
               Body(Vector3(-2.565786669256473e10, 1.459776345868732e11, -1.548952074754238e7),
                    Vector3(-2.984330713107311e4, -5.272844521387671e3, 9.256858421500258e-1),
                    5.97219e24, 6.371e6, "Earth", "cornflowerblue"),
               Body(Vector3(1.629806212726895e11, 1.449170333840721e11, -9.972368219362050e8),
                    Vector3(-1.511758798465740e4, 2.024466077262084e4, 7.950950455491554e2),
                    6.41693e23, 3.390e6, "Mars", "orangered"),
               Body(Vector3(-8.238126961879626e10, 7.005400357447663e10, 5.684910758346014e9),
                    Vector3(-2.263904820538244e4, -2.701728799104976e4, 9.352522537487609e2),
                    4.86732e24, 6.051e6, "Venus", "navajowhite"),
               Body(Vector3(-4.726172010176350e10, -4.671443491995941e10, 4.087355549094304e9),
                    Vector3(2.476489737911525e4, -3.197373466563876e4, -4.885743869363329e3),
                    3.30104e23, 2.439e6, "Mercury", "gray")]

     sim = BruteForce(bodies, 2)
     sim.run()