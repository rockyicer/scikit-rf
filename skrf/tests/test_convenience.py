
import unittest
import os
import numpy as npy

import skrf as rf


class ConvenienceTestCase(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.test_dir = os.path.dirname(os.path.abspath(__file__))+'/'
        self.hfss_oneport_file = os.path.join(self.test_dir, 'hfss_oneport.s1p')
        self.hfss_twoport_file = os.path.join(self.test_dir, 'hfss_twoport.s2p')
        self.ntwk1 = rf.Network(os.path.join(self.test_dir, 'ntwk1.s2p'))
        self.ntwk2 = rf.Network(os.path.join(self.test_dir, 'ntwk2.s2p'))
        self.ntwk3 = rf.Network(os.path.join(self.test_dir, 'ntwk3.s2p'))


    def test_hfss_touchstone_2_media(self):
        '''
        currently, this just tests the execution ability. it would
        be better to simulate a uniform line, in hfss and then confirm
        that the hfss network is same as the one generated by the
        media object this function returns
        '''
        med = rf.hfss_touchstone_2_media(self.hfss_oneport_file)[0]
        med.line(1)
        med_p1,med_p2 = rf.hfss_touchstone_2_media(self.hfss_twoport_file)
        med_p1.line(1)
        med_p2.line(1)
        
    def test_hfss_touchstone_renormalization(self):
        '''
        Scattering matrices are given for a given impedance z0, 
        which is usually assumed to be 50 Ohm, unless otherwise stated.
        
        Touchstone files are not necessarly indicating such impedances, 
        especially if they vary with frequency.
        
        HFSS Touchstone file format supports port informations (as an option) for gamma and z0
        When HFSS file are read with hfss_touchstone_2_network(),
        the port informations are taken into account, while this is not the case with Network()
        since the latter function should work with any Touchstone files, not especially HFSS's.
        '''
        # Comparing the S-params of the same device expressed with same z0 
        nw_50 = rf.hfss_touchstone_2_network(os.path.join(self.test_dir, 'hfss_threeport_DB_50Ohm.s3p'))
        nw = rf.hfss_touchstone_2_network(os.path.join(self.test_dir, 'hfss_threeport_DB.s3p'))
        nw.renormalize(z_new=50)       
        self.assertTrue(npy.all(npy.abs(nw.s - nw_50.s) < 1e-6))
        

