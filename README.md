# Site de la mairie de Campigny (27500)

Refonte du site [campigny27.fr](https://www.campigny27.fr) : site statique, léger, accessible et sans traceur.

## Structure

```
src/pages/*.html   → contenu de chaque page (à modifier)
build.py           → assemble les pages avec l'en-tête et le pied de page
assets/css/        → styles
assets/js/         → menu mobile, taille du texte, statut « ouvert/fermé », formulaire
*.html (racine)    → pages générées, publiées telles quelles
```

## Modifier une page

1. Éditer le fichier dans `src/pages/` (ex. `src/pages/salles.html`).
2. Lancer `python3 build.py` (Python 3, aucune dépendance).
3. Commiter les fichiers modifiés.

Les horaires du secrétariat utilisés pour le badge « ouvert / fermé » sont dans `assets/js/main.js` (constante `HORAIRES`).

## Publier avec GitHub Pages

Settings → Pages → *Deploy from a branch* → `main` / racine (`/`).
Pour garder l'adresse campigny27.fr, ajouter un fichier `CNAME` contenant `www.campigny27.fr` et faire pointer le DNS vers GitHub Pages.

## Choix techniques

- **RGPD** : aucune police Google, aucun cookie, aucune statistique tierce. Le formulaire de contact ouvre la messagerie de l'internaute (rien n'est stocké).
- **Accessibilité (RGAA)** : lien d'évitement, navigation clavier, contrastes, agrandissement du texte, `prefers-reduced-motion`.
- **Mobile d'abord**, impression propre.

## Contenus à compléter

Les éléments surlignés en jaune `[À compléter]` sur le site signalent les informations à fournir ou à valider par la mairie (édito du maire, délégations des adjoints, comptes rendus 2026, menus de cantine, collecte des déchets, associations, commerces, tarifs 2026…). Pour les lister :

```
grep -o 'a-completer">[^<]*' src/pages/*.html
```

Données reprises de l'ancien site et de sources publiques (résultats des municipales 2026).
