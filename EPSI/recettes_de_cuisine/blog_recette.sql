CREATE DATABASE  IF NOT EXISTS `blog_recette` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `blog_recette`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: blog_recette
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie`
--

/*!40000 ALTER TABLE `categorie` DISABLE KEYS */;
INSERT INTO `categorie` VALUES (1,'Plat principale'),(2,'Entrée');
/*!40000 ALTER TABLE `categorie` ENABLE KEYS */;

--
-- Table structure for table `commentaire`
--

DROP TABLE IF EXISTS `commentaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commentaire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idRecette` int(11) NOT NULL,
  `auteur` varchar(100) NOT NULL,
  `contenu` varchar(1000) NOT NULL,
  `note` int(11) NOT NULL,
  `dateCreation` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Commentaire_Recette` (`idRecette`),
  CONSTRAINT `FK_Commentaire_Recette` FOREIGN KEY (`idRecette`) REFERENCES `recette` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commentaire`
--

/*!40000 ALTER TABLE `commentaire` DISABLE KEYS */;
/*!40000 ALTER TABLE `commentaire` ENABLE KEYS */;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredient` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idRecette` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `quantite` int(11) NOT NULL,
  `unit` char(2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Commentaire_Recette` (`idRecette`),
  CONSTRAINT `FK_Ingredient_Recette` FOREIGN KEY (`idRecette`) REFERENCES `recette` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (1,1,'Pommes de  terre ',750,'g'),(2,1,'Reblochon',1,'u'),(3,1,'Lardons',200,'g'),(4,1,'Crème fraîche épaisse',3,'cs'),(5,1,'Oignons',2,'u'),(6,1,'Beurre',20,'g'),(7,1,'Sel',1,'cc'),(8,1,'Poivre',1,'p'),(9,2,'Carottes',800,'g'),(10,2,'Oignon',1,'u'),(11,2,'Bouillon de volaille',1,'l'),(12,2,'Cumin',1,'cs'),(13,2,'Crème fraîche épaisse',2,'cs'),(14,2,'Huile d’olive',2,'cs'),(15,2,'Sel',1,'cc'),(16,2,'Poivre',1,'p');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;

--
-- Table structure for table `recette`
--

DROP TABLE IF EXISTS `recette`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recette` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idCategorie` int(11) DEFAULT NULL,
  `titre` varchar(100) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `author` varchar(100) NOT NULL,
  `photo` varchar(250) NOT NULL,
  `dateCreation` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_recette_idCategorie_idx` (`idCategorie`),
  CONSTRAINT `fk_recette_idCategorie` FOREIGN KEY (`idCategorie`) REFERENCES `categorie` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
  ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recette`
--

/*!40000 ALTER TABLE `recette` DISABLE KEYS */;
INSERT INTO `recette` VALUES (1,1,'Tartiflette','La tartiflette savoyarde est un gratin de pommes de terre avec du Reblochon fondu dessus','Nicolas','tartiflette.jpg','2019-01-07 00:00:00'),(2,2,'Velouté de carottes au cumin','Un velouté de carotte au cumin','Nicolas','veloute-de-carotte-au-cumin.jpg','2019-01-08 00:00:00');
/*!40000 ALTER TABLE `recette` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-24  9:52:18
