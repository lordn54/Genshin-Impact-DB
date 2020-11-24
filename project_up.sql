CREATE TABLE Elemental_Interactions(
	element1 ENUM ('Anemo', 'Cryo', 'Hydro', 'Pyro', 'Electro', 'Geo', 'Dendro'),
	element2 ENUM ('Anemo', 'Cryo', 'Hydro', 'Pyro', 'Electro', 'Geo', 'Dendro'),
	name VARCHAR(255)
);

CREATE TABLE Enemies(
	name VARCHAR(255),
	element ENUM ('Anemo', 'Cryo', 'Hydro', 'Pyro', 'Electro', 'Geo', 'Dendro'),
	enemy_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE Elites(
	name VARCHAR(255),
	element ENUM ('Anemo', 'Cryo', 'Hydro', 'Pyro', 'Electro', 'Geo', 'Dendro'),
	xp_gained INT NOT NULL,
	elite_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE Domains(
	name VARCHAR(255),
	element ENUM ('Anemo', 'Cryo', 'Hydro', 'Pyro', 'Electro', 'Geo', 'Dendro'),
	xp_gained INT NOT NULL,
	domain_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE Characters(
	name VARCHAR(255),
	element ENUM ('Anemo', 'Cryo', 'Hydro', 'Pyro', 'Electro', 'Geo', 'Dendro'),
	character_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE Rewards(
	reward_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(255),
	min_level INT NOT NULL
);

CREATE TABLE Enemy_Rewards(
	enemy_id INT NOT NULL,
	reward_id INT NOT NULL,
	FOREIGN KEY (enemy_id)
	REFERENCES Enemies (enemy_id),
	FOREIGN KEY (reward_id)
	REFERENCES Rewards (reward_id)
);

CREATE TABLE Elite_Rewards(
	elite_id INT NOT NULL,
	reward_id INT NOT NULL,
	FOREIGN KEY (elite_id)
	REFERENCES Elites (elite_id),
	FOREIGN KEY (reward_id)
	REFERENCES Rewards (reward_id)
);

CREATE TABLE Domain_Rewards(
	domain_id INT NOT NULL,
	reward_id INT NOT NULL,
	FOREIGN KEY (domain_id)
	REFERENCES Domains (domain_id),
	FOREIGN KEY (reward_id)
	REFERENCES Rewards (reward_id)
);

CREATE TABLE Character_Rewards(
	character_id INT NOT NULL,
	reward_id INT NOT NULL,
	FOREIGN KEY (character_id)
	REFERENCES Characters (character_id),
	FOREIGN KEY (reward_id)
	REFERENCES Rewards (reward_id)
);

INSERT INTO Characters (name, element) VALUES
	("Amber", "Pyro"),
	("Barbara", "Hydro"),
	("Beidou", "Electro"),
	("Bennett", "Pyro"),
	("Chongyun", "Cryo"),
	("Diluc", "Pyro"),
	("Diona", "Cryo"),
	("Fischl", "Electro"),
	("Jean", "Anemo"),
	("Kaeya", "Cryo"),
	("Keqing", "Electro"),
	("Klee", "Pyro"),
	("Lisa", "Electro"),
	("Mona", "Hydro"),
	("Ningguang", "Geo"),
	("Noelle", "Geo"),
	("Qiqi", "Cryo"),
	("Razor", "Electro"),
	("Sucrose", "Anemo"),
	("Tartaglia", "Hydro"),
	("Venti", "Anemo"),
	("Xiangling", "Pyro"),
	("Xingqiu", "Hydro");

INSERT INTO Enemies (name, element) VALUES
	("Anemo Slime", "Anemo"),
	("Hydro Slime", "Hydro"),
	("Cryo Slime", "Cryo"),
	("Geo Slime", "Geo"),
	("Electro Slime", "Electro"),
	("Pyro Slime", "Pyro"),
	("Dendro Slime", "Dendro"),
	("Pyro Whopperflower", "Pyro"),
	("Cryo Whopperflower", "Cryo"),
	("Hilichurl", NULL),
	("Hilichurl Berserker", NULL),
	("Hilichurl Grenadier", NULL),
	("Wooden Shield Hilichurl Guard", "Dendro"),
	("Rock Shield Hilichurl Guard", "Geo"),
	("Hilichurl Shooter", NULL),
	("Samachurl", NULL),
	("Wooden Shield Mitachurl", "Dendro"),
	("Blazing Axe Mitachurl", NULL),
	("Rock Shieldwall Mitachurl", "Geo"),
	("Stonehide Lawachurl", "Geo"),
	("Ruin Guard", NULL),
	("Ruin Hunter", NULL),
	("Pyro Abyss Mage", "Pyro"),
	("Cryo Abyss Mage", "Cryo"),
	("Hydro Abyss Mage", "Hydro"),
	("Treasure Hoarder", NULL),
	("Fatui Pyro Agent", NULL),
	("Anemoboxer Vanguard", "Anemo"),
	("Electro-hammer Vanguard", "Electro"),
	("Geo-chanter Bracer", "Geo"),
	("Pyro-slinger Bracer", "Pyro"),
	("Cryo-gunner Legionnaire", "Cryo"),
	("Hydro-gunner Legionnaire", "Hydro"),
	("Electro Cicin Mage", "Electro"),
	("Geovishap Hatchling", NULL);

INSERT INTO Elites (name, element, xp_gained) VALUES
	("Anemo Hypostasis", "Anemo", 200),
	("Electro Hypostasis", "Electro", 200),
	("Geo Hypostasis", "Geo", 200),
	("Cryo Regisvine", "Cryo", 200),
	("Pyro Regisvine", "Pyro", 200),
	("Oceanid", "Hydro", 200),
	("Stormterror", NULL, 300),
	("Andrius", "Cryo", 300),
	("Tartaglia", "Hydro", 300);

INSERT INTO Domains (name, element, xp_gained) VALUES
	("Hidden Palace of Lianshan Formula", "Electro", 100),
	("Cecilia Garden", "Hydro", 100),
	("Forsaken Rift", "Cryo", 100),
	("Taishan Mansion", "Pyro", 100);

INSERT INTO Elemental_Interactions (element1, element2, name) VALUES
	("Pyro", "Dendro", "Burning"),
	("Hydro", "Pyro", "Vaporize"),
	("Pyro", "Cryo", "Melt"),
	("Cryo", "Electro", "Superconduct"),
	("Cryo", "Hydro", "Frozen"),
	("Electro", "Hydro", "Electro-Chraged"),
	("Pyro", "Electro", "Overload"),
	("Anemo", "Pyro", "Swirl"),
	("Anemo", "Hydro", "Swirl"),
	("Anemo", "Electro", "Swirl"),
	("Anemo", "Cryo", "Swirl");

INSERT INTO Rewards (name, min_level) VALUES
    ("Vayuda Turquoise Sliver", 0),
	("Vayuda Turquoise Fragment", 40),
	("Vayuda Turquoise Chunk", 60),
	("Vayuda Turquoise Gemstone", 75),
	("Shivada Jade Sliver", 0),
	("Shivada Jade Fragment", 40),
	("Shivada Jade Chunk", 60),
	("Shivada Jade Gemstone", 75),
	("Vajrada Amethyst Sliver", 0),
	("Vajrada Amethyst Fragment", 40),
	("Vajrada Amethyst Chunk", 60),
	("Vajrada Amethyst Gemstone", 75),
	("Prithiva Topaz Sliver", 0),
	("Prithiva Topaz Fragment", 40),
	("Prithiva Topaz Chunk", 60),
	("Prithiva Topaz Gemstone", 75),
	("Varunada Lazurite Sliver", 0),
	("Varunada Lazurite Fragment", 40),
	("Varunada Lazurite Chunk", 60),
	("Varunada Lazurite Gemstone", 75),
	("Agnidus Agate Sliver", 0),
	("Agnidus Agate Fragment", 40),
	("Agnidus Agate Chunk", 60),
	("Agnidus Agate Gemstone", 75),
	('Teachings of "Prosperity"', 27),
	('Guide to "Prosperity"', 28),
	('Philosophies of "Prosperity"', 45),
	('Teachings of "Diligence"', 27),
	('Guide to "Diligence"', 28),
	('Philosophies of "Diligence"', 45),
	('Teachings of "Gold"', 27),
	('Guide to "Gold"', 28),
	('Philosophies of "Gold"', 45),
	('Teachings of "Freedom"', 27),
	('Guide to "Freedom"', 28),
	('Philosophies of "Freedom"', 45),
	('Teachings of "Resistance"', 27),
	('Guide to "Resistance"', 28),
	('Philosophies of "Resistance"', 45),
	('Teachings of "Ballad"', 27),
	('Guide to "Ballad"', 28),
	('Philosophies of "Ballad"', 45),
	("Tail of Boreas", 70),
	("Ring of Boreas", 70),
	("Spirit Locket of Boreas", 70),
	("Dvalin's Plume", 70),
	("Dvalin's Claw", 70),
	("Dvalin's Sigh", 70),
	("Tuck of Monoceros Caeli", 70),
	("Shard of a Foul Legacy", 70),
	("Shadow of the Warrior", 70),
	("Tile of Decarabian's Tower", 16),
	("Debris of Decarabian's City", 21),
	("Fragment of Decarabian's Epic", 30),
	("Scattered Piece of Decarabian's Dream", 40),
	("Boreal Wolf's Milk Tooth", 16),
	("Boreal Wolf's Cracked Tooth", 21),
	("Boreal Wolf's Broken Fang", 30),
	("Boreal Wolf's Nostalgia", 40),
	("Fetters of the Dandelion Gladiator", 16),
	("Chains of the Dandelion Gladiator", 21),
	("Shackles of the Dandelion Gladiator", 30),
	("Dream of the Dandelion Gladiator", 40),
	("Luminous Sands from Guyun", 16),
	("Lustrous Stone from Guyun", 21),
	("Relic from Guyun", 30),
	("Divine Body from Guyun", 40),
	("Mist Veiled Lead Elixir", 16),
	("Mist Veiled Mercury Elixir", 21),
	("Mist Veiled Gold Elixir", 30),
	("Mist Veiled Primo Elixir", 40),
	("Grain of Aerosiderite", 16),
	("Piece of Aerosiderite", 21),
	("Bit of Aerosiderite", 30),
	("Chunk of Aerosiderite", 40),
	("Slime Condensate", 0),
	("Slime Secretions", 40),
	("Slime Concentrate", 60),
	("Damaged Mask", 0),
	("Stained Mask", 40),
	("Ominous Mask", 60),
	("Firm Arrowhead", 0),
	("Sharp Arrowhead", 40),
	("Weathered Arrowhead", 60),
	("Divining Scroll", 0),
	("Sealed Scroll", 40),
	("Forbidden Curse Scroll", 60),
	("Heavy Horn", 0),
	("Black Bronze Horn", 40),
	("Black Crystal Horn", 60),
	("Dead Ley Line Branch", 0),
	("Dead Ley Line Leaves", 40),
	("Ley Line Sprout", 60),
	("Chaos Device", 0),
	("Chaos Circuit", 40),
	("Chaos Core", 60),
	("Mist Grass Pollen", 0),
	("Mist Grass", 40),
	("Mist Grass Lamp", 60),
	("Hunter's Sacrificial Knife", 0),
	("Agent's Sacrificial Knife", 40),
	("Inspector's Sacrificial Knife", 60),
	("Recruit's Insignia", 0),
	("Sergeant's Insignia", 40),
	("Lieutenant's Insignia", 60),
	("Treasure Hoarder Insignia", 0),
	("Silver Raven Insignia", 40),
	("Golden Raven Insignia", 60),
	("Fragile Bone Shard", 0),
	("Sturdy Bone Shard", 40),
	("Fossilized Bone Shard", 60),
	("Whopperflower Nectar", 0),
	("Shimmering Nectar", 40),
	("Energy Nectar", 60),
	("Lightning Prism", 0),
	("Hurricane Seed", 0),
	("Hoarfrost Core", 0),
	("Basalt Pillar", 0),
	("Cleansing Heart", 0),
	("Everflame Seed", 0);
	
INSERT INTO Character_Rewards (character_id, reward_id) VALUES
    (1, 21),(1, 22),(1, 23),(1, 24),(1, 34),(1, 35),(1, 36),(1, 48),(1, 82),(1, 83),(1, 84),(1, 120),
	(2, 17),(2, 18),(2, 19),(2, 20),(2, 119),(2, 44),(2, 34),(2, 35),(2, 36),(2, 85),(2, 86),(2, 87),
	(3, 9),(3, 10),(3, 11),(3, 12),(3, 48),(3, 115),(3, 106),(3, 107),(3, 108),(3, 31),(3, 32),(3, 33),
	(4, 21),(4, 22),(4, 23),(4, 24),(4, 120),(4, 37),(4, 38),(4, 39),(4, 46),(4, 106),(4, 107),(4, 108),
	(5, 5),(5, 6),(5, 7),(5, 8),(5, 117),(5, 28),(5, 29),(5, 30),(5, 48),(5, 79),(5, 80),(5, 81),
	(6, 21),(6, 22),(6, 23),(6, 24),(6, 120),(6, 37),(6, 38),(6, 39),(6, 46),(6, 103),(6, 104),(6, 105),
	(7, 5),(7, 6),(7, 7),(7, 8),(7, 117),(7, 34),(7, 35),(7, 36),(7, 50),(7, 82),(7, 83),(7, 84),
	(8, 9),(8, 10),(8, 11),(8, 12),(8, 115),(8, 40),(8, 41),(8, 42),(8, 45),(8, 82),(8, 83),(8, 84),
	(9, 1),(9, 2),(9, 3),(9, 4),(9, 116),(9, 37),(9, 38),(9, 39),(9, 46),(9, 79),(9, 80),(9, 81),
	(10, 5),(10, 6),(10, 7),(10, 8),(10, 117),(10, 40),(10, 41),(10, 42),(10, 45),(10, 106),(10, 107),(10, 108),
	(11, 9),(11, 10),(11, 11),(11, 12),(11, 115),(11, 25),(11, 26),(11, 27),(11, 44),(11, 112),(11, 113),(11, 114),
	(12, 21),(12, 22),(12, 23),(12, 24),(12, 120),(12, 34),(12, 35),(12, 36),(12, 44),(12, 85),(12, 86),(12, 87),
	(13, 9),(13, 10),(13, 11),(13, 12),(13, 115),(13, 40),(13, 41),(13, 42),(13, 47),(13, 76),(13, 77),(13, 78),
	(14, 17),(14, 18),(14, 19),(14, 20),(14, 119),(14, 37),(14, 38),(14, 39),(14, 44),(14, 112),(14, 113),(14, 114),
	(15, 13),(15, 14),(15, 15),(15, 16),(15, 118),(15, 25),(15, 26),(15, 27),(15, 45),(15, 103),(15, 104),(15, 105),
	(16, 13),(16, 14),(16, 15),(16, 16),(16, 118),(16, 37),(16, 38),(16, 39),(16, 47),(16, 79),(16, 80),(16, 81),
	(17, 5),(17, 6),(17, 7),(17, 8),(17, 117),(17, 25),(17, 26),(17, 27),(17, 43),(17, 85),(17, 86),(17, 87),
	(18, 9),(18, 10),(18, 11),(18, 12),(18, 115),(18, 37),(18, 38),(18, 39),(18, 47),(18, 79),(18, 80),(18, 81),
	(19, 1),(19, 2),(19, 3),(19, 4),(19, 116),(19, 34),(19, 35),(19, 36),(19, 45),(19, 112),(19, 113),(19, 114),
	(20, 17),(20, 18),(20, 19),(20, 20),(20, 119),(20, 34),(20, 35),(20, 36),(20, 50),(20, 103),(20, 104),(20, 105),
	(21, 1),(21, 2),(21, 3),(21, 4),(21, 116),(21, 40),(21, 41),(21, 42),(21, 43),(21, 76),(21, 77),(21, 78),
	(22, 21),(22, 22),(22, 23),(22, 24),(22, 120),(22, 28),(22, 29),(22, 30),(22, 47),(22, 76),(22, 77),(22, 78),
	(23, 17),(23, 18),(23, 19),(23, 20),(23, 119),(23, 31),(23, 32),(23, 33),(23, 43),(23, 79),(23, 80),(23, 81);
	
INSERT INTO Enemy_Rewards (enemy_id, reward_id) VALUES
    (1, 76),(1, 77),(1, 78),
	(2, 76),(2, 77),(2, 78),
	(3, 76),(3, 77),(3, 78),
	(4, 76),(4, 77),(4, 78),
	(5, 76),(5, 77),(5, 78),
	(6, 76),(6, 77),(6, 78),
	(7, 76),(7, 77),(7, 78),
	(8, 112),(8, 113),(8, 114),
	(9, 112),(9, 113),(9, 114),
	(10, 79),(10, 80),(10, 81),
	(11, 79),(11, 80),(11, 81),
	(12, 79),(12, 80),(12, 81),
	(13, 79),(13, 80),(13, 81),
	(14, 79),(14, 80),(14, 81),
	(15, 79),(15, 80),(15, 81),(15, 82),(15, 83),(15, 84),
	(16, 79),(16, 80),(16, 81),(16, 85),(16, 86),(16, 87),
	(17, 79),(17, 80),(17, 81),(17, 88),(17, 89),(17, 90),
	(18, 79),(18, 80),(18, 81),(18, 88),(18, 89),(18, 90),
	(19, 79),(19, 80),(19, 81),(19, 88),(19, 89),(19, 90),
	(20, 79),(20, 80),(20, 81),(20, 88),(20, 89),(20, 90),
	(21, 94),(21, 95),(21, 96),
	(22, 94),(22, 95),(22, 96),
	(23, 91),(23, 92),(23, 93),
	(24, 91),(24, 92),(24, 93),
	(25, 91),(25, 92),(25, 93),
	(26, 106),(26, 107),(26, 108),
	(27, 103),(27, 104),(27, 105),(27, 100),(27, 101),(27, 102),
	(28, 103),(28, 104),(28, 105),
	(29, 103),(29, 104),(29, 105),
	(30, 103),(30, 104),(30, 105),
	(31, 103),(31, 104),(31, 105),
	(32, 103),(32, 104),(32, 105),
	(33, 103),(33, 104),(33, 105),
	(34, 103),(34, 104),(34, 105),(34, 97),(34, 98),(34, 99),
	(35, 109),(35, 110),(35, 111);
	
INSERT INTO Elite_Rewards (elite_id, reward_id) VALUES
    (1, 1),(1, 2),(1, 3),(1, 4),(1, 116),
	(2, 9),(2, 10),(2, 11),(2, 12),(2, 115),
	(3, 13),(3, 14),(3, 15),(3, 16),(3, 118),
	(4, 5),(4, 6),(4, 7),(4, 8),(4, 117),
	(5, 21),(5, 22),(5, 23),(5, 24),(5, 120),
	(6, 17),(6, 18),(6, 19),(6, 20),(6, 119),
	(7, 1),(7, 2),(7, 3),(7, 4),(7, 9),(7, 10),(7, 11),(7, 12),(7, 17),(7, 18),(7, 19),(7, 20),(7, 46),(7, 47),(7, 48),
	(8, 5),(8, 6),(8, 7),(8, 8),(8, 13),(8, 14),(8, 15),(8, 16),(8, 21),(8, 22),(8, 23),(8, 24),(8, 43),(8, 44),(8, 45),
	(9, 17),(9, 18),(9, 19),(9, 20),(9, 9),(9, 10),(9, 11),(9, 12),(9, 5),(9, 6),(9, 7),(9, 8),(9, 49),(9, 50),(9, 51);
	
INSERT INTO Domain_Rewards (domain_id, reward_id) VALUES
    (1, 52),(1, 53),(1, 54),(1, 55),(1, 56),(1, 57),(1, 58),(1, 59),(1, 60),(1, 61),(1, 62),(1, 63),
	(2, 64),(2, 65),(2, 66),(2, 67),(2, 68),(2, 69),(2, 70),(2, 71),(2, 72),(2, 73),(2, 74),(2, 75),
	(3, 34),(3, 35),(3, 36),(3, 37),(3, 38),(3, 39),(3, 40),(3, 41),(3, 42),
	(4, 25),(4, 26),(4, 27),(4, 28),(4, 29),(4, 30),(4, 31),(4, 32),(4, 33);

DELIMITER //
CREATE PROCEDURE search_enemy(IN name VARCHAR(255))
BEGIN
    SELECT Rewards.name AS Name, min_level AS Level FROM Enemies
        JOIN Enemy_Rewards USING (enemy_id) 
        JOIN Rewards USING (reward_id)
    WHERE Enemies.name = name;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE search_character(IN name VARCHAR(255))
BEGIN
    SELECT Rewards.name AS Name FROM Characters
        JOIN Character_Rewards USING (character_id) 
        JOIN Rewards USING (reward_id)
    WHERE Characters.name = name;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE search_domain(IN name VARCHAR(255))
BEGIN
    SELECT Rewards.name AS Name, min_level AS Level FROM Domains
        JOIN Domain_Rewards USING (domain_id) 
        JOIN Rewards USING (reward_id)
    WHERE Domains.name = name;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE search_elite(IN name VARCHAR(255))
BEGIN
    SELECT Rewards.name AS Name, min_level AS Level FROM Elites
        JOIN Elite_Rewards USING (elite_id) 
        JOIN Rewards USING (reward_id)
    WHERE Elites.name = name;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE search_item(IN name VARCHAR(255))
BEGIN
    SELECT * FROM 
        (SELECT Enemies.name AS Name, min_level AS Level FROM Rewards 
            JOIN Enemy_Rewards USING (reward_id) 
            JOIN Enemies USING (enemy_id)
        WHERE Rewards.name = name
        UNION
        SELECT Domains.name AS Name, min_level AS Level FROM Rewards 
            JOIN Domain_Rewards USING (reward_id) 
            JOIN Domains USING (domain_id)
        WHERE Rewards.name = name
        UNION
        SELECT Elites.name AS Name, min_level AS Level FROM Rewards 
            JOIN Elite_Rewards USING (reward_id) 
            JOIN Elites USING (elite_id)
        WHERE Rewards.name = name
        UNION
        SELECT Characters.name AS Name, min_level AS Level FROM Rewards 
            JOIN Character_Rewards USING (reward_id) 
            JOIN Characters USING (character_id)
        WHERE Rewards.name = name
        )search;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE characters_by_element(IN enemyName VARCHAR(255))
BEGIN
    SELECT * FROM
	(SELECT Characters.name AS Name, Elemental_Interactions.name AS Interaction FROM Characters
	    JOIN Elemental_Interactions ON Characters.element = element1
		JOIN Enemies ON Enemies.element = element2
    WHERE Enemies.name = enemyName
	UNION
	SELECT Characters.name AS Name, Elemental_Interactions.name AS Interaction FROM Characters
	    JOIN Elemental_Interactions ON Characters.element = element1
		JOIN Elites ON Elites.element = element2
    WHERE Elites.name = enemyName
	UNION
	SELECT Characters.name AS Name, Elemental_Interactions.name AS Interaction FROM Characters
	    JOIN Elemental_Interactions ON Characters.element = element1
		JOIN Domains ON Domains.element = element2
    WHERE Domains.name = enemyName
	)search GROUP BY Name ORDER BY Interaction;
END //
DELIMITER ;