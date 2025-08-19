from constants import *
from data_loader import *
from basic_cal import *
import numpy as np
factor = 1
electron_factor = 1


def neutral_N_O_generate_NO_O(all_particles_nDensity, all_particles, temperature):
    density_r1 = all_particles_nDensity[all_particles.index("N")]
    density_r2 = all_particles_nDensity[all_particles.index("O")]
    r_coeff = 1.5e-20 * factor * temperature * np.exp(-3270/temperature)
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N"), -rate])
    return_list.append([all_particles.index("O"), -rate])
    return_list.append([all_particles.index("NO"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_N_NO_generate_N2_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 4e-17 * factor * (temperature / 300)**0.2 * np.exp(-20/temperature)
    density_r1 = all_particles_nDensity[all_particles.index("N")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("O"), rate])
    return_list.append([all_particles.index("N2"), rate])
    return return_list

def neutral_N_CO2_generate_NO_CO(all_particles_nDensity, all_particles, temperature):
    r_coeff = 1.7e-22
    density_r1 = all_particles_nDensity[all_particles.index("N")]
    density_r2 = all_particles_nDensity[all_particles.index("CO2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N"), -rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return_list.append([all_particles.index("NO"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_NOpos1_e_generate_N_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 8.4e-14 * factor * electron_factor * (300/temperature)**0.85
    density_r1 = all_particles_nDensity[all_particles.index("NO+")]
    density_r2 = all_particles_nDensity[all_particles.index("e")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("NO+"), -rate])
    return_list.append([all_particles.index("e"), -rate])
    return_list.append([all_particles.index("N"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_Opos1_NO_generate_NOpos1_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 7e-19 * factor * (temperature / 300)**0.87
    density_r1 = all_particles_nDensity[all_particles.index("O+")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("O+"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list
    
def neutral_Opos1_CO2_generate_O2pos1_CO(all_particles_nDensity, all_particles, temperature):
    if temperature < 800:
        r_coeff = 1.1e-15 * factor
    else:
        r_coeff = 1.1e-15 * factor * (temperature / 800)**-0.39
    density_r1 = all_particles_nDensity[all_particles.index("O+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("O+"), -rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return_list.append([all_particles.index("O2+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list


def neutral_Opos1_N2_generate_NOpos1_N(all_particles_nDensity, all_particles, temperature):
    # 167: O+ + N2 -> NO+ + N
    # k = 1.20e-12*(300/T)^0.45 (T<=1000K) ; 7.0e-13*(T/1000)^2.12 (T>=1000K)
    if temperature <= 1000.0:
        r_coeff = 1.20e-18 * factor * (300.0/temperature)**0.45
    else:
        r_coeff = 7.0e-19 * factor * (temperature/1000.0)**2.12
    density_r1 = all_particles_nDensity[all_particles.index("O+")]
    density_r2 = all_particles_nDensity[all_particles.index("N2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("O+"), -rate])
    return_list.append([all_particles.index("N2"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("N"), rate])
    return return_list

def neutral_Opos1_O2_generate_O2pos1_O(all_particles_nDensity, all_particles, temperature):
    # 169: O+ + O2 -> O2+ + O
    # k = 1.6e-11*(300/T)^0.52 (T<=900K) ; 9.0e-12*(T/900)^0.92 (T>=900K)
    if temperature <= 900.0:
        r_coeff = 1.6e-17 * factor * (300.0/temperature)**0.52
    else:
        r_coeff = 9.0e-18 * factor * (temperature/900.0)**0.92
    density_r1 = all_particles_nDensity[all_particles.index("O+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("O+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("O2+"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_Opos1_e_generate_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 3.7e-18 * factor * electron_factor * (250.0/temperature)**0.7
    density_r1 = all_particles_nDensity[all_particles.index("O+")]
    density_r2 = all_particles_nDensity[all_particles.index("e")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("O+"), -rate])
    return_list.append([all_particles.index("e"), -rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_Opos1_C_generate_Cpos1_O(all_particles_nDensity, all_particles, temperature):
    # 173: O+ + C -> C+ + O ; k = 1.0e-10
    r_coeff = 1.0e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("O+")]
    density_r2 = all_particles_nDensity[all_particles.index("C")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("O+"), -rate])
    return_list.append([all_particles.index("C"), -rate])
    return_list.append([all_particles.index("C+"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_CO2pos1_O_generate_O2pos1_CO(all_particles_nDensity, all_particles, temperature):
    # 177: CO2+ + O -> O2+ + CO ; k = 1.0e-10
    r_coeff = 1.6e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO2+")]
    density_r2 = all_particles_nDensity[all_particles.index("O")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO2+"), -rate])
    return_list.append([all_particles.index("O"), -rate])
    return_list.append([all_particles.index("O2+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_CO2pos1_O_generate_Opos1_CO2(all_particles_nDensity, all_particles, temperature):
    # 178: CO2+ + O -> O+ + CO2 ; k = 1.0e-10
    r_coeff = 1.0e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO2+")]
    density_r2 = all_particles_nDensity[all_particles.index("O")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO2+"), -rate])
    return_list.append([all_particles.index("O"), -rate])
    return_list.append([all_particles.index("O+"), rate])
    return_list.append([all_particles.index("CO2"), rate])
    return return_list

def neutral_CO2pos1_NO_generate_NOpos1_CO2(all_particles_nDensity, all_particles, temperature):
    # 179: CO2+ + NO -> NO+ + CO2 ; k = 1.2e-10
    r_coeff = 1.2e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO2+")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO2+"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("CO2"), rate])
    return return_list

def neutral_CO2pos1_e_generate_CO_O(all_particles_nDensity, all_particles, temperature):
    # 181: CO2+ + e- -> CO + O ; k = 3.5e-7 * (300/T)^0.5
    r_coeff = 3.5e-13 * factor * electron_factor * (300.0/temperature)**0.5
    density_r1 = all_particles_nDensity[all_particles.index("CO2+")]
    density_r2 = all_particles_nDensity[all_particles.index("e")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO2+"), -rate])
    return_list.append([all_particles.index("e"), -rate])
    return_list.append([all_particles.index("CO"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_CO2pos1_O2_generate_CO2_O2pos1(all_particles_nDensity, all_particles, temperature):
    # 182: CO2+ + O2 -> CO2 + O2+ ;
    # k = 5.5e-11*(300/T)^0.82 (T<=1500K) ; 1.5e-11*(T/1500)^0.75 (T>=1500K)
    if temperature <= 1500.0:
        r_coeff = 5.5e-17 * factor * (300.0/temperature)**0.82
    else:
        r_coeff = 1.5e-17 * factor * (temperature/1500.0)**0.75
    density_r1 = all_particles_nDensity[all_particles.index("CO2+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO2+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("CO2"), rate])
    return_list.append([all_particles.index("O2+"), rate])
    return return_list

def neutral_CO2pos1_N_generate_NO_COpos1(all_particles_nDensity, all_particles, temperature):
    # 184: CO2+ + N -> NO + CO+ ; k = 3.4e-10
    r_coeff = 3.4e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO2+")]
    density_r2 = all_particles_nDensity[all_particles.index("N")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO2+"), -rate])
    return_list.append([all_particles.index("N"), -rate])
    return_list.append([all_particles.index("NO"), rate])
    return_list.append([all_particles.index("CO+"), rate])
    return return_list

def neutral_COpp_O_generate_Opos1_CO(all_particles_nDensity, all_particles, temperature):
    # 189: CO+ + O -> O+ + CO ; k = 1.4e-10
    r_coeff = 1.4e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO+")]
    density_r2 = all_particles_nDensity[all_particles.index("O")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO+"), -rate])
    return_list.append([all_particles.index("O"), -rate])
    return_list.append([all_particles.index("O+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_COpp_NO_generate_NOpos1_CO(all_particles_nDensity, all_particles, temperature):
    # 190: CO+ + NO -> NO+ + CO ; k = 4.2e-10
    r_coeff = 4.2e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO+")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO+"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

# ===================== 192–199（先前已给） =====================

def neutral_COpos1_CO2_generate_CO2pos1_CO(all_particles_nDensity, all_particles, temperature):
    # 191: CO+ + CO2 -> CO2+ + CO ; k = 1.7e-7 * (300/T)^0.55
    r_coeff = 1.1e-15 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO+"), -rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return_list.append([all_particles.index("CO2+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_COpos1_O2_generate_O2pos1_CO(all_particles_nDensity, all_particles, temperature):
    r_coeff = 1.5e-16 * factor * (300.0/temperature)**1.1
    density_r1 = all_particles_nDensity[all_particles.index("CO+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("O2+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_COpos1_N_generate_NOpos1_C(all_particles_nDensity, all_particles, temperature):
    r_coeff = 8.2e-17 * factor
    density_r1 = all_particles_nDensity[all_particles.index("CO+")]
    density_r2 = all_particles_nDensity[all_particles.index("N")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO+"), -rate])
    return_list.append([all_particles.index("N"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("C"), rate])
    return return_list

def neutral_COpos1_e_generate_C_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 1.8e-13 * factor * electron_factor * (300.0/temperature)**0.55
    density_r1 = all_particles_nDensity[all_particles.index("CO+")]
    density_r2 = all_particles_nDensity[all_particles.index("e")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("CO+"), -rate])
    return_list.append([all_particles.index("e"), -rate])
    return_list.append([all_particles.index("C"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

# ===================== 200–217（先前已给） =====================

def neutral_Npos1_O2_generate_Opos1_NO(all_particles_nDensity, all_particles, temperature):
    if temperature <= 1000.0:
        r_coeff = 4.34e-17 * factor * (300.0/temperature)**0.45
    else:
        r_coeff = 7.53e-17 * factor
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("O+"), rate])
    return_list.append([all_particles.index("NO"), rate])
    return return_list

def neutral_Npos1_O2_generate_O2pos1_N(all_particles_nDensity, all_particles, temperature):
    if temperature <= 1000.0:
        r_coeff = 2.02e-16 * factor * (300.0/temperature)**0.45
    else:
        r_coeff = 3.49e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("O2+"), rate])
    return_list.append([all_particles.index("N"), rate])
    return return_list

def neutral_Npos1_O2_generate_NOpos1_O(all_particles_nDensity, all_particles, temperature):
    if temperature <= 1000.0:
        r_coeff = 4.32e-17 * factor * (300.0/temperature)**0.45
    else:
        r_coeff = 7.47e-17 * factor
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_Npos1_O_generate_Opos1_N(all_particles_nDensity, all_particles, temperature):
    r_coeff = 2.2e-18
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("O")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("O"), -rate])
    return_list.append([all_particles.index("O+"), rate])
    return_list.append([all_particles.index("N"), rate])
    return return_list

def neutral_Npos1_NO_generate_NOpos1_N(all_particles_nDensity, all_particles, temperature):
    r_coeff = 4.72e-16 * factor * (300.0/temperature)**0.24
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("N"), rate])
    return return_list

def neutral_Npos1_CO2_generate_CO2pos1_N(all_particles_nDensity, all_particles, temperature):
    r_coeff = 9.2e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return_list.append([all_particles.index("CO+"), rate])
    return_list.append([all_particles.index("NO"), rate])
    return return_list

def neutral_Npos1_CO2_generate_COpp_NO(all_particles_nDensity, all_particles, temperature):
    r_coeff = 2.0e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return_list.append([all_particles.index("CO+"), rate])
    return_list.append([all_particles.index("NO"), rate])
    return return_list

def neutral_Npos1_CO_generate_COpp_N(all_particles_nDensity, all_particles, temperature):
    r_coeff = 4.93e-16 * factor * (300.0/temperature)**0.5
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("CO"), -rate])
    return_list.append([all_particles.index("NO"), rate])
    return return_list

def neutral_Npos1_e_generate_N(all_particles_nDensity, all_particles, temperature):
    r_coeff = 3.6e-18 * factor * electron_factor * (250.0/temperature)**0.7
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("e")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("e"), -rate])
    return_list.append([all_particles.index("N"), rate])
    return return_list

def neutral_Npos1_NO_generate_N2pos1_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 8.33e-17 * factor * (300.0/temperature)**0.24
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("N2+"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_Npos1_CO_generate_NOpos1_C(all_particles_nDensity, all_particles, temperature):
    r_coeff = 6.16e-17 * factor * (300.0/temperature)**0.5
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("CO"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("C"), rate])
    return return_list

def neutral_Npos1_CO_generate_Cpos1_NO(all_particles_nDensity, all_particles, temperature):
    r_coeff = 5.60e-18 * factor * (300.0/temperature)**0.5
    density_r1 = all_particles_nDensity[all_particles.index("N+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("N+"), -rate])
    return_list.append([all_particles.index("CO"), -rate])
    return_list.append([all_particles.index("C+"), rate])
    return_list.append([all_particles.index("NO"), rate])
    return return_list

# ===================== 324–327（先前已给） =====================

def neutral_Cpos1_CO2_generate_COpp_CO(all_particles_nDensity, all_particles, temperature):
    r_coeff = 1.1e-15 * factor
    density_r1 = all_particles_nDensity[all_particles.index("C+")]
    density_r2 = all_particles_nDensity[all_particles.index("CO2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("C+"), -rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return_list.append([all_particles.index("CO+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_Cpos1_NO_generate_NOpp_C(all_particles_nDensity, all_particles, temperature):
    r_coeff = 7.5e-16 * factor * (300.0/temperature)**0.2
    density_r1 = all_particles_nDensity[all_particles.index("C+")]
    density_r2 = all_particles_nDensity[all_particles.index("NO")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("C+"), -rate])
    return_list.append([all_particles.index("NO"), -rate])
    return_list.append([all_particles.index("NO+"), rate])
    return_list.append([all_particles.index("C"), rate])
    return return_list

def neutral_Cpos1_O2_generate_Opos1_CO(all_particles_nDensity, all_particles, temperature):
    r_coeff = 5.22e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("C+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("C+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("O+"), rate])
    return_list.append([all_particles.index("CO"), rate])
    return return_list

def neutral_Cpos1_O2_generate_COpp_O(all_particles_nDensity, all_particles, temperature):
    r_coeff = 3.48e-16 * factor
    density_r1 = all_particles_nDensity[all_particles.index("C+")]
    density_r2 = all_particles_nDensity[all_particles.index("O2")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("C+"), -rate])
    return_list.append([all_particles.index("O2"), -rate])
    return_list.append([all_particles.index("CO+"), rate])
    return_list.append([all_particles.index("O"), rate])
    return return_list

def neutral_Cpos1_e_generate_C(all_particles_nDensity, all_particles, temperature):
    r_coeff = 1.43e-16 * factor * electron_factor * temperature**-0.6
    density_r1 = all_particles_nDensity[all_particles.index("C+")]
    density_r2 = all_particles_nDensity[all_particles.index("e")]
    rate = r_coeff * density_r1 * density_r2
    return_list = []
    return_list.append([all_particles.index("C+"), -rate])
    return_list.append([all_particles.index("e"), -rate])
    return_list.append([all_particles.index("C"), rate])
    return return_list

def sum_returned_list(returned_list_list, all_particles):
    sum_list = np.zeros(len(all_particles))
    for i in range(len(returned_list_list)):
        for j in range(len(returned_list_list[i])):
            sum_list[returned_list_list[i][j][0]] += returned_list_list[i][j][1]
    return sum_list

def get_update_particles(sum_returned_list, all_particles_nDensity):
    for i in range(len(sum_returned_list)):
        all_particles_nDensity[i] += sum_returned_list[i]
    return all_particles_nDensity

def run_all_neutral_reactions(temperature, all_particles_nDensity, all_particles):
    returned_list_list = []
    # N 相关反应
    returned_list_list.append(neutral_N_O_generate_NO_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_N_NO_generate_N2_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_N_CO2_generate_NO_CO(all_particles_nDensity, all_particles, temperature))
    
    # NO+ 相关反应
    returned_list_list.append(neutral_NOpos1_e_generate_N_O(all_particles_nDensity, all_particles, temperature))
    
    # O+ 相关反应
    returned_list_list.append(neutral_Opos1_NO_generate_NOpos1_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Opos1_CO2_generate_O2pos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Opos1_N2_generate_NOpos1_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Opos1_O2_generate_O2pos1_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Opos1_e_generate_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Opos1_C_generate_Cpos1_O(all_particles_nDensity, all_particles, temperature))
    
    # CO2+ 相关反应
    returned_list_list.append(neutral_CO2pos1_O_generate_O2pos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_CO2pos1_O_generate_Opos1_CO2(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_CO2pos1_NO_generate_NOpos1_CO2(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_CO2pos1_e_generate_CO_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_CO2pos1_O2_generate_CO2_O2pos1(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_CO2pos1_N_generate_NO_COpos1(all_particles_nDensity, all_particles, temperature))
    
    # CO+ 相关反应
    returned_list_list.append(neutral_COpp_O_generate_Opos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_COpp_NO_generate_NOpos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_COpos1_CO2_generate_CO2pos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_COpos1_O2_generate_O2pos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_COpos1_N_generate_NOpos1_C(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_COpos1_e_generate_C_O(all_particles_nDensity, all_particles, temperature))
    
    # N+ 相关反应
    returned_list_list.append(neutral_Npos1_O2_generate_Opos1_NO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_O2_generate_O2pos1_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_O2_generate_NOpos1_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_O_generate_Opos1_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_NO_generate_NOpos1_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_CO2_generate_CO2pos1_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_CO2_generate_COpp_NO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_CO_generate_COpp_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_e_generate_N(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_NO_generate_N2pos1_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_CO_generate_NOpos1_C(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Npos1_CO_generate_Cpos1_NO(all_particles_nDensity, all_particles, temperature))
    
    # C+ 相关反应
    returned_list_list.append(neutral_Cpos1_CO2_generate_COpp_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Cpos1_NO_generate_NOpp_C(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Cpos1_O2_generate_Opos1_CO(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Cpos1_O2_generate_COpp_O(all_particles_nDensity, all_particles, temperature))
    returned_list_list.append(neutral_Cpos1_e_generate_C(all_particles_nDensity, all_particles, temperature))
    sum_returned = sum_returned_list(returned_list_list, all_particles)
    all_particles_nDensity = get_update_particles(sum_returned, all_particles_nDensity)
    return all_particles_nDensity