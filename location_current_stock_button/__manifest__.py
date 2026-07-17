{
    "name": "Location Current Stock Button",
    "version": "19.0.1.0.0",
    "category": "Inventory",
    "summary": "Smart button on location to show current stock",
    "description": """
        <div style="margin: 16px 0;">
            <p>Adds a <strong>smart button</strong> on stock location forms
            showing the current stock quantity, with quick access to the
            location's stock quants.</p>
        </div>
        <h3>Features</h3>
        <ul>
            <li>Smart button on stock location showing current stock quantity</li>
            <li>Computed stock field summing all positive quants per location</li>
            <li>One-click navigation to location stock quants</li>
        </ul>
        <h3>Usage</h3>
        <ol>
            <li>Open any <strong>Stock Location</strong> form</li>
            <li>View the <strong>Current Stock</strong> smart button in the top button box</li>
            <li>Click the button to navigate to the detailed stock quants list</li>
        </ol>
    """,
    "author": "Digital Art",
    "website": "https://www.digitalart.com",
    "depends": ["stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_location_views.xml",
    ],
    "images": ["static/description/thumbnail.png"],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
