-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 10, 2024 at 05:19 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pefa_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `aboutchurch`
--

CREATE TABLE `aboutchurch` (
  `about_id` int(11) NOT NULL,
  `church_name` text NOT NULL,
  `postal` varchar(50) NOT NULL,
  `paybill` int(11) NOT NULL,
  `account_no` text NOT NULL,
  `theme` text NOT NULL,
  `vision` text NOT NULL,
  `mission` text NOT NULL,
  `ministry_message` text NOT NULL,
  `core_message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `aboutchurch`
--

INSERT INTO `aboutchurch` (`about_id`, `church_name`, `postal`, `paybill`, `account_no`, `theme`, `vision`, `mission`, `ministry_message`, `core_message`) VALUES
(1, 'PEFA KAYOLE B', 'P.O.Box 5790-00200 Nairobi.', 4068291, '(Tithe/ Offering)', 'DOMINION.(Genesis 1:26-28)', 'Making Disciples of all nations (Matthew 28:19)', 'To effectively and rightly declare the message of the scripture that is socially and spiritually relevant, equipping saints to do the work of the ministry.', 'To bring people to Christ and to the membership of His family, disciple and equip the for(Ephesians 4:12)\r\n\r\nTo add value in people lives, through teaching and biblical principles and being a role model,\r\n\r\nTo develop a Kingdom community that impacts other communities.\r\nExample Academic Community\r\n and Business Community', '.We are a family.\r\n.Excellence in Service\r\n.Sound Biblical Teachings.\r\n.Learning.\r\n.God Centered worship.\r\n.Children Ministry.\r\n'),
(1, 'PEFA KAYOLE B', 'P.O.Box 5790-00200 Nairobi.', 4068291, '(Tithe/ Offering)', 'DOMINION.(Genesis 1:26-28)', 'Making Disciples of all nations (Matthew 28:19)', 'To effectively and rightly declare the message of the scripture that is socially and spiritually relevant, equipping saints to do the work of the ministry.', 'To bring people to Christ and to the membership of His family, disciple and equip the for(Ephesians 4:12)\r\n\r\nTo add value in people lives, through teaching and biblical principles and being a role model,\r\n\r\nTo develop a Kingdom community that impacts other communities.\r\nExample Academic Community\r\n and Business Community', '.We are a family.\r\n.Excellence in Service\r\n.Sound Biblical Teachings.\r\n.Learning.\r\n.God Centered worship.\r\n.Children Ministry.\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `email` varchar(250) NOT NULL,
  `username` text NOT NULL,
  `status` tinyint(1) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `desk_post`
--

CREATE TABLE `desk_post` (
  `desk_id` int(11) NOT NULL,
  `desk_title` text NOT NULL,
  `message` varchar(2000) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `desk_post`
--

INSERT INTO `desk_post` (`desk_id`, `desk_title`, `message`, `reg_date`) VALUES
(1, ' The birth of church and its challenges', 'The chuurch age started on the day of pentacost whe n God the  Holy Spirit came upon individual believers. Beforee the day of pentaacost, the belivers were individul Christians.After day of pentacost, they became the church. The Holy Spirit united them to be one.(Act 1:1-5)  We are living inthe dispensation ofgrace and Holy Spirit.(See John 16:7-15)', '2024-08-08 10:06:53'),
(2, ' The birth of church and its challenges', 'The chuurch age started on the day of pentacost whe n God the  Holy Spirit came upon individual believers. Beforee the day of pentaacost, the belivers were individul Christians.After day of pentacost, they became the church. The Holy Spirit united them to be one.(Act 1:1-5)  We are living inthe dispensation ofgrace and Holy Spirit.(See John 16:7-15)', '2024-08-10 14:05:20'),
(3, ' The birth of church and its challenges', 'The chuurch age started on the day of pentacost whe n God the  Holy Spirit came upon individual believers. Beforee the day of pentaacost, the belivers were individul Christians.After day of pentacost, they became the church. The Holy Spirit united them to be one.(Act 1:1-5)  We are living inthe dispensation ofgrace and Holy Spirit.(See John 16:7-15)', '2024-08-10 14:05:25');

-- --------------------------------------------------------

--
-- Table structure for table `elders`
--

CREATE TABLE `elders` (
  `elder_id` int(11) NOT NULL,
  `surname` text NOT NULL,
  `other` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `elders`
--

INSERT INTO `elders` (`elder_id`, `surname`, `other`) VALUES
(1, 'Ken ', 'Owino'),
(2, 'Martin', 'Mbindyo');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `member_id` int(11) NOT NULL,
  `surname` text NOT NULL,
  `other` text NOT NULL,
  `gender` text NOT NULL,
  `dob` date NOT NULL,
  `phone` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `password` varchar(200) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`member_id`, `surname`, `other`, `gender`, `dob`, `phone`, `status`, `password`, `reg_date`) VALUES
(1, 'Sherrif', 'Frank', 'Male', '2005-08-06', 'gAAAAABmr6-Iz0-5RNLTVcpcD7boUEiLLoCx8Kq97CMF5RghPs8aw3fReeMj32F9NrSFQUwMw3YwSKDj2XI5FPsxEAqv9iGA0w==', 0, '$2b$12$EPGlLSoLUuwBbCthklu0duJv1ybG1HqCInwVYQRoOJ.GhcqE1QfWi', '2024-08-04 16:42:48'),
(2, 'Sherrif', 'Frank', 'Male', '2005-08-06', '+254746096499', 0, '$2b$12$UsT/VZZUeySBQsvOvPH/eecQCrHmWPME8YFS7kGJo3kNmqze3nvzu', '2024-08-07 11:02:46'),
(3, 'Sherrif', 'Frank', 'Male', '2005-08-06', 'fgh6096499', 0, '$2b$12$dY4eulRwsK355qL3YhNY3uaFFrnYXJYq2hVnt6s297Uf2amhU3txW', '2024-08-07 11:37:01'),
(4, 'Sherrif', 'Frank', 'Male', '2005-08-06', '+254796096499', 0, '$2b$12$r4/tPONg942hmee8HTCJ7.ndfYFAUTMbD999pzjUgw.Q6IoLceCXi', '2024-08-07 11:39:39');

-- --------------------------------------------------------

--
-- Table structure for table `pastor`
--

CREATE TABLE `pastor` (
  `pastor_id` int(11) NOT NULL,
  `surname` text NOT NULL,
  `other` text NOT NULL,
  `gender` text NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `rank` text NOT NULL,
  `spouse` text NOT NULL,
  `password` varchar(200) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `desk_post`
--
ALTER TABLE `desk_post`
  ADD PRIMARY KEY (`desk_id`);

--
-- Indexes for table `elders`
--
ALTER TABLE `elders`
  ADD PRIMARY KEY (`elder_id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`member_id`);

--
-- Indexes for table `pastor`
--
ALTER TABLE `pastor`
  ADD PRIMARY KEY (`pastor_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `desk_post`
--
ALTER TABLE `desk_post`
  MODIFY `desk_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `elders`
--
ALTER TABLE `elders`
  MODIFY `elder_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `member_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `pastor`
--
ALTER TABLE `pastor`
  MODIFY `pastor_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
