# Dedsafío 3 — Etapa 7: tres espadas con propiedades de Forge

Se inspeccionaron `HealingswordItem`, `IceSwordItem`, `EspadaItem` y sus clases internas `$1` (Tier) con `javap -c -p` desde el JAR aportado.

| ID | Durabilidad | Velocidad minería | Bonus Tier | Daño base espada | Velocidad de ataque | Nivel minado Forge | Encantabilidad |
|---|---:|---:|---:|---:|---:|---:|---:|
| healingsword | 2032 | 4 | 5 | 3 | -2.4 | 4 | 2 |
| ice_sword | 1561 | 8 | 5 | 3 | -2.4 | 0 | 10 |
| espada | 860 | 4 | 2 | 3 | -2.4 | 4 | 2 |

## Código nuevo
- `OriginalSwordMaterial.java`: adapta estadísticas Tier a interfaz ToolMaterial de Yarn 1.21.1, con reparación vacía.
- `Dedsafio3Items.java`: registra los tres IDs con `SwordItem` y modificadores de daño/velocidad; restantes IDs continúan provisionales.
- `AUDITORIA_ESPADAS_ETAPA_7.json`: valores recuperados y limitaciones.

## Pendiente crítico
- **NO** funciona todavía la curación ni congelación. El bytecode exige encantamientos `LEECHING_ASPECT` y `FREEZING_ASPECT`; se deben migrar ambos encantamientos, contadores, partículas, efectos y procedimientos antes de atribuir habilidades.
- El nivel de minería de Forge se conserva como dato, pero Fabric 1.21.1 usa etiquetas de bloques; hay que portar estas reglas (actualmente tag inverso de diamante provisional).
- La sintaxis se cotejó con documentación API Yarn 1.21.1, pero **NO ESTÁ COMPILADO NI PROBADO**. Tampoco afirmar compatibilidad de servidor Arclight.
- Quedan las 139 entradas genéricas restantes y 28 huevos sin portar, así como el resto de sistemas del mod.
