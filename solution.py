import pandas as pd
import numpy as np

from scipy.stats import ttest_ind

chat_id = 121482204 # Ваш chat ID, не меняйте название переменной

def solution(control_sample, test_sample) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.09
    _, pval = ttest_ind(control_sample, test_sample, equal_var=False, alternative="two-sided")
    return pval < alpha # Ваш ответ, True или False
