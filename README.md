# Mancha Burger Studio · tarjeta digital

Landing de enlaces de Mancha Burger Studio, desarrollada como producto FLEXCORE. La composición toma la tarjeta compartida como referencia y usa únicamente la información y publicaciones facilitadas por el usuario.

## Abrir

Desde la raíz del repositorio:

```powershell
npm run build:mancha
npm run start:mancha
```

Abre http://localhost:8087. La entrada reproduce la secuencia de 6,7 segundos de FLEXQR con puntos iniciales, logo oficial de Mancha, el eslogan «Creemos que una hamburguesa honesta es la mejor razón para volver a juntarnos» y transición del logo hacia la cabecera, todo sobre rojo. En escritorio se muestra una vez por sesión; en móvil, en cada entrada. Si el sistema prefiere movimiento reducido, se usa una versión breve. Para revisar siempre la secuencia completa, abre http://localhost:8087/?splash=full.

## Contenido

- Pedido por WhatsApp y llamada al 961818343.
- Instagram y TikTok de @manchaburgerstudio.
- Enlace directo para dejar una opinión en Google.
- Mapa de Google Maps de Mancha Burger Studio proporcionado por el usuario.
- Portadas locales de los dos TikTok y el reel de Instagram proporcionados como última sección de contenido; cada tarjeta abre la publicación original en su plataforma.
- Contacto de FLEXCORE (992272521) en el pie, separado del teléfono de Mancha.

Los dos archivos de logo en `public/` se extrajeron de la página 4 del manual de marca aportado. `scripts/extract-mancha-logo.py` permite repetir la extracción con ese PDF si se dispone del original. Las tres portadas se guardaron desde las publicaciones indicadas por el usuario para evitar cuadros vacíos cuando fallen las inserciones externas. No se generaron fotografías ni imágenes de comida.
