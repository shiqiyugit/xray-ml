from xspec import *

def mk_clumpy(nh_gal,z,
        pars=[1,3,4,10,11,20,25],
        par_vals=[1.0,1,1.8,1.0e-4,1.0e-3,0.6,1.0e-4],
        par_fixed=[True,False,False,False,False,True,False],
        one_epoch=True,
        par_var=[False,False,False,False,False,False,False],
        bxa = False):
    """
    default pars: constant, nH, Gamma, norm, omni
    """
    xspec.Xset.abund="wilm" #Abundances for the uxclumpy model
    m = xspec.model.Model("constant*phabs(atable{uxclumpy-cutoff.fits} + constant*atable{uxclumpy-cutoff-omni.fits} + mekal)")
    m(2).values = [nh_gal,-1]#ISM absorption
    m(5).values = [400,-1] #E-cutoff
    m(6).values = [45,-1] #TORsigma
    m(7).values = [0.4,-1] #CTKcover
    m(8).values = [90.0,-1] #Theta_inc
    m(9).values = [z,-1,0.0,0.0,10.0,10.0] #Redshift
    m(11).values = [1.0e-5,1.0e-5,1.0e-5,1.0e-5,0.1,0.1]
    m(21).values = [1.0,-1] #nH for soft excess
    m(23).values = [z,-1] #redshift


    ######## omni component
    if AllData.nGroups == 0:
        n_spec = 1
    else:
        n_spec = AllData.nGroups
    for i_model in range(1,n_spec+1):
        AllModels(i_model)(12).link = m(3)
        AllModels(i_model)(13).link = m(4)
        AllModels(i_model)(14).link = m(5)
        AllModels(i_model)(15).link = m(6)
        AllModels(i_model)(16).link = m(7)
        AllModels(i_model)(17).link = m(8)
        AllModels(i_model)(18).link = m(9)
        AllModels(i_model)(19).link = m(10)
    set_pars(m,pars,par_vals,par_fixed,one_epoch,
        par_var)
    m(1).values = 1.0,-1