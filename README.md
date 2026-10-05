# AdminPlus – sitio público

Sitio estático (GitHub Pages) de **AdminPlus**, la app Android de gestión para pequeños negocios desarrollada por TotoLab (paquete `com.totolab.myapplottery`). Versión de la app: 2.0.

## Páginas

| Página | Ruta relativa | Uso |
| ------ | ------------- | --- |
| Inicio | [`index.html`](index.html) | Presentación de la app, módulos, privacidad y contacto |
| Política de privacidad | [`privacy-policy.html`](privacy-policy.html) | URL de la política en Google Play Console |
| Descripción y Términos y Condiciones | [`terminos_y_descripcion.html`](terminos_y_descripcion.html) | Enlazada desde Play Console (no renombrar) |
| Eliminar datos | [`eliminar-datos.html`](eliminar-datos.html) | Instrucciones para el formulario de Seguridad de los datos |
| Página 404 | [`404.html`](404.html) | Página de error que GitHub Pages sirve para rutas inexistentes |

`.nojekyll` (vacío) desactiva el procesamiento de Jekyll en GitHub Pages.

Cada página es autocontenida: HTML con CSS en línea, sin JavaScript. Solo carga la fuente IBM Plex Sans desde Google Fonts (con fuente del sistema como respaldo).

## Mantenimiento

- Al cambiar la forma en que la app maneja datos o permisos, actualizar `privacy-policy.html` y su fecha de entrada en vigor **antes** de publicar la versión.
- Las páginas se generan con `build.py` (cabecera, pie y tokens de color compartidos): editar el script y ejecutar `python3 build.py`, no los HTML a mano.
- Las capturas de pantalla de `index.html` son marcadores de posición: reemplazar cada `<figure class="shot">` por un `<img>` cuando haya imágenes.

## Contacto

TotoLab · <totolab2025@gmail.com> · Managua, Nicaragua
