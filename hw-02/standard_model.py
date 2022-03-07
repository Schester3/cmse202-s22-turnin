"""Module containing the elementary particle classes. """

import numpy as np


class ElementaryParticle:
    """ Elementary particle class.

    Attributes
    ----------
    x : float
        x-position of the particle.

    y: float
        y-position of the particle.

    ptype: str
        Statistics obeyed by the particle.

    charge : float
        Electric charge of the particle.

    mass : float
        Rest mass in MeV of the particle.

    spin: float
        Spin of the particle.

    Methods
    -------
    info():
        Prints particles information.

    is_antiparticle(other):
        Check if the other is this particle anti-particle

    move()
        Move the particle randomly.

    place_at(coord):
        Place the particle at passed coord.


    """
    x = None
    y = None

    def __init__(self, charge, mass, spin, ptype=None):
        """Initialize the particle's attributes.

        Parameters
        ----------
        charge : float
            Electric charge of the particle.

        mass : float
            Rest mass in MeV of the particle.

        spin: float
            Spin of the particle.

        """
        self.charge = charge
        self.mass = mass
        self.spin = spin
        self.ptype = ptype

    def info(self):
        """Print to scree information about the particle."""

        print(f"The particle has a mass of {self.mass} MeV")
        print(f"The particle's charge is {self.charge} e")
        print(f"The particle's spin is {self.spin}")

    def place_at(self, coord):
        """Place particles at coordinates (x,y).

        Parameters
        ----------
        coord: tuple
            (x,y) coordinates where to place the particle.
        """
        self.x = coord[0]
        self.y = coord[1]

    def move(self):
        """Move the particle by randomly pushing it in both directions."""
        self.x += np.random.randint(low=-1, high=2)
        self.y += np.random.randint(low=-1, high=2)
        
    
    def check_type(self):
        """Updates type by spin
            returns ptype"""
        if self.spin.is_integer():
            self.ptype = "boson"
        else:
            self.ptype = "fermion"
        return self.ptype
    

    def compare(self, other):
        """Compares two particles
        
            Parameters:
            other: ElementaryParticle"""
        if isinstance(other, ElementaryParticle):
            print("The two particles have the same charge: ",self.charge == other.charge)
            print("The two particles have the same mass: ",self.mass == other.mass)
            print("The two particles have the same spin: ", self.spin == other.spin)
        else:
            raise ValueError("Not Valid Particle... enter ElementaryParticle")
            


class Boson(ElementaryParticle):
    """
    Boson: elementary particle that obeys Bose-Einstein statistics.
    This class inherits the ElementaryParticle class with all its attributes and methods.
    Further attributes and methods are

    Attributes
    ----------
    name: str
        Name of the particle.

    Methods
    -------
    check_existence()
        Checks whether this Boson can exists by calling its parent's method check_type()
        Raises a ValueError if check_type() returns "fermion"

    """
    def __init__(self, name, charge, mass, spin):
        self.name = name
        
        if spin.is_integer() == False:
            raise ValueError("fermion")
            
        super(Boson, self).__init__(charge=charge, mass=mass, spin=spin, ptype=None)
        
        
        
    
    def check_existence(self):
        if super().check_type(self) == "fermion":
            raise ValueError("fermion")
        else:
            return True


class Fermion(ElementaryParticle):
    """
    Fermion: elementary particle that obeys Fermi-Dirac statistics.
    This class inherits the ElementaryParticle class with all its attributes and methods.
    Further attributes and methods are

    Attributes
    ----------
    name: str
        Name of the particle.

    Methods
    -------
    check_existence()
        Checks whether this Fermion can exists by calling its parent's method check_type()
        Raises a ValueError if the check_type() returns "boson"

    is_antiparticle(other):
        Check whether other is the anti-particle of this Fermion 
        by checking if other is an instance of Fermion first.

    """
    def __init__(self, name, charge, mass, spin):
        self.name = name
        super(Fermion, self).__init__(charge=charge, mass=mass, spin=spin, ptype=None)
        
    
    
    def check_existence(self):
        if super().check_type(self) == "boson":
            raise ValueError("boson")
        else:
            return True
        
    def is_antiparticle(self, other):
        if isinstance(other, Fermion) and self.charge == -other.charge and self.spin == other.spin and self.mass == other.mass:
            return True
        
        return False


class CompositeParticle(ElementaryParticle):
    """
    A particle composed of several elementary particles.

    Parameters
    ----------

    name: str
        Name of the particle.

    particles : list
        List of particles objects that compose this particle.

    charge : float
        Electric charge of the particle.

    mass : float
        Rest mass in MeV of the particle.

    spin: float
        Spin of the particle.

    """
    
    def __init__(self, name, particles):
        self.name = name
        self.charge = 0
        self.mass = 0
        self.spin = 0
        for i in particles:
            self.charge += i.charge
            self.mass += i.mass
            self.spin += i.spin



