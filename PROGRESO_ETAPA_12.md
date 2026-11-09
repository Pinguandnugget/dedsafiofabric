# Etapa 12: extracción de energía por muertes (experimental)

## Evidencia verificada en el JAR original

- `net.mcreator.dedsafio3.procedures.DeddelProcedure.onEntityDeath` se suscribe a `LivingDeathEvent` de Forge.
- El atacante debe ser un jugador (entidad atacante de `DamageSource`).
- Se consulta el **bioma de la víctima**: tags `minecraft:is_nether` / `minecraft:is_overworld`.
- El procedimiento original comprueba solamente **mano principal**, aunque el tooltip del ítem dice «alguna de las dos manos»; esta discrepancia se preserva y documenta.
- Si coincide el extractor del bioma, `ItemStack.hurtAndBreak(-1, random, null)`: disminuye 1 punto de daño, aumentando en 1 la carga.
- `NetherExtractorItem` y `OverworldExtractorItem` cambian a sus respectivas versiones `_filled` cuando `200 - damage >= 200`, siempre que el stack esté en una mano del jugador.

## Código incorporado

- `OriginalExtractorKillEvents.java`: callback Fabric `ServerLivingEntityEvents.AFTER_DEATH`, identifica fuente directa/bioma, reduce daño con límite inferior 0.
- `OriginalExtractorItem.java`: conversión en `inventoryTick` a versión completa en mano principal o secundaria; tooltip ajustado a comportamiento del código original.
- `Dedsafio3Fabric.java`: registra los eventos.

## Limitaciones explícitas

- **No se ha compilado ni probado en Minecraft**: se requieren Gradle, dependencias Fabric y entorno de pruebas.
- Registro original `getId` y `BiomeTags` deben verificarse con mappings Yarn exactos al compilar.
- Los extractores de Borg, Limbo y Nereida aún no están reconstruidos.
- El método de Forge utilizado para recuperar carga admite particularidades no replicadas exactamente en Fabric; la adaptación usa `setDamage`.
- Se usa `DamageSource.getSource()` (atacante directo, como `getDirectEntity()` de Forge); muertes con proyectiles no cuentan salvo que el origen directo sea un jugador. Pendiente verificar la equivalencia fina en pruebas.
- No instalar en mundos reales, no es un JAR Fabric ejecutable.
