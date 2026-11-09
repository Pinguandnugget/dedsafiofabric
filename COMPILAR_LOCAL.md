# Compilación de prueba — Etapa 15

1. Instalar Java 21 y Gradle 8.12, o usar GitHub Actions incluido.
2. Desde esta carpeta ejecutar `python3 verificar_recursos.py`.
3. Ejecutar `gradle --no-daemon --stacktrace build`.
4. Leer los errores del compilador antes de intentar instalar el mod.
5. Solo si termina en BUILD SUCCESSFUL: inspeccionar `build/libs/` y probar en un entorno aislado de Fabric 1.21.1 + Fabric API. **Una compilación exitosa no demuestra compatibilidad de mecánicas**.

En GitHub: subir el contenido de esta carpeta a la raíz de un repositorio; ejecutar Actions > Compilar Dedsafio3 Fabric 1.21.1 > Run workflow. No es necesario guardar el JAR original en ese repositorio; su uso sigue siendo solo de auditoría. Si falla, consultar las líneas `error:` del paso Compilar con Fabric Loom. Nunca subirlo directamente a PotitoSafio sin pruebas.

El flujo utiliza Gradle descargado por Actions; no requiere `gradlew` ni archivo wrapper en este ZIP.
