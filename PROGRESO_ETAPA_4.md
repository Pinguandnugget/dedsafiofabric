# Etapa 4 — Fabric 1.21.1: 21 registros de bloque en código fuente

## Recuperación real del JAR original
- Se consultaron con `javap -c -p` las clases `BatidoraLegendariaBlock`, `RunaRedBlock`, `RunaCelestBlock`, `RunaRoseBlock`, `RunaYellowBlock` y `TestRNGBlockBlock`.
- Cinco bloques usan `FACING` horizontal (N/S/E/O), orientación al colocar, rotación, espejo y forma de colisión vacía. Implementado en `DirectionalSpecialBlock`.
- `test_rng_block` ejecuta al clic derecho del jugador de servidor `(int)(Math.random()*900+100)` y le envía `Número generado: N`; implementado en `OriginalRngBlock`.
- Los 21 identificadores están registrados en código fuente; **no significa que los 21 bloques estén portados completamente**.

## Pendiente
- Las formas de contorno (`getOutlineShape`) de las 5 piezas especiales son detalladas y dependientes de FACING en el original, NO están reconstruidas. Se mantienen contornos por defecto hasta reconstruirlos.
- La Batidora Legendaria y las runas no muestran método de clic en sus clases bloque originales; sus posibles mecánicas por procedimientos externos, eventos o ítems no han sido trazadas.
- Los 15 bloques anteriores siguen necesitando revisar comportamientos, materiales, drops, herramientas y renderizado.
- No se han portado ítems generales, recetas, mobs, mundos, bosses, etc.
- No compilado, no validado con servidor ni cliente. No instalar en mundos reales.
- **Atención:** APIs Yarn / Fabric 1.21.1 requieren compilación con Gradle y posible ajuste de firmas.

## Prueba local sugerida (cuando haya acceso a dependencias)
`gradle build` con Java 21 y Gradle/Loom compatibles, luego `runClient` y `runServer` en mundos de prueba.
