DROP TABLE BVG_COFFEE;

CREATE TABLE BVG_COFFEE (
    CID NUMBER,
    CNAME VARCHAR2(50) NOT NULL,
    CCOLOR VARCHAR2(25),
    CFLAVOR VARCHAR2(25),
    CORIGIN VARCHAR2(25),
    CONSTRAINT BVG_PRIMARY_KEY PRIMARY KEY (CID));

INSERT INTO BVG_COFFEE VALUES (1, 'DALGONA', 'BEIGE', 'CHOCOLATE', 'INDIA');
INSERT INTO BVG_COFFEE VALUES (2, 'MOCHA', 'BROWN', 'OREO', 'ETHIOPIA');
INSERT INTO BVG_COFFEE VALUES (3, 'CAPUCCINO', 'WHITE', 'VANILLA', 'ITALY');
INSERT INTO BVG_COFFEE VALUES (4, 'ESPRESSO', 'DARK BROWN', 'HAZELNUT', 'USA');

COMMIT;