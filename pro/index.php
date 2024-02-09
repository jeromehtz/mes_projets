<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>index</title>
</head>
<body>
    <header>
    <h1><a href='index.php'>Mon Blog de Recettes</a></h1>

                <br>
                <p>Bienvenue sur mon blog de recettes</p>
    </header>
    <main>
        <div class = "entete">
        <span><a href="categorie.php?id=1">Entrées</a></span>
        <span><a href="categorie.php?id=2">Plats</a></span>
        </div>
        <?php

    // Connexion à la base de données
    $bd = new PDO('mysql:host=localhost;dbname=blog_recette;charset=utf8', 'root', 'N22YK936Zi7w9B7K');

    // Vérifier la connexion
    if (!$bd) {
        die("La connexion à la base de données a échoué.");
    }

    // Requête SQL pour récupérer les détails de la recette
    $sqlRecette = "SELECT * FROM recette";
    $respRecette = $bd->query($sqlRecette);
    

    // Afficher les détails de la recette
       
        
        while($rowRecette = $respRecette->fetch()) {
            $titre = $rowRecette['titre'];
            $description = $rowRecette['description'];
            $photo = "img/" . $rowRecette['photo'];
            $id = $rowRecette['id'];
            echo "<h3><a href='recette.php?id=".$id."'>".$titre."</a></h3>";
        echo "<img src='$photo' alt='$titre'> <br>";
        echo "<p class='desc_recette'>$description</p><hr>";
        }
        ?>
        </main>
    </body>

    <footer>

    </footer>

</html>
</html>
