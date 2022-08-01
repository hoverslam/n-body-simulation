import matplotlib.pyplot as plt
from celestial import Body
from vector import Vector3


class Simulation:
    """This is the parent class for the different simulations. The specifc calculation is implemented in the subclass.
    """
    
    def __init__(self, bodies: list[Body], size: int, duration: float) -> None:
        """Initialize class.

        Args:
            bodies (list[Body]): A list of celestial objects.
            size (int): Size of the canvas in each directions in astronomical units (AU).
            duration (float): Duration of the simulation.
        """
        self.bodies = bodies
        self.size = size
        self.duration = duration
        self.time = 0

        # Create canvas
        plt.style.use("dark_background")
        self.fig = plt.figure(dpi=200)
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
            marker_size = b.radius / 6.957e8 * 1e2 / self.size    # make the marker a seeable size
            self.ax.scatter(b.position[0], b.position[1], b.position[2], s=marker_size, c=b.color)
        plt.pause(0.0001)
        self.ax.clear()
            
    def run(self, show_every: int = 3600) -> None:
        """Run the simulation.

        Args:
            show_every (int, optional): Show the movement of planets only every specified timestep. Defaults to 3600.
        """
        while self.time < self.duration:       
            self.time +=1
            self.update()
            if self.time % show_every == 0:          
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
        limit = self.size * 149_597_870_700    # convert AU in meter
        self.ax.set_xlim((-limit, limit))
        self.ax.set_ylim((-limit, limit))
        self.ax.set_zlim((-limit, limit))
        
        
class BruteForce(Simulation):
    """This class implements the direct brute-force method. The force acting on a single body is calculated by looping over all other bodies. 
    It is simple and accurate but has a complexity of O(n^2). 
    """
    
    def __init__(self, bodies: list[Body], size: int, duration: float = 31.536e6) -> None:
        """Initialize class.

        Args:
            bodies (list[Body]): A list of celestial objects.
            size (int): Size of the canvas in each directions in astronomical units (AU).
            duration (float): Duration of the simulation. Defaults to 31.536e6, i.e. one "year".
        """
        super().__init__(bodies, size, duration)
        
    def update(self) -> None:
        """Calculate the forces exerted on each body and move them accordingly.
        """
        forces = []
        for i, first in enumerate(self.bodies):
            forces.append(Vector3())
            for second in self.bodies:
                if first != second:
                    forces[i] += first.gravitational_force(second)      
        
        for i, b in enumerate(self.bodies):        
            b.move(forces[i])  