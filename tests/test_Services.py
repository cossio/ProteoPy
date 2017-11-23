"""
Tests for the Services class
"""

from unittest import TestCase

import ProteoPy

class TestServices(TestCase):
    """
    Contains tests for the Services class
    """

    def setUp(self):
        self.services = ProteoPy.Services()


    def test_uniprot_id(self):
        '''
        Tests Services.uniprot_id method.
        '''
        self.assertEqual(self.services.uniprot_id('G6PD'), 'P11413')
        self.assertEqual(self.services.uniprot_id('PGD'), 'P52209')


    def test_uniprot_data(self):
        '''
        Tests Services.uniprot_data method.
        '''
        self.assertEqual(self.services.uniprot_data('O95336'), (27547.0, 258.0))
        self.assertEqual(self.services.uniprot_data('P29401'), (67878.0, 623.0))


    def test_goproteins(self):
        '''
        Tests Services.goproteins method.
        '''
        self.assertEqual(self.services.goproteins('GO:0009051'),
                         ['O95336', 'P52209', 'P11413'])
        self.assertEqual(self.services.goproteins('GO:0009052'),
                         ['P49247', 'Q2QD12', 'P29401', 'P37837', 'Q96AT9', 'Q9UHJ6'])


    def test_gogenes(self):
        '''
        Tests Services.gogenes method.
        '''
        self.assertEqual(self.services.gogenes('GO:0009051'),
                         ['PGLS', '6PGL', 'HEL-S-304', 'PGD', '6PGD', 'G6PD', 'G6PD1'])
        self.assertEqual(self.services.gogenes('GO:0009052'),
                         ['RPIA', 'RPI', 'RPIAD', 'RPEL1', 'TKT', 'HEL-S-48', 'HEL107',
                          'SDDHD', 'TK', 'TKT1', 'TALDO1', 'TAL', 'TAL-H', 'TALDOR',
                          'TALH', 'RPE', 'RPE2-1', 'SHPK', 'CARKL', 'SHK'])
