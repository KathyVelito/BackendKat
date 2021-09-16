CREATE DATABASE EMPRESA;
USE EMPRESA;

CREATE TABLE DEPARTAMENTOS(
    ID INT NOT NULL auto_iNCREment PRIMARY KEY,
    NOMBRE VARCHAR(30)
);

CREATE TABLE PERSONALES(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    IDENTIFICADOR TEXT,
    NOMBRE VARCHAR(40),
    APELLIDO VARCHAR(40),
    DEPARTAMENTO_ID INT,
    SUPERVISOR_ID INT,
    FOREIGN KEY (DEPARTAMENTO_ID) REFERENCES DEPARTAMENTOS(ID),
    FOREIGN KEY (SUPERVISOR_ID) REFERENCES PERSONALES(ID)
);
ALTER TABLE PERSONALES
ADD FOREIGN KEY(SUPERVISOR_ID) REFERENCES PERSONALES(ID);

INSERT INTO DEPARTAMENTOS (NOMBRE) VALUES 
											('INFORMATICA'),
											('PUBLICADAD'),
											('MARKETING'),
											('FINANZAS');

UPDATE DEPARTAMENTOS SET NOMBRE = 'PUBLICIDAD' WHERE NOMBRE = 'PUBLICADAD';

SET SQL_SAFE_UPDATES = 0;
-- 0 == FALSE
-- 1 == TRUE

SELECT * FROM DEPARTAMENTOS;

SELECT * FROM PERSONALES;

USE empresa;