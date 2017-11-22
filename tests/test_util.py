from unittest import TestCase

import ProteoPy

class Test_util(TestCase):
    def setUp(self):
        self.compartment_proteins = [{'A', 'B'}, {'B', 'C'}]
        self.compartment_names = ['a', 'b']

    def test_compartmentidx(self):
        self.assertEqual(ProteoPy.util.compartmentidx('A', self.compartment_proteins), 0)
        self.assertEqual(ProteoPy.util.compartmentidx('B', self.compartment_proteins), 0)
        self.assertEqual(ProteoPy.util.compartmentidx('C', self.compartment_proteins), 1)
