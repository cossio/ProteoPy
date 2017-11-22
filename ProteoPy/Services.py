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

        query = self._mygene.query(goid, scopes='goid', fields='symbol',
                                   species='human', fetch_all=True, verbose=False)

        genes = [str(q['symbol']) for q in query]
        return genes
