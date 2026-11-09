# Dedsafio 3 -> Fabric 1.21.1: etapa 2

## Implementado en codigo fuente
- Registro Fabric de 12 bloques basicos con sus IDs exactos extraidos de `Dedsafio3ModBlocks.class`.
- Registro de `BlockItem` para cada uno y exposicion en grupo de bloques de construccion.
- Uso de bloques cubicos y slabs donde corresponde; se preservan recursos visuales del ZIP previo.

## NO implementado / limitaciones
- NO ES MOD COMPLETO NI COMPILACION PROBADA.
- La dureza de bloques se ha establecido de forma provisional, NO se ha verificado contra Forge.
- No se han migrado drops, generacion, comportamiento, efectos, recetas 1.21, entidades, jefes, comandos, armaduras, items especiales, dimensions, sonidos asociados a logica, renderizadores, ni sistemas avanzados.
- Los 9 IDs restantes de bloques especiales y escaleras aun NO se registran.
- Algunas rutas de recursos/recetas de Forge 1.20.1 necesitan conversion para 1.21.1.
- No instalar en mundos reales. Probar en mundo nuevo SOLO despues de compilar y verificar arranque.

## Como continuar
1. Compilar con Java 21 y Gradle (generar wrapper para Gradle 8.10.x si fuese necesario) en equipo con dependencias Fabric accesibles.
2. Corregir cualquier error de mappings/API que arroje compilacion; despues realizar prueba de inicio.
3. Recuperar propiedades originales por descompilacion de `net.mcreator.dedsafio3.block.*`.
4. Portar bloques complejos, items y entidades por lotes con test de equivalencia.
