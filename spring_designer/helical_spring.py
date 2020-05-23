#!/usr/bin/env python3

class HelicalCompressionSpring:
    """A class for the design of helical compression springs. Based upon
    Shigley's Mechanical Engineering Design."""

    def __init__(self, d, D, C, OD, Na, Ls, L0, L0cr, ns, fom):
        """Constructor method for the HelicalCompressionSpring class.
        Takes a priori decisions and sets them as the initial guess."""
        self.material = "Hard-drawn wire"
        self.d = d
        self.D = D
        self.C = C
        self.OD = OD
        self.Na = Na
        self.Ls = Ls
        self.L0 = L0
        self.L0cr = L0cr
        self.ns = ns
        self.fom = fom

    def getUltimateStrength(self):
        """Takes HelicalCompressionSpring object and uses diameter and
        material to find the ultimate strength of the spring."""

        print('Connecting to database...')
        conn = sqlite3.connect('../tables/test.dB')
        print('Connection successful!')

        cursor = conn.execute('''
        select material, exponent, A_metric from table10_4
        where material = ?
        ''', (self.material))

        entry = cursor.fetchone()

        return (A/d**m)
