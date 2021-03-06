![VenC](https://download.tuxfamily.org/dsalem/img/2017_-_Denis_Salem_-_CC_By_SA_-_VenC-logo.svg "VenC")

# Tutoriels

1. [Installer VenC et créer son blog en moins de 5 minutes!](#installer-venc-et-cr%C3%A9er-son-blog-en-moins-de-5-minutes)
2. [Créer une nouvelle publication](#créer-une-nouvelle-publication)
3. [Publier](#publier)
4. [Mettre en ligne](#mettre-en-ligne)

## Installer VenC et créer son blog en moins de 5 minutes!

Et ouais, c'est possible!

Dabord, il faut installer [pip](https://pypi.python.org/pypi/pip), si ce n'est pas déjà le cas! VenC utilise la version 3 de python, assurez vous donc d'avoir la version de [pip](https://pypi.python.org/pypi/pip) correspondante!

Une fois que c'est fait on install VenC. Pour de vrai.

	pip install venc --user

Vous pouvez maintenant créer votre blog!

	venc --new-blog "MonSuperBlog"

Après cette commande, VenC a créer un répertoire appelé "MonSuperBlog" à l'endroit où vous avez lancé la commande. Ce repertoire contient toutes les informations de votre blog. Il faut donc le garder préciseument, et même en faire des sauvegardes de temps à autres!

La prochaine étape consiste à paramétrer un peu le blog. Pour ça il suffit d'éditer le fichier *blog_configuration.yaml* à la racine de ce repertoire. Vous pourrez notamment y définir le nom de votre blog, sa langue, ses mots clef, etc. Pour plus d'informations sur la configuration du blog, rendez-vous [ici](https://framagit.org/denissalem/VenC/blob/master/doc/FR.md#fichier-de-configuration-principal)

Et voilà, c'est terminé! Votre blog est prêt à l'emploi!

_Si vous avez rencontré une difficulté durant ce tutoriel, jetez un oeil à la [FAQ](faqFR.md), la solution s'y trouvera certainement!_

## Créer une nouvelle publication

Pour créer une nouvelle publication, placez vous dans le répertoire de votre blog et tapez la commande suivante

	venc --new-entry "Ma Première Publication"

Cette commande crée la publication et la stock dans le repertoire *entries* de votre blog.

__Astuce : L'éditeur de texte par défaut définit dans votre fichier de configuration devrait être _nano_. Quand vous créez une nouvelle publication VenC l'ouvre pour vous dans l'éditeur de texte ainsi définit. Vous pouvez changer votre éditeur de texte dans *blog_configuration.yaml*.__

Une publication vierge ressemble à ça

	CSS: ''
	authors: ''
	categories: ''
	entry_name: Ma Première Publication
	tags: ''
	---

C'est un document découpé en deux parties à l'aide de la ligne _triple tiret du six_

La premiére partie contient les méta-données de la publication au format [yaml](http://www.yaml.org/) et la seconde contient la publication à proprement parler au format [Markdown](https://daringfireball.net/projects/markdown/).

__Astuce : Par défaut VenC utilise la syntax [Markdown](https://daringfireball.net/projects/markdown/), vous pouvez cependant désactiver [Markdown](https://daringfireball.net/projects/markdown/) en ajoutant le champ _doNotUseMarkdown_ à la liste des méta-données du document. Oui, le champ est vide, il n'a pas besoin de valeur particulière.__

Pour en savoir plus sur les méta-données des publications rendez vous [ici](FR.md#les-publications)

La rédaction de la publication se fait dans la seconde partie du document donc, après les trois tiret.

Une fois que vous avez terminé d'écrire le meilleur billet de blog de tous les internets, enregistrez, et c'est finis! Il n'y à plus qu'à publier!

## Publier

Vous avez donc écris un ou plusieurs articles et vous voulez voir ce que ça donne! Placez vous dans le répertoire de votre blog et lancez la commande

	venc --export-blog gentle

Cette commande va créer les pages HTML de votre blog en utilisant le thème __*gentle*__. Pour connaitre quels sont les thèmes disponibles, tapez

	venc --themes

Vous pouvez alors recompiler votre blog en passant en paramètre le nom d'un des thèmes dans la liste, en vert.

Si vous souhaitez faire votre propre thème HTML/CSS vous pouvez vous aider du thème __*dummy*__ qui contiens un squelette HTML pouvant servir de base. Copiez alors les fichiers de celui-ci dans le répertoire _theme_ de votre blog. Si VenC est installé correctement, __*dummy*__ devrait se trouver dans _~/.local/share/VenC/themes/_.

Pour compiler le blog avec ce thème bien à vous:

	venc --export-blog

VenC utilise par défaut le thème local quand aucun nom de thème ne lui est précisé.

Pour en savoir plus sur les thèmes rendez-vous [ici](FR.md#les-thèmes)

Le contenu de votre site est maintenant disponible dans le repertoire _blog_ de votre blog. Pour visualiser le résultat vous pouvez ouvrir dans le navigateur de votre choix le fichier index.html qui s'y trouve.

Et voilà, le moins qu'on puisse dire, c'est que _vous pesez lourd dans le game_ maintenant!

## Mettre en ligne

Maintenant que votre blog vous plait, il est temps de le mettre en ligne et d'en faire profiter les internautes!

Il y a plusieurs façon de faire. La première approche consiste à copier manuellement le contenu du répertoire _blog_ vers le serveur en ligne. Mais ce peut-être un peu fastidieux quand on sait que VenC prend peut prendre en charge le transfert de votre blog en ligne.

Pour que VenC puisse mettre en ligne votre blog, vous devez lui fournir quelques informations dans le fichier _blog_configuration.yaml_. Pour cela renseignez le champ _ftp_host_ avec l'adresse du serveur FTP de destination. Renseignez également le sous-champ _ftp_ du champ _path_ en indiquant le chemin de destination où sera copié le contenu de votre blog, sur le serveur en ligne.

__Attention: Soyez vigilant en renseignant le champ _ftp_ qui détermine le chemin de destination. Au moment de l'exporation en ligne, VenC efface le contenu de ce répertoire! Assurez de savoir ce que vous faite!__

Après avoir fournis les informations dont VenC a besoin, vous pouvez copier votre blog en ligne:

	venc --remote-copy

De cette façon, VenC vous demandera de vous authentifier auprès du serveur. C'est seulement après vous être authentifié que le transfert commencera. Vous pouvez allers vous chercher un café, ou un jus de tomate. Perso, je préfère le jus de tomate.

Une autre façon de faire est de compiler le blog et de l'exporter en ligne en une seule commande

	venc --export-via-ftp [thème]

Comme pour la commande précédente, vous devrez vous authentifier. Vous pouvez également préciser un nom de thème avec lequel vous voulez compiler votre blog.

Voilà, c'est tout! Normalement, votre blog devrait être en ligne avec ça!
