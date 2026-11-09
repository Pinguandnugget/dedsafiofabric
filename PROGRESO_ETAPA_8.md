# Etapa 8 — Efectos originales de las espadas (código experimental)

Inspeccionadas con `javap -c -p` las cuatro clases originales: `OnhitProcedure`, `OnhitFreezingProcedure`, `LeechingAspectEnchantment`, `FreezingAspectEnchantment` y las clases de ítems.

## Código añadido
- `Dedsafio3Enchantments`: claves estables a encantamientos dinámicos de 1.21.1.
- `OriginalEffectSwordItem`: dispara efectos después del golpe vanilla.
- `OriginalSwordEffects`: contador por atacante para regeneración y por víctima para congelación, tiempos originales, partículas, apagado de fuego.
- `data/dedsafio3/enchantment/*.json`: definiciones de encantamientos para 1.21.1; costos/weight provisionales, aún no validados.

## Detalles originales comprobados
- Healing Sword: requiere Leeching Aspect en la mano principal del atacante. En cada segundo golpe elegible da Regeneration II (amplifier 1) durante 25 ticks al atacante y cinco corazones.
- Ice Sword: requiere Freezing Aspect en la mano principal del atacante. Apaga al objetivo si arde; cada segundo golpe elegible **sobre ese objetivo** aplica 50 ticks de congelación y Slowness II durante 50 ticks, con cinco copos de nieve.
- Ambos encantamientos: máximo nivel 2, rareza VERY_RARE, solo se aplicaban en mesa a su espada específica. El original no permitía libros normales mediante los métodos inspeccionados.

## Pendiente / honestidad
- **SIN compilar / SIN prueba dentro de juego**; comprobar mappings, schema de encantamientos, flags y efectos. No instalar en mundos reales.
- Las condiciones y dos contadores vienen de bytecode; implementación actual es una aproximación técnica y no se ha demostrado equivalencia absoluta.
- El resto de los sistemas (139 ítems genéricos, 28 huevos, 61 entidades, etc.) continúa pendiente.
- Se conserva el namespace `dedsafio3`, pero la migración completa no está hecha.
