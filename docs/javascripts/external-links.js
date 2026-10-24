// Ouvre les liens externes (autre nom d'hôte que celui du site) dans un nouvel onglet.
// Les liens internes restent dans l'onglet courant : la navigation du site n'est pas modifiée.
(function () {
  function isExternal(link) {
    return /^https?:$/.test(link.protocol) && link.hostname !== window.location.hostname;
  }

  function mark(link) {
    if (isExternal(link) && !link.target) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  }

  function markAll() {
    document.querySelectorAll("a[href]").forEach(mark);
  }

  // Filet de sécurité : un lien ajouté après le chargement est marqué au moment du clic
  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[href]");
    if (link) { mark(link); }
  }, true);

  // « document$ » est publié par le thème à chaque page, y compris avec la navigation instantanée
  if (typeof document$ !== "undefined") {
    document$.subscribe(markAll);
  } else {
    document.addEventListener("DOMContentLoaded", markAll);
  }
})();
