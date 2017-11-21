"""
Contains the Services class
"""
import bioservices
import mygene


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


    def gogenes(self, goid):
        """
        List of proteins (Uniprot IDs) for a GO annotation.
        """

        result = self._mygene.query(goid, scopes='goid', fields='uniprot.Swiss-Prot',
                                    species='human')['hits']
        prots = [str(r['uniprot']['Swiss-Prot']) for r in result]
        return prots
