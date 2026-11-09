# Etapa 13 — Extractores Borg, Limbo y Nereida (código experimental)

## Hallazgos del JAR original

Se comprobó con `javap -c -p` sobre `dedsafio3-0.0.9-forge-1.20.1.jar` que las clases `BorgExtractorItem`, `LimboExtractorItem` y `NereidaExtractorItem` crean ítems con durabilidad máxima **200** y no apilables. En cada `inventoryTick` comprueban `200 - getDamage() >= 200` y, si el stack está en la mano principal o secundaria, lo reemplazan por `BORG_EXTRACTOR_FILLED`, `LIMBO_EXTRACTOR_FILLED` o `NEREIDA_EXTRACTOR_FILLED`, respectivamente.

## Cambios reales de la Etapa 13

- `Dedsafio3Items.java`: los cinco IDs de extractores vacíos (Nether, Overworld, Borg, Limbo, Nereida) crean instancias `OriginalExtractorItem` con máximo daño 200.
- `OriginalExtractorItem.java`: conversión genérica a sus cinco variantes `_filled`, respetando la condición de estar en alguna de las manos; identificación mediante namespace + path y protección si falta el ID de destino.
- El tooltip de Borg/Limbo/Nereida ya no afirma que se cargan matando mobs, porque **no se ha recuperado ni demostrado** ese procedimiento para estas tres variantes.
- Se conserva íntegra la lógica experimental previa de Nether/Overworld; no se han añadido eventos de carga ficticios para las otras dimensiones.

## Pendientes y limitaciones

- Localizar los procedimientos de carga específicos de Borg/Limbo/Nereida en el bytecode y reproducir condiciones exactas; por ahora los tres no se cargan por medios normales en este port.
- Verificar API exacta de Yarn 1.21.1 (`getOrEmpty`, `appendTooltip`, `inventoryTick`) durante compilación real.
- Proyecto sin Gradle wrapper ni dependencias descargadas en este entorno; no se realizó compilación ni prueba en Minecraft.
- **NO INSTALAR** en mundo de producción. Los restantes ítems y entidades siguen incompletos.
