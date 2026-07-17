from odoo import api, fields, models


class StockLocation(models.Model):
    _inherit = "stock.location"

    stock_quantity = fields.Float(
        string="Current Stock",
        compute="_compute_stock_quantity",
        digits="Product Unit of Measure",
    )

    def _compute_stock_quantity(self):
        quant_data = self.env["stock.quant"].read_group(
            [("location_id", "in", self.ids), ("quantity", ">", 0)],
            ["quantity:sum"],
            ["location_id"],
        )
        mapped = {data["location_id"][0]: data["quantity"] for data in quant_data}
        for loc in self:
            loc.stock_quantity = mapped.get(loc.id, 0.0)

    def action_open_stock_quants(self):
        self.ensure_one()
        return {
            "name": "Stock by Location",
            "type": "ir.actions.act_window",
            "res_model": "stock.quant",
            "view_mode": "list,form",
            "domain": [("location_id", "=", self.id), ("quantity", ">", 0)],
            "context": {
                "search_default_location_id": self.id,
            },
        }
