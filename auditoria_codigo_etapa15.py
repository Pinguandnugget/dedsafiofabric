from pathlib import Path
import json, re, sys
base=Path(__file__).resolve().parent
javas=list((base/'src/main/java').rglob('*.java'))
resources=list((base/'src/main/resources').rglob('*.json'))
errors=[]
for p in resources:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'JSON {p.relative_to(base)}: {e}')
ids={}
for p in javas:
    s=p.read_text(encoding='utf-8')
    if not s.startswith('package '): errors.append(f'No package: {p.name}')
    if s.count('{')!=s.count('}'): errors.append(f'Llaves no balanceadas: {p.name}')
mod=json.loads((base/'src/main/resources/fabric.mod.json').read_text())
if mod.get('version')!='${version}': errors.append('La version fabric.mod.json no se expande desde Gradle')
wf=base/'.github/workflows/compilar-fabric.yml'
if not wf.exists(): errors.append('Falta workflow de compilacion')
print(f'Fuentes Java: {len(javas)}; JSON legibles: {len(resources)}; incidencias estructurales: {len(errors)}')
for e in errors: print('ERROR',e)
print('ADVERTENCIA: esta prueba no compila ni valida las APIs Yarn/Fabric.')
sys.exit(bool(errors))
