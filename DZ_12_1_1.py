import A12_1
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        nik = A12_1.Runner('Nik')
        for _ in range(10):
            nik.walk()
        self.assertEqual(nik.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        nikita = A12_1.Runner('Nikita')
        for _ in range(10):
            nikita.run()
        self.assertEqual(nikita.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        niki = A12_1.Runner('Niki')
        ta = A12_1.Runner('Ta')
        for _ in range(10):
            niki.walk()
            ta.run()
        self.assertEqual((niki.distance,ta.distance), (50,100))
