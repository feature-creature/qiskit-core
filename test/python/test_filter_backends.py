# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name

"""Backends Filtering Test."""

from qiskit.wrapper import register, available_backends, least_busy
from .common import requires_qe_access, QiskitTestCase


class TestBackendFilters(QiskitTestCase):
    """QISKit Backend Filtering Tests."""

    @requires_qe_access
    def test_filter_config_dict(self, QE_TOKEN, QE_URL, hub=None, group=None, project=None):
        """Test filtering by dictionary of configuration properties"""
        register(QE_TOKEN, QE_URL, hub, group, project)
        filter_ = {'n_qubits': 5, 'local': False}
        filtered_backends = available_backends(filter_)
        self.assertTrue(filtered_backends)

    @requires_qe_access
    def test_filter_status_config_dict(self, QE_TOKEN, QE_URL, hub=None, group=None, project=None):
        """Test filtering by dictionary of mixed status/configuration properties"""
        register(QE_TOKEN, QE_URL, hub, group, project)
        filter_ = {'available': True, 'local': False, 'simulator': True}
        filtered_backends = available_backends(filter_)
        self.assertTrue(filtered_backends)

    @requires_qe_access
    def test_filter_config_callable(self, QE_TOKEN, QE_URL, hub=None, group=None, project=None):
        """Test filtering by lambda function on configuration properties"""
        register(QE_TOKEN, QE_URL, hub, group, project)
        filtered_backends = available_backends(lambda x: (not x.configuration['simulator'] and
                                                          x.configuration['n_qubits'] > 5))
        self.assertTrue(filtered_backends)

    @requires_qe_access
    def test_filter_least_busy(self, QE_TOKEN, QE_URL, hub=None, group=None, project=None):
        """Test filtering by least busy function"""
        register(QE_TOKEN, QE_URL, hub, group, project)
        filtered_backends = least_busy(available_backends())
        self.assertTrue(filtered_backends)
