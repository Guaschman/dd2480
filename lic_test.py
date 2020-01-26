import unittest
import json
import main

class LICTestCase(unittest.TestCase):

    """
    Test case for LIC0 function in module 'main'
    """
    def test_LIC0(self):
        main.PARAMETERS_T["LENGTH1"] = 30
        main.POINTS = [
            (0, 0), (1, -1), (3, 6), (1, 1),
            (1, 3), (2, 2), (-9, -5), (-1, -5),
            (2, 3), (-1, -5), (0, -2), (2, 2)]
        main.NUMPOINTS = len(main.POINTS)

        self.assertFalse(main.LIC0())

        main.PARAMETERS_T["LENGTH1"] = 17
        main.POINTS = [
            (0, 0), (1, -1), (3, 6), (1, 1),
            (1, 3), (2, 2), (-1, -5), (-1, -5),
            (2, 3), (-1, -5), (0, 0), (8, 15)]

        self.assertFalse(main.LIC0())

        main.POINTS = [
            (0, 0), (1, -1), (3, 6), (1, 1),
            (1, 3), (2, 2), (-9, -5), (-1, -5),
            (2, 3), (-1, -5), (0, 0), (8, 15.1)]

        self.assertTrue(main.LIC0())

    """
    Test case for LIC2 function in module 'main'
    """
    def test_LIC2(self):
        main.PARAMETERS_T["EPSILON"] = 0.5  # Tests NUMPOINTS < 3
        main.POINTS = [
            (0, 0), (1, -1)]
        main.NUMPOINTS = len(main.POINTS)

        self.assertFalse(main.LIC2())

        main.PARAMETERS_T["EPSILON"] = 0.87
        main.POINTS = [
            (2, 3), (1, 4), (0, 0), (3, 3)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertTrue(main.LIC2())

        main.PARAMETERS_T["EPSILON"] = 0.2
        main.POINTS = [
            (0, 1), (0, 0), (0, -1)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC2())

        main.PARAMETERS_T["EPSILON"] = 0.2 # Tests invalid angle
        main.POINTS = [
            (1, 1), (0, 0), (0, 0)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC2())

    """
    Test case for LIC3 function in module 'main'
    """
    def test_LIC3(self):
        main.AREA1 = 1
        main.POINTS = [[0,0],[1,0],[1,2]] # ==> area = 1
        main.NUMPOINTS = len(main.POINTS)

        self.assertTrue(main.LIC3())
        main.AREA1 = 0
        self.assertFalse(main.LIC3())

        main.POINTS = [[0,0],[1,0],[1,100]] # ==> area = 50
        main.AREA1 = 51
        self.assertTrue(main.LIC3())
        main.AREA1 = 49
        self.assertFalse(main.LIC3())

    """
    Test case for LIC4 function in module 'main'
    """
    def test_LIC4(self):

        main.Q_PTS = 4
        main.QUADS = 2
        main.POINTS = [
            (7, 8), (-12, 19), (-12, -22), (51, 91),
            (42, 85), (62, 32), (79, 15), (11, 95),
            (2, 73), (70, 50), (60, 32), (28, 24),
            (60, 29), (14, 59), (97, 71), (60, 45),
            (21, 17), (8, 49), (93, 74), (18, 66),
            (23, 26), (25, 44), (78, 40), (31, 25),
            (47, 84), (5, 56), (99, 34), (23, 26)]
        main.NUMPOINTS = len(main.POINTS)

        self.assertTrue(main.LIC4())

        main.Q_PTS = 3
        main.QUADS = 2
        main.POINTS = [
            (7, 8), (-12, 19), (-12, 22), (51, 91),
            (42, 85), (62, 32), (79, 15), (11, 95),
            (2, 73), (-70, -50), (60, -32), (28, 24),
            ]
        main.NUMPOINTS = len(main.POINTS)
        self.assertTrue(main.LIC4())

        main.QUADS = 3
        self.assertFalse(main.LIC4())

        main.Q_PTS = 1
        self.assertFalse(main.LIC4())

    """
    Test case for LIC5 function in module 'main'
    """
    def test_LIC5(self):
        main.POINTS = [
            (0, 0), (1, -1), (3, 6), (3, 1)]
        main.NUMPOINTS = len(main.POINTS)

        self.assertFalse(main.LIC5())

        main.POINTS = [
            (0, 0), (1, -1), (3, 6), (2, 1)]
        self.assertTrue(main.LIC5())

        self.assertTrue(main.LIC5())


    """
    Test case for LIC7 function in module 'main'
    """
    def test_LIC7(self):

        main.PARAMETERS_T["LENGTH1"] = 1  # Tests NUMPOINTS < 3
        main.PARAMETERS_T["K_PTS"] = 1
        main.POINTS = [
            (0, 0), (2, 2)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC7())

        main.PARAMETERS_T["LENGTH1"] = 1
        main.PARAMETERS_T["K_PTS"] = 2
        main.POINTS = [
            (0, 0), (2, 2), (0, 0), (3, 3)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC7())

        main.PARAMETERS_T["LENGTH1"] = 2
        main.PARAMETERS_T["K_PTS"] = 2
        main.POINTS = [
            (0, 0), (2, 2), (0, 0), (3,3)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC7())

    """
    Test case for LIC8 function in module 'main'
    """
    def test_LIC8(self):
        main.RADIUS1 = 0
        main.POINTS = [[0,0],[-1,-1],[-1,-1],[1,0],[1,2]]
        main.NUMPOINTS = len(main.POINTS)
        main.A_PTS = 3
        main.B_PTS = 1
        self.assertTrue(main.LIC8())
        main.RADIUS1 = 2
        self.assertFalse(main.LIC8())

    """
    Test case for LIC9 function in module 'main'
    """
    def test_LIC9(self):
        main.POINTS = [
            (3, 3), (-12, 19), (1, 1),
            (51, 91), (1, 3), (99, 99)
            ]
        main.NUMPOINTS = len(main.POINTS)
        main.C_PTS = 1
        main.D_PTS = 1
        main.EPSILON = 2.1
        main.PI = 3.1415926535
        self.assertTrue(main.LIC9())

        main.EPSILON = 4
        self.assertFalse(main.LIC9())

        main.EPSILON = 2.1
        main.D_PTS = 3
        self.assertFalse(main.LIC9())

    """
    Test case for LIC10 function in module 'main'
    """
    def test_LIC10(self):
        main.PARAMETERS_T["E_PTS"] = 1
        main.PARAMETERS_T["F_PTS"] = 1
        main.PARAMETERS_T["AREA1"] = 0
        main.POINTS = [
            (0, 0), (1, -1), (0, 0), (3, 1), (0, 0)]
        main.NUMPOINTS = len(main.POINTS)

        self.assertFalse(main.LIC10())

        main.PARAMETERS_T["AREA1"] = 18
        main.POINTS = [
            (0, 0), (1, -1), (0, 6), (2, 1), (6.01, 0)]

        self.assertTrue(main.LIC10())

    """
       Test case for LIC12 function in module 'main'
    """
    def test_LIC12(self):

        main.PARAMETERS_T["LENGTH1"] = 1  # Tests NUMPOINTS < 3
        main.PARAMETERS_T["LENGTH2"] = 1
        main.PARAMETERS_T["K_PTS"] = 1
        main.POINTS = [
            (0, 0), (1, -1)]
        main.NUMPOINTS = len(main.POINTS)

        self.assertFalse(main.LIC12())

        main.PARAMETERS_T["LENGTH1"] = 1
        main.PARAMETERS_T["LENGTH2"] = 4
        main.PARAMETERS_T["K_PTS"] = 2
        main.POINTS = [
            (0, 0), (0, 0), (0, 0), (3, 3)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC12())

        main.PARAMETERS_T["LENGTH1"] = 1
        main.PARAMETERS_T["LENGTH2"] = 1
        main.PARAMETERS_T["K_PTS"] = 1
        main.POINTS = [
            (0, 0), (2, 2), (0, 0), (3,3)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC12())

        main.PARAMETERS_T["LENGTH1"] = 5
        main.PARAMETERS_T["LENGTH2"] = 5
        main.PARAMETERS_T["K_PTS"] = 1
        main.POINTS = [
            (0, 0), (2, 2), (0, 0), (3, 3)]
        main.NUMPOINTS = len(main.POINTS)
        self.assertFalse(main.LIC12())

    """
    Test case for LIC13 function in module 'main'
    """
    def test_LIC13(self):
        main.RADIUS1 = 0
        main.RADIUS2 = 0
        main.POINTS = [[0,0],[-1,-1],[-1,-1],[1,0],[1,2]]
        main.NUMPOINTS = len(main.POINTS)
        main.A_PTS = 3
        main.B_PTS = 1
        self.assertFalse(main.LIC13())
        main.RADIUS2 = 10
        self.assertTrue(main.LIC13())

    """
       Test case for LIC14 function in module 'main'
    """
    def test_LIC14(self):
        main.E_PTS = 1
        main.F_PTS = 1
        main.NUMPOINTS = 5

        self.assertFalse(main.LIC14())

        main.POINTS = [
                (3, 3), (-12, 19), (1, 1),
                (51, 91), (1, 3), (99, 99)
            ]
        main.NUMPOINTS = len(main.POINTS)
        main.AREA1 = 4
        main.AREA2 = 400

        self.assertTrue(main.LIC14())

        main.AREA2 = 3000
        self.assertFalse(main.LIC14())

if __name__ == '__main__':
    unittest.main()