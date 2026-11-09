# Etapa 10 — Compatibilidad de recetas Minecraft 1.21.1

- Se detectaron **45 recetas** en `data/dedsafio3/recipes` (ruta de 1.20.x).
- **43 recetas** fueron movidas a `data/dedsafio3/recipe`, la ruta de 1.21.1.
- Se cambió la clave `result.item` por `result.id` en resultados de tipo objeto; se mantuvieron las cantidades y los ingredientes sin alterar.
- **2 recetas se dejaron fuera de la carpeta cargable** porque el original usa `result.nbt: "{Damage:200}"`, formato obsoleto. Los JSON originales están en `pendientes_recetas_NBT/`. Antes de activarlas hace falta migrar el daño a componentes de ítem y reconstruir los extractores como ítems durables. No es seguro activarlas como están.
- Se actualizó el verificador para detectar carpetas antiguas y resultados de recetas incompatibles.

## Limitaciones

No se ejecutó Gradle, ni se confirmó compilación Java ni funcionamiento en Minecraft. Este ZIP contiene **fuente experimental**, no un mod funcional. Los 43 JSON migrados pasan sintaxis/estructura básica pero pueden fallar por IDs de ítems no registrados o propiedades no implementadas. No usar en mundos de producción.

## Próximo paso recomendado

Compilar con Gradle 8.x y Java 21 en un entorno con dependencias accesibles; corregir errores de API/arranque antes de integrar más entidades.
