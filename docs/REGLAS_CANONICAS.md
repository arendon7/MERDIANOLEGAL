# Reglas canónicas de Meridiano Legal

Estas reglas deben mantenerse en cada iteración, incluyendo cambios realizados con asistentes de IA.

## Identidad

- Nombre visible: **Meridiano Legal**.
- Descriptor: **Derecho · Empresa · Tecnología**.
- Mensaje principal: **Dirección jurídica para decisiones que deben avanzar**.
- Logo único: `assets/logo-meridiano.svg`.
- Paleta principal: azul marino, azul institucional, marfil y dorado.
- No crear logos alternativos ni deformar el logo existente.

## Arquitectura pública

La web debe conservar estos bloques:

1. Firma y propuesta de valor.
2. Orientador por necesidades.
3. Ocho servicios profesionales.
4. Ocho productos de alcance cerrado.
5. Cinco planes recurrentes.
6. Seis documentos guiados.
7. Sectores priorizados.
8. Ruta Meridiano.
9. Portal demostrativo.
10. Contacto y advertencias.

## Portal demostrativo

Módulos mínimos:

- Resumen.
- Solicitudes.
- Expedientes.
- Documentos guiados.
- Archivos.
- Obligaciones.
- Calendario.
- Riesgos.
- Analítica.

Los datos y credenciales deben ser exclusivamente ficticios. Nunca se deben incluir secretos, tokens, datos personales reales, expedientes reales o información confidencial.

## Reglas técnicas

- Usar rutas relativas; no usar rutas que comiencen con `/`.
- Mantener el sitio autocontenido y sin imágenes remotas.
- Ejecutar `python3 scripts/validate_site.py` antes de publicar.
- Ejecutar `node --check app.js` y `node --check demo.js`.
- Mantener diseño responsive y navegación por teclado.
- Toda imagen debe tener texto alternativo.
- No eliminar avisos sobre límites de la demo y ausencia de asesoría jurídica.

## Cambios de contenido

- No inventar resultados, clientes, alianzas, certificaciones, cifras o reconocimientos.
- No presentar como operativo un módulo que solo sea demostrativo.
- No prometer resultados dependientes de autoridades, contrapartes o terceros.
- Mantener clara la separación entre la landing pública y el backend productivo futuro.
