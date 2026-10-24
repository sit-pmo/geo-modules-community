# Méthode de débogage qui a marché

1. **Sonder l'application vivante** dans la console du navigateur plutôt que fouiller des bundles minifiés de plusieurs Mo.
2. ⚠️ Le **copier-coller dans un terminal peut supprimer des espaces** (`var s` devient `vars`) : écrivez vos sondes en expressions pures, sans
   `var`, `let` ni `return`.
3. Semez des `console.log('[nom-module][diag] …')`, construisez, essayez, puis **retirez-les**.
4. Un **symptôme sans erreur** doit faire chercher une branche de repli silencieuse avant d'incriminer la plateforme.
5. **Mesurez plutôt que supposer** (rapports de zoom, tailles, `z-index` calculés) et consignez le résultat dans le message de commit : symptôme, cause,
   correction, ce qui est validé sur GEO et ce qui ne l'est pas.
6. Les tests automatiques couvrent la logique pure (Node). Ce qui dépend de GEO se vérifie par une **liste de contrôle manuelle** ; un exemple est
   dans le [guide de développement de geo-module-panoramax](https://github.com/vienne-condrieu-agglomeration/geo-module-panoramax/blob/main/GUIDE-DEV.md).
