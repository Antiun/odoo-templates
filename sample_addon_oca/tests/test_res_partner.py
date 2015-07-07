# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2015 Antiun Ingenieria, SL (Madrid, Spain, http://www.antiun.com)
#                 Antonio Espinosa <antonioea@antiun.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests.common import TransactionCase


# One test case per method
class TestResPartner(TransactionCase):
    # Use case : Prepare some data for current test case
    # def setUp(self):
    #     super(TestResPartner, self).setUp()
    #     # More initializations here ...

    # Use case : Clean data after current test case
    # def tearDown(self):
    #     # Clean data here ...
    #     super(TestResPartner, self).tearDown()

    def test_some_action(self):
        record = self.env['res.partner'].create({'name': 'Firstname Lastname'})
        self.assertTrue(record)

        # Use case: Test some action
        # record.some_action()
        # self.assertEqual(
        #     record.field,
        #     expected_field_value)
