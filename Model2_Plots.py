# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:53:57 2024

@author: ragha
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

nH1array = np.array([0.736610,0.653137,0.692759,0.698754])
gamma1array = np.array([1.92082,1.89016,1.88735,1.90633])
covfrac1array = np.array([0.417263,0.414473,0.393787,0.467646])
Tin1array = np.array([0.281272,0.276305,0.281219,0.325635])
diskbbnorm1array = np.array([1.21952E+05,1.07050E+05,1.03832E+05,5.03833E+04])
relxillnorm1array = np.array([3.15237E-02,2.64967E-02,2.77548E-02,2.94469E-02])
unabslum1array = np.array([2.114462E+37,1.8356928E+37,1.85523957E+37,1.6741717E+37])
thlum1array = np.array([8.0112447E+36,6.434281E+36,6.69884609E+36,5.8519418E+36])
nonthlum1array = unabslum1array - thlum1array
obs1segments = [1,2,3,4]

nHerr1array = np.array([[0.0451714,0.0458714,0.04708,0.0462178],[0.0577325,0.109346,0.0722984,0.0640336]])
gammaerr1array = np.array([[0.0167758,0.0185176,0.0181629,0.0187581],[0.0167464,0.0181718,0.0178572,0.0181402]])
covfracerr1array = np.array([[0.045388,0.0699885,0.0494827,0.0466506],[0.0402476,0.046949,0.0430517,0.0403164]])
Tinerr1array = np.array([[0.0129056,0.0125232,0.0127293,0.0147855],[0.0116414,0.0128896,0.0134215,0.0152839]])
diskbbnormerr1array = np.array([[26696.1,26001.2,25173.3,11199.1],[44598.2,44982.9,37059.1,16011.4]])
relxillnormerr1array = np.array([[0.00496008,0.00452527,0.00447842,0.00467504],[0.00521258,0.00476537,0.00468187,0.00484596]])
unabslumerr1array = np.array([[1.002746E+36,9.18794E+35,8.960835E+35,5.720902E+35],[1.55925E+36,2.860855E+36,1.6591719E+36,8.7804332E+35]])
thlumerr1array = np.array([[7.401467E+35,6.399937E+35,6.482244E+35,4.51864233E+35],[9.6924455E+35,1.3156889E+36,5.3717793E+35,6.4037941E+35]])
nonthlumerr1array = unabslumerr1array + thlumerr1array

nH2array = np.array([0.746400,0.740193,0.746791,0.729700,0.860949])
gamma2array = np.array([2.04048,2.04375,2.04871,2.05949,2.07930])
covfrac2array = np.array([0.374899,0.421038,0.423171,0.439570,0.399878])
Tin2array = np.array([0.288080,0.318883,0.294796,0.318532,0.297649])
diskbbnorm2array = np.array([1.68391E+05,1.05359E+05,1.60453E+05,1.13449E+05,1.82150E+05])
relxillnorm2array = np.array([5.51076E-02,5.70217E-02,6.31024E-02,6.54580E-02,7.08314E-02])
unabslum2array = np.array([2.54859014E+37,2.4372495E+37,2.7258377E+37,2.58464E+37,3.093143E+37])
thlum2array = np.array([1.2003282E+37,1.12382839E+37,1.2508349E+37,1.205591E+37,1.488675E+37])
nonthlum2array = unabslum2array - thlum2array
obs2segments = [5,6,7,8,9]

nHerr2array = np.array([[0.0908605,0.0446488,0.0424242,0.0384733,0.0894546],[0.0810722,0.0547616,0.0554744,0.0463732,0.115494]])
gammaerr2array = np.array([[0.0194645,0.0196036,0.0188809,0.0189191,0.0180584],[0.0192472,0.0190809,0.0185125,0.0184067,0.0174686]])
covfracerr2array = np.array([[0.0411821,0.031886,0.0370694,0.0313375,0.0681551],[0.036487,0.0312621,0.0349778,0.0294743,0.0643769]])
Tinerr2array = np.array([[0.010526,0.0110908,0.0103832,0.012034,0.0187648],[0.0108714,0.0114689,0.0116303,0.0112528,0.0187648]])
diskbbnormerr2array = np.array([[35923.2,24517.7,32537.1,20402.8,62679.8],[49840.8,25239.7,41522.8,28644.7,103255]])
relxillnormerr2array = np.array([[0.00751153,0.00799335,0.00867335,0.00877792,0.00934279],[0.00825716,0.00857131,0.0093263,0.00939384,0.01011]])
unabslumerr2array = np.array([[1.924561E+36,1.18787E+36,1.4536069E+36,1.123462E+36,3.477786E+36],[4.101035E+36,1.8576077E+36,2.131651E+36,1.468528E+36,6.0343606E+36]])
thlumerr2array = np.array([[1.1290145E+36,7.781954E+35,1.0056438E+36,7.943126E+35,2.2306506E+36],[1.5798527E+36,1.0050586E+36,2.1316506E+36,9.817604E+35,2.941139E+36]])
nonthlumerr2array = unabslumerr2array + thlumerr2array

nH3array = np.array([0.772729,0.834494,0.668704,0.768331,0.844347,0.893326,0.898971])
gamma3array = np.array([1.96600,2.06250,1.94806,2.12134,2.10243,2.13203,2.12841])
covfrac3array = np.array([0.388926,0.431818,0.376099,0.611775,0.525864,0.629671,0.569012])
Tin3array = np.array([0.290817,0.302864,0.405269,0.345925,0.342126,0.306193,0.340819])
diskbbnorm3array = np.array([1.53406E+05,1.65385E+05,5.43173E+04,1.04832E+05,1.25408E+05,2.35056E+05,1.39169E+05])
relxillnorm3array = np.array([5.56949E-02,0.107443,6.51935E-02,0.154641,0.143650,0.193352,0.166729])
unabslum3array = np.array([2.715813857E+37,3.21292065E+37,3.565332188E+37,3.672823E+37,4.02346288E+37,5.10504999E+37,4.428942E+37])
thlum3array = np.array([1.128236122E+37,1.4203651E+37,1.513561248E+37,1.54988687E+37,1.773781E+37,2.13059E+37,1.9399923E+37])
nonthlum3array = unabslum3array - thlum3array
obs3segments = [10,11,12,13,14,15,16]

nHerr3array = np.array([[0.0390496,0.0441791,0.0143101,0.0355737,0.0349967,0.0355287,0.0329452],[0.0501444,0.0461047,0.0165375,0.0386151,0.0173783,0.0354283,0.0315097]])
gammaerr3array = np.array([[0.014125,0.0186696,0.0227939,0.0138934,0.0142938,0.0140154,0.0126927],[0.0140213,0.0166131,0.0215106,0.0134087,0.0151037,0.0130068,0.0138831]])
covfracerr3array = np.array([[0.0304137,0.028741,0.0209687,0.0300137,0.0244373,0.0370716,0.0240488],[0.0294728,0.0334741,0.0187016,0.0304083,0.026316,0.0380902,0.0262176]])
Tinerr3array = np.array([[0.00858005,0.00801283,0.00877634,0.0088815,0.00894532,0.0108812,0.0262176],[0.00880282,0.0107999,0.00881523,0.0101978,0.00471315,0.0110766,0.00858587]])
diskbbnormerr3array = np.array([[25190.3,30894.3,5623.94,14798.6,16749.7,43361.6,17460.8],[27060.3,30246.2,6816.62,17432.7,20059,46447.9,26098.8]])
relxillnormerr3array = np.array([[0.00622149,0.0119259,0.0112705,0.014711,0.0139493,0.0198166,0.015052],[0.0065761,0.0117815,0.011603,0.0156393,0.0161942,0.020457,0.0180808]])
unabslumerr3array = np.array([[1.15055516E+36,1.495468E+36,7.47328657E+35,1.04205512E+36,1.2044987E+36,1.7331196E+36,1.24667177E+36],[1.7819595E+36,2.13179073E+36,7.80103128E+35,1.06378074E+36,9.56149587E+35,1.8427192E+36,1.34578367E+36]])
thlumerr3array = np.array([[7.94184408E+35,9.7851971E+35,5.20572764E+35,7.1119023E+35,8.41183716E+35,1.25195234E+36,8.64606489E+35],[1.00900051E+36,1.17081332E+36,5.535558641E+35,7.82840703E+35,9.21689848E+35,1.40319836E+36,8.39587555E+35]])
nonthlumerr3array = unabslumerr3array + thlumerr3array


gabsflag = 1
if(gabsflag==0):
    obs1_powlawnormarray = np.array([5.27581E-04,5.30593E-04,5.25609E-04,5.33091E-04])
    obs1_lore1linearray = np.array([0.268403,0.268403,0.268403,0.268403])
    obs1_lore1normarray = np.array([6.08823E-02,6.12298E-02,6.06548E-02,6.15181E-02])
    obs1_lore2linearray = np.array([2.99969,2.99969,2.99969,2.99969])
    obs1_lore2normarray = np.array([4.34868E-02,4.37349E-02,4.33242E-02,4.39409E-02])

    obs1_powlawnormerrarray = np.array([[9.52402e-05,9.57838e-05,9.48843e-05,9.62348e-05],[8.97307e-05,9.02428e-05,8.93954e-05,9.06678e-05]])
    obs1_lore1lineerrarray = np.array([[0.0141251,0.0141251,0.0141251,0.0141251],[0.0132155,0.0132155,0.0132155,0.0132155]])
    obs1_lore1normerrarray = np.array([[0.00113714,0.00114363,0.00113289,0.00114901],[0.00113056,0.00113701,0.00112634,0.00114237]])
    obs1_lore2lineerrarray = np.array([[0.0797268,0.0797269,0.0797268,0.0797268],[0.0742272,0.0742272,0.0742272,0.0742272]])
    obs1_lore2normerrarray = np.array([[0.00202666,0.00203822,0.00201908,0.00204782],[0.00217293,0.00218533,0.00216481,0.00219562]])

else:
    obs1_gabslinearray = np.array([1.70637,1.70634,1.70634,1.70634])
    obs1_gabsstrengtharray = np.array([6.02831E-02,6.02782E-02,6.02782E-02,6.02782E-02])
    obs1_powlawnormarray = np.array([3.80322E-04,3.82484E-04,3.78893E-04,3.84286E-04])
    obs1_lore1linearray = np.array([0.255938,0.255939,0.255939,0.255939])
    obs1_lore1normarray = np.array([6.06095E-02,6.09553E-02,6.03830E-02,6.12424E-02])
    obs1_lore2linearray = np.array([2.80625,2.80626,2.80626,2.80626])
    obs1_lore2normarray = np.array([4.71948E-02,4.74641E-02,4.70184E-02,4.76877E-02])
    
    obs1_gabslineerrarray = np.array([[0.0226366,0.0226145,0.0226145,0.0226145],[0.0221646,0.0221974,0.0221974,0.0221974]])
    obs1_gabsstrengtherrarray = np.array([[0.0109654,0.0109631,0.0109631,0.0109631],[0.0120893,0.0120915,0.0120915,0.0120915]])
    obs1_powlawnormerrarray = np.array([[9.66265e-05,9.71759e-05,9.62633e-05,9.76335e-05],[8.97718e-05,9.02864e-05,8.94385e-05,9.07116e-05]])
    obs1_lore1lineerrarray = np.array([[0.0153744,0.0153742,0.0153742,0.0153742],[0.0141735,0.0141738,0.0141738,0.0141738]])
    obs1_lore1normerrarray = np.array([[0.00127921,0.0012866,0.00127451,0.00129266],[0.00127112,0.00127829,0.00126629,0.00128431]])
    obs1_lore2lineerrarray = np.array([[0.104246,0.104255,0.104255,0.104255],[0.0937931,0.0937848,0.0937848,0.0937848]])
    obs1_lore2normerrarray = np.array([[0.00230933,0.00232241,0.0023006,0.00233335],[0.00251631,0.00253075,0.00250699,0.00254267]])
    
obs2_powlawnormarray = np.array([3.09260E-04,2.46399E-04,1.04111E-04,6.35528E-05,4.50237E-09])
obs2_lore1linearray = np.array([0.442984,0.508447,0.431682,0.471258,0.420664])
obs2_lore1normarray = np.array([2.57883E-02,2.50749E-02,2.60496E-02,2.33206E-02,2.63511E-02])
obs2_lore2linearray = np.array([4.59075,4.77148,4.67200,4.86532,5.33077])
obs2_lore2normarray = np.array([1.52746E-02,1.58679E-02,1.62883E-02,1.60486E-02,1.56613E-02])

obs2_powlawnormerrarray = np.array([[0.000104481,0.000107887,0.000104219,6.35528e-05,1.35626e-11],[9.20398e-05,9.57799e-05,0.000100366,0.000191623,0.000158658]])
obs2_lore1lineerrarray = np.array([[0.0326861,0.0322899,0.0351783,0.0555046,0.0665769],[0.029728,0.0294849,0.0318698,0.0480231,0.0517288]])
obs2_lore1normerrarray = np.array([[0.000656395,0.00063053,0.000695331,0.000935073,0.000834093],[0.000654961,0.000632065,0.000690813,0.00093923,0.000856934]])
obs2_lore2lineerrarray = np.array([[0.0911254,0.0812433,0.106161,0.151088,0.143861],[0.0867362,0.0788786,0.0999145,0.141918,0.139476]])
obs2_lore2normerrarray = np.array([[0.00149496,0.00146983,0.00171594,0.00287576,0.00240744],[0.00174855,0.00171109,0.00199966,0.00145207,0.000462255]])

obs3_powlawnormarray = np.array([2.94285E-04,3.60560E-04,8.34496E-03,6.91736E-03,7.23063E-03,1.46333E-02,8.60991E-03]) 
obs3_lore1linearray = np.array([0.321724,0.492189,0.971673,1.17165,0.812999,1.15974,1.10842])
obs3_lore1normarray = np.array([2.96731E-02,2.65703E-02,1.46861E-02,1.45208E-02,1.49190E-02,1.80187E-02,1.52407E-02])
obs3_lore2linearray = np.array([3.78060,4.19477,4.97590,5.27705,4.68608,4.43687,5.36415])
obs3_lore2normarray = np.array([1.85163E-02,1.34740E-02,1.33748E-02,1.22789E-02,1.41612E-02,1.07614E-02,9.22467E-03])

obs3_powlawnormerrarray = np.array([[7.84956e-05,4.1516e-05,0.0013041,0.000990215,0.00165915,0.000599896,0.00071398],[7.23488e-05,0.00117746,0.00117746,0.000709095,0.00150473,0.000599355,0.000461988]]) 
obs3_lore1lineerrarray = np.array([[0.0303586,0.0228622,0.0887806,0.0812994,0.0797011,0.000599896,0.0513893],[0.0273721,0.0215619,0.0870193,0.0684207,0.0769257,0.000599355,0.171336]])
obs3_lore1normerrarray = np.array([[0.000850648,0.000521403,0.00372149,0.00261478,0.00260926,0.000302102,0.00467581],[0.000853879,0.000523218,0.00339887,0.00284712,0.00244982,0.000302083,0.00028895]])
obs3_lore2lineerrarray = np.array([[0.0865258,0.0502559,0.118261,0.123729,0.153032,0.115915,0.353714],[0.0827856,0.0496646,0.124503,0.126985,0.145331,0.114483,0.189131]])
obs3_lore2normerrarray = np.array([[0.0013176,0.000667318,0.00104384,0.000855662,0.000821357,0.000174231,0.000213721],[0.00144557,0.000709783,0.00104384,0.000653611,0.000799095,0.000174254,0.00148811]])


nH = np.concatenate((nH1array,nH2array,nH3array))
gamma = np.concatenate((gamma1array,gamma2array,gamma3array))
covfrac = np.concatenate((covfrac1array,covfrac2array,covfrac3array))
Tin = np.concatenate((Tin1array,Tin2array,Tin3array))
diskbbnorm = np.concatenate((diskbbnorm1array,diskbbnorm2array,diskbbnorm3array))
unabslum = np.concatenate((unabslum1array,unabslum2array,unabslum3array))
thlum = np.concatenate((thlum1array,thlum2array,thlum3array))
nonthlum = np.concatenate((nonthlum1array,nonthlum2array,nonthlum3array))
powlawnorm = np.concatenate((obs1_powlawnormarray,obs2_powlawnormarray,obs3_powlawnormarray))
lore1line = np.concatenate((obs1_lore1linearray,obs2_lore1linearray,obs3_lore1linearray))
lore1norm = np.concatenate((obs1_lore1normarray,obs2_lore1normarray,obs3_lore1normarray))
lore2line = np.concatenate((obs1_lore2linearray,obs2_lore2linearray,obs3_lore2linearray))
lore2norm = np.concatenate((obs1_lore2normarray,obs2_lore2normarray,obs3_lore2normarray))

def timevariation(obs1,obs2,obs3,array1,array2,array3,errarray1,errarray2,errarray3,plxlabel,plylabel,pltitle):
    plt.errorbar(obs1,array1,yerr=errarray1,color='red',fmt='*',label='March 20 2017')
    plt.errorbar(obs2,array2,yerr=errarray2,color='blue',fmt='*',label='March 31 2017')
    plt.errorbar(obs3,array3,yerr=errarray3,color='green',fmt='*',label='June 12 2019')
    plt.ylabel(plylabel,fontsize=8)
    plt.xlabel(plxlabel,fontsize=8)
    plt.title(pltitle,size=10)
    plt.legend()
    plt.show()


def paravariation(xarray1,xarray2,xarray3,yarray1,yarray2,yarray3,xerrarray1,xerrarray2,xerrarray3,yerrarray1,yerrarray2,yerrarray3,plxlabel,plylabel,pltitle):
    plt.errorbar(xarray1,yarray1,xerr=xerrarray1,yerr=yerrarray1,color='red',fmt='*',label='March 20 2017')
    plt.errorbar(xarray2,yarray2,xerr=xerrarray2,yerr=yerrarray2,color='blue',fmt='*',label='March 31 2017')
    plt.errorbar(xarray3,yarray3,xerr=xerrarray3,yerr=yerrarray3,color='green',fmt='*',label='June 12 2019')
    plt.xlabel(plxlabel,fontsize=8)
    plt.ylabel(plylabel,fontsize=8)
    plt.title(pltitle,size=10)
    plt.legend()
    plt.show()


def Spcorr(q1,q2):
    corr,Pval = sts.spearmanr(q1,q2)
    return corr,Pval


def Pearcorr(q1,q2):
    corr,Pval = sts.pearsonr(q1,q2)
    return corr,Pval

stef = 5.67 * 10**-8 
G = 6.674 * 10**-11
M = 21.2 * 1.989 * 10**30
costheta = np.cos(0.698132)

def calcMdot(disknorm,T):
    R = np.sqrt(disknorm/costheta) * 0.2 * 1000    
    Tk = T * 11604525.0061657
    mdot = 8 * np.pi * R**3 * stef * Tk**4 / (3 * G * M) * 1000
    print (R)
    return mdot/1e18


mdot1array = calcMdot(diskbbnorm1array,Tin1array) 
mdoterr1array = mdot1array * (1.5 * diskbbnormerr1array/diskbbnorm1array + 4 * Tinerr1array/Tin1array)    
mdot2array = calcMdot(diskbbnorm2array,Tin2array) 
mdoterr2array = mdot2array * (1.5 * diskbbnormerr2array/diskbbnorm2array + 4 * Tinerr2array/Tin2array)    
mdot3array = calcMdot(diskbbnorm3array,Tin3array) 
mdoterr3array = mdot3array * (1.5 * diskbbnormerr3array/diskbbnorm3array + 4 * Tinerr3array/Tin3array)    

mdot = np.concatenate((mdot1array,mdot2array,mdot3array))

#Hardness Ratio
hardness1array = nonthlum1array/thlum1array
hardness2array = nonthlum2array/thlum2array
hardness3array = nonthlum3array/thlum3array
hardnesserr1array = hardness1array * (nonthlumerr1array/nonthlum1array + thlumerr1array/thlum1array)
hardnesserr2array = hardness2array * (nonthlumerr2array/nonthlum2array + thlumerr2array/thlum2array)
hardnesserr3array = hardness3array * (nonthlumerr3array/nonthlum3array + thlumerr3array/thlum3array)

#Time Variation Plots
timevariation(obs1segments,obs2segments,obs3segments,nH1array,nH2array,nH3array,nHerr1array,nHerr2array,nHerr3array,'Observation Number','ISM Hydrogen Column Density (10^22 atoms cm^-2)','Variation of ISM Hydrogen Column Density ')
timevariation(obs1segments,obs2segments,obs3segments,gamma1array,gamma2array,gamma3array,gammaerr1array,gammaerr2array,gammaerr3array,'Observation Number','Thermal Comptonization Photon Index','Variation of Thermal Comptonization Photon Index ')
timevariation(obs1segments,obs2segments,obs3segments,covfrac1array,covfrac2array,covfrac3array,covfracerr1array,covfracerr2array,covfracerr3array,'Observation Number','Covering Fraction','Variation of Covering Fraction ')
timevariation(obs1segments,obs2segments,obs3segments,Tin1array,Tin2array,Tin3array,Tinerr1array,Tinerr2array,Tinerr3array,'Observation Number','Disk Temperature (keV)','Variation of Disk Temperature ')
timevariation(obs1segments,obs2segments,obs3segments,diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,'Observation Number','Disk Normalization','Variation of Disk Black Body Normalization ')
timevariation(obs1segments,obs2segments,obs3segments,unabslum1array,unabslum2array,unabslum3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Observation Number','Unabsorbed Total Luminsoity (erg/s)','Variation of Unabsorbed Total Luminosity ')
timevariation(obs1segments,obs2segments,obs3segments,thlum1array,thlum2array,thlum3array,thlumerr1array,thlumerr2array,thlumerr3array,'Observation Number','Thermal Luminosity (erg/s)','Variation of Thermal Luminosity ')
timevariation(obs1segments,obs2segments,obs3segments,nonthlum1array,nonthlum2array,nonthlum3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Observation Number','Non Thermal Luminosity','Variation of Non Thermal Luminosity ')
timevariation(obs1segments,obs2segments,obs3segments,mdot1array,mdot2array,mdot3array,mdoterr1array,mdoterr2array,mdoterr3array,'Observation Number','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Black Hole Mass Accretion Rate ')
timevariation(obs1segments,obs2segments,obs3segments,hardness1array,hardness2array,hardness3array,hardnesserr1array,hardnesserr2array,hardnesserr3array,'Observation Number','Hardness Ratio','Variation of Hardness Ratio ')

#nH with other parameters
paravariation(nH1array,nH2array,nH3array,gamma1array,gamma2array,gamma3array,nHerr1array,nHerr2array,nHerr3array,gammaerr1array,gammaerr2array,gammaerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Thermal Comptonization Photon Index','Variation of ISM Hydrogen Column Density with Thermal Comptonization Photon Index ')
paravariation(nH1array,nH2array,nH3array,covfrac1array,covfrac2array,covfrac3array,nHerr1array,nHerr2array,nHerr3array,covfracerr1array,covfracerr2array,covfracerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Covering Fraction','Variation of ISM Hydrogen Column Density with Covering Fraction ')
paravariation(nH1array,nH2array,nH3array,Tin1array,Tin2array,Tin3array,nHerr1array,nHerr2array,nHerr3array,Tinerr1array,Tinerr2array,Tinerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Disk Temperature (keV)','Variation of ISM Hydrogen Column Density with Disk Temperature ')
paravariation(nH1array,nH2array,nH3array,diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,nHerr1array,nHerr2array,nHerr3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Disk Black Body Normalization','Variation of ISM Hydrogen Column Density with Disk Normalization ')
paravariation(nH1array,nH2array,nH3array,unabslum1array,unabslum2array,unabslum3array,nHerr1array,nHerr2array,nHerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Unabsorbed Total Luminosity (erg/s)','Variation of ISM Hydrogen Column Density with Unabsorbed Total Luminosity ')
paravariation(nH1array,nH2array,nH3array,thlum1array,thlum2array,thlum3array,nHerr1array,nHerr2array,nHerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Thermal Luminosity (erg/s)','Variation of ISM Hydrogen Column Density with Thermal Luminosity ')
paravariation(nH1array,nH2array,nH3array,nonthlum1array,nonthlum2array,nonthlum3array,nHerr1array,nHerr2array,nHerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Non Thermal Luminosity (erg/s)','Variation of ISM Hydrogen Column Density with Non Thermal Luminosity ')
paravariation(nH1array,nH2array,nH3array,mdot1array,mdot2array,mdot3array,nHerr1array,nHerr2array,nHerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of ISM Hydrogen Column Density with Black Hole Mass Accretion Rate ')

#gamma with other parameters
paravariation(gamma1array,gamma2array,gamma3array,covfrac1array,covfrac2array,covfrac3array,gammaerr1array,gammaerr2array,gammaerr3array,covfracerr1array,covfracerr2array,covfracerr3array,'Thermal Comptonization Photon Index','Covering Fraction','Variation of Thermal Comptonization Photon Index with Covering Fraction ')
paravariation(gamma1array,gamma2array,gamma3array,Tin1array,Tin2array,Tin3array,gammaerr1array,gammaerr2array,gammaerr3array,Tinerr1array,Tinerr2array,Tinerr3array,'Thermal Comptonization Photon Index','Disk Temperature (keV)','Variation of Thermal Comptonization Photon Index with Disk Temperature ')
paravariation(gamma1array,gamma2array,gamma3array,diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,gammaerr1array,gammaerr2array,gammaerr3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,'Thermal Comptonization Photon Index','Disk Black Body Normalization','Variation of Thermal Comptonization Photon Index with Disk Black Body Normalization ')
paravariation(gamma1array,gamma2array,gamma3array,unabslum1array,unabslum2array,unabslum3array,gammaerr1array,gammaerr2array,gammaerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Thermal Comptonization Photon Index','Unabsorbed Total Luminosity (erg/s)','Variation of Thermal Comptonization Photon Index with Unabsorbed Total Luminosity ')
paravariation(gamma1array,gamma2array,gamma3array,thlum1array,thlum2array,thlum3array,gammaerr1array,gammaerr2array,gammaerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Thermal Comptonization Photon Index','Thermal Luminosity (erg/s)','Variation of Thermal Comptonization Photon Index with Thermal Luminosity ')
paravariation(gamma1array,gamma2array,gamma3array,nonthlum1array,nonthlum2array,nonthlum3array,gammaerr1array,gammaerr2array,gammaerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Thermal Comptonization Photon Index','Non Thermal Luminosity (erg/s)','Variation of Thermal Comptonization Photon Index with Non Thermal Luminosity ')
paravariation(gamma1array,gamma2array,gamma3array,mdot1array,mdot2array,mdot3array,gammaerr1array,gammaerr2array,gammaerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Thermal Comptonization Photon Index','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Thermal Comptonization Photon Index with Black Hole Mass Accretion Rate ')

#covfrac with other parameters
paravariation(covfrac1array,covfrac2array,covfrac3array,Tin1array,Tin2array,Tin3array,covfracerr1array,covfracerr2array,covfracerr3array,Tinerr1array,Tinerr2array,Tinerr3array,'Covering Fraction','Disk Temperature (keV)','Variation of Covering Fraction with Disk Temperature ')
paravariation(covfrac1array,covfrac2array,covfrac3array,diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,covfracerr1array,covfracerr2array,covfracerr3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,'Covering Fraction','Disk Black Body Normalization','Variation of Covering Fraction with Disk Black Body Normalization ')
paravariation(covfrac1array,covfrac2array,covfrac3array,unabslum1array,unabslum2array,unabslum3array,covfracerr1array,covfracerr2array,covfracerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Covering Fraction','Total Unabsorbed Luminosity (erg/s)','Variation of Covering Fraction with Total Unabsorbed Luminosity ')
paravariation(covfrac1array,covfrac2array,covfrac3array,thlum1array,thlum2array,thlum3array,covfracerr1array,covfracerr2array,covfracerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Covering Fraction','Thermal Luminosity (erg/s)','Variation of Covering Fraction with Thermal Luminosity ')
paravariation(covfrac1array,covfrac2array,covfrac3array,nonthlum1array,nonthlum2array,nonthlum3array,covfracerr1array,covfracerr2array,covfracerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Covering Fraction','Non Thermal Luminosity (erg/s)','Variation of Covering Fraction with Non Thermal Luminosity ')
paravariation(covfrac1array,covfrac2array,covfrac3array,mdot1array,mdot2array,mdot3array,covfracerr1array,covfracerr2array,covfracerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Covering Fraction','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Covering Fraction with Black Hole Mass Accretion Rate ')

#Tin with other parameters
paravariation(Tin1array,Tin2array,Tin3array,diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,Tinerr1array,Tinerr2array,Tinerr3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,'Disk Temperature (keV)','Disk Black Body Normalization','Variation of Disk Temperature with Disk Black Body Normalization ')
paravariation(Tin1array,Tin2array,Tin3array,unabslum1array,unabslum2array,unabslum3array,Tinerr1array,Tinerr2array,Tinerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Disk Temperature (keV)','Total Unabsorbed Luminosity (erg/s)','Variation of Disk Temperature with Total Unabsorbed Luminosity ')
paravariation(Tin1array,Tin2array,Tin3array,thlum1array,thlum2array,thlum3array,Tinerr1array,Tinerr2array,Tinerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Disk Temperature (keV)','Thermal Luminosity (erg/s)','Variation of Disk Temperature with Thermal Luminosity ')
paravariation(Tin1array,Tin2array,Tin3array,nonthlum1array,nonthlum2array,nonthlum3array,Tinerr1array,Tinerr2array,Tinerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Disk Temperature (keV)','Non Thermal Luminosity (erg/s)','Variation of Disk Temperature with Non Thermal Luminosity ')
paravariation(Tin1array,Tin2array,Tin3array,mdot1array,mdot2array,mdot3array,Tinerr1array,Tinerr2array,Tinerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Disk Temperature (keV)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Disk Temperature with Black Hole Mass Accretion Rate ')

#Diskbb norm with other parameters
paravariation(diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,unabslum1array,unabslum2array,unabslum3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Disk Black Body Normalization','Total Unabsorbed Luminosity (erg/s)','Variation of Disk Black Body Normalization with Total Unabsorbed Luminosity ')
paravariation(diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,thlum1array,thlum2array,thlum3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Disk Black Body Normalization','Thermal Luminosity (erg/s)','Variation of Disk Black Body Normalization with Thermal Luminosity ')
paravariation(diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,nonthlum1array,nonthlum2array,nonthlum3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Disk Black Body Normalization','Non Thermal Luminosity (erg/s)','Variation of Disk Black Body Normalization with Non Thermal Luminosity ')
paravariation(diskbbnorm1array,diskbbnorm2array,diskbbnorm3array,mdot1array,mdot2array,mdot3array,diskbbnormerr1array,diskbbnormerr2array,diskbbnormerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Disk Black Body Normalization','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Disk Black Body Normalization with Black Hole Mass Accretion Rate ')

#Total Unabsorbed Luminosity with other parameters
paravariation(unabslum1array,unabslum2array,unabslum3array,thlum1array,thlum2array,thlum3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Total Unabsorbed Luminosity (erg/s)','Thermal Luminosity (erg/s)','Variation of Total Unabsorbed Luminosity with Thermal Luminosity ')
paravariation(unabslum1array,unabslum2array,unabslum3array,nonthlum1array,nonthlum2array,nonthlum3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Total Unabsorbed Luminosity (erg/s)','Non Thermal Luminosity (erg/s)','Variation of Total Unabsorbed Luminosity with Non Thermal Luminosity ')
paravariation(unabslum1array,unabslum2array,unabslum3array,mdot1array,mdot2array,mdot3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Total Unabsorbed Luminosity (erg/s)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Total Unabsorbed Luminosity with Black Hole Mass Accretion Rate ')

#Thermal Luminosity with other parameters
paravariation(thlum1array,thlum2array,thlum3array,nonthlum1array,nonthlum2array,nonthlum3array,thlumerr1array,thlumerr2array,thlumerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Thermal Luminosity (erg/s)','Non Thermal Luminosity (erg/s)','Variation of Thermal Luminosity with Non Thermal Luminosity ')
paravariation(thlum1array,thlum2array,thlum3array,mdot1array,mdot2array,mdot3array,thlumerr1array,thlumerr2array,thlumerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Thermal Luminosity (erg/s)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Thermal Luminosity with Black Hole Mass Accretion Rate ')

#Non Thermal with mass accretion rate
paravariation(nonthlum1array,nonthlum2array,nonthlum3array,mdot1array,mdot2array,mdot3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Non Thermal Luminosity (erg/s)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Non Thermal Luminosity with Black Hole Mass Accretion Rate ')

#Correlation Coefficients
#nH with other parameters
Pear_nHgammaCorr,Pear_nHgammaPval = Pearcorr(nH,gamma)
Pear_nHcovCorr,Pear_nHcovPval = Pearcorr(nH,covfrac)
Pear_nHTinCorr,Pear_nHTinPval = Pearcorr(nH,Tin)
Pear_nHdiskbbCorr,Pear_nHdiskbbPval = Pearcorr(nH,diskbbnorm)
Pear_nHlumCorr,Pear_nHlumPval = Pearcorr(nH,unabslum)
Pear_nHthlumCorr,Pear_nHthlumPval = Pearcorr(nH,thlum)
Pear_nHnonthlumCorr,Pear_nHnonthlumPval = Pearcorr(nH,nonthlum)
Pear_nHmdotCorr,Pear_nHmdotPval = Pearcorr(nH,mdot)

#gamma with other parameters
Pear_gammacovCorr,Pear_gammacovPval = Pearcorr(gamma,covfrac)
Pear_gammaTinCorr,Pear_gammaTinPval = Pearcorr(gamma,Tin)
Pear_gammadiskbbCorr,Pear_gammadiskbbPval = Pearcorr(gamma,diskbbnorm)
Pear_gammalumCorr,Pear_gammalumPval = Pearcorr(gamma,unabslum)
Pear_gammathlumCorr,Pear_gammathlumPval = Pearcorr(gamma,thlum)
Pear_gammanonthlumCorr,Pear_gammanonthlumPval = Pearcorr(gamma,nonthlum)
Pear_gammamdotCorr,Pear_gammamdotPval = Pearcorr(gamma,mdot)

#covfrac with other parameters
Pear_covTinCorr, Pear_covTinPval = Pearcorr(covfrac,Tin) 
Pear_covdiskbbCorr, Pear_covdiskbbPval = Pearcorr(covfrac,diskbbnorm) 
Pear_covlumCorr, Pear_covlumPval = Pearcorr(covfrac,unabslum) 
Pear_covthlumCorr, Pear_covthlumPval = Pearcorr(covfrac,thlum) 
Pear_covnonthlumCorr, Pear_covnonthlumPval = Pearcorr(covfrac,nonthlum) 
Pear_covmdotCorr, Pear_covmdotPval = Pearcorr(covfrac,mdot)

#Tin with other parameters
Pear_TindiskbbCorr, Pear_TindiskbbPval = Pearcorr(Tin, diskbbnorm)
Pear_TinlumCorr, Pear_TinlumPval = Pearcorr(Tin, unabslum)
Pear_TinthlumCorr, Pear_TinthlumPval = Pearcorr(Tin, thlum)
Pear_TinnonthlumCorr, Pear_TinnonthlumPval = Pearcorr(Tin, nonthlum)
Pear_TinmdotCorr, Pear_TinmdotPval = Pearcorr(Tin, mdot)

#diskbbnorm with other parameters
Pear_diskbblumCorr, Pear_diskbblumPval = Pearcorr(diskbbnorm, unabslum)
Pear_diskbbthlumCorr, Pear_diskbbthlumPval = Pearcorr(diskbbnorm, thlum)
Pear_diskbbnonthlumCorr, Pear_diskbbnonthlumPval = Pearcorr(diskbbnorm, nonthlum)
Pear_diskbbmdotCorr, Pear_diskbbmdotPval = Pearcorr(diskbbnorm, mdot)

#Total unabsorbed luminosity with other parameters
Pear_lumthlumCorr, Pear_lumthlumPval = Pearcorr(unabslum, thlum)
Pear_lumnonthlumCorr, Pear_lumnonthlumPval = Pearcorr(unabslum, nonthlum)
Pear_lummdotCorr, Pear_lummdotPval = Pearcorr(unabslum, mdot)

#Thermal luminosity with other parameters
Pear_thlumnonthlumCorr, Pear_thlumnonthlumPval = Pearcorr(thlum, nonthlum)
Pear_thlummdotCorr, Pear_thlummdotPval = Pearcorr(thlum, mdot)

#Non Thermal Luminosity with black hole mass accretion rate
Pear_nonthlummdotCorr, Pear_nonthlummdotPval = Pearcorr(nonthlum, mdot)

#Spearman Correlations
# nH with other parameters
Sp_nHgammaCorr, Sp_nHgammaPval = Spcorr(nH, gamma)
Sp_nHcovCorr, Sp_nHcovPval = Spcorr(nH, covfrac)
Sp_nHTinCorr, Sp_nHTinPval = Spcorr(nH, Tin)
Sp_nHdiskbbCorr, Sp_nHdiskbbPval = Spcorr(nH, diskbbnorm)
Sp_nHlumCorr, Sp_nHlumPval = Spcorr(nH, unabslum)
Sp_nHthlumCorr, Sp_nHthlumPval = Spcorr(nH, thlum)
Sp_nHnonthlumCorr, Sp_nHnonthlumPval = Spcorr(nH, nonthlum)
Sp_nHmdotCorr, Sp_nHmdotPval = Spcorr(nH, mdot)

# gamma with other parameters
Sp_gammacovCorr, Sp_gammacovPval = Spcorr(gamma, covfrac)
Sp_gammaTinCorr, Sp_gammaTinPval = Spcorr(gamma, Tin)
Sp_gammadiskbbCorr, Sp_gammadiskbbPval = Spcorr(gamma, diskbbnorm)
Sp_gammalumCorr, Sp_gammalumPval = Spcorr(gamma, unabslum)
Sp_gammathlumCorr, Sp_gammathlumPval = Spcorr(gamma, thlum)
Sp_gammanonthlumCorr, Sp_gammanonthlumPval = Spcorr(gamma, nonthlum)
Sp_gammamdotCorr, Sp_gammamdotPval = Spcorr(gamma, mdot)

# covfrac with other parameters
Sp_covTinCorr, Sp_covTinPval = Spcorr(covfrac, Tin)
Sp_covdiskbbCorr, Sp_covdiskbbPval = Spcorr(covfrac, diskbbnorm)
Sp_covlumCorr, Sp_covlumPval = Spcorr(covfrac, unabslum)
Sp_covthlumCorr, Sp_covthlumPval = Spcorr(covfrac, thlum)
Sp_covnonthlumCorr, Sp_covnonthlumPval = Spcorr(covfrac, nonthlum)
Sp_covmdotCorr, Sp_covmdotPval = Spcorr(covfrac, mdot)

# Tin with other parameters
Sp_TindiskbbCorr, Sp_TindiskbbPval = Spcorr(Tin, diskbbnorm)
Sp_TinlumCorr, Sp_TinlumPval = Spcorr(Tin, unabslum)
Sp_TinthlumCorr, Sp_TinthlumPval = Spcorr(Tin, thlum)
Sp_TinnonthlumCorr, Sp_TinnonthlumPval = Spcorr(Tin, nonthlum)
Sp_TinmdotCorr, Sp_TinmdotPval = Spcorr(Tin, mdot)

# diskbbnorm with other parameters
Sp_diskbblumCorr, Sp_diskbblumPval = Spcorr(diskbbnorm, unabslum)
Sp_diskbbthlumCorr, Sp_diskbbthlumPval = Spcorr(diskbbnorm, thlum)
Sp_diskbbnonthlumCorr, Sp_diskbbnonthlumPval = Spcorr(diskbbnorm, nonthlum)
Sp_diskbbmdotCorr, Sp_diskbbmdotPval = Spcorr(diskbbnorm, mdot)

# Total unabsorbed luminosity with other parameters
Sp_lumthlumCorr, Sp_lumthlumPval = Spcorr(unabslum, thlum)
Sp_lumnonthlumCorr, Sp_lumnonthlumPval = Spcorr(unabslum, nonthlum)
Sp_lummdotCorr, Sp_lummdotPval = Spcorr(unabslum, mdot)

# Thermal luminosity with other parameters
Sp_thlumnonthlumCorr, Sp_thlumnonthlumPval = Spcorr(thlum, nonthlum)
Sp_thlummdotCorr, Sp_thlummdotPval = Spcorr(thlum, mdot)

# Non Thermal Luminosity with black hole mass accretion rate
Sp_nonthlummdotCorr, Sp_nonthlummdotPval = Spcorr(nonthlum, mdot)

#Variation of power law normalization with spectral parameters
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, nH1array, nH2array, nH3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, nHerr1array, nHerr2array, nHerr3array, 'Power Law Normalization', 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Variation of Power Law Normalization with ISM Hydrogen Column Density ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, covfrac1array, covfrac2array, covfrac3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, covfracerr1array, covfracerr2array, covfracerr3array, 'Power Law Normalization', 'Covering Fraction', 'Variation of Power Law Normalization with Covering Fraction ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, gamma1array, gamma2array, gamma3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, gammaerr1array, gammaerr2array, gammaerr3array, 'Power Law Normalization', 'Thermal Comptonization Photon Index', 'Variation of Power Law Normalization with Thermal Comptonization Photon Index ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, Tin1array, Tin2array, Tin3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, Tinerr1array, Tinerr2array, Tinerr3array, 'Power Law Normalization', 'Disk Temperature (keV)', 'Variation of Power Law Normalization with Disk Temperature ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, diskbbnorm1array, diskbbnorm2array, diskbbnorm3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, diskbbnormerr1array, diskbbnormerr2array, diskbbnormerr3array, 'Power Law Normalization', 'Diskbb Normalization', 'Variation of Power Law Normalization with Diskbb Normalization ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, unabslum1array, unabslum2array, unabslum3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, 'Power Law Normalization', 'Unabsorbed Total Luminosity (erg/s)', 'Variation of Power Law Normalization with Unabsorbed Total Luminosity ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, thlum1array, thlum2array, thlum3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, thlumerr1array, thlumerr2array, thlumerr3array, 'Power Law Normalization', 'Thermal Luminosity (erg/s)', 'Variation of Power Law Normalization with Thermal Luminosity ')
paravariation(obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, nonthlum1array, nonthlum2array, nonthlum3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, 'Power Law Normalization', 'Non-Thermal Luminosity (erg/s)', 'Variation of Power Law Normalization with Non-Thermal Luminosity ')

#Variation of lorentzian 1 line frequency with spectral parameters
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, nH1array, nH2array, nH3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, nHerr1array, nHerr2array, nHerr3array, 'Lorentzian 1 Line Frequency', 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Variation of Lorentzian 1 Line Frequency with ISM Hydrogen Column Density ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, covfrac1array, covfrac2array, covfrac3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, covfracerr1array, covfracerr2array, covfracerr3array, 'Lorentzian 1 Line Frequency', 'Covering Fraction', 'Variation of Lorentzian 1 Line Frequency with Covering Fraction ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, gamma1array, gamma2array, gamma3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, gammaerr1array, gammaerr2array, gammaerr3array, 'Lorentzian 1 Line Frequency', 'Thermal Comptonization Photon Index', 'Variation of Lorentzian 1 Line Frequency with Thermal Comptonization Photon Index ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, Tin1array, Tin2array, Tin3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, Tinerr1array, Tinerr2array, Tinerr3array, 'Lorentzian 1 Line Frequency', 'Disk Temperature (keV)', 'Variation of Lorentzian 1 Line Frequency with Disk Temperature ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, diskbbnorm1array, diskbbnorm2array, diskbbnorm3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, diskbbnormerr1array, diskbbnormerr2array, diskbbnormerr3array, 'Lorentzian 1 Line Frequency', 'Diskbb Normalization', 'Variation of Lorentzian 1 Line Frequency with Diskbb Normalization ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, unabslum1array, unabslum2array, unabslum3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, 'Lorentzian 1 Line Frequency', 'Unabsorbed Total Luminosity (erg/s)', 'Variation of Lorentzian 1 Line Frequency with Unabsorbed Total Luminosity ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, thlum1array, thlum2array, thlum3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, thlumerr1array, thlumerr2array, thlumerr3array, 'Lorentzian 1 Line Frequency', 'Thermal Luminosity (erg/s)', 'Variation of Lorentzian 1 Line Frequency with Thermal Luminosity ')
paravariation(obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, 'Lorentzian 1 Line Frequency', 'Non-Thermal Luminosity (erg/s)', 'Variation of Lorentzian 1 Line Frequency with Non-Thermal Luminosity ')

#Variation of lore1 normalization with spectral parameters
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, nH1array, nH2array, nH3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, nHerr1array, nHerr2array, nHerr3array, 'Lorentzian 1 Normalization', 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Variation of Lorentzian 1 Normalization with ISM Hydrogen Column Density ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, covfrac1array, covfrac2array, covfrac3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, covfracerr1array, covfracerr2array, covfracerr3array, 'Lorentzian 1 Normalization', 'Covering Fraction', 'Variation of Lorentzian 1 Normalization with Covering Fraction ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, gamma1array, gamma2array, gamma3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, gammaerr1array, gammaerr2array, gammaerr3array, 'Lorentzian 1 Normalization', 'Thermal Comptonization Photon Index', 'Variation of Lorentzian 1 Normalization with Thermal Comptonization Photon Index ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, Tin1array, Tin2array, Tin3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, Tinerr1array, Tinerr2array, Tinerr3array, 'Lorentzian 1 Normalization', 'Disk Temperature (keV)', 'Variation of Lorentzian 1 Normalization with Disk Temperature ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, diskbbnorm1array, diskbbnorm2array, diskbbnorm3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, diskbbnormerr1array, diskbbnormerr2array, diskbbnormerr3array, 'Lorentzian 1 Normalization', 'Diskbb Normalization', 'Variation of Lorentzian 1 Normalization with Diskbb Normalization ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, unabslum1array, unabslum2array, unabslum3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, 'Lorentzian 1 Normalization', 'Unabsorbed Total Luminosity (erg/s)', 'Variation of Lorentzian 1 Normalization with Unabsorbed Total Luminosity ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, thlum1array, thlum2array, thlum3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, thlumerr1array, thlumerr2array, thlumerr3array, 'Lorentzian 1 Normalization', 'Thermal Luminosity (erg/s)', 'Variation of Lorentzian 1 Normalization with Thermal Luminosity ')
paravariation(obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, 'Lorentzian 1 Normalization', 'Non-Thermal Luminosity (erg/s)', 'Variation of Lorentzian 1 Normalization with Non-Thermal Luminosity ')

#Variation of lore2 line frequency with spectral parameters
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, nH1array, nH2array, nH3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, nHerr1array, nHerr2array, nHerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Variation of Lorentzian 2 Line Frequency with ISM Hydrogen Column Density ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, covfrac1array, covfrac2array, covfrac3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, covfracerr1array, covfracerr2array, covfracerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Covering Fraction', 'Variation of Lorentzian 2 Line Frequency with Covering Fraction ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, gamma1array, gamma2array, gamma3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, gammaerr1array, gammaerr2array, gammaerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Thermal Comptonization Photon Index', 'Variation of Lorentzian 2 Line Frequency with Thermal Comptonization Photon Index ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, Tin1array, Tin2array, Tin3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, Tinerr1array, Tinerr2array, Tinerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Disk Temperature (keV)', 'Variation of Lorentzian 2 Line Frequency with Disk Temperature ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, diskbbnorm1array, diskbbnorm2array, diskbbnorm3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, diskbbnormerr1array, diskbbnormerr2array, diskbbnormerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Diskbb Normalization', 'Variation of Lorentzian 2 Line Frequency with Diskbb Normalization ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, unabslum1array, unabslum2array, unabslum3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Unabsorbed Total Luminosity (erg/s)', 'Variation of Lorentzian 2 Line Frequency with Unabsorbed Total Luminosity ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, thlum1array, thlum2array, thlum3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, thlumerr1array, thlumerr2array, thlumerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Thermal Luminosity (erg/s)', 'Variation of Lorentzian 2 Line Frequency with Thermal Luminosity ')
paravariation(obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, 'Lorentzian 2 Line Frequency (Hz)', 'Non-Thermal Luminosity (erg/s)', 'Variation of Lorentzian 2 Line Frequency with Non-Thermal Luminosity ')

#Variation of lore2 normalization with spectral parameters
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, nH1array, nH2array, nH3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, nHerr1array, nHerr2array, nHerr3array, 'Lorentzian 2 Normalization', 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Variation of Lorentzian 2 Normalization with ISM Hydrogen Column Density ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, covfrac1array, covfrac2array, covfrac3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, covfracerr1array, covfracerr2array, covfracerr3array, 'Lorentzian 2 Normalization', 'Covering Fraction', 'Variation of Lorentzian 2 Normalization with Covering Fraction ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, gamma1array, gamma2array, gamma3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, gammaerr1array, gammaerr2array, gammaerr3array, 'Lorentzian 2 Normalization', 'Thermal Comptonization Photon Index', 'Variation of Lorentzian 2 Normalization with Thermal Comptonization Photon Index ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, Tin1array, Tin2array, Tin3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, Tinerr1array, Tinerr2array, Tinerr3array, 'Lorentzian 2 Normalization', 'Disk Temperature (keV)', 'Variation of Lorentzian 2 Normalization with Disk Temperature ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, diskbbnorm1array, diskbbnorm2array, diskbbnorm3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, diskbbnormerr1array, diskbbnormerr2array, diskbbnormerr3array, 'Lorentzian 2 Normalization', 'Diskbb Normalization', 'Variation of Lorentzian 2 Normalization with Diskbb Normalization ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, unabslum1array, unabslum2array, unabslum3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, 'Lorentzian 2 Normalization', 'Unabsorbed Total Luminosity (erg/s)', 'Variation of Lorentzian 2 Normalization with Unabsorbed Total Luminosity ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, thlum1array, thlum2array, thlum3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, thlumerr1array, thlumerr2array, thlumerr3array, 'Lorentzian 2 Normalization', 'Thermal Luminosity (erg/s)', 'Variation of Lorentzian 2 Normalization with Thermal Luminosity ')
paravariation(obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, 'Lorentzian 2 Normalization', 'Non-Thermal Luminosity (erg/s)', 'Variation of Lorentzian 2 Normalization with Non-Thermal Luminosity ')


#Pearson Correlation Coefficients
#nH with other timing parameters
Pear_nHpowlawnormCorr, Pear_nHpowlawnormPval = Pearcorr(nH, powlawnorm)
Pear_nHlore1lineCorr, Pear_nHlore1linePval = Pearcorr(nH, lore1line)
Pear_nHlore2lineCorr, Pear_nHlore2linePval = Pearcorr(nH, lore2line)
Pear_nHlore1normCorr, Pear_nHlore1normPval = Pearcorr(nH, lore1norm)
Pear_nHlore2normCorr, Pear_nHlore2normPval = Pearcorr(nH, lore2norm)

#gamma with other timing parameters
Pear_gammaPowlawnormCorr, Pear_gammaPowlawnormPval = Pearcorr(gamma, powlawnorm)
Pear_gammaLore1lineCorr, Pear_gammaLore1linePval = Pearcorr(gamma, lore1line)
Pear_gammaLore2lineCorr, Pear_gammaLore2linePval = Pearcorr(gamma, lore2line)
Pear_gammaLore1normCorr, Pear_gammaLore1normPval = Pearcorr(gamma, lore1norm)
Pear_gammaLore2normCorr, Pear_gammaLore2normPval = Pearcorr(gamma, lore2norm)

#covfrac with other timing parameters
Pear_covfracPowlawnormCorr, Pear_covfracPowlawnormPval = Pearcorr(covfrac, powlawnorm)
Pear_covfracLore1lineCorr, Pear_covfracLore1linePval = Pearcorr(covfrac, lore1line)
Pear_covfracLore2lineCorr, Pear_covfracLore2linePval = Pearcorr(covfrac, lore2line)
Pear_covfracLore1normCorr, Pear_covfracLore1normPval = Pearcorr(covfrac, lore1norm)
Pear_covfracLore2normCorr, Pear_covfracLore2normPval = Pearcorr(covfrac, lore2norm)

#Tin with other timing parameters
Pear_TinpowlawnormCorr, Pear_TinpowlawnormPval = Pearcorr(Tin, powlawnorm)
Pear_Tinlore1lineCorr, Pear_Tinlore1linePval = Pearcorr(Tin, lore1line)
Pear_Tinlore2lineCorr, Pear_Tinlore2linePval = Pearcorr(Tin, lore2line)
Pear_Tinlore1normCorr, Pear_Tinlore1normPval = Pearcorr(Tin, lore1norm)
Pear_Tinlore2normCorr, Pear_Tinlore2normPval = Pearcorr(Tin, lore2norm)

#diskbbnorm with other timing parameters
Pear_diskbbnormpowlawnormCorr, Pear_diskbbnormpowlawnormPval = Pearcorr(diskbbnorm, powlawnorm)
Pear_diskbbnormlore1lineCorr, Pear_diskbbnormlore1linePval = Pearcorr(diskbbnorm, lore1line)
Pear_diskbbnormlore2lineCorr, Pear_diskbbnormlore2linePval = Pearcorr(diskbbnorm, lore2line)
Pear_diskbbnormlore1normCorr, Pear_diskbbnormlore1normPval = Pearcorr(diskbbnorm, lore1norm)
Pear_diskbbnormlore2normCorr, Pear_diskbbnormlore2normPval = Pearcorr(diskbbnorm, lore2norm)

#unabslum with other timing parameters
Pear_unabslumPowlawnormCorr, Pear_unabslumPowlawnormPval = Pearcorr(unabslum, powlawnorm)
Pear_unabslumLore1lineCorr, Pear_unabslumLore1linePval = Pearcorr(unabslum, lore1line)
Pear_unabslumLore2lineCorr, Pear_unabslumLore2linePval = Pearcorr(unabslum, lore2line)
Pear_unabslumLore1normCorr, Pear_unabslumLore1normPval = Pearcorr(unabslum, lore1norm)
Pear_unabslumLore2normCorr, Pear_unabslumLore2normPval = Pearcorr(unabslum, lore2norm)

#thlum with other timing parameters
Pear_thlumPowlawnormCorr, Pear_thlumPowlawnormPval = Pearcorr(thlum, powlawnorm)
Pear_thlumLore1lineCorr, Pear_thlumLore1linePval = Pearcorr(thlum, lore1line)
Pear_thlumLore2lineCorr, Pear_thlumLore2linePval = Pearcorr(thlum, lore2line)
Pear_thlumLore1normCorr, Pear_thlumLore1normPval = Pearcorr(thlum, lore1norm)
Pear_thlumLore2normCorr, Pear_thlumLore2normPval = Pearcorr(thlum, lore2norm)

#nonthlum with other timing parameters
Pear_nonthlumPowlawnormCorr, Pear_nonthlumPowlawnormPval = Pearcorr(nonthlum, powlawnorm)
Pear_nonthlumLore1lineCorr, Pear_nonthlumLore1linePval = Pearcorr(nonthlum, lore1line)
Pear_nonthlumLore2lineCorr, Pear_nonthlumLore2linePval = Pearcorr(nonthlum, lore2line)
Pear_nonthlumLore1normCorr, Pear_nonthlumLore1normPval = Pearcorr(nonthlum, lore1norm)
Pear_nonthlumLore2normCorr, Pear_nonthlumLore2normPval = Pearcorr(nonthlum, lore2norm)

#Spearman correlation coefficients
Sp_nHpowlawnormCorr, Sp_nHpowlawnormPval = Spcorr(nH, powlawnorm)
Sp_nHlore1lineCorr, Sp_nHlore1linePval = Spcorr(nH, lore1line)
Sp_nHlore2lineCorr, Sp_nHlore2linePval = Spcorr(nH, lore2line)
Sp_nHlore1normCorr, Sp_nHlore1normPval = Spcorr(nH, lore1norm)
Sp_nHlore2normCorr, Sp_nHlore2normPval = Spcorr(nH, lore2norm)

Sp_gammaPowlawnormCorr, Sp_gammaPowlawnormPval = Spcorr(gamma, powlawnorm)
Sp_gammaLore1lineCorr, Sp_gammaLore1linePval = Spcorr(gamma, lore1line)
Sp_gammaLore2lineCorr, Sp_gammaLore2linePval = Spcorr(gamma, lore2line)
Sp_gammaLore1normCorr, Sp_gammaLore1normPval = Spcorr(gamma, lore1norm)
Sp_gammaLore2normCorr, Sp_gammaLore2normPval = Spcorr(gamma, lore2norm)

Sp_covfracPowlawnormCorr, Sp_covfracPowlawnormPval = Spcorr(covfrac, powlawnorm)
Sp_covfracLore1lineCorr, Sp_covfracLore1linePval = Spcorr(covfrac, lore1line)
Sp_covfracLore2lineCorr, Sp_covfracLore2linePval = Spcorr(covfrac, lore2line)
Sp_covfracLore1normCorr, Sp_covfracLore1normPval = Spcorr(covfrac, lore1norm)
Sp_covfracLore2normCorr, Sp_covfracLore2normPval = Spcorr(covfrac, lore2norm)

Sp_TinpowlawnormCorr, Sp_TinpowlawnormPval = Spcorr(Tin, powlawnorm)
Sp_Tinlore1lineCorr, Sp_Tinlore1linePval = Spcorr(Tin, lore1line)
Sp_Tinlore2lineCorr, Sp_Tinlore2linePval = Spcorr(Tin, lore2line)
Sp_Tinlore1normCorr, Sp_Tinlore1normPval = Spcorr(Tin, lore1norm)
Sp_Tinlore2normCorr, Sp_Tinlore2normPval = Spcorr(Tin, lore2norm)

Sp_diskbbnormpowlawnormCorr, Sp_diskbbnormpowlawnormPval = Spcorr(diskbbnorm, powlawnorm)
Sp_diskbbnormlore1lineCorr, Sp_diskbbnormlore1linePval = Spcorr(diskbbnorm, lore1line)
Sp_diskbbnormlore2lineCorr, Sp_diskbbnormlore2linePval = Spcorr(diskbbnorm, lore2line)
Sp_diskbbnormlore1normCorr, Sp_diskbbnormlore1normPval = Spcorr(diskbbnorm, lore1norm)
Sp_diskbbnormlore2normCorr, Sp_diskbbnormlore2normPval = Spcorr(diskbbnorm, lore2norm)

Sp_unabslumPowlawnormCorr, Sp_unabslumPowlawnormPval = Spcorr(unabslum, powlawnorm)
Sp_unabslumLore1lineCorr, Sp_unabslumLore1linePval = Spcorr(unabslum, lore1line)
Sp_unabslumLore2lineCorr, Sp_unabslumLore2linePval = Spcorr(unabslum, lore2line)
Sp_unabslumLore1normCorr, Sp_unabslumLore1normPval = Spcorr(unabslum, lore1norm)
Sp_unabslumLore2normCorr, Sp_unabslumLore2normPval = Spcorr(unabslum, lore2norm)

Sp_thlumPowlawnormCorr, Sp_thlumPowlawnormPval = Spcorr(thlum, powlawnorm)
Sp_thlumLore1lineCorr, Sp_thlumLore1linePval = Spcorr(thlum, lore1line)
Sp_thlumLore2lineCorr, Sp_thlumLore2linePval = Spcorr(thlum, lore2line)
Sp_thlumLore1normCorr, Sp_thlumLore1normPval = Spcorr(thlum, lore1norm)
Sp_thlumLore2normCorr, Sp_thlumLore2normPval = Spcorr(thlum, lore2norm)

Sp_nonthlumPowlawnormCorr, Sp_nonthlumPowlawnormPval = Spcorr(nonthlum, powlawnorm)
Sp_nonthlumLore1lineCorr, Sp_nonthlumLore1linePval = Spcorr(nonthlum, lore1line)
Sp_nonthlumLore2lineCorr, Sp_nonthlumLore2linePval = Spcorr(nonthlum, lore2line)
Sp_nonthlumLore1normCorr, Sp_nonthlumLore1normPval = Spcorr(nonthlum, lore1norm)
Sp_nonthlumLore2normCorr, Sp_nonthlumLore2normPval = Spcorr(nonthlum, lore2norm)
