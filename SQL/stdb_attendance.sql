-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: stdb
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `student_id` int NOT NULL,
  `section_id` int NOT NULL,
  `attendance_time` time NOT NULL,
  `status_s` varchar(45) DEFAULT 'Absent',
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `class_name` varchar(10) DEFAULT NULL,
  `day` varchar(25) DEFAULT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`student_id`,`date`,`section_id`),
  KEY `day_idx` (`day`),
  KEY `daa_idx` (`day`),
  KEY `class_idx` (`class_name`),
  KEY `start_idx` (`start_time`),
  KEY `endd_idx` (`end_time`),
  KEY `student__idx` (`student_id`),
  KEY `section_i_idx` (`section_id`),
  CONSTRAINT `class_` FOREIGN KEY (`class_name`) REFERENCES `section_registration` (`class_name`),
  CONSTRAINT `daa` FOREIGN KEY (`day`) REFERENCES `section_registration` (`day`),
  CONSTRAINT `endd` FOREIGN KEY (`end_time`) REFERENCES `section_registration` (`End_time`),
  CONSTRAINT `section_i` FOREIGN KEY (`section_id`) REFERENCES `section_registration` (`section_id`),
  CONSTRAINT `start` FOREIGN KEY (`start_time`) REFERENCES `section_registration` (`Start_time`),
  CONSTRAINT `student_i` FOREIGN KEY (`student_id`) REFERENCES `section_registration` (`student_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-09 18:08:13
