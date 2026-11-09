# Dedsafío 3 — Etapa 6: inventario y registro inicial de ítems

Origen: `dedsafio3-0.0.9-forge-1.20.1 (1)(1).jar`. Inspección directa de `Dedsafio3ModItems.class`.

- Registros Forge de ítems encontrados: **170**.
- Ítems ya representados como BlockItem por los bloques anteriores: **0**.
- Huevos de invocación pospuestos (requieren entidades reales): **28**.
- IDs nuevos registrados en código fuente como `Item` provisional: **142**.
- Sin portear: estadísticas/propiedades de armas, armaduras, comidas, durabilidad, capacidades, eventos, habilidades, menús, interacción y lógica custom.
- **Estado: código experimental; no compilado ni probado.** No usar en mundo existente.

Ejemplos de comportamientos que NO implementa esta etapa: espadas y armas con daño real, bolsas que guardan inventario, alimentos que aplican efectos, objetos que ejecutan procedimientos, y los huevos de entidades.

## Próximo paso verificable

Portar primero constructores y métodos específicos de un conjunto pequeño de ítems (con auditoría `javap`), y compilar con dependencias Fabric/Yarn correspondientes antes de llamarlos funcionales. El JAR de Forge no es una dependencia ejecutable en Fabric.
