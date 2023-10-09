-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 30, 2023 at 11:11 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `breakdown`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `lid` int(11) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `lcity` varchar(100) NOT NULL,
  `Landmark` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`lid`, `lname`, `lcity`, `Landmark`) VALUES
(66, 'Imamkhan Street', 'Pollachi', 'Amman Mobiles'),
(67, 'Mahalingapuram`', 'Pollachi', 'Near Arathana Hospital'),
(68, 'Ansari Street', 'Pollachi', 'Near Ashok Hotel'),
(69, 'SS Kovil Street', 'Pollachi', 'Near Gandhi Mandapam'),
(70, 'Marapet', 'Pollachi', 'Near Reliance Petrol Bunk'),
(73, 'Zamin Muthur', 'Pollachi', 'Palakkad Road'),
(75, 'Kovil Palayam Bus Stop', 'Pollachi', 'Kovai Main Road');

-- --------------------------------------------------------

--
-- Table structure for table `mechanic`
--

CREATE TABLE `mechanic` (
  `mechid` int(11) NOT NULL,
  `mname` varchar(100) NOT NULL,
  `maddr` varchar(200) NOT NULL,
  `mcont` varchar(25) NOT NULL,
  `wname` varchar(100) NOT NULL,
  `wloc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mechanic`
--

INSERT INTO `mechanic` (`mechid`, `mname`, `maddr`, `mcont`, `wname`, `wloc`) VALUES
(3, 'Ravi', 'Pollachi', '9864751230', 'Ravi Puncher', '70'),
(5, 'Rajesh', '23, Kovilpalayam\r\nkovai Main road\r\nPollachi', '9564781230', 'Highway Helpers', '75');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `uid` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(100) NOT NULL DEFAULT 'User'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`uid`, `username`, `password`, `usertype`) VALUES
(1, 'bhuvanamohan11@gmail.com', '123', ''),
(2, '9750482299', '1234', 'User'),
(3, '9874561230', '1111', 'User'),
(4, 'bhuvanamohan11@gmail.com', '12345', 'User');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`lid`);

--
-- Indexes for table `mechanic`
--
ALTER TABLE `mechanic`
  ADD PRIMARY KEY (`mechid`);

--
-- Indexes for table `signup`
--
ALTER TABLE `signup`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `lid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `mechanic`
--
ALTER TABLE `mechanic`
  MODIFY `mechid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `signup`
--
ALTER TABLE `signup`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
