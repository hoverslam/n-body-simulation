import matplotlib.pyplot as plt
from celestial import Body
from vector import Vector3
import math

class Simulation:
    """This is the parent class for the different simulations. The specifc calculation is implemented in the subclass.
    """
    
    def __init__(self, bodies: list[Body], size: int, show_names: bool) -> None:
        """Initialize class.

        Args:
            bodies (list[Body]): A list of celestial objects.
            size (int): Size of the canvas in each directions in astronomical units (AU).
            show_names (bool): Display name of body next to it.
        """
        self.bodies = bodies
        self.size = size
        self.show_names = show_names

        # Create canvas
        plt.style.use("dark_background")
        self.fig = plt.figure(dpi=200)
        self.fig.canvas.set_window_title("N-body simulation")
        self.fig.canvas.mpl_connect("close_event", exit)
        self.ax = self.fig.add_subplot(projection="3d")
        
        # Remove panes and lines
        self.ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        self.ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        self.ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))   
        self.ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        self.ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        self.ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        
    def update(self) -> None:
        """Calculate the forces exerted on each body and move them accordingly. The technique used is implemented by the subclass.

        Raises:
            NotImplementedError: Has to be implemented by the subclass.
        """
        raise NotImplementedError 
        
    def show(self) -> None:
        """Plot the position of each body on the canvas.
        """
        self.set_limits()
        self.remove_ticks()
        for b in self.bodies:
            marker_size = math.sqrt(b.radius / 6.957e8) * 2    # make the marker a seeable size
            self.ax.scatter(b.position[0], b.position[1], b.position[2], s=marker_size, c=b.color)
            if self.show_names and b.name != "":
                self.ax.text(b.position[0], b.position[1], b.position[2], b.name, color=b.color, fontsize=4)
        plt.pause(0.0001)
        self.ax.clear()
            
    def run(self) -> None:
        """Run the simulation.
        """
        while True:
            self.update()
            self.show()
            
    def remove_ticks(self) -> None:
        """Remove ticks on all axis to get an empty "universe".
        """
        self.ax.set_xticks([]) 
        self.ax.set_yticks([]) 
        self.ax.set_zticks([])
        
    def set_limits(self) -> None:
        """Set the limit of the axis given by the size parameter.
        """
        limit = self.size * 149_597_870_700    # convert AU to meter
        self.ax.set_xlim((-limit, limit))
        self.ax.set_ylim((-limit, limit))
        self.ax.set_zlim((-limit, limit))
        
    def merge_bodies(self, b1: Body, b2: Body) -> None:
        """Merge to bodies into a new one. This works better if the leap-frog timestep dt is 
        relatively small (e.g. 10000).  

        Args:
            b1 (Body): A celestial object.
            b2 (Body): A celestial object.
        """
        if b2.mass > b1.mass:
            b1, b2 = b2, b1    # Delete smaller and update bigger body
        b1.mass += b2.mass
        b1.velocity += b2.velocity
        b1.radius += math.sqrt(b2.radius)    # A very crude/unscientific new radius
        self.remove_body(b2)
        
    def remove_body(self, b: Body) -> None:
        """Remove a body from the list.

        Args:
            b (Body): A celestial object.
        """
        new_list = []        
        for body in self.bodies:
            if body is not b:
                new_list.append(body)
        self.bodies = new_list
                
        
class BruteForce(Simulation):
    """This class implements the direct brute-force method. The force acting on a single body is calculated by looping over all other bodies. 
    It is simple and accurate but has a complexity of O(n^2). 
    """
    
    def __init__(self, bodies: list[Body], size: int, show_names: bool = False) -> None:
        """Initialize class.

        Args:
            bodies (list[Body]): A list of celestial objects.
            size (int): Size of the canvas in each directions in astronomical units (AU).
            show_names (bool): Display name of body next to it. Defaults to False.
        """
        super().__init__(bodies, size, show_names)
        
    def update(self) -> None:
        """Calculate the forces exerted on each body and move them accordingly.
        """
        forces = []
        for i, first in enumerate(self.bodies):
            forces.append(Vector3())
            for second in self.bodies:
                if first is not second:
                    # Merge bodies if distance is smaller than the sum of their radii
                    if first.distance_to(second) < first.radius + second.radius:                        
                        self.merge_bodies(first, second)
                        return    # stop this iteration of force updates since a new body was created
                    # Add force to the first body
                    forces[i] += first.gravitational_force(second)   
  
        for i, b in enumerate(self.bodies):        
            b.move(forces[i], 5000)    # 20000 is a good tradeoff between accuracy and speed