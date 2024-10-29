const questions = {
    INFO: [
        { question: "Citer 2 langage de développement web", reponse: "réponse possible :HTML,CSS,JavaScript,PHP,Python,Java,C#" },
        { question: "En quoi une variable est-elle utile dans un programme ?", reponse: "Une variable permet de stocker des données (nombres, texte, etc.) qu'on peut réutiliser ou modifier tout au long de l'exécution du programme." },
        { question: "Dans un programme, à quoi sert une boucle", reponse: "Les boucles permettent de répéter une série d'instructions plusieurs fois sans avoir à réécrire le même code" },
        { question: "A quoi sert le front-end et le back-end dans une application web ?", reponse: "Le front-end concerne la partie visible de l'application avec laquelle l'utilisateur interagit. Le back-end gère la logique métier, les bases de données et les serveurs"},
        { question: "Pourquoi utilise-t-on une adresse IP dans un réseau ?", reponse: "Une adresse IP identifie de manière unique chaque appareil connecté à un réseau, permettant ainsi l'envoi et la réception de données entre les machines." },
        { question: "Sous quelle forme une base de donnée stocke elle les informations ?", reponse: "Une base de données stocke les informations sous forme de tables, chacune composée de lignes (enregistrements) et de colonnes (champs). Chaque table représente un ensemble de données liées " },
        { question: "En base de donnée, qu'est ce qu'une clé primaire ?", reponse: "Une clé primaire est un identifiant unique pour chaque enregistrement d'une table" },
        { question: "Que veux dire SEO ?", reponse: "Le SEO (Search Engine Optimization) est l'acronyme qui signifie « Optimisation pour les moteurs de recherche » en français. C'est un ensemble de techniques permettant d'améliorer le positionnement d'un site web dans les moteurs de recherche" },
        { question: "Pourquoi les entreprises investissent elles dans la publicité sur des moteurs de recherche comme Google Ads ?", reponse: "Les entreprises investissent dans Google Ads pour atteindre rapidement des clients potentiels en haut des résultats de recherche." },
        { question: "Quelles sont les principales différences entre un réseau Wi-Fi et un réseau câblé Ethernet ?", reponse: "Un réseau Wi-Fi utilise des ondes radio pour transmettre des données sans fil, offrant plus de mobilité mais parfois moins de stabilité et de vitesse que le réseau câblé. Le réseau câblé Ethernet utilise des câbles physiques pour une connexion plus stable et rapide." },
        { question: "A quoi sert Cisco Packet tracer, un programme utilisé en première année à l’EPSI", reponse: "Cisco Packet Tracer est un simulateur de réseau permettant de créer, configurer et tester des réseaux virtuels" },
        { question: "Quel est un avantage d'un cite en CMS tel que WordPress lors du développement d'un site web ?", reponse: "Un CMS comme WordPress facilite la création et la gestion de sites web en fournissant des outils et des fonctionnalités préconstruits pour gérer le contenu, le design, et les plugins. Cela permet aux utilisateurs non techniques de mettre à jour et de personnaliser leur site sans avoir besoin de compétences en programmation." },
        { question: "C'est quoi un CMS ?", reponse: "Un CMS (Content Management System) est un système de gestion de contenu qui permet de créer, gérer et modifier facilement des sites web sans nécessiter de compétences techniques avancées." }

    ],
    EPSI: [
        { question: "Quelle est la spécialité principale des écoles EPSI ?", reponse: "L'informatique" },
        { question: "Quel est le nom du projet que les étudiants EPSI réalisent-ils en début d'année ?", reponse: "Le workshop" },
        { question: "Oui ou non est t-il possible d'apprendre de la cybersécurité à Epsi?", reponse: "Oui" },
        { question: "En quelle année a été crée EPSI?", reponse: "L’EPSI a été créée en 1961 par des professionnels du secteur informatique" },
        { question: "Oui ou non est-il possible de candidater à l'école EPSI en ligne ?", reponse: "Oui" },
        { question: " Quelle école est associée à l'Epsi ?", reponse: "Wis" },
        { question: "Que signifie Epsi ?", reponse: "École privée des science informatique" },
        { question: "Combien y a il de campus Epsi en tout ?", reponse: "Il y en a 14" },
        { question: "Oui ou non Epsi fait elle de l'ia ?", reponse: "Oui" },
        { question: "Oui ou non Epsi fait elle de la robotique ?", reponse: "Non mais le My dil en possède" },
        { question: "Quel est la première classe à Epsi ?", reponse: "Classe SN1" },
        { question: "Cite 3 campus Epsi", reponse: "Réponse possible : campus de Lyon, Paris, Toulouse" },
        { question: "Quel est le nom du laboratoire d’innovation digitale à la disposition des étudiant d'Epsi ?", reponse: "Le My Dil" }


    ],
    EVENT: [
        { question: "Workshop", reponse: "Pour la prochaine question, tt le monde peut répondre, si qqun a une bonne réponse tt le monde recoit les pts" },
        { question: "Réveil cassé", reponse: "Allez a la case retard et passez votre prochain tour" },
        { question: "Pause repas", reponse: "La prochaine fois que vous gagnez des pts, peu importe la source vous gagnez le double" },
        { question: "Rattrapage", reponse: "Allez a la case évaluation, c est votre chance de gagner beaucoup de points" },
        { question: "Oubli", reponse: "vous avez oublier votre materiel, lancez un dé et reculez du nbr de points afficher pour récupérer votre materiel " },
        { question: "Bonne note", reponse: "Vous êtes en feu ! relancez le dé" },
        { question: "Question libre", reponse: "Choisissez un des deux sujet et répondez à la question" },
        { question: "Emploi du temps", reponse: "Vous savez ou vous allez, relancez le dé" }

    ],
    Question_Difficile: [
        { question: "Quelle est la différence entre une balise <div> et une balise <span> en HTML ?", reponse: "La balise <div> est un conteneur en bloc , généralement utilisé pour regrouper des sections de contenu et organiser la mise en page. La balise <span> est un conteneur en ligne, utilisé pour appliquer du style à une partie spécifique du texte ou du contenu à l'intérieur d'autres éléments. On utilise <div> pour structurer des éléments en blocs distincts, et <span> pour des ajustements plus fins dans des éléments en ligne." },
        { question: "Quelle est la différence entre une clé primaire et une clé étrangère dans une base de données", reponse: "La clé primaire est un identifiant unique pour chaque enregistrement dans une table, garantissant que chaque ligne est distincte. La clé étrangère est un champ dans une table qui fait référence à la clé primaire d'une autre table, créant ainsi une relation entre les deux tables. " },
        { question: "Quel est le nom du programme de stage international proposé par EPSI ?", reponse: "EPSI GLOBAL" },
        { question: "Quelle est la devise des écoles EPSI ?", reponse: "“Learn, code, Lead”" }

    ]
};

function afficherQuestionAleatoire(sujet) {
    const sujetQuestions = questions[sujet];
    const randomIndex = Math.floor(Math.random() * sujetQuestions.length);
    const currentQuestion = sujetQuestions[randomIndex];
    
    const questionElement = document.getElementById(`${sujet}-question`);
    questionElement.textContent = currentQuestion.question;
    questionElement.dataset.reponse = currentQuestion.reponse;
    questionElement.classList.remove("hidden");
}

function afficherReponse(event) {
    const questionElement = event.target;
    questionElement.textContent = questionElement.dataset.reponse;
}

document.querySelectorAll(".load-question").forEach(button => {
    button.addEventListener("click", (event) => {
        const sujet = event.target.dataset.sujet;
        afficherQuestionAleatoire(sujet);
    });
});

document.querySelectorAll(".question").forEach(question => {
    question.addEventListener("click", afficherReponse);
});
