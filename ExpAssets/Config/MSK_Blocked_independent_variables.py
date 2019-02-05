from klibs.KLIndependentVariable import IndependentVariableSet

MSK_Blocked_ind_vars = IndependentVariableSet()

MSK_Blocked_ind_vars.add_variable('isoa', int, [100,200,300])
MSK_Blocked_ind_vars.add_variable('ttoa', int, [120,240,360,480,600])