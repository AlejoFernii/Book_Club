-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema book_club
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `book_club` ;

-- -----------------------------------------------------
-- Schema book_club
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `book_club` DEFAULT CHARACTER SET utf8 ;
USE `book_club` ;

-- -----------------------------------------------------
-- Table `book_club`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_club`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `password` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `book_club`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_club`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `title` VARCHAR(100) NULL,
  `description` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_books_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `book_club`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `book_club`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_club`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `book_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_books_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_books_has_users_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_has_users_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `book_club`.`books` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_books_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `book_club`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
