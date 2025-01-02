# Delphi - Design Pattern

## Comment créer un singleton ayant pour nom [MASK] ?
    - Param: NomSingleton

* Crée une classe ayant pour nom |NomSingleton|.
* Ajoute le champ static privé Instance.
* Ajoute un constructeur privé Create.
* Ajoute une méthode protected onCreate.
* Ajoute une méthode statique Get qui retourne un |NomSingleton|.
* Dans la méthode Get : 
    * Si l'instance est nulle alors
        * lance la construction de l'instance de classe |NomSingleton|.
        * lance la méthode onCreate de l'instance
    * retourne l'instance
* Explique que tu as créé un singleton ayant pour nom **|NomSingleton|**.

## Comment créer le contexte de la DLL [MASK] ?
    - Param: NomDLL

* Crée une unité Delphi ayant pour nom Lp|NomDLL|Context.pas.
* Crée un singleton ayant pour nom TLp|NomDLL|Context.
* Ajoute les propriétés status, message et header de type string. Ces champs servent à stocker les informations utiles des réponses REST.
* ajoute les propriétés PWDCrypt, UserName, PassWord et API_KEY de type string.
* ajoute un méthode setResult.
* dans la méthode setResult : 
    * Ajoute les paramètres Status, Message et Header de type string.
    * Affecte les champs Status, Message et Header avec les paramètres correspondants.
* ajoute une constante fichier ini ayant pour valeur |NomDLL|.ini.
* ajoute une méthode Charger configuration.
* dans la méthode Charger Configuration :
    * si le fichier ini n'existe pas alors
        * lance la méthode setStatus avec comme paramètres 099, Fichier ini introuvable et chain vide
        * sort
    * charge les propriétés PWDCrypt, UserName, PassWord et API_KEY depuis le fichier ini.
    * décrypte UserName, PassWord et API_KEY avec PWDCrypt comme mode.
* Explique que tu as ajouté **status**, **message** et **header** pour stocker .

## Comment créer le fichier ini de la DLL [MASK] ?
    - Param: NomDLL

## Comment créer la classe de commande générique de la DLL [MASK] ?
    - Param: NomDLL

## Comment créer l'unité des commandes de la DLL [MASK] ?
    - Param: NomDLL

## Comment créer la DLL [MASK]
    - Param: NomDLL

* Crée le projet de la DLL |NomDLL|.
* Crée le fichier ini de la DLL |NomDLL|.
* Crée le contexte de la DLL |NomDLL|.
* Crée la classe de commande générique de la DLL |NomDLL|.
* Crée l'untié des commandes de la DLL |NomDLL|.
