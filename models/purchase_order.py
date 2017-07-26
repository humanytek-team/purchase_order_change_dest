from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _get_addres(self):
        company = self.env['res.company'].browse(1)
        return company.street + ' ' + company.l10n_mx_street3 + '\n' +
        company.street2 + '\n' + company.state_id.name + ' ' + company.country_id.name + ' ' + company.zip

    new_dest = fields.Text(
        default=lambda self: self._get_addres(),
        required=True,
    )
