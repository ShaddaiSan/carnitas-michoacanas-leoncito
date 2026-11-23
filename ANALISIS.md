# ANÁLISIS — Carnitas Michoacanas Leoncito

Sitio actual: https://carnitasmichoacanasleoncito.ca/francais.php (y `/espanol.php`)
Fecha: 23/11/2026 · Estado: **Paso 1 — pendiente de tu aprobación**

> Fuentes usadas: HTML guardado de `francais.php` y la imagen del menú en francés (353×2000 px, baja resolución).
> NO he podido ver: la versión en español, el logo en alta, las fotos originales, Instagram ni Facebook.
> Todo lo marcado con ⚠️ debe confirmarlo el cliente antes de publicar.

---

## 1. Inventario

### Páginas
| Página | Contenido real |
|---|---|
| `francais.php` | Una sola imagen (`menuFran.jpg`) a todo el ancho + 2 botones de idioma |
| `espanol.php` | Igual, con la imagen del menú en español (⚠️ no revisada) |

No hay inicio, contacto, mapa, galería, ni formulario. El sitio **es** una imagen.

### Identidad de marca
- **Logo:** cerdito chef sacando la lengua dentro de una olla roja, arco amarillo con "CARNITAS", cinta amarilla con "MICHOACANAS LEONCITO" sobre fondo rojo.
- **Colores:** rojo intenso (~#C8102E), amarillo/mostaza (~#F2B705), blanco cremoso, negro, café madera. Meta `theme-color` actual: `#ee7d78` (no coincide con la marca).
- **Tipografías:** títulos tipo "slab/cartel" condensada en mayúsculas (estilo Bebas/Oswald); subtítulos serif; textos de apoyo sans simple. Se reemplazarán por equivalentes web (Google Fonts, autoalojadas).
- **Estilo visual:** fondo de madera, papel a cuadros rojo/blanco, mascotas de cerdito, fotos de comida.

### Menú (transcrito de la imagen en francés — ⚠️ verificar cada precio)
Moneda: dólares canadienses. "Sur place" = en el local · "À emporter" = para llevar.

**CARNITAS** — incluye tortillas, salsas y verduras
| Cantidad | Sur place | À emporter |
|---|---|---|
| 1 kilo | 60 $ | 55 $ |
| ½ kg | 30 $ | 30 $ ⚠️ (¿mismo precio en ambos?) |
| ¼ kg | 17 $ | 17 $ |

Cortes: maciza, croûte de cuir (cuero), oreja, surtido, costilla, codillo, buche.
**4 tacos de carnitas: 20 $** (mismos cortes).

**GORDITAS — 3 por 20 $**
Rellenos: maciza, oreja, surtido, costilla, buche, codillo, cuero, pastor (cerdo marinado), birria (res en salsa de chiles), queso, pollo.

**PASTOR** (cerdo marinado) — incluye tortillas, salsas y verduras
1 kilo 55 $ · ½ kg 30 $ · ¼ kg 15 $ · **Tacos 4 por 20 $**

**BIRRIA** (res braseada en salsa de chiles)
| Producto | Chico | Grande |
|---|---|---|
| Consomé | 20 $ | 25 $ |
| 4 tacos | 20 $ | |
| 4 quesabirrias (maíz) | 25 $ | |
| 1 quesabirria (harina) | 15 $ | |

**TACOS DE POLLO** — 4 por 20 $

**SÁBADO Y DOMINGO**
| Producto | Chico | Grande |
|---|---|---|
| Menudo | 20 $ | 25 $ |
| Pozole | 20 $ | 25 $ |

**TORTILLAS** — a voluntad en el local · para llevar 3 $

**BOISSONS (bebidas)**
Michelada 10 $ / 20 $ (chico/grande) · Cantarito 15 $ · Margaritas 15 $ · Mojitos 13 $ · Soda en botella 5 $ · Soda en lata 3 $ · Agua en botella 2 $ · Agua aromatizada 5 $ / 10 $.

### Datos de contacto (fuente: ficha de Google Maps, 23/11/2026)
- **Dirección:** 3726 Rue Jean-Talon E, Montréal, QC H2A 1X9
- **Teléfono:** (438) 835-8061
- **Horario:** lunes, miércoles, jueves, viernes, sábado y domingo 10 a. m.–9 p. m. · **martes cerrado**
- **Precio medio:** 20–30 $ por persona (dato de Google, reportado por 18 personas; no se publicará como oficial)
- **Web:** carnitasmichoacanasleoncito.ca
- **Redes:** Instagram `@carnitas_michoacanas_leoncito` · Facebook "Restaurante Carnitas Michoacanas Leoncito"
- ⚠️ Aún falta: confirmar si el (438) 835-8061 tiene WhatsApp, y correo (opcional). Esto es público en Google; el cliente debería confirmarlo.

### Imágenes
Logo, fotos de carnitas, pastor, birria/quesabirrias, menudo/pozole, michelada, mascotas de cerdito, fondo de madera, botones de idioma, favicon (`miicon.png`).
Todo viene **pegado dentro de una sola imagen** de 353×2000 px (la que tengo): inservible para reutilizar fotos sueltas. Necesito los originales (ver PENDIENTES.md).

---

## 2. Auditoría

### Crítico 🔴
1. **El sitio entero es una imagen.** Google no lee precios ni platillos; no se puede copiar el texto, traducir, ni usar lector de pantalla. Es el mayor problema.
2. **No hay datos de contacto visibles** en el sitio: ni teléfono tocable, ni dirección, ni mapa, ni horarios. Cero llamadas a la acción (llamar, WhatsApp, cómo llegar).
3. **SEO inexistente:** `<title>` genérico, descripción "Restaurant mexicain, bar" (además el negocio es de carnitas, no un bar), sin H1, sin alt, sin datos estructurados, sin sitemap.
4. **Open Graph apunta a otro negocio** (`tacoetmargarita.ca/ogimage.png`). Al compartir el enlace en WhatsApp/Facebook sale la imagen equivocada.

### Importante 🟠
5. **Rendimiento:** imagen de menú de gran tamaño en JPG, más jQuery 1.12.4 (2016), jQuery UI, Fancybox, jQuery Confirm y placeholder.js cargados sin usarse. Sin lazy-loading ni WebP.
6. **Móvil/accesibilidad:** `maximum-scale=1` bloquea el zoom; para leer precios en un celular hay que ampliar una imagen que ya es de baja resolución. Botones de idioma sin texto alternativo.
7. **Versión por idioma = página duplicada**, y cualquier cambio de precio exige rehacer dos imágenes en Photoshop.
8. **Cabeceras de caché contradictorias** (`no-cache` en todo): cada visita vuelve a descargar todo.
9. **Bloqueo anti-bot del hosting** que dificulta que buscadores y herramientas lean el sitio.

### Menor 🟡
10. Meta keywords en español en página en francés (obsoleto, sin efecto SEO).
11. Código heredado: video emergente y popup desactivados.
12. Sin favicon moderno ni manifest funcional; `theme-color` no coincide con la marca.
13. Falta de enlaces a Instagram/Facebook y de reseñas.

### Lo que sí funciona (se conserva)
Identidad visual fuerte y reconocible, menú claro con precios, mascota carismática, fotos apetitosas.

---

## 3. Plan de mejoras (por prioridad)

**P0 — Imprescindible**
- Menú en **texto real** (HTML), por secciones, con precios idénticos a los actuales.
- Cabecera con **Llamar / WhatsApp / Cómo llegar** + botón flotante de WhatsApp.
- Bloque de contacto: dirección (Montréal), teléfono, horarios (martes cerrado), mapa de Google.
- SEO completo: title/description únicos por página, un H1, Schema.org `Restaurant`/`LocalBusiness`, Open Graph con imagen propia, `sitemap.xml`, `robots.txt`, `hreflang` fr/es.
- Mobile-first, sin zoom bloqueado, contraste AA.

**P1 — Muy recomendado**
- Selector de idioma limpio (FR / ES) con la misma estructura en ambos; un solo código.
- Fotos optimizadas (WebP, lazy-loading, tamaños responsive) de los platillos estrella.
- Sección "Especiales de fin de semana" (menudo y pozole, sáb–dom) destacada.
- Enlaces a Instagram y Facebook; opcional galería con fotos reales.
- Eliminar jQuery y plugins: JS mínimo propio (menú móvil, filtros opcionales).

**P2 — Opcional**
- Menú con pestañas/ancla por categoría.
- Reseñas / testimonios (si el cliente da textos reales).
- Versión en inglés.
- Formulario de contacto o pedidos grandes por kilo (necesita backend o servicio como Formspree).

### Stack propuesto
HTML + CSS + JS sin frameworks. Estructura: `/fr/`, `/es/` (o `index.html` con redirección por idioma), `/assets/`. Se despliega en cualquier hosting estático. Meta: Lighthouse 90+.

### Cambios previstos de diseño
Conservar rojo/amarillo/crema y el cerdito; más espacio en blanco, tipografía legible (títulos de cartel + cuerpo sans), tarjetas de menú limpias, botones grandes y claros.

---

## 4. Preguntas abiertas (necesito tu respuesta o la del cliente)
1. ~~Dirección, teléfono, horarios~~ ✅ recibidos. Falta: ¿el teléfono tiene WhatsApp? ¿correo?
2. ¿Objetivo principal? (Mi suposición: **llamar y visitar el local**, WhatsApp si el número lo tiene.)
3. ¿Idiomas? (Mi suposición: francés como idioma principal + español; inglés opcional.)
4. ¿Sí al stack HTML/CSS/JS sin frameworks?
5. Extras (mi suposición: WhatsApp flotante, mapa, galería, menú con precios).
6. Confirmar los precios transcritos, sobre todo **½ kg carnitas 30 $ / 30 $**.
7. Subir los originales: logo, versión en español del menú, fotos de platillos.
8. Nombre del repositorio en GitHub (propuesto: `carnitas-michoacanas-leoncito`).
