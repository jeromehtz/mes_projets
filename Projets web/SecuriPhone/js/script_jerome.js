//<script type="text/javascript">
	// variable globale utilisée pour gérer l'ajout de fichier par type de sous-document
	window.dernierIdFichierPrecontractuel = "";
	window.dernierIdFichierIndex = "";
	window.dernierIdFichierContractuel = "";
	window.dernierIdFichierRecapitulatif = "";

	//variable globale utilisée pour gérer les contrôles de taille de fichier maximum
	window.tailleTotalFichiersPrecontractuel = "";
	window.tailleTotalFichiersIndex = "";
	window.tailleTotalFichiersContractuel = "";
	window.tailleTotalFichiersRecapitulatif = "";

	window.ongletActuel = "formulaire";

	var TypeCredit = "ContratCredit";
	$("#messageBox-msg").empty();
	$("#TypeCredit").change(function () {
		var selectedValue = $(this).val();

		if (selectedValue === "2") {
			TypeCredit = "AvenantCredit";
		}
	});

	//fonction permettant de vérifier que l'extension est bien PDF
	var isPdf = function(name) {

		return name.match(/pdf$/i);
	};

	//fonction permettant de vérifier que l'extension est bien PDF
	var reinitBtnValider = function(monBouton) {
		// on réactive le button et on retire le spinner
		monBouton.prop("disabled", false);
		monBouton.removeClass("disableClick");
		monBouton.html(
				"G&eacute;n&eacute;rer et t&eacute;l&eacutecharger un document POPS");
	};

	//fonction permettant de mettre en majuscule la premiere lettre du champ passé en parametre
	var capitalize = function(s) {
		if (typeof s !== 'string')
			return ''
		return s.charAt(0).toUpperCase() + s.slice(1)
	}

	// fonction permettant d'ajouter un fichier dans la liste des fichiers
	var ajoutFichier = function (nomChamp, dernierId, suffixeVariableDernierId) {
		var container = $('.container' + capitalize(nomChamp));
		var containerChildren = $(container).children();
		var containerChildrenCount = $(containerChildren).length;
		var inputId = 'id' + capitalize(nomChamp) + '-'
				+ containerChildrenCount;
		var nom_champ = nomChamp;
		var test = "test";


		//on vérifie qu'il ne reste pas un champ de type file qui soit encore présent mais non utilisé
		//auquel cas on le réutilise
		if (dernierId != "") {
			$('#' + dernierId).trigger('click');
			return;
		}

		//sinon on crée un nouvel objet de type file
		container
				.append('<input id="' + inputId + '" name="' + nomChamp + '" type="file"/>	'
						+ '<label for="' + inputId + '"></label> <br\>');

		// on insère du nouveau code javascript pour gérer le bouton caché de type input file qu'on vient d'ajouter
		addJSCode('$("#'
				+ inputId
				+ '").change(function(){								'
				+ 'var nomFichier=this.files[0].name;'
				+ '   nomFichier2=nomFichier;'
				+ 'var tailleFichier=(this.files[0].size / 1024).toFixed(0);				'
				+ 'var fichier_ajoute = "Fichier ajouté : "; '
				+ 'var nomchamp = this.name;'

				+ 'if (!(isPdf(nomFichier))) { 											'
				+ '   $("#messageBox-title").html("Fichier incompatible");				'
				+ '   $("#messageBox-msg").html("Le fichier sélectionné n\'est pas un fichier PDF"); '
				+ '   $("#messageBox").modal("show");'
				+ '}'

				+ 'else if($(this).val()!="" && nomFichier.length > 10){'
				+ '   var extension=nomFichier.substring(nomFichier.length-4, nomFichier.length); 				'
				+ '   nomFichier=nomFichier.substring(0, 6)+"__";   '
				+ '   nomFichier=nomFichier+extension;'
				+ '   if (nomchamp === "fichierPrecontractuel") {'
				+ '      var test = $(this).next().html("<span id=\'fichiers\' class = \'btn-fichiers\'>"+fichier_ajoute+" "+nomFichier+ " (" + tailleFichier +  "Ko)</span>"+"<span id=\'popover-fichiers-Precontractuel\' class = \'popover\'>"+nomFichier2+"</span>");'
				+ '   }'
				+ '   else if (nomchamp === "fichierIndex") {'
				+ '      var test = $(this).next().html("<span id=\'fichiers\' class = \'btn-fichiers\'>"+fichier_ajoute+" "+nomFichier+ " (" + tailleFichier +  "Ko)</span>"+"<span id=\'popover-fichiers-Index\' class = \'popover\'>"+nomFichier2+"</span>");'
				+ '   }'
				+ '   else if (nomchamp === "fichierContractuel") {'
				+ '      var test = $(this).next().html("<span id=\'fichiers\' class = \'btn-fichiers\'>"+fichier_ajoute+" "+nomFichier+ " (" + tailleFichier +  "Ko)</span>"+"<span id=\'popover-fichiers-Contractuel\' class = \'popover\'>"+nomFichier2+"</span>");'
				+ '   }'
				+ '   else if (nomchamp === "fichierRecapitulatif") {'
				+ '      var test = $(this).next().html("<span id=\'fichiers\' class = \'btn-fichiers\'>"+fichier_ajoute+" "+nomFichier+ " (" + tailleFichier +  "Ko)</span>"+"<span id=\'popover-fichiers-Recapitulatif\' class = \'popover\'>"+nomFichier2+"</span>");'
				+ '   }'
				+ '} '
				+ 'else if($(this).val()!="") {'
				+ '	  $(this).next().html("<span id=\'fichiers\' class = \'btn-fichiers\'>"+fichier_ajoute+" "+nomFichier+ " (" + tailleFichier +  "Ko)</span>");	'
				+ '   window.dernierIdFichier'
				+     suffixeVariableDernierId
				+ '   ="";				'
				+ '}'
				+ '});																	');
		var click = $('#' + inputId).trigger('click');
		return true;
	};

	var test = function(identifiant) {
		identifiant.show();
	}

	var cliqueBoutonValider = function(monBouton) {
		var up_forms = document.getElementsByName(TypeCredit.charAt(0).toLowerCase() + TypeCredit.slice(1));

		//////////
		// on désactive le button
		monBouton.prop("disabled", true);
		monBouton.addClass("disableClick");

		// et on fait tourner un spinner d'attente
		monBouton
				.html(
						'<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Traitement en cours...');
		//////////

		//on réinitialise les anomalies
		$("#erreurs").empty();
		$("#reussite").empty();
		$("#messageBox-msg").empty();


		var request = new XMLHttpRequest();

		request
				.addEventListener(
						'readystatechange',
						function(e) {
							if (request.readyState == 4) {
								if (request.status == 250) { //retour OK
									$("#erreurs").empty();
									$("#messageBox-msg").empty();
									var ligneMessage = "<table class='reussiteContainer'>";
									let responseHeader = request.getResponseHeader("MsgGenerate");
									if (!!responseHeader) {
										//ligneMessage = ligneMessage + "<tr><td>"+ v.codeRetour + "</td><td>" + v.message+"</td></tr>";
										ligneMessage += "<tr class='tr-reussite'><td>" + responseHeader
												+ "</td><br/></tr>";
									}
									;
									ligneMessage = ligneMessage + "</table>";
									$("#reussite")
											.html(ligneMessage);

									if (request.response.size == 0) {
										$(
												"#erreurs"
												+ TypeCredit)
												.html(
														"Une erreur inattendue est survenue : Fichier vide");
										return;
									}

									var filename = 'documentPops_'
											+ $('#NoProj')[0].value
											+ '.pdf';
									// compatibilité sur IE 11 afin de gérer le download
									if (window.navigator
											&& typeof (window.navigator.msSaveBlob) == 'function') {
										window.navigator.msSaveBlob(
												request.response, filename);
									} else //chrome ou autre navigateur que IE
									{
										_OBJECT_URL = URL
												.createObjectURL(request.response);

										// le lien de download
										var link = document.createElement('a');
										link.href = _OBJECT_URL;
										link.download = filename;

										document.body.appendChild(link);

										//$("#messageBox-title").html("Message RGPD");
										//$("#messageBox-msg").html("Message RGPD");
										//$('#messageBox').modal("show");

										//$('#messageBox').on('hidden.bs.modal', function (e) {
										// faire kkchose
										//})

										link.click();
										document.body.removeChild(link);

										// on révoque l'OBJET après 2 minutes, pour être propre dans la gestion mémoire du navigateur
										// il n'y a aucun moyen de savoir si le download est terminé ou non
										setTimeout(
												function() {
													window.URL
															.revokeObjectURL(_OBJECT_URL);
												}, 120 * 1000);
									}
								}
								// retour KO
								else if (request.status == 450) {
									$("#reussite").empty();
									reponse = JSON.parse(request.response);
									var ligneMessage = "<table class='erreursContainer'>";
									$.each(reponse, function(k, v) {
										//ligneMessage = ligneMessage + "<tr><td>"+ v.codeRetour + "</td><td>" + v.message+"</td></tr>";
										ligneMessage = ligneMessage
												+ "<tr class='tr-erreurs'><td>" + v.message
												+ "</td></tr>";
									});
									ligneMessage = ligneMessage + "</table>";
									$("#erreurs")
											.html(ligneMessage);

								} else if (request.status >= 400) {
									//alert(request.response);
									//$("#messageBox-title").html("Erreur " + request.status);
									//$("#messageBox-msg").html("Une erreur inattendue est survenue : " + request.statusText);
									//$('#messageBox').modal("show");
									$("#erreurs")
											.html(
													"Une erreur inattendue est survenue : "
													+ request.status
													+ " - "
													+ request.statusText);
								}

								//remet le bouton de validation en fonction après une pause de 3 secondes
								setTimeout(function() {
									reinitBtnValider(monBouton);
								}, 3 * 1000);

							} else if (request.readyState == 2) {
								if (request.status >= 200
										&& request.status < 300) {
									request.responseType = "blob";
								} else {
									request.responseType = "text";
								}
							}
						});
		request.addEventListener('progress', function(e) {
			var percent_complete = (e.loaded / e.total) * 100;
			console.log(percent_complete);
		});
		request.open("POST", "GenererDocumentPOPS", true);
		var formData = new FormData(document.getElementById('formulaire'));
		request.send(formData);
	};

	var cliqueBoutonReset = function() {
		$("#erreurs").empty();
		$("#reussite").empty();
		$("#btn-fichiers").empty();
		$("#messageBox-msg").empty();
		var tableauContainer = document.querySelectorAll("[id^='containerFichier']")
		for ( var i=0 ; i < tableauContainer.length ; i++ )
		{
			if (tableauContainer[i].id.indexOf("containerFichier") >= 0)
			{
				if (tableauContainer[i].id.indexOf(TypeCredit) >= 0)
				{
					tableauContainer[i].innerHTML = "";
				}
			}
		}
		document.forms[ongletActuel.charAt(0).toLowerCase() + ongletActuel.slice(1)].reset();
	};

	$(document).ready(
			function() {
				$("#fichiers").show();
				$('#popover-fichiers').show();
				$("#messageBox-msg").hide();
				$("#my-popover").hide();
				$('#popover').click(
						//Numéro de Crédit
						function () {
							var popover = document.getElementById("my-popover");
							document.getElementById("my-popover").showPopover();
							$("#my-popover").show();
						}
				);

				$("#my-popover").click(
						function () {
							$("#my-popover").hide();
						}
				);

				$("#my-popover1").hide();
				$('#popover1').click(
						//Numéro de Crédit
						function () {
							var popover = document.getElementById("my-popover1");
							document.getElementById("my-popover1").showPopover();
							$("#my-popover1").show();
						}
				);

				$("#my-popover1").click(
						function () {
							$("#my-popover1").hide();
						}
				);

				$("#my-popover2").hide();
				$('#popover2').click(
						//Numéro de Crédit
						function () {
							var popover = document.getElementById("my-popover2");
							document.getElementById("my-popover2").showPopover();
							$("#my-popover2").show();
						}
				);

				$("#my-popover2").click(
						function () {
							$("#my-popover2").hide();
						}
				);

				$("#my-popover3").hide();
				$('#popover3').click(
						//Numéro de Crédit
						function () {
							var popover = document.getElementById("my-popover3");
							document.getElementById("my-popover3").showPopover();
							$("#my-popover3").show();
						}
				);

				$("#my-popover3").click(
						function () {
							$("#my-popover3").hide();
						}
				);

				$("#my-popover4").hide();
				$('#popover4').click(
						//Numéro de Crédit
						function () {
							var popover = document.getElementById("my-popover4");
							document.getElementById("my-popover4").showPopover();
							$("#my-popover4").show();
						}
				);

				$("#my-popover4").click(
						function () {
							$("#my-popover4").hide();
						}
				);

				$("#messageBox-msg").click(
						function () {
							$("#messageBox-msg").hide();
						}
				);

				// gere le click sur l'ajout de sous-document Precontractuel

				$('#btnAjouteFichierPrecontractuel').click(
						function() {
							$("#messageBox-msg").show();
							ajoutFichier("fichierPrecontractuel",
									window.dernierIdFichierPrecontractuel,
									'Precontractuel'+TypeCredit);
							$("#messageBox-msg").empty();
							$('#btnAjouteFichierPrecontractuel').hide();
							$('#btnAjouteFichierPrecontractuel').empty();
							setTimeout(function(){$("#popover-fichiers-Precontractuel").hide();}, 5000);
						});

				// gere le click sur l'ajout de sous-document Index
				$('#btnAjouteFichierIndex').click(
						function() {
							$("#messageBox-msg").show();
							ajoutFichier("fichierIndex",
									window.dernierIdFichierIndex,
									'Index'+TypeCredit);
							$("#messageBox-msg").empty();
							$('#btnAjouteFichierIndex').hide();
							$('#btnAjouteFichierIndex').empty();
							setTimeout(function(){$("#popover-fichiers-Index").hide();}, 5000);
						});
				// gere le click sur l'ajout de sous-document Contractuel
				$('#btnAjouteFichierContractuel').click(
						function() {
							$("#messageBox-msg").show();
							ajoutFichier("fichierContractuel",
									window.dernierIdFichierContractuel,
									'Contractuel'+TypeCredit);
							$("#messageBox-msg").empty();
							$('#btnAjouteFichierContractuel').hide();
							$('#btnAjouteFichierContractuel').empty();
							setTimeout(function(){$("#popover-fichiers-Contractuel").hide();}, 5000);
						});

				// gere le click sur l'ajout de sous-document Recapitulatif
				$('#btnAjouteFichierRecapitulatif').click(
						function() {
							$("#messageBox-msg").show();
							ajoutFichier("fichierRecapitulatif",
									window.dernierIdFichierRecapitulatif,
									'Recapitulatif'+TypeCredit);
							$("#messageBox-msg").empty();
							$('#btnAjouteFichierRecapitulatif').hide();
							$('#btnAjouteFichierRecapitulatif').empty();
							setTimeout(function(){$("#popover-fichiers-Recapitulatif").hide();}, 5000);
						});

				var _OBJECT_URL;

				//gere la validation du formulaire POPS
				//c'est là qu'on appelle la servlet d'upload
				//c'est aussi là qu'on gère la restitution des anomalies à l'utilisateur

				$('#btnValiderCredit').on('click', function() {
					cliqueBoutonValider($(this));
				});

				$('#btnResetCredit').click(function()
				{
					cliqueBoutonReset();
				});

				$("#AssuranceADE").show();
				$("#TypeAvenantCredit").hide();

				$("#TypeCredit").change(function () {
					var selectedValue = $(this).val();

					if (selectedValue === "1") {
						$("#AssuranceADE").show();
						$("#TypeAvenantCredit").hide();
					} else if (selectedValue === "2") {
						$("#AssuranceADE").hide();
						$("#TypeAvenantCredit").show();
					}
				});
			});

	//ajoute du code javascript dynamiquement
	function addJSCode(code) {
		var JS = document.createElement('script');
		JS.text = code;
		document.body.appendChild(JS);
	}
//</script>