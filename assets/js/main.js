// Mairie de Campigny — scripts légers, sans dépendance ni traceur
(function () {
  // Menu mobile
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav-principale');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var ouvert = nav.classList.toggle('ouvert');
      burger.setAttribute('aria-expanded', ouvert ? 'true' : 'false');
    });
  }

  // Taille du texte (mémorisée si possible)
  var html = document.documentElement;
  var classes = ['', 'grand', 'tres-grand'];
  function appliquer(i) {
    classes.forEach(function (c) { if (c) html.classList.remove(c); });
    if (classes[i]) html.classList.add(classes[i]);
    document.querySelectorAll('[data-taille]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(Number(b.dataset.taille) === i));
    });
    try { localStorage.setItem('campigny-taille', i); } catch (e) {}
  }
  var init = 0;
  try { init = Number(localStorage.getItem('campigny-taille')) || 0; } catch (e) {}
  appliquer(init);
  document.querySelectorAll('[data-taille]').forEach(function (b) {
    b.addEventListener('click', function () { appliquer(Number(b.dataset.taille)); });
  });

  // Horaires du secrétariat : statut ouvert / fermé + ligne du jour
  // jour JS : 0 = dimanche … 6 = samedi ; plages en heures décimales
  var HORAIRES = { 1: [[14, 18]], 4: [[14, 19]], 5: [[9, 12]] };
  var maintenant = new Date();
  var j = maintenant.getDay();
  var h = maintenant.getHours() + maintenant.getMinutes() / 60;
  document.querySelectorAll('table.horaires tr[data-jour]').forEach(function (tr) {
    if (Number(tr.dataset.jour) === j) tr.classList.add('aujourdhui');
  });
  var ouvert = (HORAIRES[j] || []).some(function (p) { return h >= p[0] && h < p[1]; });
  document.querySelectorAll('[data-statut-mairie]').forEach(function (el) {
    el.classList.add(ouvert ? 'ouvert' : 'ferme');
    el.textContent = ouvert ? 'Secrétariat ouvert en ce moment' : 'Secrétariat fermé en ce moment';
  });

  // Formulaire de contact : ouvre la messagerie (aucune donnée stockée sur le site)
  var form = document.querySelector('form.contact');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var sujet = '[Site web] ' + d.get('objet') + ' — ' + d.get('nom');
      var corps = d.get('message') + '\n\n—\n' + d.get('nom') + '\n' + d.get('email') + (d.get('tel') ? '\n' + d.get('tel') : '');
      window.location.href = 'mailto:mairie.campigny27@orange.fr?subject=' + encodeURIComponent(sujet) + '&body=' + encodeURIComponent(corps);
    });
  }

  // Année du pied de page
  document.querySelectorAll('[data-annee]').forEach(function (el) { el.textContent = maintenant.getFullYear(); });
})();
