# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# OlaudahEquiano [Person]
* name: Olaudah Equiano
* description: The author of the narrative, a slave who was sold to Mr. King and later became a merchant.

# MrMondle [Person]
* name: Mr. Mondle
* description: An officer who believed the author was on the ship when he was actually in a boat.

# Lieutenant [Person]
* name: Lieutenant
* description: An officer who was in a boat with the author when Mr. Mondle searched the ship.

# CaptainDoran [Person]
* name: Captain Doran
* description: The captain of the ship who sent the author to be sold in Montserrat.
* worksFor: MrKing

# MrRobertKing [Person]
* name: Mr. Robert King
* description: A Quaker and the first merchant in Montserrat, who bought the author.
* owns: OlaudahEquiano
* worksFor: OlaudahEquiano

# FormerMaster [Person]
* name: Former Master
* description: The author's previous master who sent him to be sold in Montserrat.
* owns: OlaudahEquiano

# Sailor [Person]
* name: Sailor
* description: A sailor on board who took a guinea from the author promising to get him a boat.

# OldShipmates [Person]
* name: Old Shipmates
* description: The author's former shipmates who sent him oranges and tokens of regard.
* knows: OlaudahEquiano

# LadyInGosport [Person]
* name: Lady in Gosport
* description: A lady who lived in Gosport and was once intimate with the author's former master.
* knows: OlaudahEquiano
* knows: FormerMaster

# AnotherLady [Person]
* name: Another Lady
* description: A lady who succeeded the Lady in Gosport in the former master's good graces and instigated the master to treat the author cruelly.
* knows: OlaudahEquiano
* knows: FormerMaster

# CaptainThomasFarmer [Person]
* name: Captain Thomas Farmer
* description: An English captain who commanded a Bermudas sloop and employed the author as a sailor.
* worksFor: MrKing
* worksFor: OlaudahEquiano

# EmanuelSankey [Person]
* name: Emanuel Sankey
* description: A negro man who tried to escape from bondage by hiding on a London ship.

# MrJamesTobin [Person]
* name: Mr. James Tobin
* description: A zealous labourer in the vineyard of slavery who gave an account of a French planter.

# FrenchPlanter [Person]
* name: French Planter
* description: A planter in Martinico who had mulattoes working in the fields, who were his own children.

# MrDubury [Person]
* name: Mr. Dubury
* description: A gentleman in Montserrat known for humane treatment of slaves.

# SirPhilipGibbes [Person]
* name: Sir Philip Gibbes
* description: A native of Barbadoes with estates there, who wrote a treatise on the usage of his slaves.

# DoctorPerkins [Person]
* name: Doctor Perkins
* description: A doctor who nearly murdered the author in Savannah.

# Governor [Person]
* name: Governor
* description: The governor who seized a boat from a negro-man and later died in poverty.

# WhiteMan [Person]
* name: White Man
* description: A white man who bought a boat for a negro-man.

# Gentleman [Person]
* name: Gentleman
* description: A gentleman who begged off a negro-man from receiving a hundred lashes.

# Overseeer [Person]
* name: Overseer
* description: A cruel overseer whom a negro man attempted to poison.

# BritishSeaman [Person]
* name: British Seaman
* description: A seaman on board who prevented a depredator from striking the author.

# Depredator [Person]
* name: Depredator
* description: A man in St. Eustatia who bought fowls and pigs from the author and tried to take his money back.

# MrKing [Organization]
* name: Mr. King
* description: The mercantile house in Philadelphia with which Mr. Robert King was connected.
* memberOf: MrKing

# Montserrat [Place]
* name: Montserrat
* description: An island in the West Indies where the author was sold to Mr. King.

# Philadelphia [Place]
* name: Philadelphia
* description: A city in America where Mr. Robert King lived and was going soon.

# Portsmouth [Place]
* name: Portsmouth
* description: A location where the ship waited for the West India convoy.

# Gosport [Place]
* name: Gosport
* description: A location where a lady lived who wanted to take the author out of the ship.

# London [Place]
* name: London
* description: A city in England where the author was taken and where he later saw Emanuel Sankey.

# Barbadoes [Place]
* name: Barbadoes
* description: An island in the West Indies.

# StEustatia [Place]
* name: St. Eustatia
* description: An island where a depredator bought goods from the author.

# StKitts [Place]
* name: St. Kitt's
* description: An island where slaves were commonly branded.

# Martinico [Place]
* name: Martinico
* description: An island where a French planter had mulattoes working.

# Savannah [Place]
* name: Savannah
* description: A location where the author was nearly murdered by Doctor Perkins.

# Guadaloupe [Place]
* name: Guadaloupe
* description: A French island where the author traded.

# Grenada [Place]
* name: Grenada
* description: An island where the author traded.

# SantaCruz [Place]
* name: Santa Cruz
* description: An island where the author and Emanuel Sankey went to sell fruits.