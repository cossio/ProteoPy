from unittest import TestCase

import ProteoPy

class TestServices(TestCase):
    def setUp(self):
        self.services = ProteoPy.Services()

    def test_uniprot_id(self):
        self.assertEqual(self.services.uniprot_id('G6PD'), 'P11413')
        self.assertEqual(self.services.uniprot_id('PGD'), 'P52209')

    def test_uniprot_data(self):
        self.assertEqual(self.services.uniprot_data('O95336'), (27547.0, 258.0))
        self.assertEqual(self.services.uniprot_data('P29401'), (67878.0, 623.0))

    def test_gogenes(self):
        self.assertEqual(self.services.gogenes('GO:0009051'), ['O95336', 'P52209', 'P11413'])
        self.assertEqual(self.services.gogenes('GO:0009052'), ['P49247', 'Q2QD12', 'P29401', 'P37837', 'Q96AT9', 'Q9UHJ6'])
