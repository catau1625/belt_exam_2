-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_revistas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_revistas` ;

-- -----------------------------------------------------
-- Schema esquema_revistas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_revistas` DEFAULT CHARACTER SET utf8 ;
USE `esquema_revistas` ;

-- -----------------------------------------------------
-- Table `esquema_revistas`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_revistas`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_revistas`.`revistas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_revistas`.`revistas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `descripcion` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_revistas`.`suscripciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_revistas`.`suscripciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `revista_id` INT NOT NULL,
  PRIMARY KEY (`id`, `usuario_id`, `revista_id`),
  INDEX `fk_usuarios_has_revistas_revistas1_idx` (`revista_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_revistas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_revistas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_revistas`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_revistas_revistas1`
    FOREIGN KEY (`revista_id`)
    REFERENCES `esquema_revistas`.`revistas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
