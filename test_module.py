# test_module.py

import unittest
import os

class TestSeaLevelPredictor(unittest.TestCase):

    def test_plot_exists(self):
        self.assertTrue(os.path.isfile("sea_level_plot.png"), "Grafik dosyası bulunamadı.")

    def test_plot_dimensions(self):
        self.assertGreater(os.path.getsize("sea_level_plot.png"), 0, "Grafik dosyası boş.")

if __name__ == "__main__":
    unittest.main()