import numpy as np
from constants import *
from data_loader import *

#gravitational acceleration in different heights
def cal_g(z, planet_radius, planet_mass):
    return gravitational_constant * planet_mass / ((planet_radius + z)**2)

#this function calculate the energy of a photon, given the wavelength in nm
def cal_energy_J(wavelength_nm):
    return planck_constant * light_speed / (wavelength_nm * 1e-9)#J

#given the reactant, this function return the cross section of the reactant
#the return value is a whole pandas dataframe
#return value is a pandas dataframe
def find_croSec_reactant(reactant_name):
    if reactant_name == "CO2":
        return CO2_croSec_df
    elif reactant_name == "O2":
        return O2_croSec_df
    elif reactant_name == "CO":
        return CO_croSec_df

#helper function of cal_rate_coefficient
#given the product and croSec of a specific reaction, this function return the cross section of one of the specific products
#return value is a pandas series
def find_croSec_product(croSec_df, product_name):
    if product_name == "sCO/O1D":
        return croSec_df["sCO/O1D"] * 1e-4#m2
    elif product_name == "sCO/O":
        return croSec_df["sCO/O"] * 1e-4#m2
    elif product_name == "O/O":
        return croSec_df["O/O"] * 1e-4#m2
    elif product_name == "O/O1D":
        return croSec_df["O/O1D"] * 1e-4#m2
    elif product_name == "C/O":
        return croSec_df["C/O"] * 1e-4#m2
    elif product_name == "C1D/O1D":
        return croSec_df["C1D/O1D"] * 1e-4#m2
    else:
        raise ValueError(f"Unknown product_name: {product_name}")

#this function can calculate the rate coefficient for any reaction
def get_croSec_inter(reactant_name, product_name):
    croSec_df = croSec_dict[reactant_name]
    lamda_croSec = croSec_df["Lambda"] * 0.1#nm
    croSec = croSec_df[product_name] * 1e-4#m2
    croSec_inter = np.interp(valid_wavelength, lamda_croSec, croSec)
    return croSec_inter

def cal_rate_coefficient(reactant_name, product_name):
    croSec_inter = get_croSec_inter(reactant_name, product_name)
    energy = cal_energy_J(valid_wavelength)
    temp_k_rate = valid_flux * croSec_inter / energy
    integrated_rate = np.trapz(temp_k_rate, valid_wavelength)
    return integrated_rate

def cal_thermo_speed(temperature, particle_name):
    mass = all_particles_real_mass_dict[particle_name]
    factor = 2 * Boltzmann_constant * temperature / mass
    return np.sqrt(factor)

def cal_Jeans_parameter(temperature, particle_name):
    mass = all_particles_real_mass_dict[particle_name]
    factor1 = gravitational_constant * mass * planet_mass
    factor2 = planet_radius * Boltzmann_constant * temperature
    return factor1 / factor2

def cal_escape_speed(temperature, particle_name, all_particles_nDensity, all_particles):
    parameter = cal_Jeans_parameter(temperature, particle_name)/3
    speed = cal_thermo_speed(temperature, particle_name)
    nDensity = all_particles_nDensity[all_particles.index(particle_name)]
    factor = (1 + parameter) * np.exp(-parameter) / (2 * np.sqrt(np.pi))
    return speed * factor * nDensity

def plot_croSec():
    x = np.linspace(0, 300, 3000)
    y = get_croSec_inter("CO2", "Total")
    plt.xlabel("wavelength (nm)")
    plt.ylabel("cross section (m2)")
    plt.title("cross section all photo chemical reactions\n with reactant CO2")
    plt.plot(x, y, color = "green")
    plt.show()

def cal_total_flux():
    total_flux = 0
    for i in range(len(valid_wavelength)):
        flux = valid_flux[i]
        total_flux += flux
    return total_flux