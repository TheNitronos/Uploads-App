===========================
jQuery Mobile et Bootstrap
===========================

***************************************
Fonctionnement général de jQuery Mobile
***************************************

La majeure partie de jQuery Mobile se joue dans le balisage de son code html. 
Dans la mesure où l'on définit si le contenu d'un balisage:

Du contenu:

.. code-block:: html

    <div>contenu</div>

Un lien:

.. code-block:: html

    <a href="#">lien</a>
    
et pourquoi pas un bouton:

.. code-block:: html

    <button>bouton</button>
    
deviendra une page, une boîte de dialogue ou encore une liste entre autres. Pour un petit test, 
faisons l'exemple avec ces trois morceaux de code. Ainsi en ajoutant des classes 
telles que ui-content pour le contenu:

.. code-block:: html

    <div class="ui-content">contenu</div> 

Les scripts jQuery Mobile viendront s'appliquer là-dessus et considéreront ceci 
comme le contenu d'une page et appliqueront le code css nécessaire. 
Pareil pour le lien et le bouton qui suivent. Nous pouvons y ajouter la classe 
'ui-btn' qui dira aux scripts jQuery Mobile d'appliquer de code css nécessaire 
pour avoir l'allure d'un bouton.

.. code-block:: html

    <a href="#" class="ui-btn">lien</a>
    <button class="ui-btn">bouton</button>
    
Pour l'utilisation de jQuery Mobile, il est donc nécessaire de travailler avec ce balisage 
qui permettra à la bibliotheque d'interpréter le code et d'y appliquer les 
attributs et la mise en page nécessaire avec une allure très agréable à 
l'utilisation tactile et très bien adaptée aux écrans de taille plutôt réduite que l'on 
peut retrouver sur un smartphone standard voire sur une tablette de petite taille. 


***********************************
Fonctionnement général de Bootstrap
***********************************

Bootstrap ne sera pas au coeur de ce travail mais il est intéressant de comparer 
ces bibliothèques qui peuvent paraître proches mais qui finalement offrent un rendu 
relativement opposé. Le principe de bootstrap est basé non pas sur le balisage 
comme jQuery Mobile mais sur une sorte de grille. Cette grille sera composée d'un 
certain nombre de colonnes et de lignes où l'utilisateurs pourra positionner les 
éléments qu'il désire afficher sur sa page. Et c'est lors du changement de support 
que l'on peut observer toute la magie de bootstrap car cette grille s'adapte elle-même 
à l'écran. Ainsi le contenu se dit "responsive", soit "qui s'adapte". Par exemple,
un barre de navigation initialement placée sur le côté gauche verticalement si l'on consulte 
le site sur un écran large pourrait se retrouver horizontalement sur un écrant plus 
étroit au dessus du contenu principal.

**************************
Similitudes et différences
**************************

Ces deux bibliothèques se ressemblent dans la mesure où elles me seraient toutes
les deux utiles afin de créer une interface mobile pour ma future application.
Elles proposent un affichage qui est facilement utilisable dans des conditions
que l'on ne retrouve pas sur un ordinateur de bureau et auxquelles on ne pense pas 
forcément au cours du développement. Ceci nous permet donc une interface utilisateur
adaptée aux besoins d'une personne utilisant cette application mobile. Les deux
présentent également un très bon système pour modifier les thèmes et ainsi
apporter un côté ludique ou encore plus agréable.
Par contre Bootstrap se concentre vraiment sur une allure du site qui s'adapte
aux différents formats d'écrans tandis que jQuery Mobile est plutôt dans l'optique
de proposer un rendu qui lui est entièrement consacré au mobile en se souciant peu
de l'affichage sur une plus grand écran. Malgré cela, on peut dire que l'affichage
mobile sur un grand écran n'est pas désagréable notammant si l'on dispose d'un écran 
tactile mais ce n'est pas le meilleur que l'on puisse avoir.