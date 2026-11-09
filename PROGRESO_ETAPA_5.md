# Etapa 5 — Contornos originales de runas y batidora (Fabric 1.21.1)

Se extrajo el método `m_5940_` (getShape) de las cinco clases del JAR Forge mediante `javap -c -p`, recuperando los cuboides `Block.box(...)` y el mapa de direcciones del switch compilado.

- Cuatro runas: **3 cuboides cada una**, geometría idéntica en las cuatro orientaciones, verificado contra el bytecode de las cuatro clases.
- Batidora legendaria: **9 cuboides en cada orientación**, 4 geometrías diferenciadas, implementadas para NORTH/EAST/WEST/SOUTH.
- Añadido `OriginalSpecialShapes.java` con las formas de selección exactas en unidades 1/16 de bloque.
- `DirectionalSpecialBlock` ahora usa `getOutlineShape`; mantiene colisión vacía como el original.
- `AUDITORIA_FORMAS_ESPECIALES.json` contiene los valores numéricos por orientación extraídos para revisar y comparar.

**No está compilado ni probado** (no hay una instalación de Gradle/Fabric con dependencias verificadas). No instalar como mod ni usar en mundos reales. La lógica adicional, entidades, ítems, modelos y sistemas de juego aún requieren migración.
