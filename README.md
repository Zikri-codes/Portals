# Portals
A Minecraft Tool Assist that can save coordinates and converting between nether and overworld for better transportation

## Features
- Convert Nether ↔ Overworld coordinates
- Save coordinates with a custom name
- JSON-based Storage
- Clean CLI menu system
- No external dependencies

## Requirements
- Python 3.10+

## How to Use

### 1. Clone Repo
```bash
git clone https://github.com/Zikri-codes/Portals.git
cd Portals
```
### 2. Run Main Script
```bash
python main.py
```
### 3. Menu / Commands
- **Add portal**: add a new portal to storage
- **Show portals**: display all saved portals
- **Delete portal**: remove a portal by index
- **Converter**: convert Nether ↔ Overworld coordinates
### 4. Example
**Converter**
```Text
----------------------------------------
Nether → Overworld : Converter

Input : X | Y | Z
Input : 125 125

Output : 1000 | y? | 1000
----------------------------------------
```
**Add Portal**
```Text
----------------------------------------
Name      : Example
Dimension : Overworld
Coords    : 1000 1000

"Example" Has been added to the portals
----------------------------------------
```
**Delete Portal**
```Text
----------------------------------------
Wich portals do you want to delete? 0 for cancel
1. Testing
2. Base
3. Gold Farm
4. Example

Choose(num) : 1

"Testing" Has been deleted
----------------------------------------
```
**Show Portals**
```Text
----------------------------------------
The List of The Portals:
1. Base | Overworld | ['-1068', 'y?', '163']
2. Gold Farm | Overworld | ['-1134', 'y?', '167']
3. Example | Overworld | ['1000', 'y?', '1000']
----------------------------------------
```

## File Structure
```
Portals/
├── main.py          # CLI entry point
├── core/            # conversion & validation logic
│   ├── __init__.py
│   ├── converter.py
│   ├── validator.py
│   └── formatter.py
├── storage/         # portal data management
│   ├── __init__.py
│   ├── datamanager.py
│   └── portals.json
├── utils/           # CLI UI helpers
│   ├── __init__.py
│   └── menu.py
├── README.md
├── .gitignore
└── LICENSE
```

## Notes
- All portal coordinates are stored in storage/portals.json.
- Y-coordinate is optional when adding a portal.
