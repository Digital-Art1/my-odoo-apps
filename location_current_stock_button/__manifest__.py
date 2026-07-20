{
    "name": "Location Current Stock Button",
    "version": "19.0.1.0.0",
    "category": "Inventory",
    "summary": "Smart button on location to show current stock",
    "description": "Smart button on stock location showing current stock quantity",

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
