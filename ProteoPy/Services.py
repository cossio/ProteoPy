"""
Contains the Services class
"""
import bioservices
import mygene

from . import util


class Services(object):
    """
    Services to query online databases.
    """


    def __init__(self):
        self._unipro = bioservices.UniProt()
        self._mygene = mygene.MyGeneInfo()


    def uniprot_data(self, uniprotid):
        """
        Return the mass and sequence length of a protein, from its Uniprot ID.
        """

        uniprot_xml = self._unipro.retrieve(uniprotid + '_HUMAN', frmt='xml')

        mass = float([el.get('mass') for el in uniprot_xml.findAll('sequence')
                      if 'mass' in el.attrs][0])

        leng = float([el.get('length') for el in uniprot_xml.findAll('sequence')
                      if 'length' in el.attrs][0])

        return mass, leng


    def uniprot_id(self, geneid):
        """
        Gene id to uniprot id
        """

        uniprotid = self._mygene.query(geneid, scopes='symbol', fields='uniprot.Swiss-Prot',
                                       species='human')['hits'][0]['uniprot']['Swiss-Prot']

        if isinstance(uniprotid, list):
            uniprotid = uniprotid[0]

        uniprotid = str(uniprotid)
        return uniprotid


    def uniprotToEC(self, uniprotid):
        """
        Uniprot id to enzyme commision number (E.C. number)
        """

        q = self._mygene.query(uniprotid, scopes='uniprot', fields='ec', species='human')
        return str(q['hits'][0]['ec'])


    def goproteins(self, goid):
        """
        List of proteins (Uniprot IDs) for a GO annotation.
        """

        query = self._mygene.query(goid, scopes='goid', fields='uniprot.Swiss-Prot',
                                   species='human', fetch_all=True, verbose=False)

        result = [str(q['uniprot']['Swiss-Prot']) for q in query if 'uniprot' in q]
        # sometimes there are items like "[u'Q9BXH1', u'Q96PG8']", we need to flatten them
        result = [eval(r) if '[' in r else r for r in result]
        result = [str(r) for r in util.flatten(result)]
        return result


    def gogenes(self, goid):
        """
        List of genes for a GO annotation.
        """

        query = self._mygene.query(goid, scopes='goid', fields='symbol,alias',
                                   species='human', fetch_all=True, verbose=False)

        genes = []
        for q in query:
            genes.append(str(q['symbol']))
            if 'alias' in q:
                if isinstance(q['alias'], list):
                    for a in q['alias']:
                        genes.append(str(a))
                else:
                    genes.append(str(q['alias']))

        return genes


    def genealias(self, gene):
        """
        List of aliases of a gene
        """

        query = self._mygene.query(gene, scopes='symbol', fields='symbol,alias',
                                   species='human', fetch_all=True, verbose=False)

        genes = []
        for hit in query:
            genes.append(str(hit['symbol']))
            if 'alias' in hit:
                if isinstance(hit['alias'], list):
                    for alias in hit['alias']:
                        genes.append(str(alias))
                else:
                    genes.append(str(hit['alias']))

        return genes


    def genename(self, gene):
        '''
        Gene name from gene symbol
        '''

        query = self._mygene.query(gene, scopes='symbol', fields='name',
                                   species='human', fetch_all=True, verbose=False)

        return str(next(query)['name'])
