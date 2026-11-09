# Etapa 11 — Extractores Nether / Overworld

## Cambios verificados contra el JAR Forge original
- Ambos extractores usan Item.Properties durabilidad 200 y no apilables.
- Las recetas originales crean los extractores con Damage:200 (vacíos).
- Se migraron las 2 recetas pendientes al sistema 1.21.1 (`result.id` y `result.components.minecraft:damage`). Ingredientes, patrón y cantidades conservados.
- Se añadió OriginalExtractorItem con capacidad 200 y tooltip de porcentaje, usando getDamage. Los 2 IDs existentes ahora lo instancian.
- Se guardan los JSON originales en `pendientes_recetas_NBT/` para auditoría; no son cargables.

## Pendiente, NO implementado
- La lógica real de llenado por muerte de entidades en la dimensión correspondiente y cualquier cambio hacia variantes `*_filled`.
- Compilación Gradle y pruebas de funcionamiento/compatibilidad en Minecraft 1.21.1, y validación de API exacta para el método appendTooltip.
- Resto de funcionalidades del mod y pruebas con Arclight.

No instalar en producción. Es un proyecto fuente experimental.
