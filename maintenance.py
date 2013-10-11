from openerp.osv import fields, osv

class maintenance_asset_type(osv.Model):
    _name = 'maintenance.asset.type'
    _columns = {
        'name': fields.char('Name', required=True),
    }

maintenance_asset_type()

class maintenance_asset(osv.Model):

    _name = 'maintenance.asset'
    _columns = {
        'asset_type_id': fields.many2one('maintenance.asset.type', 'Type'),
        'serial_number': fields.char('Serial Number', size=32, required=True, help='Serial Number of this asset'),
        'employee_id': fields.many2one('hr.employee', 'Employee', help='Employee who has this machine'),
        'acquisition_date': fields.date('Acquisition Date', help='Date when the asset has been bought'),
        'location': fields.char('Location', size=128, help='Location of the asset'),
        'value': fields.float('asset Value', help='Value of the bought asset'),
        }
        
maintenance_asset()


class maintenance_service_type(osv.Model):
    _name = 'maintenance.service.type'
    _columns = {
        'name': fields.char('Name', required=True),
    }
    
maintenance_service_type()

class maintenance_service(osv.Model):

    _name = 'maintenance.service'
    _columns = {
        'order_id' : fields.many2one('maintenance.order', 'Order', required=True),
        'service_type_id': fields.many2one('maintenance.service.type', 'Type', required=True),
        'finish_date': fields.date('Finish Date'),
        'notes': fields.text('Notes'),
    }
    
maintenance_service()
