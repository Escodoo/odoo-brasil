# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
# Copyright (C) 2011  Renato Lima - Akretion                                    #
#                                                                               #
#This program is free software: you can redistribute it and/or modify           #
#it under the terms of the GNU Affero General Public License as published by           #
#the Free Software Foundation, either version 3 of the License, or              #
#(at your option) any later version.                                            #
#                                                                               #
#This program is distributed in the hope that it will be useful,                #
#but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#GNU General Public License for more details.                                   #
#                                                                               #
#You should have received a copy of the GNU General Public License              #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.          #
#################################################################################

{
    'name' : 'Account Payment',
    'description' : 'Brazilian Localization Account Payment',
    'category' : 'Localisation',
    'license': 'Affero GPL-3',
    'author' : 'Akretion, OpenERP Brasil',
    'website' : 'http://openerpbrasil.org',
    'version' : '0.6',
    'depends' : [
		        'l10n_br_base', 
                'l10n_br_account',
                'account_payment',
		        ],
    'init_xml' : [
		        #'l10n_br_account_payment_extension.csv',
		        ],
    'update_xml' : [
                    'l10n_br_account_payment_data.xml',
		            'account_invoice_view.xml',
                    'security/ir.model.access.csv',
                    'security/l10n_br_account_payment_security.xml',
                    ],
    'demo_xml': [
                'l10n_br_account_payment_demo.xml'
                ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: