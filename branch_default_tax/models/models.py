from odoo import api, fields, models
from odoo import Command


class BranchTaxConfig(models.Model):
    _name = "branch.tax.config"
    _description = "Branch Default Tax"

    company_id = fields.Many2one("res.company", required=True, ondelete="cascade")
    taxes_id = fields.Many2one(
        "account.tax",
        string="Default Sale Tax",
        domain="[('type_tax_use', '=', 'sale')]",
        required=True,
    )


class ResCompany(models.Model):
    _inherit = "res.company"

    branch_default_tax_ids = fields.One2many(
        "branch.tax.config", "company_id", string="Branch Default Taxes"
    )


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model_create_multi
    def create(self, vals_list):
        lines = super().create(vals_list)
        for line in lines:
            self._apply_branch_tax(line)
        return lines

    def write(self, vals):
        res = super().write(vals)
        if "product_id" in vals:
            for line in self:
                self._apply_branch_tax(line)
        return res

    @api.depends("product_id", "order_id.company_id")
    def _compute_tax_ids(self):
        no_branch = self.env["sale.order.line"]
        for line in self:
            if not line.product_id or not line.order_id:
                no_branch |= line
                continue
            if not self._apply_branch_tax(line):
                no_branch |= line
        if no_branch:
            super(SaleOrderLine, no_branch)._compute_tax_ids()

    @api.onchange("product_id")
    def _onchange_product_id(self):
        res = super()._onchange_product_id()
        if self.product_id and self.order_id and self.order_id.company_id:
            self._apply_branch_tax(self)
        return res

    def _apply_branch_tax(self, line):
        if not line.order_id or not line.order_id.company_id:
            return False
        config = (
            self.env["branch.tax.config"]
            .sudo()
            .search(
                [("company_id", "=", line.order_id.company_id.id)], limit=1
            )
        )
        if not config and line.order_id.company_id.parent_id:
            config = (
                self.env["branch.tax.config"]
                .sudo()
                .search(
                    [("company_id", "=", line.order_id.company_id.parent_id.id)],
                    limit=1,
                )
            )
        if config and config.taxes_id:
            line.tax_ids = [Command.set([config.taxes_id.id])]
            return True
        return False
