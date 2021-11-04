import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    def test_saldo_vahenee_jos_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.5")
    
    def test_saldo_ei_vahene_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_ota_rahaa_palauttaa_true_jos_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.assertTrue(self.maksukortti.ota_rahaa(50))
    
    def test_ota_rahaa_palauttaa_false_jos_ei_rahaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(50))
        