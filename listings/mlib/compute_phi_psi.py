#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import numpy as np
from Bio.PDB.vectors import Vector, calc_angle, calc_dihedral

MAX_SEQUENCE_LENGTH = 2000
AA_ID_DICT = {'A': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'K': 9,
              'L': 10, 'M': 11, 'N': 12, 'P': 13, 'Q': 14, 'R': 15, 'S': 16, 'T': 17,
              'V': 18, 'W': 19, 'Y': 20}

INVALID_ANGLE = 10  # invalid angle value


def parse_args():
    parser = argparse.ArgumentParser(description='compute_phi_psi.py')

    parser.add_argument('fname')
    parser.add_argument('-plot', action='store_true')

    args = parser.parse_args()
    return args


def encode_primary_string(primary):
    return list([AA_ID_DICT[aa]-1 for aa in primary])


class running_stats:
    '''this class computes mean and std values for a
    list of values across proteins'''

    def __init__(self, name_str):
        self.name = name_str
        self.x = 0.0
        self.x2 = 0.0
        self.n = 0

    def update(self, Vin):
        V = np.array(Vin)
        self.x += np.sum(V)
        self.x2 += np.sum(V**2)
        self.n += len(Vin)

    def print_stats(self):
        mu = self.x / self.n
        std = np.sqrt(self.x2/self.n - mu**2)
        print("bond length", self.name, mu, std)


class compute_stats:
    '''Compute mean and std values for bond lengths and bond angles'''

    def __init__(self):

        self.CN = running_stats("CN")
        self.NCa = running_stats("NCa")
        self.CaC = running_stats("CaC")

        self.CNCa = running_stats("CNCa")
        self.NCaC = running_stats("NCaC")
        self.CaCN = running_stats("CaCN")

    def update(self, v_CN, v_NCa, v_CaC, v_CNCa, v_NCaC, v_CaCN):
        self.CN.update(v_CN)
        self.NCa.update(v_NCa)
        self.CaC.update(v_CaC)

        self.CNCa.update(v_CNCa)
        self.NCaC.update(v_NCaC)
        self.CaCN.update(v_CaCN)

    def print_stats(self):
        self.CN.print_stats()
        self.NCa.print_stats()
        self.CaC.print_stats()

        self.CNCa.print_stats()
        self.NCaC.print_stats()
        self.CaCN.print_stats()


def process_tertiary(tertiary):
    '''compute the bond lengths, bond angles, and dihedral angles'''
    phi = []
    psi = []
    omega = []
    bond_angle_CNCa = []
    bond_angle_NCaC = []
    bond_angle_CaCN = []
    bond_len_NCa = []
    bond_len_CaC = []
    bond_len_CN = []
    # convert tertiary coords into Vectors
    pV = [vec for vec in map(lambda v: Vector(v[0], v[1], v[2]),
                             zip(tertiary[0], tertiary[1], tertiary[2]))]

    for i in range(0, len(pV), 3):
        # check for zero coords
        norm_im1 = False
        norm_i = False
        norm_i1 = False
        norm_i2 = False
        norm_i3 = False
        norm_i4 = False
        if i > 0 and pV[i-1].norm() > 0:
            norm_im1 = True
        if pV[i].norm() > 0:
            norm_i = True
        if pV[i+1].norm() > 0:
            norm_i1 = True
        if pV[i+2].norm() > 0:
            norm_i2 = True
        if i + 3 < len(pV) and pV[i+3].norm() > 0:
            norm_i3 = True
        if i + 3 < len(pV) and pV[i+4].norm() > 0:
            norm_i4 = True

        # compute bond lengths
        if norm_im1 and norm_i:
            blen_CN = (pV[i-1]-pV[i]).norm()
            bond_len_CN.append(blen_CN)

        if norm_i and norm_i1:
            blen_NCa = (pV[i]-pV[i+1]).norm()
            bond_len_NCa.append(blen_NCa)

        if norm_i1 and norm_i2:
            blen_CaC = (pV[i+1]-pV[i+2]).norm()
            bond_len_CaC.append(blen_CaC)

        # compute bond angles
        if norm_im1 and norm_i and norm_i1:
            theta_CNCa = calc_angle(pV[i-1], pV[i], pV[i+1])  # C-N-Ca
            bond_angle_CNCa.append(theta_CNCa)

        if norm_i and norm_i1 and norm_i2:
            theta_NCaC = calc_angle(pV[i], pV[i+1], pV[i+2])  # N-Ca-C
            bond_angle_NCaC.append(theta_NCaC)

        if norm_i1 and norm_i2 and norm_i3:
            theta_CaCN = calc_angle(pV[i+1], pV[i+2], pV[i+3])  # Ca-C-N
            bond_angle_CaCN.append(theta_CaCN)

        # compute dihedral angles
        if norm_im1 and norm_i and norm_i1 and norm_i2:
            phi_i = calc_dihedral(
                pV[i-1], pV[i], pV[i+1], pV[i+2])  # N-Ca-C-N
        else:
            phi_i = INVALID_ANGLE
        phi.append(phi_i)

        if norm_i and norm_i1 and norm_i2 and norm_i3:
            psi_i = calc_dihedral(
                pV[i], pV[i+1], pV[i+2], pV[i+3])  # C-N-Ca-C
        else:
            psi_i = INVALID_ANGLE
        psi.append(psi_i)

        if norm_i1 and norm_i2 and norm_i3 and norm_i4:
            omega_i = calc_dihedral(
                pV[i+1], pV[i+2], pV[i+3], pV[i+4])  # Ca-C-N-Ca
        else:
            omega_i = INVALID_ANGLE
        omega.append(omega_i)

    return (phi, psi, omega, bond_angle_NCaC, bond_angle_CaCN,
            bond_angle_CNCa, bond_len_CN, bond_len_NCa, bond_len_CaC)


def read_protein_from_file(args):
    '''Parse ProteinNet file and add PHIPSI entries'''
    CS = compute_stats()
    filename = args.fname
    out_fname = filename+"_ext"
    with open(out_fname, "w") as out_file:
        with open(filename, "r") as file_pointer:
            pcnt = 0
            id_next = False
            while(True):
                next_line = file_pointer.readline()
                print(next_line, file=out_file, end='')
                if id_next:
                    id_next = False
                    print("ID", next_line, end='')
                if next_line == '[ID]\n':
                    id_next = True
                if next_line == '[TERTIARY]\n':
                    tertiary = []
                    # 3 dimension
                    for _axis in range(3):
                        next_line = file_pointer.readline()
                        print(next_line, file=out_file, end='')
                        tertiary.append(
                            [float(coord)/100 for coord in next_line.split()])

                    # write the PHI_PSI angles
                    print('[PHI_PSI]', file=out_file)

                    phi, psi, omega,\
                        bond_angle_NCaC, bond_angle_CaCN, bond_angle_CNCa,\
                        bond_len_CN, bond_len_NCa, bond_len_CaC = process_tertiary(
                            tertiary)

                    CS.update(bond_len_CN, bond_len_NCa, bond_len_CaC,
                              bond_angle_CNCa, bond_angle_NCaC,
                              bond_angle_CaCN)
                    print("process", pcnt, len(tertiary[0])//3, len(phi),
                          len(psi), "\n")
                    assert(len(tertiary[0])//3 == len(phi))

                    # print(gt, bl[gt])
                    if args.plot:
                        # only plot valid phi,psi pairs (not equal to -1)
                        phi_a = np.array(phi)
                        psi_a = np.array(psi)
                        phi_idx = set(
                            np.where(phi_a != INVALID_ANGLE)[0])
                        psi_idx = set(
                            np.where(psi_a != INVALID_ANGLE)[0])
                        val_idx = list(phi_idx.intersection(psi_idx))
                        plt.plot(phi_a[val_idx], psi_a[val_idx],
                                 'o', markersize=0.5)

                    out_phi = " ".join([str(v) for v in phi])
                    print(out_phi, file=out_file)
                    out_psi = " ".join([str(v) for v in psi])
                    print(out_psi, file=out_file)

                elif next_line == '\n':
                    pcnt += 1

                elif next_line == '':
                    break
        if args.plot:
            # plt.show()
            plt.savefig(args.fname+'_phipsi_plot.png', dpi=300,
                        transparent=True)
        CS.print_stats()


if __name__ == "__main__":
    args = parse_args()
    print(args)
    read_protein_from_file(args)
