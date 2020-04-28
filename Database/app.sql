-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: Attendences
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Students` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `collegeName` varchar(256) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `roll_no` varchar(20) NOT NULL,
  `email` varchar(128) DEFAULT NULL,
  `branch` varchar(20) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `validity` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roll_no` (`roll_no`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1,'international Institute of Information Technology','babita','20161001','babita@research.iiit.ac.in','CSD','8360206891','may 2021'),(2,'international Institute of Information Technology','gita','20161002','gita@research.iiit.ac.in','CSD','8360206888','may 2021'),(3,'international Institute of Information Technology','ram','20161003','ram@research.iiit.ac.in','CSD','8360206998','may 2021'),(4,'international Institute of Information Technology','sheldon','20161004','sheldon@research.iiit.ac.in','CSD','8361106998','may 2021'),(5,'international Institute of Information Technology','Sourav Kumar','20161071','sourav.kumar@research.iiit.ac.in','CSD','8360206898','may 2021'),(6,'international Institute of Information Technology','syam','20161005','syam@research.iiit.ac.in','CSD','8231106998','may 2021'),(19,'international Institute of Information Technology','Sourav Kumar','20161072','sourav.kkumar@research.ilit.ac.in','CSD','8360206898','may 2021'),(23,'international Institute of Information Technology','Prazwal Chabbra','20171189','prazwal.chabbra@research.llit.ac.in','CSD','9888989760','may 2022');
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendence`
--

DROP TABLE IF EXISTS `attendence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attendence` (
  `student_id` varchar(20) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `subject_code` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendence`
--

LOCK TABLES `attendence` WRITE;
/*!40000 ALTER TABLE `attendence` DISABLE KEYS */;
INSERT INTO `attendence` VALUES ('20161001','25_4_2020','101'),('20161001','26_4_2020','101'),('20161001','27_4_2020','101'),('20161002','25_4_2020','101'),('20161002','26_4_2020','101'),('20161003','27_4_2020','101'),('20161004','27_4_2020','101'),('20161004','25_4_2020','101'),('20161005','26_4_2020','101'),('20161001','25_4_2020','102'),('20161001','26_4_2020','102'),('20161001','27_4_2020','102'),('20161003','27_4_2020','102'),('20161003','25_4_2020','102'),('20161004','26_4_2020','102');
/*!40000 ALTER TABLE `attendence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classes` (
  `class_id` varchar(20) DEFAULT NULL,
  `class_name` varchar(255) DEFAULT NULL,
  `student_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES ('101','algorithm','20161001'),('101','algorithm','20161002'),('101','algorithm','20161003'),('101','algorithm','20161004'),('101','algorithm','20161005'),('101','algorithm','20161072'),('102','software','20161001'),('102','software','20161003'),('102','software','20161004'),('102','software','20161072');
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-28 11:01:01
