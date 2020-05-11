import numpy as np
import matplotlib.pyplot as plt
from astropy.io import  ascii


#Loading the csv file
csv_file = ascii.read('/Users/jaimearnold/Desktop/luna_codes_2020/Crouse_combined_Jan3at258.csv')

truth_array_prox_single = ['A' in i['Class (A, B, or C)'] and 'Single' in i['Single/Combined'] and i['Site_name'] == 'Proximal' for i in csv_file]
truth_array_prox_comb = ['A' in i['Class (A, B, or C)'] and 'Combined' in i['Single/Combined'] and i['Site_name'] == 'Proximal' for i in csv_file]

truth_array_distal_single = ['A' in i['Class (A, B, or C)'] and 'Single' in i['Single/Combined'] and i['Site_name'] == 'Distal' for i in csv_file]
truth_array_distal_comb = ['A' in i['Class (A, B, or C)'] and 'Combined' in i['Single/Combined'] and i['Site_name'] == 'Distal' for i in csv_file]

# num_of_As = np.count_nonzero(['A' in i['Class (A, B, or C)'] in i['Class (A, B, or C)'] for i in csv_file])
# num_of_Cs = np.count_nonzero(['C' in i['Class (A, B, or C)'] in i['Class (A, B, or C)'] for i in csv_file])

fig = plt.figure(figsize=[8,6])
ax = plt.gca()

ax.hist(csv_file['Major Axis (km)'][truth_array_distal_single],bins=np.arange(0,11,1),histtype='step',label='Distal Site (Single)',color='Red')
ax.hist(csv_file['Major Axis (km)'][truth_array_distal_comb],bins=np.arange(0,11,1),histtype='step',label='Distal Site (Combined)',color='red',linestyle='--')

ax.hist(csv_file['Major Axis (km)'][truth_array_prox_single],bins=np.arange(0,11,1),histtype='step',label='Proximal Site (Single)',color='blue')
ax.hist(csv_file['Major Axis (km)'][truth_array_prox_comb],bins=np.arange(0,11,1),histtype='step',label='Proximal Site (Combined)',color='blue',linestyle='--')



# ax.text(0.8,0.7,'N(A) = %s'%int(num_of_As),fontsize=14,transform=ax.transAxes)
# ax.text(0.8,0.6,'N(C) = %s'%int(num_of_Cs),fontsize=14,transform=ax.transAxes)


ax.set_xticks([0,2,4,6,8,10])
ax.set_xticklabels([0,2,4,6,8,10],fontsize=18)

ax.set_yticks(np.arange(0,25,5))
ax.set_yticklabels(np.arange(0,25,5),fontsize=18)

ax.set_xlabel('Major Diameter (km)',fontsize=18)
ax.set_ylabel('Number', fontsize=18)
plt.legend(fontsize=16)
plt.tight_layout()
plt.savefig('/Users/jaimearnold/Desktop/luna_codes_2020/histogram_major_diameters.png',bbox_inches='tight')
plt.show()

