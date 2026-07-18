{
    "name": "Branch Default Tax",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "summary": "Default sale tax per company/branch with parent fallback",
    "description": """
        <div style="margin: 16px 0;">
            <p>Configure <strong>default sale taxes per company/branch</strong>.
            When creating a sales order, the tax lines are automatically set
            based on the order's company, with fallback to the parent company
            if no specific configuration exists.</p>
        </div>
        <h3>Features</h3>
        <ul>
            <li>Per-company default sale tax configuration</li>
            <li>Automatic tax application on sale order line creation</li>
            <li>Tax updates when product is changed on existing order lines</li>
            <li>Parent company tax fallback when no direct config exists</li>
            <li>Seamless integration with Odoo Sales &amp; Accounting</li>
        </ul>
        <h3>Configuration</h3>
        <ol>
            <li>Go to <strong>Settings &gt; Companies</strong> and select a company</li>
            <li>In the <strong>Branch Default Taxes</strong> tab, add a tax config</li>
            <li>Sales orders will automatically apply the configured tax</li>
        </ol>
    """,
    "author": "Digital Art",
    "website": "https://www.digitalart.com",
    "depends": ["sale", "account"],
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
    ],
    "images": ["static/description/thumbnail.png"],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
