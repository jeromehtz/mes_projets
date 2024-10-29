const quelques_tips = [
    {
        question:"Quelle méthode de verrouillage utilisez-vous pour sécuriser votre téléphone, et comment pourriez-vous la rendre encore plus robuste ?",
        tips:"Utilisez un code PIN ou une méthode de verrouillage sécurisée : Assurez-vous que votre téléphone est protégé par un code PIN, un mot de passe complexe, une empreinte digitale ou la reconnaissance faciale. Évitez les codes PIN trop simples comme \"1234\" ou \"0000\"."
    },
    {
        question:"Quand désactivez-vous le Bluetooth et le Wi-Fi sur votre téléphone, et dans quelles situations pensez-vous que cela est particulièrement important ?",
        tips:"Désactivez le Bluetooth et le Wi-Fi lorsque vous ne les utilisez pas : Cela réduit le risque de connexion non autorisée à votre appareil."
    },
    {
        question:"À quelle fréquence sauvegardez-vous les données de votre téléphone, et quels types de données considérez-vous comme les plus critiques à protéger ?",
        tips:"Faites des sauvegardes régulières : Sauvegardez régulièrement les données de votre téléphone afin de ne rien perdre en cas de piratage ou de panne."
    },
    {
        question:"Quelles méthodes utilisez-vous pour gérer vos mots de passe, et comment vous assurez-vous qu'ils sont suffisamment forts et uniques pour chaque service ?",
        tips:"Utilisez un gestionnaire de mots de passe : Un gestionnaire de mots de passe vous aidera à créer et stocker des mots de passe uniques et complexes pour chaque application."
    },
    {
        question:"Avez-vous activé le chiffrement des données sur votre téléphone, et en quoi pensez-vous que cela améliore la protection de vos informations en cas de vol ?",
        tips:"Activez le chiffrement des données : La plupart des smartphones permettent de chiffrer les données de stockage, ce qui empêche l'accès non autorisé en cas de vol."
    },
    {
        question:"À quelle fréquence mettez-vous à jour votre téléphone et vos applications, et comment vérifiez-vous que toutes les mises à jour de sécurité sont bien installées ?",
        tips:"Gardez votre téléphone et vos applications à jour : Les mises à jour contiennent souvent des correctifs de sécurité importants. Assurez-vous d'utiliser les dernières versions du système d'exploitation et des applications."
    },
    {
        question:"Comment choisissez-vous les applications à télécharger, et quels critères utilisez-vous pour vous assurer qu'elles proviennent de sources fiables ?",
        tips:"Téléchargez uniquement des applications officielles : Utilisez les boutiques d'applications officielles (App Store, Google Play) pour installer vos applications. Vérifiez les avis et le nombre de téléchargements avant d'installer une application, et méfiez-vous des sources inconnues."
    },
    {
        question:"Comment réagissez-vous face aux messages ou aux liens suspects que vous recevez, et quels sont les signes qui vous alertent d'un potentiel danger ?",
        tips:"Faites attention aux messages et aux liens suspects : Ne cliquez pas sur les liens ou les pièces jointes provenant de sources inconnues ou suspectes, que ce soit par email, SMS ou messagerie instantanée."
    },
    {
        question:"Quelle est votre stratégie pour gérer les connexions Wi-Fi publiques, et quelles mesures prenez-vous pour protéger vos données lorsque vous les utilisez ?",
        tips:"Soyez vigilant avec les connexions Wi-Fi publiques : Les réseaux Wi-Fi publics peuvent être moins sécurisés. Évitez d'accéder à des informations sensibles sur ces réseaux ou utilisez un VPN pour chiffrer votre connexion."
    },
    {
        question:"Avez-vous déjà envisagé d'activer l'authentification à deux facteurs sur vos applications sensibles, et si oui, comment cela a-t-il renforcé votre sécurité ?",
        tips:"Activez l'authentification à deux facteurs (2FA) : Pour les applications sensibles (réseaux sociaux, emails, services bancaires), activez l'authentification à deux facteurs afin d'ajouter une couche de sécurité supplémentaire."
    }
  ];

  function shuffle(quelques_tips) {
    const tipsContainer = document.getElementById("tips-container");
    tipsContainer.innerHTML = "";
    
    for (let i = 0; i<=quelques_tips.length - 1; i++) {
        // tipsContainer.textContent = `${quelques_tips[i]}`;
        const label = document.createElement("label");
        tipsContainer.appendChild(label);
        label.appendChild(document.createTextNode(quelques_tips[i].question));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode(quelques_tips[i].tips));
        tipsContainer.appendChild(document.createElement("br"));
    }
  }

  function RedirectionJavascript(page){
    document.location.href=page;
  }
  
  shuffle(quelques_tips);
