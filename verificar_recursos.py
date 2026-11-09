#!/usr/bin/env python3
"""Comprobador estatico sin dependencias. No sustituye gradle build."""
from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parent
base=root/'src/main/resources'
errors=[]; count=0
for path in base.rglob('*.json'):
    count+=1
    try: json.loads(path.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{path.relative_to(root)}: {e}')
if (base/'data/dedsafio3/loot_tables').exists(): errors.append('Ruta antigua loot_tables presente')
if not (base/'data/dedsafio3/loot_table').exists(): errors.append('Falta ruta loot_table')
if (base/'data/dedsafio3/recipes').exists(): errors.append('Ruta antigua recipes presente')
recipes=list((base/'data/dedsafio3/recipe').glob('*.json'))
if not recipes: errors.append('No hay recetas migradas')
for recipe in recipes:
    r=json.loads(recipe.read_text(encoding='utf-8')).get('result')
    if isinstance(r,dict) and ('item' in r or 'nbt' in r or 'id' not in r):
        errors.append(f'Resultado de receta incompatible: {recipe.name}')
print(f'Recetas en ruta 1.21.1: {len(recipes)}')
m=json.loads((base/'fabric.mod.json').read_text())
if m.get('id')!='dedsafio3': errors.append('Namespace distinto de dedsafio3')
print(f'JSON revisados: {count}; errores: {len(errors)}')
for e in errors: print('ERROR:', e)
print('No se verifica compilacion Java ni mecánicas.')
sys.exit(bool(errors))
