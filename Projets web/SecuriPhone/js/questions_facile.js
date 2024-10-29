const questions = [
    {
      question: "Quelles sont les principales menaces de sécurité auxquelles les appareils mobiles sont confrontés ?",
      options: [
        "Le manque de connexion",
        "Les phishing, malwares et applications malveillantes",
        "Les problèmes de batterie",
        "La casse matérielle"
      ],
      answer: 1
    },
    {
      question: "Comment fonctionne l'authentification à deux facteurs (2FA) ?",
      options: [
        "Elle n'ajoute aucune sécurité supplémentaire",
        "Elle repose sur un mot de passe très fort",
        "Elle utilise deux formes d'identification pour renforcer la sécurité",
        "Elle fonctionne sans connexion internet"
      ],
      answer: 2
    },
    {
      question: "Quelles sont les applications de sécurité mobile efficaces ?",
      options: [
        "Les applications qui codent un mot de passe en dur",
        "Les réseaux sociaux",
        "Les adblockers",
        "Les VPN"
      ],
      answer: 3
    },
    {
      question: "Pourquoi est-il risqué de télécharger des applications à partir de sources non officielles ?",
      options: [
        "Les applications sont plus chères",
        "Elles sont toujours plus lentes",
        "Elles peuvent contenir des logiciels espions",
        "Elles ne sont pas mises à jour"
      ],
      answer: 2
    },
    {
      question: "Comment le chiffrement des données protège-t-il les informations sur un appareil mobile ?",
      options: [
        "En rendant les données visibles par tous",
        "En supprimant toutes les données",
        "En transformant les données en une forme illisible pour les personnes non autorisées",
        "En envoyant les données dans un cloud sécurisé"
      ],
      answer: 2
    },
    {
      question: "Comment un VPN mobile peut-il améliorer la sécurité en ligne ?",
      options: [
        "Il améliore la qualité des vidéos en ligne",
        "Il permet d’accéder aux réseaux Wi-Fi",
        "Il masque l'adresse IP et chiffre la connexion internet",
        "Il empêche le téléphone de se connecter aux réseaux malveillants"
      ],
      answer: 2
    },
    {
      question: "Quels sont les risques de se connecter à des réseaux Wi-Fi publics avec un appareil mobile ?",
      options: [
        "Avoir un signal plus faible",
        "Être exposé aux attaques de piratage",
        "Les applications sont plus chères",
        "Empêcher le téléchargement d'une application"
      ],
      answer: 1
    },
    {
      question: "Qu'est-ce qu'un malware mobile ?",
      options: [
        "Un logiciel qui ajoute son code aux autres applications pour dérégler l'appareil",
        "Un logiciel espion",
        "C'est un logiciel malveillant",
        "Un logiciel qui demande de l'argent en échange de vos données"
      ],
      answer: 2
    },
    {
      question: "Quels signes peuvent indiquer qu’un appareil mobile est compromis par un logiciel malveillant ?",
      options: [
        "Le téléphone est plus rapide mais uniquement sur certains sites",
        "La batterie se décharge rapidement et des publicités apparaissent intempestivement",
        "La connexion internet n'est plus stable",
        "Le téléphone ne s’allume plus"
      ],
      answer: 1
    },
    {
      question: "Comment les utilisateurs peuvent-ils se protéger contre le phishing sur mobile ?",
      options: [
        "En utilisant un VPN",
        "En allant sur un réseau Wi-Fi sécurisé",
        "En utilisant des applications de messagerie sécurisée",
        "Le phishing est un phénomène uniquement sur ordinateur"
      ],
      answer: 2
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
  }
  
  function nextQuestion() {
    checkResult();

    const selectedOption = document.querySelector('input[name="answer"]:checked');
    
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
