# Landslide-spatial-modeling
This program is structed by three parts: data preparation, global application and analysis for landslide non-susceptibility, and could be run under the Grass GIS 7.6 or 7.8.

1.slope_relief_calculation.py was used to calculate local terrain slope (S) and regional relative relief (R) data based on ~90 m SRTM DEM data
(1) methodology in Marchesini et al. (2014) 
(2) SRTM data in Jarvis et al. 2008

References:
Marchesini, I., Ardizzone, F., Alvioli, M., Rossi, M., Guzzetti, F., 2014. Non-susceptible landslide areas in Italy and in the Mediterranean region. Nat. Hazards Earth Syst. Sci. 14, 2215–2231. https://doi.org/10.5194/nhess-14-2215-2014

Jarvis, A., Reuter, H., Nelson, A., Guevara, E., 2008. Hole-filled SRTM for the globe Version 4 [WWW Document]. CGIAR-CSI. URL http://srtm.csi.cgiar.org (accessed 3.1.21).

2.globe_analysis_map.py was used to calculate global landslide non-susceptibility maps based on four models. Three models are from Marchesini et al. (2014) and one is proposed by the authors based on global landslide catalog (Kirschbaum et al., 2015).

References:
Kirschbaum, D., Stanley, T., Zhou, Y., 2015. Spatial and temporal analysis of a global landslide catalog. Geomorphology 249, 4–15. https://doi.org/10.1016/j.geomorph.2015.03.016

Jia, G., Alvioli, M., Gariano, S., Guzzetti, F., Tang, Q., and Marchesini, I.: A Global Landslide Non-Susceptibility Map: variation and applicability, EGU General Assembly 2020, Online, 4–8 May 2020, EGU2020-15239, https://doi.org/10.5194/egusphere-egu2020-15239, 2020

3.zonal_stats.py was used to overlay global landslide non-susceptibility map with continents, climate zones, flood plains, susceptibility maps, populatiion and builtup maps. Summarized information was availalbe in Jia's PhD thesis, which is under review now. A journal paper is under deep review in Geomorphology. More details will be updated later utill the paper and thesis are available.

References:
Jia, G., Alvioli, M., Gariano, S., Guzzetti, F., Tang, Q., and Marchesini, I.: A Global Landslide Non-Susceptibility Map: variation and applicability, EGU General Assembly 2020, Online, 4–8 May 2020, EGU2020-15239, https://doi.org/10.5194/egusphere-egu2020-15239, 2020
