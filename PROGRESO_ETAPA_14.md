# Etapa 14 — Rastreo forense de los extractores especiales

## Trabajo realizado

Se escanearon las clases compiladas dentro del JAR original y se consultó el bytecode (`javap -c -p`) de BorgExtractorItem, LimboExtractorItem y NereidaExtractorItem. Se guardaron coincidencias exactas en `AUDITORIA_ETAPA_14.json`.

### Resultados verificables

- Los tres ítems fijan daño máximo de **200**.
- Los tres incluyen texto de ayuda que indica cargar el extractor matando entidades en la dimensión correspondiente.
- Los tres comprueban su carga en `inventoryTick` y se sustituyen por la variante llena cuando el daño llega a cero mientras están en una mano.
- El rastreo de referencias literales a `BORG_EXTRACTOR`, `LIMBO_EXTRACTOR`, `NEREIDA_EXTRACTOR` y sus clases encontró registros, pestañas creativas e ítems, pero **ningún procedimiento original** que mencione esas referencias.

## Decisión de migración

**No introducir mecánicas especulativas** para los tres extractores. Aunque el tooltip sugiere que se llenan matando entidades, no localizamos el procedimiento de carga real dentro del JAR. El código de la etapa 13 que transforma el ítem al completarse permanece sin modificación.

## Próximo bloqueo técnico

Necesitamos compilar y ejecutar la base con Java 21, Gradle, Fabric Loom y mappings correspondientes. La presente auditoría no demuestra compilación. Antes de portar nuevos jefes, hace falta una compilación mínima real.

**No instalar en el servidor de producción.**
