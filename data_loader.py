import re
import pandas as pd
from astropy.table import Table
import matplotlib.pyplot as plt
from constants import *

#this function is used in basic_cal.py
#this function calculate the energy of a photon, given the wavelength in nm
def cal_energy_J(wavelength_nm):
    return planck_constant * light_speed / (wavelength_nm * 1e-9)

#this function return a pandas dataframe of the cross section
#this pandas dataframe has three kinds of columns: Lambda, Total, and the cross section of each reaction
def read_croSec(croSec_txt_path):
    with open(croSec_txt_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    header_index = 0
    for i, line in enumerate(lines):
        if "Lambda" in line and "=" not in line:
            header_index = i
            break

    header_line = lines[header_index]
    data_lines = lines[header_index + 1:]

    columns = re.findall(r"\S+", header_line)  # 提取列名
    data = []

    for line in data_lines:
        values = re.findall(r"[-+]?\d*\.\d+E[-+]\d+|\d+\.\d+|\d+", line)
        data.append(values)

    # 4. 创建 DataFrame
    df = pd.DataFrame(data, columns=columns)
    df = df.astype(float)
    return df

#this function read the spectrum file and return a pandas dataframe
def read_spectrum(spectrum_txt_path):
    table = Table.read(spectrum_txt_path, format="ascii.ecsv")

    # 转为 pandas dataframe 方便操作
    df = table.to_pandas()
    return df
    
spectrum_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/trappist-1_model_const_res_v07.ecsv"
spectrum_df = read_spectrum(spectrum_txt_path)
valid_spectrum_df = spectrum_df[:3000]
#unit unsure
valid_flux = valid_spectrum_df["FLUX"] * distance_fac
valid_wavelength = valid_spectrum_df["WAVELENGTH"] * 0.1

CO2_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/CO2_pho_croSec.txt"
CO2_croSec_df = read_croSec(CO2_croSec_txt_path)

O2_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/O2_pho_croSec.txt"
O2_croSec_df = read_croSec(O2_croSec_txt_path)

CO_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/CO_pho_croSec.txt"
CO_croSec_df = read_croSec(CO_croSec_txt_path)

NO_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/NO_pho_croSec.txt"
NO_croSec_df = read_croSec(NO_croSec_txt_path)

N2_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/N2_pho_croSec.txt"
N2_croSec_df = read_croSec(N2_croSec_txt_path)

N_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/N_pho_croSec.txt"
N_croSec_df = read_croSec(N_croSec_txt_path)

O_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/O_pho_croSec.txt"
O_croSec_df = read_croSec(O_croSec_txt_path)

C_croSec_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/C_pho_croSec.txt"
C_croSec_df = read_croSec(C_croSec_txt_path)

croSec_dict = {
    "CO2": CO2_croSec_df,
    "O2": O2_croSec_df,
    "CO": CO_croSec_df,
    "NO": NO_croSec_df,
    "N2": N2_croSec_df,
    "N": N_croSec_df,
    "O": O_croSec_df,
    "C": C_croSec_df
}

CO2_croSec_dict = {
    "sCO/O": CO2_croSec_df["sCO/O"],
}
O2_croSec_dict = {
    "O/O": O2_croSec_df["O/O"],
    "O+O": O2_croSec_df["O+O"],
    "O2+": O2_croSec_df["O2+"],
}
CO_croSec_dict = {
    "C/O": CO_croSec_df["C/O"],
}

NO_croSec_dict = {
    "N/O": NO_croSec_df["N/O"],
    "NO+": NO_croSec_df["NO+"],
    "O+N": NO_croSec_df["O+N"],
    "N+O": NO_croSec_df["N+O"],
}

N2_croSec_dict = {
    "N/N": N2_croSec_df["N/N"],
    "N2+": N2_croSec_df["N2+"],
    "N+N": N2_croSec_df["N+N"],
}

N_croSec_dict = {
    "N+": N_croSec_df["N+"]
}

O_croSec_dict = {
    "O+": O_croSec_df["O+"]
}

C_croSec_dict = {
    "C+": C_croSec_df["C+"]
}

croSec_all_dict = {
    "CO2": CO2_croSec_dict,
    "O2": O2_croSec_dict,
    "CO": CO_croSec_dict,
    "NO": NO_croSec_dict,
    "N2": N2_croSec_dict,
    "N": N_croSec_dict,
    "O": O_croSec_dict,
    "C": C_croSec_dict
}
#test part
#this function is only for test (plot the spectrum)
def plot_spectrum(spectrum_df):
    print(spectrum_df.columns)
    plt.semilogx(spectrum_df["WAVELENGTH"], spectrum_df["FLUX"])
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Flux (W/m2/nm)")
    plt.title("Spectrum of Trappist-1")
    plt.show()

def print_valid_spectrum():
    spectrum_txt_path = "/Users/jerryjiang/Desktop/trappist/Trappist-code/trappist-1_model_const_res_v07.ecsv"
    spectrum_df = read_spectrum(spectrum_txt_path)
    valid_spectrum_df = spectrum_df[:5000]
    print("valid_spectrum_df\n", valid_spectrum_df)

def test_photon_number():
    energy = cal_energy_J(valid_spectrum_df["WAVELENGTH"])#nm
    number = valid_spectrum_df["FLUX"] * 1e-3 * distance_fac / energy
    plt.plot(valid_spectrum_df["WAVELENGTH"], number)
    plt.semilogy()
    plt.show()