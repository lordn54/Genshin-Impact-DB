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
	("Shadow of the Warrior", 70);