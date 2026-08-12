# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The author and narrator of the narrative, formerly a slave who gained freedom and traveled extensively.
* jobTitle: Steward, Hair-dresser, Sailor

# RobertKing [Person]
* name: Robert King
* description: The author's former master who provided him with a certificate of freedom.
* jobTitle: Master
* owns -> GustavusVassa

# JohnHamer [Person]
* name: Capt. John Hamer
* description: Captain of the ship Andromache who transported the author to London.
* jobTitle: Captain
* memberOf -> Andromache

# Andromache [Place]
* name: Andromache
* description: A ship on which the author traveled to London.
* type: Ship

# Montserrat [Place]
* name: Montserrat
* description: An island the author left to travel to London.

# London [Place]
* name: London
* description: A city in England where the author arrived and lived.

# CherryGardenStairs [Place]
* name: Cherry-Garden stairs
* description: A location in London where the author arrived by ship.

# MissGuerins [Person]
* name: Miss Guerins
* description: Kind ladies and cousins of Capt. Pascal who helped the author in London.
* jobTitle: Ladies
* knows -> GustavusVassa

# MayShillGreenwich [Place]
* name: May's-hill, Greenwich
* description: A location in Greenwich where the Miss Guerins lived.

# CaptPascal [Person]
* name: Capt. Pascal
* description: Cousin of the Miss Guerins and former master of the author.
* jobTitle: Captain
* memberOf -> MissGuerins
* owns -> GustavusVassa

# CaptOHara [Person]
* name: Capt. O'Hara
* description: A gentleman who recommended the author to a hair-dresser.
* jobTitle: Captain
* knows -> GustavusVassa

# CoventryCourtHaymarket [Place]
* name: Coventry-court, Haymarket
* description: A location in London where the author worked as a hair-dresser.

# RevMrGregory [Person]
* name: Rev. Mr. Gregory
* description: A teacher of arithmetic who lived in the same court as the author.
* jobTitle: Reverend, Teacher
* teaches -> GustavusVassa

# DrCharlesIrving [Person]
* name: Dr. Charles Irving
* description: A gentleman celebrated for experiments in making sea water fresh, who employed the author.
* jobTitle: Doctor, Master
* employs -> GustavusVassa

# PallMall [Place]
* name: Pall-mall
* description: A location in London where Dr. Irving lived.

# JohnJolly [Person]
* name: John Jolly
* description: The master of the ship Delawar.
* jobTitle: Master
* owns -> GustavusVassa

# Delawar [Place]
* name: Delawar
* description: A ship that sailed to Italy, Turkey, and other locations.
* type: Ship

# VillaFranca [Place]
* name: Villa Franca
* description: A location visited during the voyage.

# Nice [Place]
* name: Nice
* description: A city visited during the voyage.

# Leghorn [Place]
* name: Leghorn
* description: A city visited during the voyage.

# Smyrna [Place]
* name: Smyrna
* description: An ancient city in Turkey visited by the author.

# Oporto [Place]
* name: Oporto
* description: A city in Portugal visited by the author.

# Portugal [Place]
* name: Portugal
* description: A country visited by the author.

# Genoa [Place]
* name: Genoa
* description: A city in the Mediterranean visited by the author.

# Naples [Place]
* name: Naples
* description: A city in Italy visited by the author.

# MountVesuvius [Place]
* name: mount Vesuvius
* description: A volcano near Naples that erupted during the author's stay.

# StandgateCreek [Place]
* name: Standgate creek
* description: A location in England where the author arrived.

# WmRobertson [Person]
* name: Capt. Wm. Robertson
* description: Captain of the ship Grenada Planter.
* jobTitle: Captain
* memberOf -> GrenadaPlanter

# GrenadaPlanter [Place]
* name: Grenada Planter
* description: A ship that sailed to Madeira, Barbadoes, and the Grenades.
* type: Ship

# Madeira [Place]
* name: Madeira
* description: A location visited by the ship Grenada Planter.

# Barbadoes [Place]
* name: Barbadoes
* description: An island visited by the ship Grenada Planter.

# TheGrenades [Place]
* name: the Grenades
* description: An island visited by the ship Grenada Planter.

# MrMIntosh [Person]
* name: Mr. M'Intosh
* description: A justice of the peace whom the author complained to.
* jobTitle: Justice of the Peace

# DavidWatt [Person]
* name: Captain David Watt
* description: Captain of the ship Jamaica.
* jobTitle: Captain
* memberOf -> Jamaica

# Jamaica [Place]
* name: Jamaica
* description: A large island in the West Indies visited by the author.
* type: Ship

# PortMorant [Place]
* name: Port Morant
* description: A location in Jamaica.

# MrSmith [Person]
* name: Mr. Smith
* description: A gentleman in Port Morant who bought goods from the author.

# Kingston [Place]
* name: Kingston
* description: A city in Jamaica.

# SpringPath [Place]
* name: Spring Path
* description: A place in Kingston where Africans assembled on Sundays.

# JohnConstantinePhipps [Person]
* name: Honourable John Constantine Phipps
* description: Leader of the expedition to the north pole, later Lord Mulgrave.
* jobTitle: Honourable, Lord Mulgrave
* leads -> RaceHorse

# RaceHorse [Place]
* name: Race Horse
* description: His Majesty's sloop of war used in the Arctic expedition.
* type: Ship

# Sheerness [Place]
* name: Sheerness
* description: A location where the expedition ships joined.

# Lutwidge [Person]
* name: Captain Lutwidge
* description: Captain of the sloop Carcass.
* jobTitle: Captain
* memberOf -> Carcass

# Carcass [Place]
* name: Carcass
* description: His Majesty's sloop that joined the Race Horse.
* type: Ship

# Shetland [Place]
* name: Shetland
* description: A location off which the expedition ships were on June 15th.

# Greenland [Place]
* name: Greenland
* description: A location where the expedition made land on June 28th.

# Deptford [Place]
* name: Deptford
* description: A location in London where the expedition arrived.

# JohnHughes [Person]
* name: Captain John Hughes
* description: Commander of the ship Anglicania.
* jobTitle: Captain
* memberOf -> Anglicania

# Anglicania [Place]
* name: Anglicania
* description: A ship bound to Smyrna in Turkey.
* type: Ship

# JohnAnnis [Person]
* name: John Annis
* description: A black man kidnapped from the ship Anglicania.
* jobTitle: Cook
* employedBy -> GustavusVassa

# WilliamKirkpatrick [Person]
* name: Mr. William Kirkpatrick
* description: A gentleman from St. Kitts who kidnapped John Annis.
* jobTitle: Gentleman
* owns -> JohnAnnis

# StKitts [Place]
* name: St. Kitts
* description: An island where John Annis was sent.

# UnionStairs [Place]
* name: Union Stairs
* description: A location where Mr. Kirkpatrick took John Annis from the ship.

# Gravesend [Place]
* name: Gravesend
* description: A location the author went to find the ship that took John Annis.

# GranvilleSharp [Person]
* name: Granville Sharp, Esq.
* description: A philanthropist who assisted the author in trying to free John Annis.
* jobTitle: Philanthropist
* helps -> GustavusVassa

# Linna [Person]
* name: Capt. Linna
* description: Captain of the ship Wester Hall.
* jobTitle: Captain
* memberOf -> WesterHall

# WesterHall [Place]
* name: Wester Hall
* description: A Turkeyman ship the author engaged on.
* type: Ship

# MrCC [Person]
* name: Mr. C----
* description: An old sea-faring man and Christian acquaintance of the author.
* jobTitle: Christian
* knows -> GustavusVassa