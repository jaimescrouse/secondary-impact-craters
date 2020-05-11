import numpy as np
import matplotlib.pyplot as plt
from astropy.io import  ascii


#Loading the csv file
csv_file = ascii.read('/Users/jaimearnold/Desktop/luna_codes_2020/Crouse_combined_Jan3at258.csv')


aspect_ratios = csv_file['Minor Axis (km)']/csv_file['Major Axis (km)']
IC = 4 * np.pi * csv_file['Enclosed Area (square km)']/(csv_file['Perimeter (km)']**2)

site = 'Combined'

if not site == 'Combined':
    A_truth_array = ['A' in i['Class (A, B, or C)'] and i['Site_name'] == site for i in csv_file]
    B_truth_array = ['B' in i['Class (A, B, or C)'] and i['Site_name'] == site for i in csv_file]
    C_truth_array = ['C' in i['Class (A, B, or C)'] and i['Site_name'] == site for i in csv_file]
else:
    A_truth_array = ['A' in i['Class (A, B, or C)'] for i in csv_file]
    B_truth_array = ['B' in i['Class (A, B, or C)'] for i in csv_file]
    C_truth_array = ['C' in i['Class (A, B, or C)'] for i in csv_file]

fig = plt.figure(figsize=[8,6])
ax = plt.gca()

# ax.scatter(csv_file['Perimeter (km)'],csv_file['Major Axis (km)'],c=csv_file['Class (A, B, or C)'],s=20)
ax.plot(IC[A_truth_array],aspect_ratios[A_truth_array],marker='o',markersize=8,color='red',linestyle='None',label='A')
ax.plot(IC[B_truth_array],aspect_ratios[B_truth_array],marker='o',markersize=8,color='blue',linestyle='None',label='B')
ax.plot(IC[C_truth_array],aspect_ratios[C_truth_array],marker='o',markersize=8,color='green',linestyle='None',label='C')

ax.axvline(x=0.8,linestyle='--',color='black')
ax.legend(numpoints=1,fontsize=14)

ax.set_xlabel('Isoperimetric Circularity ($4\pi A/P^{2}$)',fontsize=18)
ax.set_ylabel('Aspect Ratio (b/a)',fontsize=18)
ax.set_xticks([0.5,0.6,0.7,0.8,0.9,1.0])
ax.set_xticklabels([0.5,0.6,0.7,0.8,0.9,1.0],fontsize=18)
ax.set_yticks([0,0.2,0.4,0.6,0.8,1.0])
ax.set_yticklabels([0,0.2,0.4,0.6,0.8,1.0],fontsize=18)
#
ax.set_ylim([0.1,1.1])
ax.set_xlim([0.5,1])

if not site=='Combined':
    plt.title('%s Site: Isoperimetric Circularity vs. Aspect Ratio'%site,fontsize=14)
else:
    plt.title('Isoperimetric Circularity vs. Aspect Ratio', fontsize=14)

plt.tight_layout()
plt.savefig('/Users/jaimearnold/Desktop/luna_codes_2020/ic_vs_aspect_ratio_%s.png'%site,bbox_inches='tight')
# plt.close(fig)
plt.show()


