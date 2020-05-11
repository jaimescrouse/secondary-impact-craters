import numpy as np
import matplotlib.pyplot as plt
from astropy.io import  ascii


#Loading the csv file
csv_file = ascii.read('/Users/jaimearnold/Desktop/luna_codes_2020/Crouse_combined_Jan3at258.csv')

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
ax.plot(csv_file['Perimeter (km)'][A_truth_array],csv_file['Major Axis (km)'][A_truth_array],marker='o',markersize=8,color='red',linestyle='None',label='A')
ax.plot(csv_file['Perimeter (km)'][B_truth_array],csv_file['Major Axis (km)'][B_truth_array],marker='o',markersize=8,color='blue',linestyle='None',label='B')
ax.plot(csv_file['Perimeter (km)'][C_truth_array],csv_file['Major Axis (km)'][C_truth_array],marker='o',markersize=8,color='green',linestyle='None',label='C')
ax.legend(numpoints=1,fontsize=14)

ax.set_xlabel('Perimeter (km)',fontsize=18)
ax.set_ylabel('Major Diameter (km)',fontsize=18)
ax.set_xticks([0,5,10,15,20,25])
ax.set_xticklabels([0,5,10,15,20,25],fontsize=18)
ax.set_yticks([0,2,4,6,8,10])
ax.set_yticklabels([0,2,4,6,8,10],fontsize=18)

ax.set_ylim([0,10])
if not site=='Combined':
    plt.title('%s Site: Perimeter vs. Major Diameter'%site,fontsize=14)
else:
    plt.title('Perimeter vs. Major Diameter', fontsize=14)

plt.tight_layout()
plt.savefig('/Users/jaimearnold/Desktop/luna_codes_2020/perimeter_vs_major_axis_%s.png'%site,bbox_inches='tight')
# plt.close(fig)
plt.show()



fig = plt.figure(figsize=[8,6])
ax = plt.gca()

# ax.scatter(csv_file['Perimeter (km)'],csv_file['Major Axis (km)'],c=csv_file['Class (A, B, or C)'],s=20)
ax.plot(csv_file['Major Axis (km)'][A_truth_array],csv_file['Minor Axis (km)'][A_truth_array],marker='o',markersize=8,color='red',linestyle='None',label='A')
ax.plot(csv_file['Major Axis (km)'][B_truth_array],csv_file['Minor Axis (km)'][B_truth_array],marker='o',markersize=8,color='blue',linestyle='None',label='B')
ax.plot(csv_file['Major Axis (km)'][C_truth_array],csv_file['Minor Axis (km)'][C_truth_array],marker='o',markersize=8,color='green',linestyle='None',label='C')

ax.plot(np.arange(0,15,1),np.arange(0,15,1),color='black',marker='None',linestyle='-')
ax.legend(numpoints=1,fontsize=14)

ax.set_xlabel('Major Diameter (km)',fontsize=18)
ax.set_ylabel('Minor Diameter (km)',fontsize=18)
ax.set_xticks([0,2,4,6,8,10])
ax.set_xticklabels([0,2,4,6,8,10],fontsize=18)
ax.set_yticks([0,2,4,6,8,10])
ax.set_yticklabels([0,2,4,6,8,10],fontsize=18)

ax.set_ylim([0,10])
ax.set_xlim([0,10])

if not site=='Combined':
    plt.title('%s Site: Minor vs. Major Diameter'%site,fontsize=14)
else:
    plt.title('Minor vs. Major Diameter', fontsize=14)

plt.tight_layout()
plt.savefig('/Users/jaimearnold/Desktop/luna_codes_2020/minor_vs_major_axis_%s.png'%site,bbox_inches='tight')
# plt.close(fig)
plt.show()

fig = plt.figure(figsize=[8,6])
ax = plt.gca()

# ax.scatter(csv_file['Perimeter (km)'],csv_file['Major Axis (km)'],c=csv_file['Class (A, B, or C)'],s=20)
ax.plot(csv_file['Perimeter (km)'][A_truth_array],csv_file['Minor Axis (km)'][A_truth_array],marker='o',markersize=8,color='red',linestyle='None',label='A')
ax.plot(csv_file['Perimeter (km)'][B_truth_array],csv_file['Minor Axis (km)'][B_truth_array],marker='o',markersize=8,color='blue',linestyle='None',label='B')
ax.plot(csv_file['Perimeter (km)'][C_truth_array],csv_file['Minor Axis (km)'][C_truth_array],marker='o',markersize=8,color='green',linestyle='None',label='C')
ax.legend(numpoints=1,fontsize=14)

ax.set_xlabel('Perimeter (km)',fontsize=18)
ax.set_ylabel('Minor Diameter (km)',fontsize=18)
ax.set_xticks([0,5,10,15,20,25])
ax.set_xticklabels([0,5,10,15,20,25],fontsize=18)
ax.set_yticks([0,2,4,6,8,10])
ax.set_yticklabels([0,2,4,6,8,10],fontsize=18)

ax.set_ylim([0,10])

if not site=='Combined':
    plt.title('%s Site: Perimeter vs. Minor Diameter'%site,fontsize=14)
else:
    plt.title('Perimeter vs. Minor Diameter', fontsize=14)

plt.tight_layout()
plt.savefig('/Users/jaimearnold/Desktop/luna_codes_2020/perimeter_vs_minor_axis_%s.png'%site,bbox_inches='tight')
# plt.close(fig)
plt.show()