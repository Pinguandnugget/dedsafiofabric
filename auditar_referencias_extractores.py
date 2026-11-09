#!/usr/bin/env python3
"""Escanea un JAR local; uso: python auditar_referencias_extractores.py ruta.jar"""
import sys,zipfile,json
terms=('BORG_EXTRACTOR','LIMBO_EXTRACTOR','NEREIDA_EXTRACTOR','BorgExtractorItem','LimboExtractorItem','NereidaExtractorItem')
with zipfile.ZipFile(sys.argv[1]) as z:
    classes={n:z.read(n) for n in z.namelist() if n.startswith('net/mcreator/dedsafio3/') and n.endswith('.class')}
print(json.dumps({t:[n for n,b in classes.items() if t.encode() in b] for t in terms},indent=2))
