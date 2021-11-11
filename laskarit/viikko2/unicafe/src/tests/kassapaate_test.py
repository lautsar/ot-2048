import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassan_alkusaldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_alkusaldo_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_alkusaldo_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullinen_kateisosto_kun_rahaa_on_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateisosto_kun_rahaa_on_rahaa_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullinen_kateisosto_kun_rahaa_on_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
    
    def test_edullinen_kateisosto_kun_rahaa_ei_ole_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_kateisosto_kun_rahaa_ei_ole_rahaa_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_kateisosto_kun_rahaa_ei_ole_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
    
    def test_maukas_kateisosto_kun_rahaa_on_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_kun_rahaa_on_rahaa_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukas_kateisosto_kun_rahaa_on_rahaa_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
    
    def test_maukas_kateisosto_kun_rahaa_ei_ole_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_kateisosto_kun_rahaa_ei_ole_rahaa_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_kateisosto_kun_rahaa_ei_ole_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_syo_edullisesti_kortilla_rahaa(self):
        maksukortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
    
    def test_syo_edullisesti_kortilla_rahaa_myydyt_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_rahaa_kassa_ei_muutu(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kortilla_rahaa_ei_ole(self):
        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))

    def test_syo_edullisesti_kortilla_rahaa_ei_ole_myydyt_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_kortilla_rahaa_ei_ole_kassa_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_rahaa(self):
        maksukortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
    
    def test_syo_maukkaasti_kortilla_rahaa_myydyt_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_rahaa_kassa_ei_muutu(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kortilla_rahaa_ei_ole(self):
        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))

    def test_syo_maukkaasti_kortilla_rahaa_ei_ole_myydyt_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_maukkaasti_kortilla_rahaa_ei_ole_kassa_ei_muutu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_kasvaa_kun_ladataan(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortti_kasvaa_kun_ladataan(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(maksukortti.saldo, 2000)

    def test_kassa_ei_kasva_jos_ladataan_alle_nolla(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_ei_kasva_jos_ladataan_alle_nolla(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(maksukortti.saldo, 1000)