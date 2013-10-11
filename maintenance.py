from openerp.osv import fields, osv

class maintenance_asset_type(osv.Model):
    _name = 'maintenance.asset.type'
    _columns = {
        'name': fields.char('Name', required=True),
    }

maintenance_asset_type()
