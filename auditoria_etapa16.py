#!/usr/bin/env python3
"""Auditoría estática de registro, recetas y JSON. No sustituye la compilación."""
from pathlib import Path
import json,re,sys,collections
root=Path(__file__).resolve().parent
res=root/'src/main/resources'
java=root/'src/main/java/dev/potitosafio/dedsafio3'
errors=[]; warnings=[]; json_count=0
for p in res.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf8')); json_count+=1
    except Exception as exc: errors.append(f'JSON inválido {p.relative_to(root)}: {exc}')
blocks=(java/'Dedsafio3Blocks.java').read_text()
items=(java/'Dedsafio3Items.java').read_text()
# Counts limited to actual literals in the registry definition; not documentation.
block_ids=re.findall(r'\b(?:simple|slab|stairs|specialDirectional)\("([a-z0-9_]+)"',blocks)+['test_rng_block']
block_ids=[x if x!='rngBlock()' else 'test_rng_block' for x in block_ids]
item_list=re.search(r'ORIGINAL_ITEM_IDS\s*=\s*\{(.*?)\};',items,re.S)
item_ids=re.findall(r'"([a-z0-9_]+)"',item_list.group(1)) if item_list else []
for what,vals in [('bloques',block_ids),('ítems',item_ids)]:
    dupe=[v for v,c in collections.Counter(vals).items() if c>1]
    if dupe: errors.append(f'IDs duplicados en {what}: {dupe}')
registered=set(block_ids)|set(item_ids)
if set(block_ids)&set(item_ids): errors.append('Registro duplicado entre BlockItem e Item: '+str(sorted(set(block_ids)&set(item_ids))))
recipe_dir=res/'data/dedsafio3/recipe'
recipes=sorted(recipe_dir.glob('*.json'))
for path in recipes:
    try: data=json.loads(path.read_text(encoding='utf8'))
    except Exception: continue
    kind=data.get('type','')
    if kind not in ('minecraft:crafting_shaped','minecraft:crafting_shapeless','minecraft:smithing_transform','minecraft:smelting','minecraft:blasting','minecraft:stonecutting','minecraft:campfire_cooking','minecraft:smoking'):
        warnings.append(f'Tipo no cubierto por auditoría: {path.name} ({kind})')
    result=data.get('result')
    result_id = result if isinstance(result,str) else result.get('id') if isinstance(result,dict) else None
    if not isinstance(result_id,str):
        errors.append(f'{path.name}: resultado inválido para receta {kind}')
    elif result_id.startswith('dedsafio3:') and result_id.split(':',1)[1] not in registered:
        errors.append(f'{path.name}: resultado propio no registrado: {result_id}')
    if kind=='minecraft:crafting_shaped':
        pattern=data.get('pattern',[]); keys=data.get('key',{})
        if not isinstance(pattern,list) or not pattern or len(pattern)>3 or any(not isinstance(row,str) or len(row)>3 for row in pattern):
            errors.append(f'{path.name}: patrón inválido')
        elif not isinstance(keys,dict): errors.append(f'{path.name}: key inválida')
        else:
            used=set(''.join(pattern)) - {' '}
            if used!=set(keys): errors.append(f'{path.name}: símbolos de patrón {sorted(used)} != claves {sorted(keys)}')
    if kind=='minecraft:crafting_shapeless' and not isinstance(data.get('ingredients'),list):
        errors.append(f'{path.name}: ingredients no es lista')
    ingredients=[]
    def visit(x, parent=''):
        if isinstance(x,dict):
            for k,v in x.items():
                if k=='item' and isinstance(v,str): ingredients.append(v)
                elif k not in ('result',): visit(v,k)
        elif isinstance(x,list):
            for v in x:visit(v,parent)
    visit(data)
    for id_ in ingredients:
        if id_.startswith('dedsafio3:') and id_.split(':',1)[1] not in registered:
            errors.append(f'{path.name}: ingrediente propio no registrado: {id_}')
for id_ in block_ids:
    if not (res/f'assets/dedsafio3/blockstates/{id_}.json').exists():
        warnings.append(f'Sin blockstate: {id_}')
for id_ in item_ids:
    if not (res/f'assets/dedsafio3/models/item/{id_}.json').exists():
        warnings.append(f'Sin modelo de ítem: {id_}')
print(f'ETAPA 16: {json_count} JSON válidos; {len(block_ids)} IDs de bloques; {len(item_ids)} IDs de ítems; {len(recipes)} recetas')
print(f'Errores detectados: {len(errors)}; advertencias: {len(warnings)}')
for e in errors:print('ERROR:',e)
for w in warnings:print('AVISO:',w)
print('NOTA: revisión estática. No prueba que el código Java compile ni que las mecánicas funcionen.')
sys.exit(1 if errors else 0)
