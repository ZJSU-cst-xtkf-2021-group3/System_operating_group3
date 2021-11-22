/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : yuegua

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 22/11/2021 20:50:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for activity
-- ----------------------------
DROP TABLE IF EXISTS `activity`;
CREATE TABLE `activity` (
  `AID` int NOT NULL AUTO_INCREMENT,
  `Title` longtext NOT NULL,
  `Introduction` longtext NOT NULL,
  `isEND` tinyint(1) NOT NULL,
  `reward` int NOT NULL,
  PRIMARY KEY (`AID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for activity_contribute
-- ----------------------------
DROP TABLE IF EXISTS `activity_contribute`;
CREATE TABLE `activity_contribute` (
  `A_CID` int NOT NULL AUTO_INCREMENT,
  `AID` int NOT NULL,
  `UID` int NOT NULL,
  `time` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `statement` longtext NOT NULL,
  `star` int NOT NULL,
  `tip_off` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`A_CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for activity_vote
-- ----------------------------
DROP TABLE IF EXISTS `activity_vote`;
CREATE TABLE `activity_vote` (
  `AID` int NOT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `item` varchar(255) NOT NULL,
  `counts` int NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for Comments
-- ----------------------------
DROP TABLE IF EXISTS `Comments`;
CREATE TABLE `Comments` (
  `CID` int NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `TID` int NOT NULL,
  `value` longtext NOT NULL,
  `time` int NOT NULL,
  `star` int NOT NULL,
  `tip_off` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for contributes_Pic
-- ----------------------------
DROP TABLE IF EXISTS `contributes_Pic`;
CREATE TABLE `contributes_Pic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `A_CID` int NOT NULL,
  `img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for Events
-- ----------------------------
DROP TABLE IF EXISTS `Events`;
CREATE TABLE `Events` (
  `EID` int NOT NULL AUTO_INCREMENT,
  `PID` int NOT NULL,
  `UID` int NOT NULL,
  `time` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `statement` longtext NOT NULL,
  `star` int NOT NULL,
  `tip_off` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `isPostByEditor` tinyint(1) NOT NULL,
  `url` varchar(255) NOT NULL,
  `eventTime` datetime(6) NOT NULL,
  PRIMARY KEY (`EID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for index_pic
-- ----------------------------
DROP TABLE IF EXISTS `index_pic`;
CREATE TABLE `index_pic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `PID` int NOT NULL,
  `img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `type` int NOT NULL,
  `value` varchar(255) NOT NULL,
  `postTime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for Revelation
-- ----------------------------
DROP TABLE IF EXISTS `Revelation`;
CREATE TABLE `Revelation` (
  `RID` int NOT NULL AUTO_INCREMENT,
  `PID` int NOT NULL,
  `UID` int NOT NULL,
  `time` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `statement` longtext NOT NULL,
  `star` int NOT NULL,
  `tip_off` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `isPostByEditor` tinyint(1) NOT NULL,
  `text` longtext NOT NULL,
  `eventTime` datetime(6) NOT NULL,
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for Revelation_Pic
-- ----------------------------
DROP TABLE IF EXISTS `Revelation_Pic`;
CREATE TABLE `Revelation_Pic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `EID` int NOT NULL,
  `img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for Topic
-- ----------------------------
DROP TABLE IF EXISTS `Topic`;
CREATE TABLE `Topic` (
  `TID` int NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `category` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `statement` longtext NOT NULL,
  `time` int NOT NULL,
  `star` int NOT NULL,
  `tip_off` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `isPostByEditor` tinyint(1) NOT NULL,
  `lastUpDateTime` int NOT NULL,
  `Fcounts` int NOT NULL,
  `Tag` varchar(255) NOT NULL,
  PRIMARY KEY (`TID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for topic_vote
-- ----------------------------
DROP TABLE IF EXISTS `topic_vote`;
CREATE TABLE `topic_vote` (
  `TID` int NOT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `item` varchar(255) NOT NULL,
  `counts` int NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for User
-- ----------------------------
DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
  `UID` int NOT NULL AUTO_INCREMENT,
  `Uname` varchar(25) NOT NULL,
  `Passwd` varchar(25) NOT NULL,
  `isEDIT` tinyint(1) NOT NULL,
  `header` varchar(100) NOT NULL,
  `AgeRange` int NOT NULL,
  `rank` int NOT NULL,
  `introduction` longtext NOT NULL,
  `wechatID` varchar(30) NOT NULL,
  `EXP` int NOT NULL,
  `Fcounts` int NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for userFollow_topic
-- ----------------------------
DROP TABLE IF EXISTS `userFollow_topic`;
CREATE TABLE `userFollow_topic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `FTID` int NOT NULL,
  `AgeRange` int NOT NULL,
  `lastVisitTime` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for userFollow_user
-- ----------------------------
DROP TABLE IF EXISTS `userFollow_user`;
CREATE TABLE `userFollow_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `FUID` int NOT NULL,
  `FUname` varchar(25) NOT NULL,
  `AgeRange` int NOT NULL,
  `lastVisitTime` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for UserInterests
-- ----------------------------
DROP TABLE IF EXISTS `UserInterests`;
CREATE TABLE `UserInterests` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `field` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for userPrivacy
-- ----------------------------
DROP TABLE IF EXISTS `userPrivacy`;
CREATE TABLE `userPrivacy` (
  `UID` int NOT NULL AUTO_INCREMENT,
  `public` tinyint(1) NOT NULL,
  `public_Ftopic` tinyint(1) NOT NULL,
  `public_Fuser` tinyint(1) NOT NULL,
  `public_comments` tinyint(1) NOT NULL,
  `public_events` tinyint(1) NOT NULL,
  `public_topics` tinyint(1) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
