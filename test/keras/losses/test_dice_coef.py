import unittest

import numpy as np

from bisbislib.keras.losses import dice_coef


class TestDiceCoef(unittest.TestCase):
    def test_dice_coef(
        self
    ):
        y_true = np.ones((28, 28), dtype=np.float32)
        y_pred = np.ones((28, 28), dtype=np.float32)
        y_pred[0][0] = 0.0

        result = dice_coef(y_true, y_pred)
        result = np.round(result, 3)
        self.assertEqual(result, 0.999)
