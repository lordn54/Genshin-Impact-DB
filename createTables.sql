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
