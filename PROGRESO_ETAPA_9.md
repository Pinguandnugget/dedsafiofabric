# Etapa 9 — Auditoría de compilación y recursos

## Cambios realizados

- Se migraron las tablas de botín de `data/dedsafio3/loot_tables/` a `data/dedsafio3/loot_table/`, ruta de Minecraft 1.21.1.
- Se sincronizó la versión experimental entre `gradle.properties`, `fabric.mod.json` y el mensaje de inicio.
- Se ejecutó auditoría estática de JSON, IDs, modelos de ítems, blockstates y superposición de registros.
- Se añadió `verificar_recursos.py` para repetir comprobaciones antes de compilar.

## Estado de compilación

**NO COMPILADO.** Java 21 está disponible, pero Gradle no está instalado, no hay caché de dependencias Fabric y la red no permite descargarlas. No se ha generado un mod `.jar` ni probado en Minecraft.

## Ejecutar en un ordenador con acceso a internet

1. Instalar JDK 21 y Gradle 8.10.x (o compatible con Fabric Loom 1.9).
2. Abrir la carpeta de proyecto y ejecutar `python verificar_recursos.py`.
3. Ejecutar `gradle build --stacktrace`.
4. No instalar en un mundo real. Compartir `build/reports/` y el error completo si falla.

**Pendiente de validar:** firmas Yarn 1.21.1, inicialización de registros, propiedades de bloques, datos de encantamientos y port real de entidades. El resultado de `gradle build` NO debe darse por positivo sin ejecutarlo.
