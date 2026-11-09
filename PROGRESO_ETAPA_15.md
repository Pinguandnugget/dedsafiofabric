# Etapa 15 — Infraestructura de compilación reproducible

## Cambios realizados

- Añadido `.github/workflows/compilar-fabric.yml` para descargar Gradle 8.12 en GitHub Actions, usar Java 21 y ejecutar `gradle build` con Fabric Loom.
- Actualizados `gradle.properties` y `fabric.mod.json` a la Etapa 15 y activada la expansión de `${version}` durante `processResources`.
- Añadidos `COMPILAR_LOCAL.md` y `auditoria_codigo_etapa15.py` para revisar recursos antes de compilar.
- Se conservan las clases, modelos y recursos de la Etapa 14 sin cambios funcionales.

## Verificaciones reales

```text
Fuentes Java: 12; JSON legibles: 490; incidencias estructurales: 0
ADVERTENCIA: esta prueba no compila ni valida las APIs Yarn/Fabric.
```

Java: `openjdk version "21.0.12.1" 2026-08-18`.
Gradle: no instalado en este entorno; sin acceso DNS a services.gradle.org. **No se ejecutó build de Gradle ni se generó un JAR jugable**.

## Próximo paso

Ejecutar el workflow en GitHub, recopilar errores reales de compilación y repararlos. No equivale a que el mod esté listo.
