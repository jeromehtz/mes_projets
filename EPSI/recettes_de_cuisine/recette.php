<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel = "stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="css/style.css">
        <title>Recettes</title>
    </head>
    <body>
        <header>
            <h1>Mon Blog de Recettes</h1>
            <h5>Bienvenue sur mon blog de recettes</h5>
        </header>
        <main>
            <div class = "entete">
            <span><a href="recette.php?categorie_id=2">Entrées</a></span>
            <span><a href="recette.php?categorie_id=1">Plats</a></span>
            </div>
            <?php //affichage des recettes
                $nom = "";
                $commentaire = "";
                $note = 0;

                $serveur = "localhost";
                $utilisateur = "root";
                $mot_de_passe = "N22YK936Zi7w9B7K";
                $base_de_donnees = "blog_recette";

                try {
                    $connexion = new PDO('mysql:host=localhost;dbname=blog_recette;charset=utf8', 'root', 'N22YK936Zi7w9B7K');
                }
                catch (Exception $e)
                {
                    die("Erreur lors de la connexion à la base de données.");
                }
                $cat_id = $_GET['categorie_id'];
                $sql = "SELECT idCategorie, titre, description, photo, dateCreation FROM recette
                INNER JOIN categorie on recette.idCategorie=categorie.id WHERE idCategorie=$cat_id";

                $sql_moyenne_notes = "SELECT AVG(note) as noteM FROM commentaire ORDER BY id DESC";


                $reponse = $connexion->query($sql);
                $reponse1 = $connexion->query($sql_moyenne_notes);
                
                while ($data = $reponse->fetch()) {
                    $image = "img/".$data['photo'];
                    echo "<img src='$image' />"."</br>";
                    echo "<h2>". $data['titre'] ."</h2>";

                    while ($data1 = $reponse1->fetch())
                    {
                        $note = $data1['noteM'];
                        $note1 = 5-$note;
                        while ($note>0)
                        {
                            $note -= 1;
                            ?>
                            <i class='fa fa-star' style='color: #f3da35'></i>
                            <?php
                        }
                    
                        if ($note1>1)
                        {
                            while ($note1 > 1)
                            {
                                $note1 -= 1;
                                ?>
                                <i class='fa fa-star' style='color: #ffffff'></i>
                                <?php
                            }
                        }
                    }
                    echo "</br></br>";
                    echo $data['dateCreation']."</br>";
                    echo $data['description'] ."</br>";
                    
                    $sql2 = "SELECT recette.id, ingredient.nom, ingredient.quantite, ingredient.unit FROM recette
                    INNER JOIN ingredient
                    on recette.id = ingredient.idRecette WHERE recette.id = $cat_id";
                    $reponse2 = $connexion->query($sql2);
                    echo "<hr>";
                    echo "<h2> Ingredients </h2>";
                    while ($data2 = $reponse2->fetch())
                    {
                        ?> <li> <?php echo $data2['quantite'].$data2['unit']. " ";
                        echo $data2['nom']."</br>"; ?> </li>
                        <?php
                    }
                    echo "</br>";
                }
            ?>

            <?php
                $nom = "";
                $commentaire = "";
                $note = 0;

                $serveur = "localhost";
                $utilisateur = "root";
                $mot_de_passe = "N22YK936Zi7w9B7K";
                $base_de_donnees = "blog_recette";

                try {
                    $connexion = new PDO('mysql:host=localhost;dbname=blog_recette;charset=utf8', 'root', 'N22YK936Zi7w9B7K');
                }
                catch (Exception $e)
                {
                    die("Erreur à la connexion lors de la base de données.");
                }
                $sql = "SELECT auteur, contenu, note FROM commentaire ORDER BY id DESC";

                $reponse = $connexion->query($sql);

                echo "<h1> Commentaires </h1>";

                while ($data = $reponse->fetch()) {
                    //echo $data['id'], "<br/>". "Auteur : ".$data['auteur'], "<br/>". $data['titre'], "<br/>". $data['contenu'] . "<br/>". $data['date_news']. "<hr/>";
                    echo "</br>" . $data['auteur']." : ";
                    echo $data['contenu']."</br>";
                    $note = $data['note'];
                    echo $note."/5"."</br></br>";
                }
                    
                if (isset($_POST["valider"]))
                {
                    $l_nom = $_POST["nom"];
                    $l_commentaire = $_POST["commentaire"];
                    $l_note = (int) $_POST["note"];

                    /* c'est là qu'on va poster dans la table commentaire et tout
                    */
                    $l_idrecette = 1;
                    $sql = "INSERT INTO commentaire(idRecette, auteur, contenu, note, dateCreation) VALUES (?, ?,?,?,NOW())";
                    $requete = $connexion->prepare($sql);
                    $requete->execute(array($l_idrecette, $l_nom, $l_commentaire, $l_note));
                }
            ?>
            <form method="post" action="index.php">
                <p>Votre nom :</p>
                <textarea type = "text" name = "nom"  rows = "1" cols="8" required></textarea>
                <p> Votre commentaire :</p>
                <textarea type = "text" name = "commentaire" required></textarea>
                
                <!-- rows="10" cols="50" -->
                
                <p>
                    Note :
                    <select name="note">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </p>
            </form>
            <button type="submit" class="sub">Commenter</button>
            <?php
                if (isset($_POST["nom"])) {
                    $nom = $_POST["nom"];
                } if (isset($_POST["msg"])) {
                    $message = $_POST["msg"];
                    }    if (isset($_POST["note"])){
                        $note = $_POST["note"];
                    }
                        if (empty($nom) || empty($message) || empty($note)) {
                        echo "Veuillez remplir tous les champs !";
                    }
            ?>
        </main>
    </body>

    <footer>

    </footer>

</html>