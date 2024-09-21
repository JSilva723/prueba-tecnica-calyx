# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request

import logging
log = logging.getLogger(__name__)

class CreditGroupController(http.Controller):
    
    @http.route('/create_credit_group', type='json', auth='public', methods=['POST'], csrf=False)
    def create_credit_group(self):
        try:
            body = http.request.jsonrequest
            if not body:
                return {'status': 400, 'message': 'Invalid JSON format'}
            
            credit_groups = body['credit_groups']
            if not credit_groups or not isinstance(credit_groups, list):
                return {'status': 400, 'message': 'Invalid JSON format'}
            
            for group_data in credit_groups:
                name = group_data.get('name', '')
                if not name:
                    return {'status': 400, 'message': 'Missing group name'}

            return {'status': 200, 'message': 'ok'}
        
        except Exception as e:
            log.error(f'[ERROR]: {str(e)}')
            return {'status': 500, 'message': 'Ups..!'}