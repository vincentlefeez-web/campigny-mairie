#!/usr/bin/env python3
"""
Générateur du site de la mairie de Campigny.

Chaque page vit dans src/pages/<nom>.html. Ses premières lignes contiennent
ses métadonnées sous forme de commentaire :

    <!--
    titre: La mairie
    description: Horaires, coordonnées, élus…
    nav: mairie
    -->

Lancer `python3 build.py` régénère les fichiers .html à la racine
(c'est ce que GitHub Pages publie). Aucune dépendance.
"""
import re
from pathlib import Path

RACINE = Path(__file__).parent
PAGES = RACINE / "src" / "pages"

SITE = "Mairie de Campigny"
URL = "https://www.campigny27.fr"

NAV = [
    ("index", "Accueil"),
    ("mairie", "La mairie"),
    ("demarches", "Démarches"),
    ("enfance", "Enfance & école"),
    ("vivre", "Vivre à Campigny"),
    ("associations", "Associations"),
    ("decouvrir", "Découvrir"),
    ("contact", "Contact"),
]

LOGO = """<svg viewBox="0 0 48 48" aria-hidden="true">
  <path d="M24 3 6 9v14c0 11 8 19 18 22 10-3 18-11 18-22V9L24 3Z" fill="#1f5643"/>
  <path d="M6 27c5-4 11-5 18-2s13 2 18-2v-.1C41 34 33 42 24 45 15 42 7 35 6 27Z" fill="#2f7a5f"/>
  <circle cx="24" cy="19" r="7" fill="#b5352b"/>
  <path d="M24 12c0-3 2-5 4-5" stroke="#c99a2e" stroke-width="2.2" fill="none" stroke-linecap="round"/>
  <path d="M25 11c2-2 5-2 6 0-2 2-4 2-6 0Z" fill="#c99a2e"/>
</svg>"""


def lire_page(fichier: Path):
    texte = fichier.read_text(encoding="utf-8")
    m = re.match(r"\s*<!--(.*?)-->\s*", texte, re.S)
    meta = {}
    if m:
        for ligne in m.group(1).strip().splitlines():
            if ":" in ligne:
                cle, val = ligne.split(":", 1)
                meta[cle.strip()] = val.strip()
        texte = texte[m.end():]
    return meta, texte


def gabarit(nom, meta, corps):
    titre = meta.get("titre", SITE)
    titre_complet = SITE if nom == "index" else f"{titre} — {SITE}"
    desc = meta.get("description", "Site officiel de la commune de Campigny (Eure, Normandie).")
    actif = meta.get("nav", nom)
    courant = ' aria-current="page"'
    liens = "\n".join(
        '        <li><a href="' + ("./" if n == "index" else n + ".html") + '"'
        + (courant if n == actif else "") + ">" + lib + "</a></li>"
        for n, lib in NAV
    )
    canon = URL + "/" + ("" if nom == "index" else f"{nom}.html")
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titre_complet}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canon}">
  <meta property="og:title" content="{titre_complet}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta name="theme-color" content="#12332a">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="evitement" href="#contenu">Aller au contenu</a>

  <div class="outils">
    <div class="conteneur">
      <span>Commune de Campigny · Eure · Normandie</span>
      <div class="taille" role="group" aria-label="Taille du texte">
        <span aria-hidden="true">Texte :</span>
        <button type="button" data-taille="0" aria-label="Taille normale">A</button>
        <button type="button" data-taille="1" aria-label="Texte agrandi">A+</button>
        <button type="button" data-taille="2" aria-label="Texte très agrandi">A++</button>
      </div>
    </div>
  </div>

  <header class="entete">
    <div class="conteneur">
      <a class="marque" href="./" aria-label="{SITE} — accueil">
        {LOGO}
        <div><strong>Campigny</strong><span>Mairie · Eure</span></div>
      </a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="nav-principale">
        <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        Menu
      </button>
      <nav class="nav" id="nav-principale" aria-label="Navigation principale">
        <ul>
{liens}
        </ul>
      </nav>
    </div>
  </header>

  <main id="contenu" tabindex="-1">
{corps}
  </main>

  <footer class="pied">
    <div class="conteneur">
      <div class="grille">
        <div>
          <h2>Mairie de Campigny</h2>
          <p>Place de la Pelouse<br>27500 Campigny</p>
          <p>Tél. <a href="tel:+33232410252">02 32 41 02 52</a><br>
          <a href="mailto:mairie.campigny27@orange.fr">mairie.campigny27@orange.fr</a></p>
        </div>
        <div>
          <h2>Secrétariat</h2>
          <ul>
            <li>Lundi : 14 h – 18 h</li>
            <li>Jeudi : 14 h – 19 h</li>
            <li>Vendredi : 9 h – 12 h</li>
          </ul>
          <p><small>Sur rendez-vous de préférence.</small></p>
        </div>
        <div>
          <h2>Accès rapides</h2>
          <ul>
            <li><a href="salles.html">Location des salles</a></li>
            <li><a href="enfance.html#cantine">Cantine</a></li>
            <li><a href="demarches.html">Démarches</a></li>
            <li><a href="mairie.html#conseil">Conseil municipal</a></li>
          </ul>
        </div>
        <div>
          <h2>Liens utiles</h2>
          <ul>
            <li><a href="https://www.service-public.fr" rel="noopener">Service-public.fr</a></li>
            <li><a href="https://ants.gouv.fr" rel="noopener">ANTS (titres d'identité, permis, cartes grises)</a></li>
            <li><a href="https://www.eure.gouv.fr" rel="noopener">Préfecture de l'Eure</a></li>
          </ul>
        </div>
      </div>
      <div class="bas">
        <span>© <span data-annee>2026</span> Commune de Campigny</span>
        <ul>
          <li><a href="mentions-legales.html">Mentions légales</a></li>
          <li><a href="accessibilite.html">Accessibilité : partiellement conforme</a></li>
          <li><a href="plan-du-site.html">Plan du site</a></li>
        </ul>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def main():
    plan = []
    for fichier in sorted(PAGES.glob("*.html")):
        nom = fichier.stem
        meta, corps = lire_page(fichier)
        (RACINE / f"{nom}.html").write_text(gabarit(nom, meta, corps), encoding="utf-8")
        plan.append((nom, meta.get("titre", nom)))
        print(f"  ✓ {nom}.html")

    # Plan du site généré automatiquement
    items = "\n".join(
        f'        <li><a href="{"./" if n == "index" else n + ".html"}">{t}</a></li>'
        for n, t in plan if n not in ("404",)
    )
    corps = f"""    <div class="bandeau-page"><div class="conteneur">
      <p class="fil"><a href="./">Accueil</a> › Plan du site</p>
      <h1>Plan du site</h1>
    </div></div>
    <div class="conteneur" style="padding-block:2.5rem 4rem">
      <ul class="liste-coche">
{items}
      </ul>
    </div>"""
    (RACINE / "plan-du-site.html").write_text(
        gabarit("plan-du-site", {"titre": "Plan du site", "nav": ""}, corps), encoding="utf-8")
    print("  ✓ plan-du-site.html")


if __name__ == "__main__":
    main()
