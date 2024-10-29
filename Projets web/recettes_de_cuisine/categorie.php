<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Categories</title>
</head>

<body>
    <header>
    <h1><a href='index.php'>Mon Blog de Recettes</a></h1>
        <h5>Bienvenue sur mon blog de recettes</h5>
    </header>

    <main>
        <hr>
    <div class = "entete">
        </div>
        <?php
// Se connecter à la base de données
$conn = new PDO('mysql:host=localhost;dbname=blog_recette;charset=utf8', 'root', 'N22YK936Zi7w9B7K');

// Sélectionner les catégories de recettes depuis la base de données
$sql = "SELECT id, nom FROM categorie";
$result = $conn->query($sql);

   while ($data = $result->fetch()) {
        echo "<span><a href='categorie.php?id=" . $data["id"] . "'>" . $data["nom"] . "</a></span>";
   }

// Récupérer l'ID de la catégorie depuis le paramètre GET
if (isset($_GET["id"])) {
    $categorie_id = $_GET["id"];

    // Sélectionner les recettes de la catégorie spécifiée depuis la base de données
    $sql = "SELECT id, titre, photo, description FROM recette WHERE idCategorie = $categorie_id";
    $result = $conn->query($sql);

   
    while($row = $result->fetch()) {
        $pho = "img/".$row["photo"];
        echo "<h3><a href='recette.php?id=".$row["id"]."'>".$row["titre"]."</a></h3>";
        echo "<img src='$pho'>";
        echo "<p class='desc_velou'>" . $row["description"] . "</p>";
        echo "<hr>";
    }
    
} else {
    echo "ID de catégorie non spécifié.";
}
?>

    </main>

    <footer>

    </footer>

</body>
</html>