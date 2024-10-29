const questions = [
    {
      question: "Quelle est la méthode la plus courante pour éviter que quelqu'un accède à votre smartphone sans votre permission ?",
      options: [
        "Ne pas installer d'applications",
        "Activer la localisation GPS",
        "Utiliser un code PIN ou une empreinte digitale",
        "Mettre le téléphone en mode avion"
      ],
      answer: 2
    },
    {
      question: "Qu'est-ce que le phishing ?",
      options: [
        "Un type de malware qui crypte vos fichiers pour faire crasher l'appareil",
        "Une attaque qui vise à obtenir des informations personnelles en se faisant passer pour un site ou un service légitime",
        "Un logiciel qui infecte les téléphones portables pour espionner les utilisateurs",
        "Votre poissonnerie locale"
      ],
      answer: 1
    },
    {
      question: "Quel type de connexion est considéré comme le plus risqué pour la sécurité des données mobiles ?",
      options: [
        "Les réseaux Wi-Fi publics",
        "La 4G",
        "Les connexions Bluetooth",
        "Les câbles USB"
      ],
      answer: 0
    },
    {
      question: "Quelle est la meilleure méthode pour sécuriser vos données en cas de vol de votre téléphone ?",
      options: [
        "Désactiver le verrouillage de l'écran",
        "Activer le chiffrement de l'appareil",
        "Désactiver la localisation GPS",
        "Mettre le téléphone en mode avion"
      ],
      answer: 1
    },
    {
      question: "Qu'est-ce qu'un rootkit sur un appareil mobile ?",
      options: [
        "Un virus qui redirige toutes vos connexions internet",
        "Un malware qui permet à un attaquant d'obtenir des privilèges",
        "Un logiciel de gestion de mots de passe",
        "Un malware de gestion des fichiers système"
      ],
      answer: 1
    },
    {
      question: "Comment fonctionne une attaque de type MITM sur un réseau mobile ?",
      options: [
        "L'attaquant intercepte et modifie les communications entre deux parties sans qu'elles ne le sachent",
        "L'attaquant infecte les appareils avec des virus",
        "L'attaquant envoie des emails de phishing",
        "L'attaquant décrypte les données privées sans autorisation"
      ],
      answer: 0
    },
    {
      question: "Qu'est-ce que le chiffrement de bout en bout ?",
      options: [
        "Un processus qui permet à un service de sauvegarder automatiquement les données utilisateur",
        "Un programme de gestion des fichiers sensibles",
        "Un pare-feu mobile qui bloque les connexions non autorisées",
        "Un mécanisme de sécurité qui crypte les messages pour qu'ils ne puissent être lus que par l'expéditeur et le destinataire"
      ],
      answer: 3
    },
    {
      question: "Qu’est-ce qu’une attaque de type smishing ?",
      options: [
        "Une attaque par email visant à voler des informations personnelles",
        "Une forme de phishing via SMS",
        "Une méthode pour bloquer les connexions Bluetooth",
        "Un malware conçu pour crypter les fichiers sur mobile"
      ],
      answer: 1
    },
    {
      question: "Quel est le rôle d’un certificat SSL dans une application mobile ?",
      options: [
        "Gérer les sauvegardes de l'application",
        "Améliorer la rapidité des transactions de l’application",
        "Assurer une connexion sécurisée et chiffrée entre l’application et le serveur",
        "Bloquer les connexions non sécurisées à l’application"
      ],
      answer: 2
    },
    {
      question: "Pourquoi est-il recommandé de désactiver le Bluetooth lorsqu’il n’est pas utilisé ?",
      options: [
        "Cela améliore la réception du signal Wi-Fi",
        "Cela empêche des attaques potentielles",
        "Cela libère plus d’espace de stockage",
        "Cela réduit le niveau de radiation émis par le téléphone"
      ],
      answer: 1
    }
  ];
  
  let currentQuestionIndex = 0;
  let score = 0;
  
  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
  
  function loadQuestion() {
    const questionContainer = document.getElementById("question-container");
    const optionsContainer = document.getElementById("options-container");
  
    questionContainer.innerHTML = "";
    optionsContainer.innerHTML = "";
  
    const question = questions[currentQuestionIndex];
    questionContainer.textContent = `${currentQuestionIndex + 1}. ${question.question}`;
    
    question.options.forEach((option, index) => {
      const label = document.createElement("label");
      const input = document.createElement("input");
      input.type = "radio";
      input.name = "answer";
      input.value = index;
  
      label.appendChild(input);
      label.appendChild(document.createTextNode(option));
      optionsContainer.appendChild(label);
      optionsContainer.appendChild(document.createElement("br"));
    });
    
    
  }

  function checkResult() {
    const reponse = document.getElementById("reponse");
    const selectedOption = document.querySelector('input[name="answer"]:checked');
    if (!selectedOption) {
      alert("Veuillez sélectionner une option!");
      return;
    }
    const answer = parseInt(selectedOption.value);
    reponse.classList.remove("hidden");
    if (answer === questions[currentQuestionIndex].answer) {
      reponse.textContent = `Vous avez trouvé la bonne réponse, continuez comme ça!`;
    }
    else
    {
      reponse.textContent = `La réponse juste était la proposition `+(questions[currentQuestionIndex].answer+1)+`.`;
    }
    // alert(reponse.textContent);
  }
  
  function nextQuestion() {
    checkResult();
    // const reponse = document.getElementById("reponse");

    const selectedOption = document.querySelector('input[name="answer"]:checked');
    // if (!selectedOption) {
    //   alert("Veuillez sélectionner une réponse !");
    //   return;
    // }
    
    const answer = parseInt(selectedOption.value);
    if (answer === questions[currentQuestionIndex].answer) {
      score++;
    }
  
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      loadQuestion(); 
    } else {
      showResults();
    }

    // reponse.classList.add("hidden");
  }

  function RedirectionJavascript(page){
    document.location.href=page;
  }
  
  function showResults() {
    const quizContainer = document.getElementById("quiz-container");
    const resultsContainer = document.getElementById("results");
  
    quizContainer.classList.add("hidden");
    resultsContainer.classList.remove("hidden");
    resultsContainer.textContent = `Vous avez obtenu ${score} sur ${questions.length} bonnes réponses.`;

    const retake = document.getElementById("retake");
    retake.classList.remove("hidden");
    retake.textContent = `Recommencer`;
    
  }
  
  shuffle(questions);
  loadQuestion();
