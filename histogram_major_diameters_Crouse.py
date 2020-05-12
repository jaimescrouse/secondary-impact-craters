'''
Measurements of each crater’s area, perimeter, major and minor axis to produce dimensionless shape parameters of aspect ratio 
and isoperimetric circularity. A statistical population to establish quantitative parameters for secondary crater shape in a 
2D data set was created and analyzed. The method to explicate these diversities include separating various crater shapes into 
three distinguishable categories: (A) highest continuous rim, (B) depressions interrupted by a convex arc from an overprinted 
crater (C) multi-basin cases containing complied features from category (A) and (B).

The long-term goal of this research is to provide a catalog of data that establishes the quantitative diversity of secondary 
impact craters to distinguish them from small primary impacts, small volcanic vents, and collapsed features found on the Moon
and Mars. 

This routine accepts the applicable data to analyze each class of secondary impact craters laid out in the methodology of this
project and generates a histogram of each site (proximal and distal) displaying the number of compound secondary impact crater 
features (combined) which can be described as a Class A feature with 1-3 B features (making it a Class C feature) and compares
this to the number of secondary impact crater features described as a Class A feature only (single).

Project Title:  DEFINING PARAMETERS FOR SECONDARY IMPACT CRATERS ON THE MOON
 Abstract: https://ui.adsabs.harvard.edu/abs/2020AAS...23516901C/abstract
 Publication: American Astronomical Society meeting #235, id. 169.01. 
              Bulletin of the American Astronomical Society, Vol. 52, No. 1
 Pub Date: January 2020
 Bibcode: 2020AAS...23516901C 
 
 Author: Jaime S. Crouse
 Email: jsazq8@mail.umkc.edu
 
 Co-author: Alison H. Graettinger
 Acknowledgements: Thank you to my research advisor and co-author, Dr. Alison H. Graettinger and
 to my graduate student mentor, Kameswara Bharadwaj Mantha (AgentM-GEG) for the support.  
'''



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

