#all constants
import numpy as np

N_A = 6.02214076e23#mol^-1
all_particles_real_mass_dict = {
    "CO2": 44e-3 / N_A,
    "O2": 32e-3 / N_A,
    "CO": 28e-3 / N_A,
    "NO": 30e-3 / N_A,
    "N2": 28e-3 / N_A,
    "N+": 14e-3 / N_A,
    "N": 14e-3 / N_A,
    "e": 0.00000054858 / N_A,
    "O": 16e-3 / N_A,
    "C": 12e-3 / N_A,
    "C+": 12e-3 / N_A,
    "O+": 16e-3 / N_A,
    "O2+": 32e-3 / N_A,
    "CO2+": 44e-3 / N_A,
    "CO+": 28e-3 / N_A,
    "NO+": 30e-3 / N_A,
    "N2+": 28e-3 / N_A,
}

ave_particle_mol_mass = 28e-3#kg/mol
Earth_mass = 5.972e24#kg
Earth_radius = 6371000#m
Earth_pressure = 101325#Pa

planet_mass = 0.8 * Earth_mass
planet_radius = Earth_radius
sur_pressure = Earth_pressure * 0.01#Pa
sur_temp = 300#K

Boltzmann_constant = 1.380649e-23#J/K
gravitational_constant = 6.67430e-11#m^3/kg/s^2
planck_constant = 6.62607015e-34#J*s
light_speed = 299792458#m/s
eV_to_J = 1.602176634e-19#J/eV

d_pc = 12.43
d_au = d_pc * 206265
a_au = 0.011
distance_fac = (d_au / a_au)**2