
use attendance;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

create table administrator (
  `admin_id` int(11)  AUTO_INCREMENT PRIMARY KEY,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



create table faculty (
  `teacher_id` int(11)  AUTO_INCREMENT PRIMARY KEY,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO administrator (first_name, last_name, username, password) VALUES ('Tarun','Mukherjee','tmukherjee07','tk56'),('Somraj','Roy','sroy','srk100');

INSERT INTO faculty (first_name, last_name, username, password) VALUES ('Sayan','Dutta','Sdutta','abc123'),('Shyamal','Das','Sdas','abcd'),('Anupam','Roy','Aroy','abd');

create table teacherloggedin (
  `series` int auto_increment primary key,
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

create table classsec (
	`classes` varchar(20) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
Insert into classsec(classes) values
('Class_11A'),
('Class_11B'),
('Class_11C'),
('Class_12A'),
('Class_12B'),
('Class_12C');


create table Class_11A (Roll int not null primary key,
	name varchar(50),
	phone_no varchar(10) unique,
	year int,attendance int) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO  Class_11A VALUES(1,"RIK GUPTA","9823416567",2022,0);
INSERT INTO  Class_11A VALUES(2,"SOUMIK SAHA","7006345135",2022,0);
INSERT INTO  Class_11A VALUES(3,"PRITHA BISWAS","9123074790",2022,0);
INSERT INTO  Class_11A VALUES(4,"KASTURI ROY","8012385778",2022,0);
INSERT INTO  Class_11A VALUES(5,"SOHAIL ALI","9268003573",2022,0);
INSERT INTO  Class_11A VALUES(6,"AHELI SARKAR","7006724687",2022,0);
INSERT INTO  Class_11A VALUES(7,"PRITAM DAS","9903689218",2022,0);
INSERT INTO  Class_11A VALUES(8,"ANIL KUMAR","7054289069",2022,0);
INSERT INTO  Class_11A VALUES(9,"GARGI GANDHI","9826105375",2022,0);
INSERT INTO  Class_11A VALUES(10,"NAKUL BOSE","9521803268",2022,0);

create table Class_11B(Roll int not null primary key,
	name varchar(50),
	phone_no varchar(10) unique,
	year int,attendance int) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO Class_11B VALUES(1,"SAILESH ROY","7194217400",2022,0);
INSERT INTO Class_11B VALUES(2,"BISAKHA DAS","9197678175",2022,0);
INSERT INTO Class_11B VALUES(3,"SRIJEETA GANGULY","7703598588",2022,0);
INSERT INTO Class_11B VALUES(4,"ANIMESH BAGCHI","6266729887",2022,0);
INSERT INTO Class_11B VALUES(5,"ROHIT MALLIK","8572733103",2022,0);
INSERT INTO Class_11B VALUES(6,"ASHA PAL","9818636072",2022,0);
INSERT INTO Class_11B VALUES(7,"KISHORE KAUSHAL","9205464773",2022,0);
INSERT INTO Class_11B VALUES(8,"RUPAM LAHIRI","9457239975",2022,0);
INSERT INTO Class_11B VALUES(9,"SOMRAJ ROY","8130227245",2022,0);
INSERT INTO Class_11B VALUES(10,"AMIT DEY","7987368321",2022,0);

create table Class_11C (Roll int not null primary key,
	name varchar(50),
    phone_no varchar(10) unique,
    year int,
    attendance int)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO Class_11C VALUES(1,"ASHISH YADAV","9899944310",2022,0);
INSERT INTO Class_11C VALUES(2,"KUNAL MISHRA","8046151300",2022,0);
INSERT INTO Class_11C VALUES(3,"RAHUL SARKAR","9305515833",2022,0);
INSERT INTO Class_11C VALUES(4,"AJAY MAJUMDER","7003491682",2022,0);
INSERT INTO Class_11C VALUES(5,"KHUSI THAKUR","9886727417",2022,0);
INSERT INTO Class_11C VALUES(6,"RIYA DAS","9124910021",2022,0);
INSERT INTO Class_11C VALUES(7,"AMER ALI","9381397174",2022,0);
INSERT INTO Class_11C VALUES(8,"OMAR NOOR","6175508902",2022,0);
INSERT INTO Class_11C VALUES(9,"PRAGATI KUMARI","9783450058",2022,0);
INSERT INTO Class_11C VALUES(10,"SOMA HALDER","7012993720",2022,0);

create table CLASS_12A(Roll int not null primary key,
	name varchar(50),
    phone_no varchar(10) unique,
    year int,
    attendance int)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO CLASS_12A VALUES(1,"Varun Nag","8875038104",2022,0);
INSERT INTO CLASS_12A VALUES (2,"Shankar Hazra","9814052680",2022,0);
INSERT INTO CLASS_12A VALUES (3,"Ashish Gautam","8600147997",2022,0);
INSERT INTO CLASS_12A VALUES (4,"Rumeli Mukherjee","7802589637",2022,0);
INSERT INTO CLASS_12A VALUES (5,"Sneha Roy","8803789054",2022,0);
INSERT INTO CLASS_12A VALUES (6,"Rishika Das","7004269069",2022,0);
INSERT INTO CLASS_12A VALUES (7,"Piyush Waddader","9738072689",2022,0);
INSERT INTO CLASS_12A VALUES (8,"Kushali Nath","9817179965",2022,0);
INSERT INTO CLASS_12A VALUES (9,"Debanjan Kumar","7004168042",2022,0);
INSERT INTO CLASS_12A VALUES (10,"Anurag Basu","9225062799",2022,0);

create table CLASS_12B(Roll int not null primary key,
	name varchar(50),
    phone_no varchar(10) unique,
    year int,
    attendance int) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO CLASS_12B VALUES (1,"Rounak Bose","7802578938",2022,0);
INSERT INTO CLASS_12B VALUES (2,"Srijan Guha","8258051689",2022,0);
INSERT INTO CLASS_12B VALUES (3,"Rishi Sinha","8925890426",2022,0);
INSERT INTO CLASS_12B VALUES (4,"Saheli Ghosh","7290526890",2022,0);
INSERT INTO CLASS_12B VALUES (5,"Anrina Majumder","8247900522",2022,0);
INSERT INTO CLASS_12B VALUES (6,"Srijita Ghoshal","7035892790",2022,0);
INSERT INTO CLASS_12B VALUES (7,"Niharika Mahajan","8628074379",2022,0);
INSERT INTO CLASS_12B VALUES (8,"Souvik Das","9939033688",2022,0);
INSERT INTO CLASS_12B VALUES (9,"Dishari Paul","8728005589",2022,0);
INSERT INTO CLASS_12B VALUES (10,"Satyaki Das","7037904268",2022,0);

create table CLASS_12C(Roll int not null primary key,
	name varchar(50),
    phone_no varchar(10) unique,
    year int,
    attendance int) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO CLASS_12C VALUES (1,"Sayan Ghosh","8370053799",2022,0);
INSERT INTO CLASS_12C VALUES (2,"Nayan Dey","9827953898",2022,0);
INSERT INTO CLASS_12C VALUES (3,"Ishita Santra","8690372689",2022,0);
INSERT INTO CLASS_12C VALUES (4,"Ankita Roy","9837269003",2022,0);
INSERT INTO CLASS_12C VALUES (5,"Nairita Karmakar","7002748938",2022,0);
INSERT INTO CLASS_12C VALUES (6,"Kaustav Saha","8837042795",2022,0);
INSERT INTO CLASS_12C VALUES (7,"Nilami Gomes","7003794937",2022,0);
INSERT INTO CLASS_12C VALUES (8,"Aisha Ahmed","9883695892",2022,0);
INSERT INTO CLASS_12C VALUES (9,"Surya Mishra","8379480379",2022,0);
INSERT INTO CLASS_12C VALUES (10,"Priyanka Tripathi","9825905795",2022,0);

create table Attendance_daywise(dates date,
attendance_taken_by varchar(50),
username varchar(50),
class varchar(10),
students_present varchar(500),
absentees_list varchar(500))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

Create table Teacher(Teacher_id varchar(20) primary key,
name varchar(50), 
subject varchar(50),
contact bigint unique not null)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

Insert into Teacher values("EMP001","Sayan Dutta","Physics",9051792463);
Insert into Teacher values("EMP002","Shyamal Das","Maths",8794673695);
Insert into Teacher values("EMP003","Anupam Roy","Chemistry",9368036784);
Insert into Teacher values("EMP004","Mahuya Bakshi","Computer Science",7002579269);
Insert into Teacher values("EMP005","English","Sudeshna Banerjee",9357279955);
Insert into Teacher values("EMP006","Farooq Sheikh","Bengali",8379025895);





/*!40101 SET CHARACTER_SET_CLIENT=@@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@@OLD_COLLATION_CONNECTION */;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;