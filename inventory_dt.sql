-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2018 at 06:20 AM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `billing_dt`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory_dt`
--

CREATE TABLE `inventory_dt` (
  `Serial` int(10) DEFAULT NULL,
  `ProductID` varchar(20) DEFAULT NULL,
  `Product_Name` varchar(40) DEFAULT NULL,
  `Quantity` int(10) DEFAULT NULL,
  `PPU` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `inventory_dt`
--

INSERT INTO `inventory_dt` (`Serial`, `ProductID`, `Product_Name`, `Quantity`, `PPU`) VALUES
(1, '1624ASDF', 'Soundarya Sabun Nirma', 5, 20),
(2, '1724AFGH', 'Parle G', 3, 10);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
