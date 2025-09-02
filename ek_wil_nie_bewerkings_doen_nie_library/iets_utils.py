import scipy.stats as stats
import numpy as np

def iets():
    return

def een_t_toets(data, mean):
    t_stat, p_val = stats.ttest_1samp(data, mean)
    return t_stat, p_val

def twee_t_toets(a, b):
    t_stat, p_val = stats.ttest_ind(a, b)
    return t_stat, p_val

def gepaard_t_toets(before, after):
    t_stat, p_val = stats.ttest_rel(before, after)
    return t_stat, p_val

def anova(*args):
    f_stat, p_val = stats.f_oneway(*args)
    return f_stat, p_val

def chi_kwadraat_onafhanklik(data):
    chi2_stat, p_val, dof, ex = stats.chi2_contingency(data)
    return chi2_stat, p_val

def chi_kwadraat_pasvorm(observed, expected):
    chi2_stat, p_val = stats.chisquare(observed, f_exp=expected)
    return chi2_stat, p_val

def f_toets(a, b):
    var1 = np.var(a, ddof=1)
    var2 = np.var(b, ddof=1)
    
    f_stat = var1 / var2
    dof1 = len(a) - 1
    dof2 = len(b) - 1
    p_val = stats.f.cdf(f_stat, dof1, dof2) if f_stat < 1 else 1 - stats.f.cdf(f_stat, dof1, dof2)
    return f_stat, p_val

def z_toets(data, pop_var):
    pop_std = np.sqrt(pop_var)

    sample_mean = np.mean(data)
    n = len(data)

    z_stat = (sample_mean - 500) / (pop_std / np.sqrt(n))
    p_val = 2 * (1 - stats.norm.cdf(np.abs(z_stat)))
    return z_stat, p_val