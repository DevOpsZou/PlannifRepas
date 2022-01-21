-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema projet
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projet
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projet` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `projet` ;

-- -----------------------------------------------------
-- Table `projet`.`utilisateur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projet`.`utilisateur` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(25) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci' NOT NULL,
  `prenom` VARCHAR(25) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci' NOT NULL,
  `civilite` VARCHAR(5) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci' NOT NULL COMMENT 'M.\\nMme\\nMlle\\nAutre',
  `naissance` DATETIME NOT NULL,
  `mail` VARCHAR(150) NOT NULL,
  `numero` INT NOT NULL,
  `cplmt_numero` VARCHAR(10) NULL DEFAULT NULL,
  `voie` VARCHAR(150) NOT NULL,
  `cplmt_adresse` VARCHAR(100) NULL DEFAULT NULL,
  `cp` INT NOT NULL,
  `ville` VARCHAR(45) NOT NULL,
  `pays` VARCHAR(45) NOT NULL,
  `password` CHAR(100) NOT NULL COMMENT 'INSERT INTO utilisateur VALUES md5(\'mdp\')\\nselect * from utilisateur where password = md5(\'blabla\')\\n',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `mail_UNIQUE` (`mail` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;