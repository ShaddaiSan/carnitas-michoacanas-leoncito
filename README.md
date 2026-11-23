# Carnitas Michoacanas Leoncito — sitio web

Sitio estático (HTML + CSS + JS mínimo, sin frameworks) en francés y español.

```
index.html          selector de idioma (redirige según el navegador)
fr/index.html       versión en francés (generada)
es/index.html       versión en español (generada)
assets/             css, js, fuentes e imágenes (WebP)
tools/build.py      genera fr/, es/, sitemap.xml, robots.txt y CREDITOS.md
```

## Editar contenido (precios, horarios, textos)
Todo el texto y los precios están en **`tools/build.py`** (un solo lugar para los dos idiomas).

```bash
python3 tools/build.py      # regenera fr/index.html, es/index.html, sitemap.xml
python3 -m http.server 8765 # abrir http://localhost:8765/
```

Requiere Python 3 y Pillow (`pip install pillow`) solo para regenerar. El sitio publicado es 100 % estático.

## Publicar
Subir el contenido de esta carpeta (menos `docs/`, `tools/` y los `.md`) a la raíz del hosting.
El dominio, URLs canónicas y sitemap usan `https://carnitasmichoacanasleoncito.ca`.

Documentos: `ANALISIS.md` · `CAMBIOS.md` · `PENDIENTES.md` · `CREDITOS.md`
