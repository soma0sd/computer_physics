# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:05:29 2016
@author: soma0sd
"""
from matplotlib import pyplot as plt
import pickle

nucid = '2350920'

symbols = {0: 'n', 1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Uut', 114: 'Fl', 115: 'Uup', 116: 'Lv', 118: 'Uuo'}


with open('decays02.pkl', 'rb') as f:
  data = pickle.load(f)

lines = []

plt.figure(figsize=(10,5))
max_Z = max_N = 0
min_Z = min_N = 300

def decays(nucid):
  global data, lines, max_Z, min_Z, max_N, min_N
  for m in data[nucid]['DM']:
    for i, ems in enumerate(m[0]):
      if i < 1:
        iZ, fZ = int(nucid[4:6]), int(ems[4:6])
        iN, fN = int(nucid[:3])-iZ, int(ems[:3])-fZ
        plt.plot([iZ, fZ], [iN, fN])
        sym = str(symbols[iZ])
        A = str(iN+iZ)
        tx = '$^{'+A+'}\mathrm{'+sym+'}$'
        plt.text(iZ, iN, tx, fontsize=12,
                 verticalalignment='bottom', horizontalalignment='center')
        sym = str(symbols[fZ])
        A = str(fN+fZ)
        tx = '$^{'+A+'}\mathrm{'+sym+'}$'
        plt.text(fZ, fN, tx, fontsize=12,
                 verticalalignment='bottom', horizontalalignment='center')
        max_Z, min_Z = max([iZ, fZ, max_Z]), min([iZ, fZ, min_Z])
        max_N, min_N = max([iN, fN, max_N]), min([iN, fN, min_N])
        decays(ems)


sym = symbols[int(nucid[4:6])]
A = int(nucid[:3])
tx = '$^{'+str(A)+'}\mathrm{'+sym+'}$'
plt.title(tx+' Decay Chain')
plt.xlabel('Z')
plt.ylabel('N')
decays(nucid)
plt.xlim(min_Z-2, max_Z+2)
plt.ylim(min_N-2, max_N+2)