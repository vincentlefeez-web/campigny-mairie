# Télécharge les photos de paysages de l'ancien site campigny27.fr
# dans le dossier Téléchargements\campigny-photos, avec les noms attendus par le nouveau site.
# Utilisation : clic droit sur ce fichier > « Exécuter avec PowerShell »

$dest = Join-Path ([Environment]::GetFolderPath("UserProfile")) "Downloads\campigny-photos"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

$base = "https://www.campigny27.fr/sites/default/files/images"
$photos = [ordered]@{
  "bandeau-site.jpg"            = "https://www.campigny27.fr/sites/all/themes/resiaw/images/bandeau-site.jpg"
  "vue-aerienne.jpg"            = "$base/campigny-vue-aerienne.jpg"
  "coucher-de-soleil.jpg"       = "$base/photo_jeanne_4_campigny.jpg"
  "campagne.jpg"                = "$base/photo_jeanne_1_campigny.jpg"
  "chemin-mare-aux-perdrix.jpg" = "$base/chemin_de_la_mare_aux_perdrix_1.jpg"
  "campagne-juin-2017.jpg"      = "$base/juin_2017_campagne_1.jpg"
  "campigny-juillet-2019.jpg"   = "$base/campigny_07_2019_2.jpg"
  "cheval.jpg"                  = "$base/cheval_campigny.jpg"
  "vaches.jpg"                  = "$base/vaches_4_06_2019.jpg"
  "moutons.jpg"                 = "$base/moutons.jpg"
}

foreach ($nom in $photos.Keys) {
  try {
    Invoke-WebRequest -Uri $photos[$nom] -OutFile (Join-Path $dest $nom) -UseBasicParsing
    Write-Host "OK  $nom"
  } catch {
    Write-Host "ERREUR  $nom : $($_.Exception.Message)" -ForegroundColor Red
  }
}

Compress-Archive -Path "$dest\*" -DestinationPath "$dest.zip" -Force
Write-Host "`nTerminé : $dest.zip — glisse ce fichier dans la conversation avec Claude."
Read-Host "Appuie sur Entrée pour fermer"
