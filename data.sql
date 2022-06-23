-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2022 at 08:54 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data`
--

-- --------------------------------------------------------

--
-- Table structure for table `jops`
--

CREATE TABLE `jops` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `jobcatogory` varchar(50) NOT NULL,
  `discription` varchar(500) NOT NULL,
  `vacancy` int(10) NOT NULL,
  `applyed` int(10) NOT NULL,
  `tname` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jops`
--

INSERT INTO `jops` (`id`, `email`, `jobcatogory`, `discription`, `vacancy`, `applyed`, `tname`) VALUES
(15, 'kd@gmail.com', 'hgfhf', 'sad', 12, 0, 'table1');

-- --------------------------------------------------------

--
-- Table structure for table `jpdetaile`
--

CREATE TABLE `jpdetaile` (
  `Cname` varchar(50) NOT NULL,
  `Cyear` varchar(5) NOT NULL,
  `ceo` varchar(50) NOT NULL,
  `founder` varchar(50) NOT NULL,
  `MobileNo` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `capital` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `profile` varchar(50) NOT NULL,
  `disc` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jpdetaile`
--

INSERT INTO `jpdetaile` (`Cname`, `Cyear`, `ceo`, `founder`, `MobileNo`, `Email`, `capital`, `city`, `profile`, `disc`) VALUES
('Krishnadas P V', '2019', 'asd', 'qweqwe', '8943114039', 'admin@gmail.com', 'asd', 'Valanchery', '../static/profileimage/DSC_9175.jpg', 'asddddddd\r\ndass');

-- --------------------------------------------------------

--
-- Table structure for table `jsdetaile`
--

CREATE TABLE `jsdetaile` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `bio` varchar(2000) NOT NULL,
  `age` int(3) NOT NULL,
  `dob` varchar(12) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `gender` varchar(7) NOT NULL,
  `city` varchar(50) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `photo` varchar(300) NOT NULL,
  `cv` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jsdetaile`
--

INSERT INTO `jsdetaile` (`email`, `name`, `bio`, `age`, `dob`, `qualification`, `gender`, `city`, `phone`, `photo`, `cv`) VALUES
('ad@gmail.com', 'Krishnadas P V', '123dsasdasd', 20, '2022-03-16', '123', 'male', '123', '753215989', '../static/profileimage/2.PNG', '../static/cv/ST MODULE 1.pdf'),
('kd@gamil.com', 'Krishnadas P V', 'asdaSDASDSAFSDFSDAFSDFSADF', 213, '2022-02-09', 'eqwe', 'male', 'asdasd', '12343453', '../static/profileimage/1.PNG', '../static/profileimage/ST_Module_1- Software_Testing.pdf'),
('ls@gmail.com', 'Krishnadas P V', '122222222222222222', 123, '', '123', 'male', 'Valanchery', '8943114039', '../static/profileimage/1.PNG', '../static/profileimage/procedures and macros.pdf'),
('sreejithasreenivas92@gmail.com', 'Krishnadas P V', 'asdddd\r\ndsa\r\ndas\r\ndas\r\ndasdas', 12, '', 'asdsa', 'male', 'asdsad', '8943114039', '../static/profileimage/SIVA.jpg', '../static/cv/The AVR Microcontroller and Embedded System by Muhammad Ali Mazidi ( PDFDrive ) (1)-pages-154-157,162-171.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `logindata`
--

CREATE TABLE `logindata` (
  `fname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phoneno` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL,
  `vmode` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logindata`
--

INSERT INTO `logindata` (`fname`, `email`, `phoneno`, `password`, `vmode`) VALUES
('Krishnadas P V', 'ad@gmail.com', '753215989', '123', 'js'),
('Krishnadas P V', 'admin@gmail.com', '8943114039', '123', 'jp'),
('Krishnadas P V', 'kd@gamil.com', '12343453', '123', 'js');

-- --------------------------------------------------------

--
-- Table structure for table `table13`
--

CREATE TABLE `table13` (
  `id` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `table14`
--

CREATE TABLE `table14` (
  `id` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jops`
--
ALTER TABLE `jops`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jpdetaile`
--
ALTER TABLE `jpdetaile`
  ADD PRIMARY KEY (`Email`);

--
-- Indexes for table `jsdetaile`
--
ALTER TABLE `jsdetaile`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `logindata`
--
ALTER TABLE `logindata`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `table13`
--
ALTER TABLE `table13`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `table14`
--
ALTER TABLE `table14`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jops`
--
ALTER TABLE `jops`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `table13`
--
ALTER TABLE `table13`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `table14`
--
ALTER TABLE `table14`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
