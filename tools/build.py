#!/usr/bin/env python3
"""Genera fr/index.html y es/index.html, sitemap.xml y CREDITOS.md.

Un solo contenido para los dos idiomas => los precios nunca se desincronizan.
Uso:  python3 tools/build.py
Requiere Pillow (solo para leer tamaños de imagen).
"""
import json, html, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://carnitasmichoacanasleoncito.ca"
PHONE_TEL, PHONE_DISPLAY, PHONE_WA = "+14388358061", "(438) 835-8061", "14388358061"
ADDRESS = dict(street="3726 Rue Jean-Talon E", city="Montréal", region="QC", zip="H2A 1X9", country="CA")
MAPS_Q = "3726 Rue Jean-Talon E, Montréal, QC H2A 1X9"
INSTAGRAM = "https://www.instagram.com/carnitas_michoacanas_leoncito/"
FACEBOOK = "https://www.facebook.com/p/Restaurante-Carnitas-Michoacanas-Leoncito-61577244354542/"

e = html.escape

def img(slug, alt, sizes="(min-width: 860px) 560px, 100vw", eager=False, cls=""):
    w6 = Image.open(ROOT / f"assets/img/{slug}-600.webp").size
    w12 = Image.open(ROOT / f"assets/img/{slug}-1200.webp").size
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="../assets/img/{slug}-1200.webp" '
            f'srcset="../assets/img/{slug}-600.webp {w6[0]}w, ../assets/img/{slug}-1200.webp {w12[0]}w" '
            f'sizes="{sizes}" width="{w12[0]}" height="{w12[1]}" alt="{e(alt)}" {load}>')

# ----------------------------------------------------------------- textos
T = {
 "fr": dict(
  lang="fr", locale="fr_CA", other="es", other_label="Español", other_name="Ver en español",
  title="Carnitas Michoacanas Leoncito | Restaurant mexicain à Montréal",
  desc="Carnitas, pastor, birria, gorditas et tacos à Montréal (Jean-Talon Est). Au kilo ou en tacos, sur place ou à emporter. Ouvert tous les jours sauf le mardi.",
  skip="Aller au contenu", nav_menu="Menu", nav_visit="Nous trouver", nav_label="Navigation principale",
  call="Appeler", wa="WhatsApp", dir="Itinéraire",
  open_now="Ouvert maintenant", closed_now="Fermé en ce moment", closed_tue="Fermé le mardi", opens="Ouvre à 10 h",
  h1="Carnitas Michoacanas Leoncito",
  tagline="Les vraies carnitas michoacanas, à Montréal.",
  lead="Carnitas, pastor et birria préparés à la mexicaine. Commandez au kilo pour la famille, en tacos pour le lunch, sur place ou à emporter.",
  hero_alt="Carnitas de porc dans un grand chaudron en cuivre",
  hero_facts=["Ouvert 7 jours sur 7 sauf le mardi", "10 h à 21 h", "Sur place ou à emporter"],
  menu_h="Notre menu", menu_intro="Prix en dollars canadiens. Les carnitas et le pastor sont servis avec tortillas, salsas et légumes.",
  here="Sur place", togo="À emporter",
  carnitas="Carnitas", carnitas_note="Comprend : tortillas, salsas et légumes",
  kilo="1 kilo", half="½ kg", quarter="¼ kg",
  cuts_h="Choisissez votre coupe",
  cuts=["Maciza", "Croûte de cuir", "Oreille", "Assortiment", "Côte", "Jarret de porc", "Bûche"],
  tacos4="4 tacos", tacos4_note="Choisissez votre coupe",
  gorditas="Gorditas", gorditas_price_note="3 pour 20 $", gorditas_h="Fourrées au choix",
  gordita_fill=["Maciza", "Oreille", "Assortiment", "Côte", "Bûche", "Jarret de porc", "Croûte de cuir", "Pastor (porc mariné)", "Birria (bœuf braisé dans une sauce aux piments)", "Fromage", "Poulet"],
  pastor="Pastor", pastor_sub="Porc mariné", pastor_note="Comprend : tortillas, salsas et légumes",
  birria="Birria", birria_sub="Bœuf braisé dans une sauce aux piments",
  consomme="Consommé", small="Petit", large="Grand",
  quesa_corn="4 quesabirrias au maïs", quesa_flour="1 quesabirria à la farine", tacos_birria="4 tacos",
  poulet="Tacos au poulet", poulet_sub="4 tacos",
  weekend="Samedi et dimanche", weekend_sub="Les classiques du week-end",
  menudo="Menudo", pozole="Pozole",
  tortillas="Tortillas", tortillas_here="À volonté au restaurant", tortillas_togo="À emporter",
  drinks="Boissons",
  michelada="Michelada", cantarito="Cantarito", margaritas="Margaritas", mojitos="Mojitos",
  soda_b="Soda en bouteille", soda_c="Soda en canette", water="Eau en bouteille", flavored="Eau aromatisée",
  alt_gorditas="Gorditas de maïs sur le gril", alt_birria="Quesabirrias dorées avec leur consommé", alt_menudo="Bol de menudo avec tortilla, piments et origan",
  alt_michelada="Michelada au bord givré de piment", alt_tacos="Tacos garnis de viande hachée, oignon et coriandre",
  visit_h="Venez nous voir", visit_lead="Nous sommes sur la rue Jean-Talon Est, à Montréal.",
  addr_h="Adresse", hours_h="Heures d'ouverture", map_title="Carte Google Maps : Carnitas Michoacanas Leoncito",
  days=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"], closed="Fermé", hours_fmt="10 h – 21 h",
  phone_h="Téléphone", follow_h="Suivez-nous", ig="Instagram", fb="Facebook",
  wa_msg="Bonjour, j'aimerais commander des carnitas.", wa_label="Écrire sur WhatsApp",
  footer_rights="Tous droits réservés.", credits_h="Crédits photo", credits_intro="Photos sous licence libre (Wikimedia Commons) :", logo_credit="Logo et mascotte : Carnitas Michoacanas Leoncito.",
  menu_ld="Menu", sr_prices="Prix",
 ),
 "es": dict(
  lang="es", locale="es_MX", other="fr", other_label="Français", other_name="Voir en français",
  title="Carnitas Michoacanas Leoncito | Restaurante mexicano en Montreal",
  desc="Carnitas, pastor, birria, gorditas y tacos en Montreal (Jean-Talon Este). Por kilo o en tacos, para comer aquí o llevar. Abierto todos los días menos el martes.",
  skip="Saltar al contenido", nav_menu="Menú", nav_visit="Cómo llegar", nav_label="Navegación principal",
  call="Llamar", wa="WhatsApp", dir="Cómo llegar",
  open_now="Abierto ahora", closed_now="Cerrado por el momento", closed_tue="Cerrado los martes", opens="Abre a las 10 a. m.",
  h1="Carnitas Michoacanas Leoncito",
  tagline="Las verdaderas carnitas michoacanas, en Montreal.",
  lead="Carnitas, pastor y birria preparados a la mexicana. Pide por kilo para la familia o en tacos para la comida, para comer aquí o para llevar.",
  hero_alt="Carnitas de cerdo en un cazo de cobre",
  hero_facts=["Abierto 7 días, menos los martes", "10 a. m. a 9 p. m.", "Para comer aquí o llevar"],
  menu_h="Nuestro menú", menu_intro="Precios en dólares canadienses. Las carnitas y el pastor incluyen tortillas, salsas y verduras.",
  here="En el local", togo="Para llevar",
  carnitas="Carnitas", carnitas_note="Incluye: tortillas, salsas y verduras",
  kilo="1 kilo", half="½ kg", quarter="¼ kg",
  cuts_h="Elige tu corte",
  cuts=["Maciza", "Cuero", "Oreja", "Surtido", "Costilla", "Codillo", "Buche"],
  tacos4="4 tacos", tacos4_note="Elige tu corte",
  gorditas="Gorditas", gorditas_price_note="3 por 20 $", gorditas_h="Rellenas a tu gusto",
  gordita_fill=["Maciza", "Oreja", "Surtido", "Costilla", "Buche", "Codillo", "Cuero", "Pastor (cerdo marinado)", "Birria (res en salsa de chiles)", "Queso", "Pollo"],
  pastor="Pastor", pastor_sub="Cerdo marinado", pastor_note="Incluye: tortillas, salsas y verduras",
  birria="Birria", birria_sub="Res braseada en salsa de chiles",
  consomme="Consomé", small="Chico", large="Grande",
  quesa_corn="4 quesabirrias de maíz", quesa_flour="1 quesabirria de harina", tacos_birria="4 tacos",
  poulet="Tacos de pollo", poulet_sub="4 tacos",
  weekend="Sábado y domingo", weekend_sub="Los clásicos del fin de semana",
  menudo="Menudo", pozole="Pozole",
  tortillas="Tortillas", tortillas_here="A voluntad en el local", tortillas_togo="Para llevar",
  drinks="Bebidas",
  michelada="Michelada", cantarito="Cantarito", margaritas="Margaritas", mojitos="Mojitos",
  soda_b="Refresco en botella", soda_c="Refresco en lata", water="Agua en botella", flavored="Agua de sabor",
  alt_gorditas="Gorditas de maíz en el comal", alt_birria="Quesabirrias doradas con su consomé", alt_menudo="Plato de menudo con tortilla, chiles y orégano",
  alt_michelada="Michelada con borde enchilado", alt_tacos="Tacos con carne picada, cebolla y cilantro",
  visit_h="Ven a visitarnos", visit_lead="Estamos en la calle Jean-Talon Este, en Montreal.",
  addr_h="Dirección", hours_h="Horario", map_title="Mapa de Google Maps: Carnitas Michoacanas Leoncito",
  days=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], closed="Cerrado", hours_fmt="10 a. m. – 9 p. m.",
  phone_h="Teléfono", follow_h="Síguenos", ig="Instagram", fb="Facebook",
  wa_msg="Hola, quisiera hacer un pedido de carnitas.", wa_label="Escribir por WhatsApp",
  footer_rights="Todos los derechos reservados.", credits_h="Créditos de fotos", credits_intro="Fotos con licencia libre (Wikimedia Commons):", logo_credit="Logo y mascota: Carnitas Michoacanas Leoncito.",
  menu_ld="Menú", sr_prices="Precios",
 ),
}

def usd(lang, n):
    return f"{n} $" if lang == "fr" else f"${n}"

def build(lang):
    t = T[lang]
    p = lambda n: usd(lang, n)
    credits = json.load(open(ROOT / "assets/credits.json", encoding="utf-8"))
    canonical = f"{SITE}/{lang}/"
    other = t["other"]
    wa_url = f"https://wa.me/{PHONE_WA}?text=" + __import__("urllib.parse").parse.quote(t["wa_msg"])
    maps_dir = "https://www.google.com/maps/dir/?api=1&destination=" + __import__("urllib.parse").parse.quote(MAPS_Q)
    maps_embed = "https://www.google.com/maps?q=" + __import__("urllib.parse").parse.quote(MAPS_Q) + f"&hl={lang}&z=16&output=embed"

    def prices(rows):  # rows: [(label, price)]
        return "".join(f'<li><span>{e(a)}</span><b>{e(b)}</b></li>' for a, b in rows)

    cuts = "".join(f"<li>{e(c)}</li>" for c in t["cuts"])
    fill = "".join(f"<li>{e(c)}</li>" for c in t["gordita_fill"])
    days = ""
    for i, d in enumerate(t["days"]):
        closed = i == 1
        days += f'<tr{" class=closed" if closed else ""} data-day="{(i + 1) % 7}"><th scope="row">{e(d)}</th><td>{e(t["closed"] if closed else t["hours_fmt"])}</td></tr>'

    ld = {
        "@context": "https://schema.org",
        "@type": "Restaurant",
        "@id": SITE + "/#restaurant",
        "name": "Carnitas Michoacanas Leoncito",
        "url": canonical,
        "image": [f"{SITE}/assets/img/og-image.jpg", f"{SITE}/assets/img/logo-600.webp"],
        "logo": f"{SITE}/assets/img/logo-600.webp",
        "description": t["desc"],
        "telephone": PHONE_TEL,
        "servesCuisine": ["Mexicaine" if lang == "fr" else "Mexicana", "Carnitas", "Birria", "Tacos"],
        "hasMenu": canonical + "#menu",
        "inLanguage": lang,
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS["street"], "addressLocality": ADDRESS["city"],
                    "addressRegion": ADDRESS["region"], "postalCode": ADDRESS["zip"], "addressCountry": ADDRESS["country"]},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "10:00", "closes": "21:00"}],
        "sameAs": [INSTAGRAM, FACEBOOK],
        "currenciesAccepted": "CAD",
    }

    credit_items = "".join(
        f'<li><a href="{e(c["page"])}" rel="noopener">{e(c["title"].rsplit(".", 1)[0])}</a> — {e(c["artist"])}, '
        f'<a href="{e(c["licenseUrl"])}" rel="noopener">{e(c["license"])}</a></li>' for c in credits.values())

    ico = {
        "phone": '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
        "wa": '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.6-.1l1.8.9c.3.1.5.2.5.3.1.2.1.8-.1 1.4z"/></svg>',
        "pin": '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
        "ig": '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7zm5 3.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 0 1 12 7.5zm0 2A2.5 2.5 0 1 0 14.5 12 2.5 2.5 0 0 0 12 9.5zM17.3 6a1.1 1.1 0 1 1-1.1 1.1A1.1 1.1 0 0 1 17.3 6z"/></svg>',
        "fb": '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.5 1.6-1.5h1.7V4.4A22 22 0 0 0 14.4 4c-2.4 0-4.1 1.5-4.1 4.2v2.6H7.5V14h2.8v8z"/></svg>',
    }

    page = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="theme-color" content="#c4161c">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="fr" href="{SITE}/fr/">
<link rel="alternate" hreflang="es" href="{SITE}/es/">
<link rel="alternate" hreflang="x-default" href="{SITE}/fr/">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="../assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<meta property="og:type" content="restaurant">
<meta property="og:site_name" content="Carnitas Michoacanas Leoncito">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{T[other]["locale"]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="../assets/fonts/bebas-neue-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/css/styles.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#contenu">{e(t["skip"])}</a>

<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="#top" aria-label="{e(t["h1"])}">
      <img src="../assets/img/logo-300.webp" width="300" height="270" alt="" class="brand-logo">
      <span class="brand-name">Carnitas<br>Michoacanas Leoncito</span>
    </a>
    <nav class="nav" aria-label="{e(t["nav_label"])}">
      <a href="#menu">{e(t["nav_menu"])}</a>
      <a href="#visite">{e(t["nav_visit"])}</a>
      <a class="lang" href="../{other}/" hreflang="{other}" lang="{other}" title="{e(t["other_name"])}">{e(t["other_label"])}</a>
    </nav>
    <a class="btn btn-call head-call" href="tel:{PHONE_TEL}" aria-label="{e(t["call"])} {PHONE_DISPLAY}">{ico["phone"]}<span>{e(t["call"])}</span></a>
  </div>
</header>

<main id="contenu">
<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="status" id="status" data-open="{e(t["open_now"])}" data-closed="{e(t["closed_now"])}" data-tue="{e(t["closed_tue"])}" data-opens="{e(t["opens"])}"></p>
      <h1>{e(t["h1"])}</h1>
      <p class="tagline">{e(t["tagline"])}</p>
      <p class="lead">{e(t["lead"])}</p>
      <div class="cta">
        <a class="btn btn-call" href="tel:{PHONE_TEL}">{ico["phone"]}<span>{e(t["call"])} {PHONE_DISPLAY}</span></a>
        <a class="btn btn-wa" href="{wa_url}" rel="noopener">{ico["wa"]}<span>{e(t["wa"])}</span></a>
        <a class="btn btn-ghost" href="{maps_dir}" rel="noopener">{ico["pin"]}<span>{e(t["dir"])}</span></a>
      </div>
      <ul class="facts">{"".join(f"<li>{e(f)}</li>" for f in t["hero_facts"])}</ul>
    </div>
    <div class="hero-photo">{img("carnitas-cazo", t["hero_alt"], sizes="(min-width: 860px) 460px, 90vw", eager=True)}</div>
  </div>
</section>

<section class="menu" id="menu" aria-labelledby="menu-h">
  <div class="wrap">
    <h2 id="menu-h">{e(t["menu_h"])}</h2>
    <p class="section-intro">{e(t["menu_intro"])}</p>

    <div class="grid">
      <article class="card card-wide">
        <header><h3>{e(t["carnitas"])}</h3><p class="note">{e(t["carnitas_note"])}</p></header>
        <table class="ptable">
          <caption class="sr">{e(t["carnitas"])} — {e(t["sr_prices"])}</caption>
          <thead><tr><th scope="col"></th><th scope="col">{e(t["here"])}</th><th scope="col">{e(t["togo"])}</th></tr></thead>
          <tbody>
            <tr><th scope="row">{e(t["kilo"])}</th><td>{p(60)}</td><td>{p(55)}</td></tr>
            <tr><th scope="row">{e(t["half"])}</th><td>{p(30)}</td><td>{p(30)}</td></tr>
            <tr><th scope="row">{e(t["quarter"])}</th><td>{p(17)}</td><td>{p(17)}</td></tr>
          </tbody>
        </table>
        <h4>{e(t["cuts_h"])}</h4>
        <ul class="chips">{cuts}</ul>
        <ul class="prices"><li><span>{e(t["tacos4"])} <small>{e(t["tacos4_note"])}</small></span><b>{p(20)}</b></li></ul>
      </article>
      <figure class="photo">{img("carnitas-tacos", t["alt_tacos"])}</figure>

      <figure class="photo">{img("gorditas", t["alt_gorditas"])}</figure>
      <article class="card">
        <header><h3>{e(t["gorditas"])}</h3><p class="big">{e(t["gorditas_price_note"])}</p></header>
        <h4>{e(t["gorditas_h"])}</h4>
        <ul class="chips">{fill}</ul>
      </article>

      <article class="card">
        <header><h3>{e(t["pastor"])}</h3><p class="note">{e(t["pastor_sub"])} · {e(t["pastor_note"])}</p></header>
        <ul class="prices">{prices([(t["kilo"], p(55)), (t["half"], p(30)), (t["quarter"], p(15)), (t["tacos4"], p(20))])}</ul>
      </article>

      <article class="card">
        <header><h3>{e(t["poulet"])}</h3></header>
        <ul class="prices">{prices([(t["poulet_sub"], p(20))])}</ul>
      </article>

      <article class="card card-wide">
        <header><h3>{e(t["birria"])}</h3><p class="note">{e(t["birria_sub"])}</p></header>
        <table class="ptable">
          <caption class="sr">{e(t["birria"])} — {e(t["sr_prices"])}</caption>
          <thead><tr><th scope="col"></th><th scope="col">{e(t["small"])}</th><th scope="col">{e(t["large"])}</th></tr></thead>
          <tbody><tr><th scope="row">{e(t["consomme"])}</th><td>{p(20)}</td><td>{p(25)}</td></tr></tbody>
        </table>
        <ul class="prices">{prices([(t["tacos_birria"], p(20)), (t["quesa_corn"], p(25)), (t["quesa_flour"], p(15))])}</ul>
      </article>
      <figure class="photo">{img("birria", t["alt_birria"])}</figure>

      <figure class="photo">{img("menudo", t["alt_menudo"])}</figure>
      <article class="card card-gold">
        <header><h3>{e(t["weekend"])}</h3><p class="note">{e(t["weekend_sub"])}</p></header>
        <table class="ptable">
          <caption class="sr">{e(t["weekend"])} — {e(t["sr_prices"])}</caption>
          <thead><tr><th scope="col"></th><th scope="col">{e(t["small"])}</th><th scope="col">{e(t["large"])}</th></tr></thead>
          <tbody>
            <tr><th scope="row">{e(t["menudo"])}</th><td>{p(20)}</td><td>{p(25)}</td></tr>
            <tr><th scope="row">{e(t["pozole"])}</th><td>{p(20)}</td><td>{p(25)}</td></tr>
          </tbody>
        </table>
      </article>

      <article class="card">
        <header><h3>{e(t["tortillas"])}</h3></header>
        <ul class="prices">{prices([(t["tortillas_here"], "✓"), (t["tortillas_togo"], p(3))])}</ul>
      </article>

      <article class="card">
        <header><h3>{e(t["drinks"])}</h3></header>
        <table class="ptable">
          <caption class="sr">{e(t["drinks"])} — {e(t["sr_prices"])}</caption>
          <thead><tr><th scope="col"></th><th scope="col">{e(t["small"])}</th><th scope="col">{e(t["large"])}</th></tr></thead>
          <tbody>
            <tr><th scope="row">{e(t["michelada"])}</th><td>{p(10)}</td><td>{p(20)}</td></tr>
            <tr><th scope="row">{e(t["flavored"])}</th><td>{p(5)}</td><td>{p(10)}</td></tr>
          </tbody>
        </table>
        <ul class="prices">{prices([(t["cantarito"], p(15)), (t["margaritas"], p(15)), (t["mojitos"], p(13)), (t["soda_b"], p(5)), (t["soda_c"], p(3)), (t["water"], p(2))])}</ul>
      </article>
      <figure class="photo">{img("michelada", t["alt_michelada"])}</figure>
    </div>
  </div>
</section>

<section class="visit" id="visite" aria-labelledby="visit-h">
  <div class="wrap">
    <h2 id="visit-h">{e(t["visit_h"])}</h2>
    <p class="section-intro">{e(t["visit_lead"])}</p>
    <div class="visit-grid">
      <div class="info">
        <h3>{e(t["addr_h"])}</h3>
        <address><a href="{maps_dir}" rel="noopener">{e(ADDRESS["street"])}<br>{e(ADDRESS["city"])} ({e(ADDRESS["region"])}) {e(ADDRESS["zip"])}</a></address>
        <h3>{e(t["phone_h"])}</h3>
        <p><a class="phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <h3>{e(t["hours_h"])}</h3>
        <table class="hours"><tbody>{days}</tbody></table>
        <div class="cta">
          <a class="btn btn-call" href="tel:{PHONE_TEL}">{ico["phone"]}<span>{e(t["call"])}</span></a>
          <a class="btn btn-wa" href="{wa_url}" rel="noopener">{ico["wa"]}<span>{e(t["wa"])}</span></a>
        </div>
        <h3>{e(t["follow_h"])}</h3>
        <p class="social">
          <a href="{INSTAGRAM}" rel="noopener me" target="_blank">{ico["ig"]}<span>{e(t["ig"])}</span></a>
          <a href="{FACEBOOK}" rel="noopener me" target="_blank">{ico["fb"]}<span>{e(t["fb"])}</span></a>
        </p>
      </div>
      <div class="map">
        <iframe title="{e(t["map_title"])}" src="{maps_embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p><strong>Carnitas Michoacanas Leoncito</strong> · {e(ADDRESS["street"])}, {e(ADDRESS["city"])} · <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
    <p class="small">© 2026 Carnitas Michoacanas Leoncito. {e(t["footer_rights"])} {e(t["logo_credit"])}</p>
    <details class="credits"><summary>{e(t["credits_h"])}</summary><p>{e(t["credits_intro"])}</p><ul>{credit_items}</ul></details>
  </div>
</footer>

<a class="fab" href="{wa_url}" rel="noopener" aria-label="{e(t["wa_label"])}">{ico["wa"]}</a>
<script src="../assets/js/main.js" defer></script>
</body>
</html>
'''
    (ROOT / lang).mkdir(exist_ok=True)
    (ROOT / lang / "index.html").write_text(page, encoding="utf-8")

for l in ("fr", "es"):
    build(l)

# sitemap + credits
(ROOT / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{SITE}/fr/</loc><xhtml:link rel="alternate" hreflang="fr" href="{SITE}/fr/"/><xhtml:link rel="alternate" hreflang="es" href="{SITE}/es/"/></url>
  <url><loc>{SITE}/es/</loc><xhtml:link rel="alternate" hreflang="fr" href="{SITE}/fr/"/><xhtml:link rel="alternate" hreflang="es" href="{SITE}/es/"/></url>
</urlset>
''', encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
cr = json.load(open(ROOT / "assets/credits.json", encoding="utf-8"))
lines = ["# Créditos de imágenes\n", "Fotos de platillos tomadas de Wikimedia Commons con licencias libres que exigen atribución (ya incluida en el pie de cada página).\n",
         "Logo y mascota: propiedad de Carnitas Michoacanas Leoncito.\n", "| Archivo local | Título | Autor | Licencia | Fuente |", "|---|---|---|---|---|"]
for slug, c in cr.items():
    lines.append(f"| `assets/img/{slug}-*.webp` | {c['title']} | {c['artist']} | {c['license']} | {c['page']} |")
(ROOT / "CREDITOS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("OK: fr/index.html, es/index.html, sitemap.xml, robots.txt, CREDITOS.md")
