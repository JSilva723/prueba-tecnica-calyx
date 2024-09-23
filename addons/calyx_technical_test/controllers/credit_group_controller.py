# -*- coding: utf-8 -*-
import json
import logging
from odoo import http, _

log = logging.getLogger(__name__)

class CreditGroupController(http.Controller):

    @http.route('/create_edit_credit_group', type='json', auth='public', methods=['POST'], csrf=False)
    def create_edit_credit_group(self, request):
        try:
            body = request.jsonrequest
            if not body:
                return  {'status': 400, 'message': _('Invalid JSON format')}

            credit_groups = body['credit_groups']
            if not credit_groups or not isinstance(credit_groups, list):
                return  {'status': 400, 'message': _('Invalid JSON format')}
            
            for group_data in credit_groups:
                name = group_data.get('name', '')
                if not name:
                    return  {'status': 400, 'message': _('Missing group name')}

                code = group_data.get('code', '')
                if not code:
                    return  {'status': 400, 'message': _('Missing group code')}

                credit_global = group_data.get('credit_global', '')
                if not credit_global:
                    return  {'status': 400, 'message': _('Missing group credit global')}
                try:
                    credit_global = float(credit_global)
                except ValueError:
                    return {'status': 400, 'message': _('The credit global must be number')}

                channel = group_data.get('channel', '')
                if not channel:
                    return  {'status': 400, 'message': _('Missing group channel')}
                try:
                    channel = int(channel)
                except ValueError:
                    return {'status': 400, 'message': _('The channel must be number')}

                # Get channel
                SaleChannel = request.env['calyx_technical_test.sale_channel'].sudo()
                channel_id = SaleChannel.search([('id', '=', channel)])
                if not channel_id:
                    return  {'status': 404, 'message': _('Channel not found (%s)', channel)}

                # Get credit grup
                CreditGroup = request.env['calyx_technical_test.credit_group'].sudo()
                credit_group_id = CreditGroup.search([('code', '=', code)])

                group = {
                    'name': name,
                    'code': code,
                    'channel_id': channel_id.id,
                    'credit_global': credit_global,
                }

                try:
                    # Edit group
                    if credit_group_id:
                        credit_group_id.write(group)
                    # Create group
                    else:
                        credit_group_id.create(group)  
                except Exception as e:
                    log.error(f'[ERROR]: {str(e)}')
                    return {'status': 500, 'message': _('Error on create or edit')}

            return  {'status': 200, 'message': 'ok'}
        except Exception as e:
            log.error(f'[ERROR]: {str(e)}')
            return {'status': 500, 'message': 'Ups...!'}