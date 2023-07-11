import numpy as np


def dice_coef(y_true, y_pred):
    y_true = np.ravel(y_true)
    y_pred = np.ravel(y_pred)
    intersection = np.sum(y_true * y_pred)
    return 2.0 * intersection / (np.sum(y_true) + np.sum(y_pred) + 1e-7)
