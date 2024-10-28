# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:26:36 2024

@author: ragha
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

nH1array = np.array([0.680737,0.599269,0.637309,0.744385])
gamma1array = np.array([1.80633,1.77858,1.77039,1.78128])
covfrac1array= np.array([0.331949,0.330851,0.304824,0.275413])
mdot1array = np.array([2.44328E-02,2.04130E-02,2.14996E-02,2.44998E-02])
logxi1array = np.array([3.30437,3.30199,3.30511,3.30392])
unabslum1array = np.array([10**37.3382,10**37.2847,10**37.2889,10**37.2926])
thlum1array = np.array([10**36.805,10**36.7181,10**36.7440,10**36.765])
nonthlum1array = unabslum1array - thlum1array

nHerr1array = np.array([[0.0189293,0.0205718,0.0227777,0.0218803],[0.022355,0.0287026,0.0320707,0.0302132]])
gammaerr1array = np.array([[0.00540943,0.00527469,0.00402877,0.0115648],[0.00442132,0.00428315,0.00508262,0.00388762]])
covfracerr1array = np.array([[0.0103004,0.0148917,0.0114826,0.0226658],[0.0139478,0.0109979,0.0121645,0.0105558]])
mdoterr1array = np.array([[0.000689702,0.000537899,0.000602153,0.000836532],[0.000917665,0.000747213,0.000889352,0.00134585]])
logxierr1array = np.array([[0.0168324,0.0168138,0.0197629,0.0225731],[0.023498,0.0429841,0.0256525,0.0925002]])
unabslumerr1array = np.array([[10**37.3382-10**37.3312,10**37.2847-10**37.2782,10**37.2889-10**37.2851,10**37.2926-10**37.2843],[10**37.345-10**37.3382,10**37.2942-10**37.2847,10**37.3004-10**37.2889,10**37.304-10**37.2926]])
thlumerr1array = np.array([[10**36.805-10**36.7693,10**36.7181-10**36.6993,10**36.774-10**36.7142,10**36.765-10**36.7315],[10**36.8122-10**36.805,10**36.7394-10**36.7181,10**36.7561-10**36.744,10**36.7919-10**36.765]])
nonthlumerr1array = unabslumerr1array + thlumerr1array

nH2array = np.array([0.634989,0.689779,0.666605,0.684820,0.735800])
gamma2array = np.array([1.87452,1.88103,1.88576,1.89056,1.90825])
covfrac2array = np.array([0.287485,0.276834,0.315323,0.289499,0.302881])
mdot2array = np.array([3.37392E-02,3.78772E-02,3.69322E-02,4.02627E-02,4.15359E-02])
logxi2array = np.array([3.31256,3.31864,3.31443,3.31204,3.32761])
unabslum2array = np.array([10**37.3958,10**37.4240,10**37.4475,10**37.4525,10**37.4774])
thlum2array = np.array([10**36.9357,10**36.9872,10**36.9738,10**37.0024,10**37.0313])
nonthlum2array = unabslum2array - thlum2array

nHerr2array = np.array([[0.0144597,0.0164279,0.0187898,0.0189378,0.0360659],[0.0166761,0.019268,0.0153954,0.0149967,0.0361418]])
gammaerr2array = np.array([[0.00632336,0.00949848,0.00798775,0.00603551,0.0126994],[0.00713502,0.0040618,0.00712604,0.00576673,0.00423184]])
covfracerr2array = np.array([[0.0114911,0.0158419,0.0148843,0.0107181,0.0250126],[0.0137766,0.009068,0.0160819,0.0098197,0.0155247]])
mdoterr2array = np.array([[0.000763289,0.000854436,0.00100377,0.000946679,0.00216977],[0.000978759,0.000869448,0.000879311,0.00092686,0.00210866]])
logxierr2array = np.array([[0.0305603,0.0158758,0.0312013,0.0166856,0.0116674],[0.0380347,0.0555434,0.0517268,0.0391067,0.082971]])
unabslumerr2array = np.array([[10**37.3958-10**37.3898,10**37.4240-10**37.4163,10**37.4475-10**37.4403,10**37.4525-10**37.447,10**37.4774-10**37.4684],[10**37.4042-10**37.3958,10**37.4327-10**37.424,10**37.4542-10**37.4475,10**37.4588-10**37.4525,10**37.4874-10**37.4774]])
thlumerr2array = np.array([[10**36.9357-10**36.9231,10**36.9872-10**36.9661,10**36.9738-10**36.9567,10**37.0024-10**36.9921,10**37.0313-10**36.9961],[10**36.9525-10**36.9357,10**36.9971-10**36.9872,10**36.9869-10**36.9738,10**37.0205-10**37.0024,10**37.0574-10**37.0313]])
nonthlumerr2array = unabslumerr2array + thlumerr2array

nH3array = np.array([0.694838,0.755654,0.819525,0.842870,0.820478,0.848761,0.877283])
gamma3array = np.array([1.81453,1.84325,1.89119,1.91072,1.89645,1.92728,1.92044])
covfrac3array = np.array([0.283635,0.269787,0.292996,0.304608,0.291533,0.401277,0.313999])
mdot3array = np.array([3.28627E-02,4.17607E-02,5.31165E-02,5.66176E-02,5.86447E-02,5.95587E-02,6.28227E-02])
logxi3array = np.array([3.30111,3.30559,3.32993,3.31197,3.32870,3.35985,3.35178])
unabslum3array = np.array([10**37.4513,10**37.5319,10**37.6413,10**37.6697,10**37.6708,10**37.7658,10**37.719])
thlum3array = np.array([10**36.9235,10**37.0249,10**37.1218,10**37.1467,10**37.1614,10**37.1778,10**37.1959])
nonthlum3array = unabslum3array - thlum3array

nHerr3array = np.array([[0.0112686,0.0140795,0.0176341,0.0170862,0.0190087,0.0155986,0.0162303],[0.0145435,0.0144341,0.0172124,0.0174057,0.0169905,0.0174755,0.0187871]])
gammaerr3array = np.array([[0.00551685,0.00533016,0.010665,0.0108255,0.0114923,0.0109025,0.00985676],[0.00378643,0.00602548,0.00506988,0.00560333,0.00386279,0.00933424,0.00755395]])
covfracerr3array = np.array([[0.00938329,0.00889308,0.0205728,0.0148841,0.0210382,0.0267628,0.0198267],[0.00652405,0.0112055,0.011669,0.0115612,0.00933829,0.0254018,0.0181432]])
mdoterr3array = np.array([[0.000455171,0.00083873,0.00115743,0.00138662,0.00143797,0.00151101,0.00120972],[0.000499897,0.000842719,0.00112047,0.00117618,0.00116416,0.00150744,0.00125428]])
logxierr3array = np.array([[0.0101556,0.0190249,0.0135651,0.0167929,0.00649863,0.052073,0.0403697],[0.0225002,0.0220178,0.0513642,0.0531024,0.0582399,0.0568774,0.0501907]])
unabslumerr3array = np.array([[10**37.4513-10**37.4472,10**37.5319-10**37.5293,10**37.6413-10**37.6345,10**37.6697-10**37.6636,10**37.6708-10**37.6654,10**37.7658-10**37.7597,10**37.719-10**37.7137],[10**37.457-10**37.4513,10**37.539-10**37.5319,10**37.6485-10**37.6413,10**37.6766-10**37.6697,10**37.6775-10**37.6708,10**37.7714-10**37.7658,10**37.7267-10**37.719]])
thlumerr3array = np.array([[10**36.9235-10**36.9112,10**37.0249-10**37.0133,10**37.1218-10**37.1103,10**37.1467-10**37.1338,10**37.1614-10**37.1529,10**37.1778-10**37.1637,10**37.1959-10**37.1851],[10**36.9328-10**36.9235,10**37.033-10**37.0249,10**37.1348-10**37.1218,10**37.1602-10**37.1467,10**37.1793-10**37.1614,10**37.1915-10**37.1778,10**37.2073-10**37.1959]])
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


obs1segments = [1,2,3,4]
obs2segments = [5,6,7,8,9]
obs3segments = [10,11,12,13,14,15,16]

nH = np.concatenate((nH1array,nH2array,nH3array))
gamma = np.concatenate((gamma1array,gamma2array,gamma3array))
covfrac = np.concatenate((covfrac1array,covfrac2array,covfrac3array))
mdot = np.concatenate((mdot1array,mdot2array,mdot3array))
logxi = np.concatenate((logxi1array,logxi2array,logxi3array))
unabslum = np.concatenate((unabslum1array,unabslum2array,unabslum3array))
thlum = np.concatenate((thlum1array,thlum2array,thlum3array))
nonthlum = np.concatenate((nonthlum1array,nonthlum2array,nonthlum3array))
powlawnorm = np.concatenate((obs1_powlawnormarray,obs2_powlawnormarray,obs3_powlawnormarray))
lore1line = np.concatenate((obs1_lore1linearray,obs2_lore1linearray,obs3_lore1linearray))
lore1norm = np.concatenate((obs1_lore1normarray,obs2_lore1normarray,obs3_lore1normarray))
lore2line = np.concatenate((obs1_lore2linearray,obs2_lore2linearray,obs3_lore2linearray))
lore2norm = np.concatenate((obs1_lore2normarray,obs2_lore2normarray,obs3_lore2normarray))

hardness1array = nonthlum1array/thlum1array
hardness2array = nonthlum2array/thlum2array
hardness3array = nonthlum3array/thlum3array
hardnesserr1array = hardness1array * (nonthlumerr1array/nonthlum1array + thlumerr1array/thlum1array)
hardnesserr2array = hardness2array * (nonthlumerr2array/nonthlum2array + thlumerr2array/thlum2array)
hardnesserr3array = hardness3array * (nonthlumerr3array/nonthlum3array + thlumerr3array/thlum3array)

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


#Time Variation Plots
timevariation(obs1segments,obs2segments,obs3segments,nH1array,nH2array,nH3array,nHerr1array,nHerr2array,nHerr3array,'Observation Number','ISM Hydrogen Column Density (10^22 atoms cm^-2)','Variation of ISM Hydrogen Column Density ')
timevariation(obs1segments,obs2segments,obs3segments,gamma1array,gamma2array,gamma3array,gammaerr1array,gammaerr2array,gammaerr3array,'Observation Number','Thermal Comptonization Photon Index','Variation of Thermal Comptonization Photon Index ')
timevariation(obs1segments,obs2segments,obs3segments,covfrac1array,covfrac2array,covfrac3array,covfracerr1array,covfracerr2array,covfracerr3array,'Observation Number','Covering Fraction','Variation of Covering Fraction ')
timevariation(obs1segments,obs2segments,obs3segments,logxi1array,logxi2array,logxi3array,logxierr1array,logxierr2array,logxierr3array,'Observation Number','Ionization Gradient','Variation of Ionization Gradient ')
timevariation(obs1segments,obs2segments,obs3segments,mdot1array,mdot2array,mdot3array,mdoterr1array,mdoterr2array,mdoterr3array,'Observation Number','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Black Hole Mass Accretion Rate ')
timevariation(obs1segments,obs2segments,obs3segments,unabslum1array,unabslum2array,unabslum3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Observation Number','Unabsorbed Total Luminsoity (erg/s)','Variation of Unabsorbed Total Luminosity ')
timevariation(obs1segments,obs2segments,obs3segments,thlum1array,thlum2array,thlum3array,thlumerr1array,thlumerr2array,thlumerr3array,'Observation Number','Thermal Luminosity (erg/s)','Variation of Thermal Luminosity ')
timevariation(obs1segments,obs2segments,obs3segments,nonthlum1array,nonthlum2array,nonthlum3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Observation Number','Non Thermal Luminosity','Variation of Non Thermal Luminosity ')
timevariation(obs1segments,obs2segments,obs3segments,hardness1array,hardness2array,hardness3array,hardnesserr1array,hardnesserr2array,hardnesserr3array,'Observation Number','Hardness Ratio','Variation of Hardness Ratio ')

#nH with other parameters
paravariation(nH1array,nH2array,nH3array,gamma1array,gamma2array,gamma3array,nHerr1array,nHerr2array,nHerr3array,gammaerr1array,gammaerr2array,gammaerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Thermal Comptonization Photon Index','Variation of ISM Hydrogen Column Density with Thermal Comptonization Photon Index ')
paravariation(nH1array,nH2array,nH3array,covfrac1array,covfrac2array,covfrac3array,nHerr1array,nHerr2array,nHerr3array,covfracerr1array,covfracerr2array,covfracerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Covering Fraction','Variation of ISM Hydrogen Column Density with Covering Fraction ')
paravariation(nH1array,nH2array,nH3array,logxi1array,logxi2array,logxi3array,nHerr1array,nHerr2array,nHerr3array,logxierr1array,logxierr2array,logxierr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Ionization Gradient','Variation of ISM Hydrogen Column Density with Ionization Gradient ')
paravariation(nH1array,nH2array,nH3array,mdot1array,mdot2array,mdot3array,nHerr1array,nHerr2array,nHerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of ISM Hydrogen Column Density with Black Hole Mass Accretion Rate ')
paravariation(nH1array,nH2array,nH3array,unabslum1array,unabslum2array,unabslum3array,nHerr1array,nHerr2array,nHerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Unabsorbed Total Luminosity (erg/s)','Variation of ISM Hydrogen Column Density with Unabsorbed Total Luminosity ')
paravariation(nH1array,nH2array,nH3array,thlum1array,thlum2array,thlum3array,nHerr1array,nHerr2array,nHerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Thermal Luminosity (erg/s)','Variation of ISM Hydrogen Column Density with Thermal Luminosity ')
paravariation(nH1array,nH2array,nH3array,nonthlum1array,nonthlum2array,nonthlum3array,nHerr1array,nHerr2array,nHerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'ISM Hydrogen Column Density (10^22 atoms cm^-2)','Non Thermal Luminosity (erg/s)','Variation of ISM Hydrogen Column Density with Non Thermal Luminosity ')

#gamma with other parameters
paravariation(gamma1array,gamma2array,gamma3array,covfrac1array,covfrac2array,covfrac3array,gammaerr1array,gammaerr2array,gammaerr3array,covfracerr1array,covfracerr2array,covfracerr3array,'Thermal Comptonization Photon Index','Covering Fraction','Variation of Thermal Comptonization Photon Index with Covering Fraction ')
paravariation(gamma1array,gamma2array,gamma3array,logxi1array,logxi2array,logxi3array,gammaerr1array,gammaerr2array,gammaerr3array,logxierr1array,logxierr2array,logxierr3array,'Thermal Comptonization Photon Index','Ionization Gradient','Variation of Thermal Comptonization Photon Index with Ionization Gradient ')
paravariation(gamma1array,gamma2array,gamma3array,unabslum1array,unabslum2array,unabslum3array,gammaerr1array,gammaerr2array,gammaerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Thermal Comptonization Photon Index','Unabsorbed Total Luminosity (erg/s)','Variation of Thermal Comptonization Photon Index with Unabsorbed Total Luminosity ')
paravariation(gamma1array,gamma2array,gamma3array,mdot1array,mdot2array,mdot3array,gammaerr1array,gammaerr2array,gammaerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Thermal Comptonization Photon Index','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Thermal Comptonization Photon Index with Black Hole Mass Accretion Rate ')
paravariation(gamma1array,gamma2array,gamma3array,thlum1array,thlum2array,thlum3array,gammaerr1array,gammaerr2array,gammaerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Thermal Comptonization Photon Index','Thermal Luminosity (erg/s)','Variation of Thermal Comptonization Photon Index with Thermal Luminosity ')
paravariation(gamma1array,gamma2array,gamma3array,nonthlum1array,nonthlum2array,nonthlum3array,gammaerr1array,gammaerr2array,gammaerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Thermal Comptonization Photon Index','Non Thermal Luminosity (erg/s)','Variation of Thermal Comptonization Photon Index with Non Thermal Luminosity ')


#covering fraction with other parameters
paravariation(covfrac1array,covfrac2array,covfrac3array,logxi1array,logxi2array,logxi3array,covfracerr1array,covfracerr2array,covfracerr3array,logxierr1array,logxierr2array,logxierr3array,'Covering Fraction','Ionization Gradient','Variation of Covering Fraction with Ionization Gradient ')
paravariation(covfrac1array,covfrac2array,covfrac3array,mdot1array,mdot2array,mdot3array,covfracerr1array,covfracerr2array,covfracerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Covering Fraction','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Covering Fraction with Black Hole Mass Accretion Rate ')
paravariation(covfrac1array,covfrac2array,covfrac3array,unabslum1array,unabslum2array,unabslum3array,covfracerr1array,covfracerr2array,covfracerr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Covering Fraction','Total Unabsorbed Luminosity (erg/s)','Variation of Covering Fraction with Total Unabsorbed Luminosity ')
paravariation(covfrac1array,covfrac2array,covfrac3array,thlum1array,thlum2array,thlum3array,covfracerr1array,covfracerr2array,covfracerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Covering Fraction','Thermal Luminosity (erg/s)','Variation of Covering Fraction with Thermal Luminosity ')
paravariation(covfrac1array,covfrac2array,covfrac3array,nonthlum1array,nonthlum2array,nonthlum3array,covfracerr1array,covfracerr2array,covfracerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Covering Fraction','Non Thermal Luminosity (erg/s)','Variation of Covering Fraction with Non Thermal Luminosity ')

#logxi with other parameters
paravariation(logxi1array,logxi2array,logxi3array,mdot1array,mdot2array,mdot3array,logxierr1array,logxierr2array,logxierr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Ionization Gradient','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Ionization Gradient with Black Hole Mass Accretion Rate ')
paravariation(logxi1array,logxi2array,logxi3array,unabslum1array,unabslum2array,unabslum3array,logxierr1array,logxierr2array,logxierr3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,'Ionization Gradient','Unabsorbed Total Luminosity (erg/s)','Variation of Ionization Gradient with Unabsorbed Total Luminosity ')
paravariation(logxi1array,logxi2array,logxi3array,thlum1array,thlum2array,thlum3array,logxierr1array,logxierr2array,logxierr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Ionization Gradient','Thermal Luminosity (erg/s)','Variation of Ionization Gradient with Thermal Luminosity ')
paravariation(logxi1array,logxi2array,logxi3array,nonthlum1array,nonthlum2array,nonthlum3array,logxierr1array,logxierr2array,logxierr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Ionization Gradient','Non Thermal Luminosity (erg/s)','Variation of Ionization Gradient with Non Thermal Luminosity ')

#Total Unabsorbed Luminosity with other parameters
paravariation(unabslum1array,unabslum2array,unabslum3array,thlum1array,thlum2array,thlum3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,thlumerr1array,thlumerr2array,thlumerr3array,'Total Unabsorbed Luminosity (erg/s)','Thermal Luminosity (erg/s)','Variation of Total Unabsorbed Luminosity with Thermal Luminosity ')
paravariation(unabslum1array,unabslum2array,unabslum3array,nonthlum1array,nonthlum2array,nonthlum3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Total Unabsorbed Luminosity (erg/s)','Non Thermal Luminosity (erg/s)','Variation of Total Unabsorbed Luminosity with Non Thermal Luminosity ')
paravariation(unabslum1array,unabslum2array,unabslum3array,mdot1array,mdot2array,mdot3array,unabslumerr1array,unabslumerr2array,unabslumerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Total Unabsorbed Luminosity (erg/s)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Total Unabsorbed Luminosity with Black Hole Mass Accretion Rate ')

#Thermal Luminosity with other parameters
paravariation(thlum1array,thlum2array,thlum3array,nonthlum1array,nonthlum2array,nonthlum3array,thlumerr1array,thlumerr2array,thlumerr3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,'Thermal Luminosity (erg/s)','Non Thermal Luminosity (erg/s)','Variation of Thermal Luminosity with Non Thermal Luminosity ')
paravariation(thlum1array,thlum2array,thlum3array,mdot1array,mdot2array,mdot3array,thlumerr1array,thlumerr2array,thlumerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Thermal Luminosity (erg/s)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Thermal Luminosity with Black Hole Mass Accretion Rate ')

#Non Thermal with mass accretion rate
paravariation(nonthlum1array,nonthlum2array,nonthlum3array,mdot1array,mdot2array,mdot3array,nonthlumerr1array,nonthlumerr2array,nonthlumerr3array,mdoterr1array,mdoterr2array,mdoterr3array,'Non Thermal Luminosity (erg/s)','Black Hole Mass Accretion Rate (10^18 g/s)','Variation of Non Thermal Luminosity with Black Hole Mass Accretion Rate ')

#Pearson Correlation Coefficients
#nH with other parameters
Pear_nHgammaCorr,Pear_nHgammaPval = Pearcorr(nH,gamma)
Pear_nHcovCorr,Pear_nHcovPval = Pearcorr(nH,covfrac)
Pear_nHlogxiCorr,Pear_nHlogxiPval = Pearcorr(nH,logxi)
Pear_nHmdotCorr,Pear_nHmdotPval = Pearcorr(nH,mdot)
Pear_nHlumCorr,Pear_nHlumPval = Pearcorr(nH,unabslum)
Pear_nHthlumCorr,Pear_nHthlumPval = Pearcorr(nH,thlum)
Pear_nHnonthlumCorr,Pear_nHnonthlumPval = Pearcorr(nH,nonthlum)

#gamma with other parameters
Pear_gammacovCorr,Pear_gammacovPval = Pearcorr(gamma,covfrac)
Pear_gammalogxiCorr,Pear_gammalogxiPval = Pearcorr(gamma,logxi)
Pear_gammamdotCorr,Pear_gammamdotPval = Pearcorr(gamma,mdot)
Pear_gammalumCorr,Pear_gammalumPval = Pearcorr(gamma,unabslum)
Pear_gammathlumCorr,Pear_gammathlumPval = Pearcorr(gamma,thlum)
Pear_gammanonthlumCorr,Pear_gammanonthlumPval = Pearcorr(gamma,nonthlum)

#covfrac with other parameters
Pear_covlogxiCorr, Pear_covlogxiPval = Pearcorr(covfrac,logxi)
Pear_covmdotCorr, Pear_covmdotPval = Pearcorr(covfrac,mdot)
Pear_covlumCorr, Pear_covlumPval = Pearcorr(covfrac,unabslum) 
Pear_covthlumCorr, Pear_covthlumPval = Pearcorr(covfrac,thlum) 
Pear_covnonthlumCorr, Pear_covnonthlumPval = Pearcorr(covfrac,nonthlum) 

#logxi with other parameters
Pear_logximdotCorr, Pear_logximdotPval = Pearcorr(logxi, mdot) 
Pear_logxilumCorr, Pear_logxilumPval = Pearcorr(logxi, unabslum) 
Pear_logxithlumCorr, Pear_logxithlumPval = Pearcorr(logxi, thlum) 
Pear_logxinonthlumCorr, Pear_logxinonthlumPval = Pearcorr(logxi, nonthlum) 

#Total unabsorbed luminosity with other parameters
Pear_lumthlumCorr, Pear_lumthlumPval = Pearcorr(unabslum, thlum)
Pear_lumnonthlumCorr, Pear_lumnonthlumPval = Pearcorr(unabslum, nonthlum)
Pear_lummdotCorr, Pear_lummdotPval = Pearcorr(unabslum, mdot)

#Thermal luminosity with other parameters
Pear_thlumnonthlumCorr, Pear_thlumnonthlumPval = Pearcorr(thlum, nonthlum)
Pear_thlummdotCorr, Pear_thlummdotPval = Pearcorr(thlum, mdot)

#Non Thermal Luminosity with black hole mass accretion rate
Pear_nonthlummdotCorr, Pear_nonthlummdotPval = Pearcorr(nonthlum, mdot)

#Spearman Correlation Coefficients
# nH with other parameters
Sp_nHgammaCorr, Sp_nHgammaPval = Spcorr(nH, gamma)
Sp_nHcovCorr, Sp_nHcovPval = Spcorr(nH, covfrac)
Sp_nHlogxiCorr, Sp_nHlogxiPval = Spcorr(nH, logxi)
Sp_nHmdotCorr, Sp_nHmdotPval = Spcorr(nH, mdot)
Sp_nHlumCorr, Sp_nHlumPval = Spcorr(nH, unabslum)
Sp_nHthlumCorr, Sp_nHthlumPval = Spcorr(nH, thlum)
Sp_nHnonthlumCorr, Sp_nHnonthlumPval = Spcorr(nH, nonthlum)

# gamma with other parameters
Sp_gammacovCorr, Sp_gammacovPval = Spcorr(gamma, covfrac)
Sp_gammalogxiCorr, Sp_gammalogxiPval = Spcorr(gamma, logxi)
Sp_gammamdotCorr, Sp_gammamdotPval = Spcorr(gamma, mdot)
Sp_gammalumCorr, Sp_gammalumPval = Spcorr(gamma, unabslum)
Sp_gammathlumCorr, Sp_gammathlumPval = Spcorr(gamma, thlum)
Sp_gammanonthlumCorr, Sp_gammanonthlumPval = Spcorr(gamma, nonthlum)

# covfrac with other parameters
Sp_covlogxiCorr, Sp_covlogxiPval = Spcorr(covfrac, logxi)
Sp_covmdotCorr, Sp_covmdotPval = Spcorr(covfrac, mdot)
Sp_covlumCorr, Sp_covlumPval = Spcorr(covfrac, unabslum)
Sp_covthlumCorr, Sp_covthlumPval = Spcorr(covfrac, thlum)
Sp_covnonthlumCorr, Sp_covnonthlumPval = Spcorr(covfrac, nonthlum)

# logxi with other parameters
Sp_logximdotCorr, Sp_logximdotPval = Spcorr(logxi, mdot)
Sp_logxilumCorr, Sp_logxilumPval = Spcorr(logxi, unabslum)
Sp_logxithlumCorr, Sp_logxithlumPval = Spcorr(logxi, thlum)
Sp_logxinonthlumCorr, Sp_logxinonthlumPval = Spcorr(logxi, nonthlum)

# Total unabsorbed luminosity with other parameters
Sp_lumthlumCorr, Sp_lumthlumPval = Spcorr(unabslum, thlum)
Sp_lumnonthlumCorr, Sp_lumnonthlumPval = Spcorr(unabslum, nonthlum)
Sp_lummdotCorr, Sp_lummdotPval = Spcorr(unabslum, mdot)

# Thermal luminosity with other parameters
Sp_thlumnonthlumCorr, Sp_thlumnonthlumPval = Spcorr(thlum, nonthlum)
Sp_thlummdotCorr, Sp_thlummdotPval = Spcorr(thlum, mdot)

# Non Thermal Luminosity with black hole mass accretion rate
Sp_nonthlummdotCorr, Sp_nonthlummdotPval = Spcorr(nonthlum, mdot)


#Plots for timing analysis
timevariation(obs1segments,obs2segments,obs3segments,obs1_powlawnormarray,obs2_powlawnormarray,obs3_powlawnormarray,obs1_powlawnormerrarray,obs2_powlawnormerrarray,obs3_powlawnormerrarray,'Observation Number','Power Law Normalization','Variation of Power Law Normalization ')
timevariation(obs1segments,obs2segments,obs3segments,obs1_lore1linearray,obs2_lore1linearray,obs3_lore1linearray,obs1_lore1lineerrarray,obs2_lore1lineerrarray,obs3_lore1lineerrarray,'Observation Number','Central frequency of First Lorentzian (Hz)','Variation of First Lorentzian Frequency ')
timevariation(obs1segments,obs2segments,obs3segments,obs1_lore1normarray,obs2_lore1normarray,obs3_lore1normarray,obs1_lore1normerrarray,obs2_lore1normerrarray,obs3_lore1normerrarray,'Observation Number','Normalization of First Lorentzian','Variation of First Lorentzian Normalization ')
timevariation(obs1segments,obs2segments,obs3segments,obs1_lore2linearray,obs2_lore2linearray,obs3_lore2linearray,obs1_lore2lineerrarray,obs2_lore2lineerrarray,obs3_lore2lineerrarray,'Observation Number','Central frequency of Second Lorentzian (Hz)','Variation of Second Lorentzian Frequency ')
timevariation(obs1segments,obs2segments,obs3segments,obs1_lore2normarray,obs2_lore2normarray,obs3_lore2normarray,obs1_lore2normerrarray,obs2_lore2normerrarray,obs3_lore2normerrarray,'Observation Number','Normalization of Second Lorentzian','Variation of Second Lorentzian Normalization ')

#Correlation of power-law norm with spectral parameters
paravariation(nH1array, nH2array, nH3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, nHerr1array, nHerr2array, nHerr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Power Law Normalization', 'Variation of ISM Hydrogen Column Density with Power Law Normalization ')
paravariation(gamma1array, gamma2array, gamma3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, gammaerr1array, gammaerr2array, gammaerr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Thermal Comptonization Photon Index', 'Power Law Normalization', 'Variation of Thermal Comptonization Photon Index with Power Law Normalization ')
paravariation(covfrac1array, covfrac2array, covfrac3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, covfracerr1array, covfracerr2array, covfracerr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Covering Fraction', 'Power Law Normalization', 'Variation of Covering Fraction with Power Law Normalization ')
paravariation(mdot1array, mdot2array, mdot3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, mdoterr1array, mdoterr2array, mdoterr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Black Hole Mass Accretion Rate (10^18 g/s)', 'Power Law Normalization', 'Variation of Mass Accretion Rate with Power Law Normalization ')
paravariation(logxi1array, logxi2array, logxi3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, logxierr1array, logxierr2array, logxierr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Ionization Gradient', 'Power Law Normalization', 'Variation of Ionization Parameter with Power Law Normalization ')
paravariation(unabslum1array, unabslum2array, unabslum3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Unabsorbed Total Luminosity (erg/s)', 'Power Law Normalization', 'Variation of Unabsorbed Luminosity with Power Law Normalization ')
paravariation(thlum1array, thlum2array, thlum3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, thlumerr1array, thlumerr2array, thlumerr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Thermal Luminosity (erg/s)', 'Power Law Normalization', 'Variation of Thermal Luminosity with Power Law Normalization ')
paravariation(nonthlum1array, nonthlum2array, nonthlum3array, obs1_powlawnormarray, obs2_powlawnormarray, obs3_powlawnormarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, obs1_powlawnormerrarray, obs2_powlawnormerrarray, obs3_powlawnormerrarray, 'Non-Thermal Luminosity (erg/s)', 'Power Law Normalization', 'Variation of Non-Thermal Luminosity with Power Law Normalization ')

#Correlation of lorentzian 1 line frequency with spectral parameters
paravariation(nH1array, nH2array, nH3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, nHerr1array, nHerr2array, nHerr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of ISM Hydrogen Column Density with Lorentzian 1 Line Frequency ')
paravariation(gamma1array, gamma2array, gamma3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, gammaerr1array, gammaerr2array, gammaerr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Thermal Comptonization Photon Index', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Thermal Comptonization Photon Index with Lorentzian 1 Line Frequency ')
paravariation(covfrac1array, covfrac2array, covfrac3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, covfracerr1array, covfracerr2array, covfracerr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Covering Fraction', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Covering Fraction with Lorentzian 1 Line Frequency ')
paravariation(mdot1array, mdot2array, mdot3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, mdoterr1array, mdoterr2array, mdoterr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Black Hole Mass Accretion Rate (10^18 g/s)', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Mass Accretion Rate with Lorentzian 1 Line Frequency ')
paravariation(logxi1array, logxi2array, logxi3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, logxierr1array, logxierr2array, logxierr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Ionization Gradient', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Ionization Gradient with Lorentzian 1 Line Frequency ')
paravariation(unabslum1array, unabslum2array, unabslum3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, unabslumerr1array, unabslumerr2array, unabslumerr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Unabsorbed Total Luminosity (erg/s)', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Unabsorbed Luminosity with Lorentzian 1 Line Frequency ')
paravariation(thlum1array, thlum2array, thlum3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, thlumerr1array, thlumerr2array, thlumerr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Thermal Luminosity (erg/s)', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Thermal Luminosity with Lorentzian 1 Line Frequency ')
paravariation(nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore1linearray, obs2_lore1linearray, obs3_lore1linearray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, obs1_lore1lineerrarray, obs2_lore1lineerrarray, obs3_lore1lineerrarray, 'Non-Thermal Luminosity (erg/s)', 'Lorentzian 1 Line Frequency (Hz)', 'Variation of Non-Thermal Luminosity with Lorentzian 1 Line Frequency ')

#Correlation of lorentzian 1 normalization with spectral parameters
paravariation(nH1array, nH2array, nH3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, nHerr1array, nHerr2array, nHerr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Lorentzian 1 Normalization', 'Variation of ISM Hydrogen Column Density with Lorentzian 1 Normalization ')
paravariation(gamma1array, gamma2array, gamma3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, gammaerr1array, gammaerr2array, gammaerr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Thermal Comptonization Photon Index', 'Lorentzian 1 Normalization', 'Variation of Thermal Comptonization Photon Index with Lorentzian 1 Normalization ')
paravariation(covfrac1array, covfrac2array, covfrac3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, covfracerr1array, covfracerr2array, covfracerr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Covering Fraction', 'Lorentzian 1 Normalization', 'Variation of Covering Fraction with Lorentzian 1 Normalization ')
paravariation(mdot1array, mdot2array, mdot3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, mdoterr1array, mdoterr2array, mdoterr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Black Hole Mass Accretion Rate (10^18 g/s)', 'Lorentzian 1 Normalization', 'Variation of Mass Accretion Rate with Lorentzian 1 Normalization ')
paravariation(logxi1array, logxi2array, logxi3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, logxierr1array, logxierr2array, logxierr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Ionization Gradient', 'Lorentzian 1 Normalization', 'Variation of Ionization Gradient with Lorentzian 1 Normalization ')
paravariation(unabslum1array, unabslum2array, unabslum3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Unabsorbed Total Luminosity (erg/s)', 'Lorentzian 1 Normalization', 'Variation of Unabsorbed Luminosity with Lorentzian 1 Normalization ')
paravariation(thlum1array, thlum2array, thlum3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, thlumerr1array, thlumerr2array, thlumerr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Thermal Luminosity (erg/s)', 'Lorentzian 1 Normalization', 'Variation of Thermal Luminosity with Lorentzian 1 Normalization ')
paravariation(nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore1normarray, obs2_lore1normarray, obs3_lore1normarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, obs1_lore1normerrarray, obs2_lore1normerrarray, obs3_lore1normerrarray, 'Non-Thermal Luminosity (erg/s)', 'Lorentzian 1 Normalization', 'Variation of Non-Thermal Luminosity with Lorentzian 1 Normalization ')

#Correlation of lorentzian 2 line frequency with spectral parameters
paravariation(nH1array, nH2array, nH3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, nHerr1array, nHerr2array, nHerr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of ISM Hydrogen Column Density with Lorentzian 2 Line Frequency ')
paravariation(gamma1array, gamma2array, gamma3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, gammaerr1array, gammaerr2array, gammaerr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Thermal Comptonization Photon Index', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Thermal Comptonization Photon Index with Lorentzian 2 Line Frequency ')
paravariation(covfrac1array, covfrac2array, covfrac3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, covfracerr1array, covfracerr2array, covfracerr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Covering Fraction', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Covering Fraction with Lorentzian 2 Line Frequency ')
paravariation(mdot1array, mdot2array, mdot3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, mdoterr1array, mdoterr2array, mdoterr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Black Hole Mass Accretion Rate (10^18 g/s)', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Mass Accretion Rate with Lorentzian 2 Line Frequency ')
paravariation(logxi1array, logxi2array, logxi3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, logxierr1array, logxierr2array, logxierr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Ionization Gradient', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Ionization Gradient with Lorentzian 2 Line Frequency ')
paravariation(unabslum1array, unabslum2array, unabslum3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, unabslumerr1array, unabslumerr2array, unabslumerr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Unabsorbed Total Luminosity (erg/s)', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Unabsorbed Luminosity with Lorentzian 2 Line Frequency ')
paravariation(thlum1array, thlum2array, thlum3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, thlumerr1array, thlumerr2array, thlumerr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Thermal Luminosity (erg/s)', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Thermal Luminosity with Lorentzian 2 Line Frequency ')
paravariation(nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore2linearray, obs2_lore2linearray, obs3_lore2linearray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, obs1_lore2lineerrarray, obs2_lore2lineerrarray, obs3_lore2lineerrarray, 'Non-Thermal Luminosity (erg/s)', 'Lorentzian 2 Line Frequency (Hz)', 'Variation of Non-Thermal Luminosity with Lorentzian 2 Line Frequency ')

#Correlation of lorentzian 2 normalization with spectral parameters
paravariation(nH1array, nH2array, nH3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, nHerr1array, nHerr2array, nHerr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'ISM Hydrogen Column Density (10^22 atoms cm^-2)', 'Lorentzian 2 Norm', 'Variation of ISM Hydrogen Column Density with Lorentzian 2 Norm ')
paravariation(gamma1array, gamma2array, gamma3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, gammaerr1array, gammaerr2array, gammaerr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Thermal Comptonization Photon Index', 'Lorentzian 2 Norm', 'Variation of Thermal Comptonization Photon Index with Lorentzian 2 Norm ')
paravariation(covfrac1array, covfrac2array, covfrac3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, covfracerr1array, covfracerr2array, covfracerr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Covering Fraction', 'Lorentzian 2 Norm', 'Variation of Covering Fraction with Lorentzian 2 Norm ')
paravariation(mdot1array, mdot2array, mdot3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, mdoterr1array, mdoterr2array, mdoterr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Black Hole Mass Accretion Rate (10^18 g/s)', 'Lorentzian 2 Norm', 'Variation of Mass Accretion Rate with Lorentzian 2 Norm ')
paravariation(logxi1array, logxi2array, logxi3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, logxierr1array, logxierr2array, logxierr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Ionization Gradient', 'Lorentzian 2 Norm', 'Variation of Ionization Gradient with Lorentzian 2 Norm ')
paravariation(unabslum1array, unabslum2array, unabslum3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, unabslumerr1array, unabslumerr2array, unabslumerr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Unabsorbed Total Luminosity (erg/s)', 'Lorentzian 2 Norm', 'Variation of Unabsorbed Luminosity with Lorentzian 2 Norm ')
paravariation(thlum1array, thlum2array, thlum3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, thlumerr1array, thlumerr2array, thlumerr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Thermal Luminosity (erg/s)', 'Lorentzian 2 Norm', 'Variation of Thermal Luminosity with Lorentzian 2 Norm ')
paravariation(nonthlum1array, nonthlum2array, nonthlum3array, obs1_lore2normarray, obs2_lore2normarray, obs3_lore2normarray, nonthlumerr1array, nonthlumerr2array, nonthlumerr3array, obs1_lore2normerrarray, obs2_lore2normerrarray, obs3_lore2normerrarray, 'Non-Thermal Luminosity (erg/s)', 'Lorentzian 2 Norm', 'Variation of Non-Thermal Luminosity with Lorentzian 2 Norm ')

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

#Mdot with other timing parameters
Pear_mdotPowlawnormCorr, Pear_mdotPowlawnormPval = Pearcorr(mdot, powlawnorm)
Pear_mdotLore1lineCorr, Pear_mdotLore1linePval = Pearcorr(mdot, lore1line)
Pear_mdotLore2lineCorr, Pear_mdotLore2linePval = Pearcorr(mdot, lore2line)
Pear_mdotLore1normCorr, Pear_mdotLore1normPval = Pearcorr(mdot, lore1norm)
Pear_mdotLore2normCorr, Pear_mdotLore2normPval = Pearcorr(mdot, lore2norm)

#logxi with other timing parameters
Pear_logxiPowlawnormCorr, Pear_logxiPowlawnormPval = Pearcorr(logxi, powlawnorm)
Pear_logxiLore1lineCorr, Pear_logxiLore1linePval = Pearcorr(logxi, lore1line)
Pear_logxiLore2lineCorr, Pear_logxiLore2linePval = Pearcorr(logxi, lore2line)
Pear_logxiLore1normCorr, Pear_logxiLore1normPval = Pearcorr(logxi, lore1norm)
Pear_logxiLore2normCorr, Pear_logxiLore2normPval = Pearcorr(logxi, lore2norm)

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

Sp_mdotPowlawnormCorr, Sp_mdotPowlawnormPval = Spcorr(mdot, powlawnorm)
Sp_mdotLore1lineCorr, Sp_mdotLore1linePval = Spcorr(mdot, lore1line)
Sp_mdotLore2lineCorr, Sp_mdotLore2linePval = Spcorr(mdot, lore2line)
Sp_mdotLore1normCorr, Sp_mdotLore1normPval = Spcorr(mdot, lore1norm)
Sp_mdotLore2normCorr, Sp_mdotLore2normPval = Spcorr(mdot, lore2norm)

Sp_logxiPowlawnormCorr, Sp_logxiPowlawnormPval = Spcorr(logxi, powlawnorm)
Sp_logxiLore1lineCorr, Sp_logxiLore1linePval = Spcorr(logxi, lore1line)
Sp_logxiLore2lineCorr, Sp_logxiLore2linePval = Spcorr(logxi, lore2line)
Sp_logxiLore1normCorr, Sp_logxiLore1normPval = Spcorr(logxi, lore1norm)
Sp_logxiLore2normCorr, Sp_logxiLore2normPval = Spcorr(logxi, lore2norm)

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
