import unittest
import DZ_12_1_1
import DZ_12_2

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(DZ_12_2.TournamentTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(DZ_12_1_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)

