# Dedsafío 3 Fabric 1.21.1 — Etapa 16

## Cambios comprobados
- Auditoría adicional de JSON, registros de ítems y bloques, recetas y referencias internas del namespace `dedsafio3`.
- Auditoría ejecutada sobre el proyecto incluido: **490 JSON analizados, 21 IDs de bloques, 142 IDs de ítems y 45 recetas; 0 errores detectados por esta auditoría**.
- El auditor reconoce los resultados en forma de objeto (`id`) y los resultados en forma de cadena para hornos.
- GitHub Actions ahora guarda el log del compilador y los informes incluso cuando Gradle falla; el JAR se publica solo si compila.
- Metadatos de versión actualizados a Etapa 16.

## Límites y riesgos
- **No se ha compilado este proyecto ni probado en Minecraft**. La auditoría es sintáctica / estructural, no comprueba compatibilidad binaria con Fabric.
- 142 IDs de ítems siguen siendo en gran medida placeholders; 28 huevos y 61 entidades no están portados.
- La paridad de mecánicas y los extractores especiales todavía no están completos.
- Los archivos fuente y recursos pueden necesitar cambios al compilar con mappings Yarn de 1.21.1.

## Cómo obtener errores reales
1. Extraer el ZIP completo.
2. Subir su contenido a la raíz de un repositorio de GitHub.
3. En `Actions`, ejecutar `Compilar Dedsafio3 Fabric 1.21.1` (o efectuar push a main).
4. Abrir la ejecución fallida, descargar `informe-compilacion-etapa16` y aportar `compilacion-etapa16.log` para corregir los errores Java.

**No instalar en producción**: el proyecto sigue siendo experimental.
