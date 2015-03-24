# -*- coding: utf-8 -*-
"""
Deprecation tests.

Remove file once 0.11 has been released!
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

import importlib
import unittest
import warnings

import obspy
from obspy import ObsPyDeprecationWarning


class DeprecatedImportsTestSuite(unittest.TestCase):
    """
    "Tests" that the deprecated, rerouted imports work.
    """
    def test_normal_imports(self):
        """
        Tests direct imports.
        """
        def _test_rerouted_imps(old_imp, new_imp):
            with warnings.catch_warnings(record=True) as w:
                mod_1 = importlib.import_module(old_imp)
                mod_2 = importlib.import_module(new_imp)
            self.assertTrue(mod_1 is mod_2)
            self.assertTrue(len(w), 1)
            self.assertTrue(w[0].category is ObsPyDeprecationWarning)
            self.assertTrue(old_imp in str(w[0].message))
            self.assertTrue(new_imp in str(w[0].message))

        # Just test everything as it originally contained some typos...
        _test_rerouted_imps("obspy.ah", "obspy.io.ah")
        _test_rerouted_imps("obspy.cnv", "obspy.io.cnv")
        _test_rerouted_imps("obspy.css", "obspy.io.css")
        _test_rerouted_imps("obspy.datamark", "obspy.io.datamark")
        _test_rerouted_imps("obspy.kinemetrics", "obspy.io.kinemetrics")
        _test_rerouted_imps("obspy.mseed", "obspy.io.mseed")
        _test_rerouted_imps("obspy.gse2", "obspy.io.gse2")
        _test_rerouted_imps("obspy.sac", "obspy.io.sac")
        _test_rerouted_imps("obspy.xseed", "obspy.io.xseed")
        _test_rerouted_imps("obspy.ndk", "obspy.io.ndk")
        _test_rerouted_imps("obspy.nlloc", "obspy.io.nlloc")
        _test_rerouted_imps("obspy.pdas", "obspy.io.pdas")
        _test_rerouted_imps("obspy.pde", "obspy.io.pde")
        _test_rerouted_imps("obspy.seg2", "obspy.io.seg2")
        _test_rerouted_imps("obspy.segy", "obspy.io.segy")
        _test_rerouted_imps("obspy.seisan", "obspy.io.seisan")
        _test_rerouted_imps("obspy.sh", "obspy.io.sh")
        _test_rerouted_imps("obspy.wav", "obspy.io.wav")
        _test_rerouted_imps("obspy.y", "obspy.io.y")
        _test_rerouted_imps("obspy.zmap", "obspy.io.zmap")
        _test_rerouted_imps("obspy.station", "obspy.core.inventory")
        _test_rerouted_imps("obspy.fdsn", "obspy.clients.fdsn")
        _test_rerouted_imps("obspy.arclink", "obspy.clients.arclink")
        _test_rerouted_imps("obspy.earthworm", "obspy.clients.earthworm")
        _test_rerouted_imps("obspy.iris", "obspy.clients.iris")
        _test_rerouted_imps("obspy.neic", "obspy.clients.neic")
        _test_rerouted_imps("obspy.neries", "obspy.clients.neries")
        _test_rerouted_imps("obspy.seedlink", "obspy.clients.seedlink")
        _test_rerouted_imps("obspy.seishub", "obspy.clients.seishub")
        _test_rerouted_imps("obspy.core.util.geodetics", "obspy.geodetics")
        _test_rerouted_imps("obspy.core.ascii", "obspy.io.ascii")
        _test_rerouted_imps("obspy.core.quakeml", "obspy.io.quakeml")
        _test_rerouted_imps("obspy.core.stationxml", "obspy.io.stationxml")
        _test_rerouted_imps("obspy.core.json", "obspy.io.json")

    def test_attribute_import(self):
        """
        Tests deprecated attribute imports, e.g.

        >>> import obspy  # doctest: +SKIP
        >>> obspy.station.Inventory  # doctest: +SKIP

        should still work. This cannot be handled by fiddling with the
        import meta paths as this is essentially equal to attribute access
        on the modules.
        """
        # Old obspy.station. This has potentially been used a lot.
        self.assertTrue(obspy.station.Inventory is
                        obspy.core.inventory.Inventory)
        self.assertTrue(obspy.station.Network is
                        obspy.core.inventory.Network)
        self.assertTrue(obspy.station.Station is
                        obspy.core.inventory.Station)
        self.assertTrue(obspy.station.Channel is
                        obspy.core.inventory.Channel)
        # Submodule imports.
        self.assertTrue(obspy.station, obspy.core.inventory)
        self.assertTrue(obspy.mseed, obspy.io.mseed)
        self.assertTrue(obspy.xseed, obspy.io.xseed)
        self.assertTrue(obspy.fdsn, obspy.clients.fdsn)
        # obspy.geodetics used to be part of obspy.core.util.
        self.assertTrue(obspy.core.util.geodetics is obspy.geodetics)
        # Parser.
        self.assertTrue(obspy.xseed.Parser is obspy.io.xseed.Parser)
        # File formats previously part of obspy.core.
        self.assertTrue(obspy.core.stationxml is
                        obspy.io.stationxml.stationxml)
        self.assertTrue(obspy.core.json is
                        obspy.io.json.json)
        self.assertTrue(obspy.core.ascii is
                        obspy.io.ascii.ascii)
        self.assertTrue(obspy.core.quakeml is
                        obspy.io.quakeml.quakeml)


def suite():
    return unittest.makeSuite(DeprecatedImportsTestSuite, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
