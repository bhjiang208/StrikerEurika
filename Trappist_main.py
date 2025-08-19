from neutral import *
from photochemical import *
from basic_cal import *
import numpy as np

def cal_total_escape_speed(temperature, all_particles_nDensity, all_particles):
    total_escape_speed = 0
    for particle in all_particles:
        if particle == "e":
            continue
        escape_speed = cal_escape_speed(temperature, particle, all_particles_nDensity, all_particles)
        total_escape_speed += escape_speed
    return total_escape_speed

def get_color_list(number):
    color_list = []
    for i in range(number):
        color_list.append(plt.cm.viridis(i/number))
    return color_list

def get_escape_speed_list(ori_density, C_factor, N_factor, time_length, temperature):
    escape_speed_list = []
    all_particles = ["CO2", "O2", "CO", "NO", "N2", "O", "N+", "N", "e", "C", "O+", "CO+", "NO+", "N2+", "CO2+", "C+", "O2+"]
    all_particles_nDensity = [ori_density * C_factor, 0, 0, 0, ori_density * N_factor, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #number per m3
    for i in range(time_length):
        all_particles_nDensity = all_photochemical_reactions(all_particles_nDensity, all_particles)[0]
        all_particles_nDensity = run_all_neutral_reactions(temperature, all_particles_nDensity, all_particles)
        escape_speed_list.append(cal_total_escape_speed(temperature, all_particles_nDensity, all_particles))
    return escape_speed_list

def get_energy_consumed_list(ori_density, C_factor, N_factor, time_length, temperature):
    energy_consumed_list = []
    all_particles = ["CO2", "O2", "CO", "NO", "N2", "O", "N+", "N", "e", "C", "O+", "CO+", "NO+", "N2+", "CO2+", "C+", "O2+"]
    all_particles_nDensity = [ori_density * C_factor, 0, 0, 0, ori_density * N_factor, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #number per m3
    for i in range(time_length):
        all_particles_nDensity, energy_consumed = all_photochemical_reactions(all_particles_nDensity, all_particles)
        energy_consumed_list.append(energy_consumed)
        all_particles_nDensity = run_all_neutral_reactions(temperature, all_particles_nDensity, all_particles)
    return energy_consumed_list

def plot_different_temperature_escape(start, end, step, time_length):
    temperature_list = []
    for i in range(start, end + 1, step):
        temperature_list.append(i)
    escape_speed_list = []
    for i, temperature in enumerate(temperature_list):
        print("temperature list number: ", i)
        escape_speed_list.append(get_escape_speed_list(1e8, 5, 5, time_length, temperature))
        plt.plot(range(time_length), escape_speed_list[i], label="temperature=" + str(temperature) + "K", color=get_color_list(len(temperature_list))[i])
    plt.legend()
    plt.xlabel("time (s)")
    plt.ylabel("escape speed (kg/m2/s)")
    plt.title("escape speed in different temperature\n50%CO2 50%N2")
    plt.show()

def plot_flux():
    x = np.linspace(0, 300, 3000)
    y = valid_flux
    plt.xlabel("wavelength (nm)")
    plt.ylabel("flux (W/m2/nm)")
    plt.title("flux of Trappist-1")
    plt.plot(x, y, color = "green")
    plt.show()

def plot_different_composition_escape(ori_density, time_length, temperature):
    C_factor_list = [1,2,3,4,5,6,7,8,9]
    N_factor_list = [9,8,7,6,5,4,3,2,1]
    for i in range(9):
        print(i)
        escape_speed_list = get_escape_speed_list(ori_density, C_factor_list[i], N_factor_list[i], time_length, temperature)
        plt.plot(range(time_length), escape_speed_list, label=str(C_factor_list[i]) + "0%CO2 " + str(N_factor_list[i]) + "0%N2", color=get_color_list(9)[i])
    plt.legend()
    plt.xlabel("time (s)")
    plt.ylabel("energy consumed (J/m2/s)")
    plt.title("energy consumed in different composition\ntemperature = " + str(temperature) + "K")
    plt.show()

def plot_dif_composition_inDif_temperature_escape(ori_density, time_length, temperature_list):
    for temperature in temperature_list:
        print("temperature = ", temperature)
        plot_different_composition_escape(ori_density, time_length, temperature)

def plot_different_temperature_energy(ori_density, time_length, temperature):
    C_factor_list = [2,4,6,8]
    N_factor_list = [8,6,4,2]
    for i in range(4):
        print(i)
        energy_consumed_list = np.array(get_energy_consumed_list(ori_density , C_factor_list[i], N_factor_list[i], time_length, temperature)) * 100
        label = str(C_factor_list[i]) + "0%CO2 " + str(N_factor_list[i]) + "0%N2"
        plt.plot(range(time_length), energy_consumed_list, label=label, color=get_color_list(4)[i])
    plt.legend()
    x = np.linspace(0, 500, 5)
    y = []
    for i in range(5):
        y.append(cal_total_flux())
    plt.plot(x, y, color = "green")
    plt.semilogy()
    plt.xlabel("time (s)")
    plt.ylabel("energy consumed (J/m2/s)")
    plt.title("energy consumed in different composition")
    plt.show()

plot_different_temperature_energy(1e8, 500, 1000)