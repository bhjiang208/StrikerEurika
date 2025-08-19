import numpy as np
from data_loader import *
from basic_cal import *
from constants import *
#在bisic_cal里改了cal_rate_coefficient，现在直接返回rate
#不用考虑是否有多余光子，因为粒子数密度很低

def photoChe_CO2_generate_CO_O(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "sCO/O"
    p1 = "CO"
    p2 = "O"
    nDensity = all_particles_nDensity[all_particles.index("CO2")]
    k_coeff = cal_rate_coefficient("CO2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 5.52 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return return_list, energy_consumed

def photoChe_CO2_generate_CO2pos1(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "CO2+"
    p1 = "CO2+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("CO2")]
    k_coeff = cal_rate_coefficient("CO2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 13.77 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return return_list, energy_consumed

def photoChe_CO2_generate_COpos1_O(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "CO+O"
    p1 = "CO+"
    p2 = "O"
    p3 = "e"
    nDensity = all_particles_nDensity[all_particles.index("CO2")]
    k_coeff = cal_rate_coefficient("CO2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 19.42 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index(p3), rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return return_list, energy_consumed

def photoChe_CO2_generate_Opos1_CO(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "CO2+"
    p1 = "CO+"
    p2 = "O"
    p3 = "e"
    nDensity = all_particles_nDensity[all_particles.index("CO2")]
    k_coeff = cal_rate_coefficient("CO2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 19.4 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index(p3), rate])
    return_list.append([all_particles.index("CO2"), -rate])
    return return_list, energy_consumed

def photoChe_C_generate_Cpos1(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "C+"
    p1 = "C+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("C")]
    k_coeff = cal_rate_coefficient("C", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 19.4 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("C"), -rate])
    return return_list, energy_consumed

def photoChe_O2_generate_O_O(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "O/O"
    p1 = "O"
    p2 = "O"
    nDensity = all_particles_nDensity[all_particles.index("O2")]
    k_coeff = cal_rate_coefficient("O2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 5.12 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("O2"), -rate])
    return return_list, energy_consumed

def photoChe_O2_generate_Opos1_O(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "O+O"
    p1 = "O+"
    p2 = "O"
    nDensity = all_particles_nDensity[all_particles.index("O2")]
    k_coeff = cal_rate_coefficient("O2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 17.3 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("O2"), -rate])
    return return_list, energy_consumed

def photoChe_O2_generate_O2pos1(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "O2+"
    p1 = "O2+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("O2")]
    k_coeff = cal_rate_coefficient("O2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 12.1 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("O2"), -rate])
    return return_list, energy_consumed

def photoChe_O_generate_Opos1(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "O+"
    p1 = "O+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("O")]
    k_coeff = cal_rate_coefficient("O", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 13.6 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("O"), -rate])
    return return_list, energy_consumed

def photoChe_CO_generate_C_O(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "C/O"
    p1 = "C"
    p2 = "O"
    nDensity = all_particles_nDensity[all_particles.index("CO")]
    k_coeff = cal_rate_coefficient("CO", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 11.1 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("CO"), -rate])
    return return_list, energy_consumed

def photoChe_NO_generate_N_O(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "N/O"
    p1 = "N"
    p2 = "O"
    nDensity = all_particles_nDensity[all_particles.index("NO")]
    k_coeff = cal_rate_coefficient("NO", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 6.5 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("NO"), -rate])
    return return_list, energy_consumed

def photoChe_NO_generate_NOpos1_e(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "NO+"
    p1 = "NO+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("NO")]
    k_coeff = cal_rate_coefficient("NO", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 9.62 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("NO"), -rate])
    return return_list, energy_consumed

def photoChe_NO_generate_Opos1_N_e(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "O+N"
    p1 = "O+"
    p2 = "N"
    p3 = "e"
    nDensity = all_particles_nDensity[all_particles.index("NO")]
    k_coeff = cal_rate_coefficient("NO", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 21.7 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index(p3), rate])
    return_list.append([all_particles.index("NO"), -rate])
    return return_list, energy_consumed

def photoChe_NO_generate_O_NOpos1_e(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "N+O"
    p1 = "N+"
    p2 = "O"
    p3 = "e"
    nDensity = all_particles_nDensity[all_particles.index("NO")]
    k_coeff = cal_rate_coefficient("NO", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 21 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index(p3), rate])
    return_list.append([all_particles.index("NO"), -rate])
    return return_list, energy_consumed

def photoChe_N2_generate_N_N(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "N/N"
    p1 = "N"
    p2 = "N"
    nDensity = all_particles_nDensity[all_particles.index("N2")]
    k_coeff = cal_rate_coefficient("N2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 12.14 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("N2"), -rate])
    return return_list, energy_consumed

def photoChe_N2_generate_N2pos1_e(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "N2+"
    p1 = "N2+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("N2")]
    k_coeff = cal_rate_coefficient("N2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 15.18 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("N2"), -rate])
    return return_list, energy_consumed

def photoChe_N2_generate_Npos1_N(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "N+N"
    p1 = "N+"
    p2 = "N"
    p3 = "e"
    nDensity = all_particles_nDensity[all_particles.index("N2")]
    k_coeff = cal_rate_coefficient("N2", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 24.3 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index(p3), rate])
    return_list.append([all_particles.index("N2"), -rate])
    return return_list, energy_consumed

def photoChe_N_generate_Npos1(all_particles_nDensity, all_particles):
    return_list = []
    product_name = "N+"
    p1 = "N+"
    p2 = "e"
    nDensity = all_particles_nDensity[all_particles.index("N")]
    k_coeff = cal_rate_coefficient("N", product_name)
    rate = k_coeff * nDensity / 10
    energy_th = 24.3 * eV_to_J
    energy_consumed = rate * energy_th
    return_list.append([all_particles.index(p1), rate])
    return_list.append([all_particles.index(p2), rate])
    return_list.append([all_particles.index("N"), -rate])
    return return_list, energy_consumed

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


def all_photochemical_reactions(all_particles_nDensity, all_particles):
    energy_consumed = 0
    returned_list_list = []
    returned_list_list.append(photoChe_CO2_generate_CO_O(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_O2_generate_O_O(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_O2_generate_Opos1_O(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_O2_generate_O2pos1(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_O_generate_Opos1(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_CO_generate_C_O(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_NO_generate_N_O(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_NO_generate_Opos1_N_e(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_NO_generate_O_NOpos1_e(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_N2_generate_N_N(all_particles_nDensity, all_particles)[0]) 
    returned_list_list.append(photoChe_N2_generate_N2pos1_e(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_N2_generate_Npos1_N(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_NO_generate_NOpos1_e(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_N_generate_Npos1(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_C_generate_Cpos1(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_CO2_generate_CO2pos1(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_CO2_generate_COpos1_O(all_particles_nDensity, all_particles)[0])
    returned_list_list.append(photoChe_CO2_generate_Opos1_CO(all_particles_nDensity, all_particles)[0])
    energy_consumed += photoChe_CO2_generate_CO_O(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_O2_generate_O_O(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_O2_generate_Opos1_O(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_O2_generate_O2pos1(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_O_generate_Opos1(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_CO_generate_C_O(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_NO_generate_N_O(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_NO_generate_Opos1_N_e(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_NO_generate_O_NOpos1_e(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_N2_generate_N_N(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_N2_generate_N2pos1_e(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_N2_generate_Npos1_N(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_NO_generate_NOpos1_e(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_N_generate_Npos1(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_C_generate_Cpos1(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_CO2_generate_CO2pos1(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_CO2_generate_COpos1_O(all_particles_nDensity, all_particles)[1]
    energy_consumed += photoChe_CO2_generate_Opos1_CO(all_particles_nDensity, all_particles)[1]
    sum_returned = sum_returned_list(returned_list_list, all_particles)
    all_particles_nDensity = get_update_particles(sum_returned, all_particles_nDensity)
    return all_particles_nDensity, energy_consumed