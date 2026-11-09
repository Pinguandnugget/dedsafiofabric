# Dedsafío 3 — Port experimental Fabric 1.21.1, Etapa 3

## Trabajo efectuado
- Confirmados 21 IDs de bloques a partir del bytecode de `Dedsafio3ModBlocks.class` del JAR original.
- Agregados 3 registros **StairsBlock reales** con sus `BlockItem`: `gray_stair_block`, `polished_limbo_stair_block`, `rusty_wall_stairs`.
- Las tres clases originales Forge de escaleras especifican dureza -1.0, resistencia 3600000.0, y no son entidades; se transfirió fuerza/resistencia y geometría de escalera. No se han transferido sus métodos personalizados de velocidad de destrucción/requisitos de herramienta y otras propiedades. El sonido es provisional para dos variantes.
- TOTAL: 15/21 IDs de bloques con registros experimentales. Los restantes 6 bloques especiales requieren lectura y migración de comportamiento antes de ser registrados.
- Añadida `AUDITORIA_BLOQUES_21.json` con indicadores de existencia de recursos.

## Bloques pendientes (NO registrados)
- `batidora_legendaria`
- `runa_red`, `runa_celest`, `runa_rose`, `runa_yellow`
- `test_rng_block`

## ADVERTENCIAS
- **No compilado ni probado en Minecraft. No es instalable todavía.**
- La API exacta de Fabric/Yarn requiere prueba con dependencias accesibles.
- El código de bloques simples sigue usando propiedades provisionales de etapa 2.
- No se portaron ítems generales, entidades, jefes, mundos, generación, recetas ni comportamiento especial.
- No cargar en el mundo real; no hay garantía de compatibilidad de guardados.

## Próximo trabajo
1. Migrar los seis bloques especiales con sus triggers y procedimientos de Forge, no como placeholders.
2. Verificar la compilación Java 21 y el arranque dedicado antes de probar mundos nuevos.
3. Portar registro general de ítems y los subsistemas dependientes por grupos.
