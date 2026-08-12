# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# RobertKing [Person]
* name: Robert King
* jobTitle: Merchant
* description: A Quaker, the first merchant in Montserrat, and the author's new master. He lived in Philadelphia and was connected with a great mercantile house there.
* owns -> Equiano
* memberOf -> PhiladelphiaMercantileHouse

# CaptainDoran [Person]
* name: Captain Doran
* jobTitle: Captain
* description: The captain of the ship that brought the author to Montserrat. He recommended the author to Mr. King.
* owns -> Equiano
* knows -> RobertKing

# Equiano [Person]
* name: Equiano
* description: The author of the narrative, a slave who was sold to Mr. King in Montserrat.
* ownedBy -> RobertKing
* ownedBy -> CaptainDoran
* employedBy -> RobertKing

# LadyOfGosport [Person]
* name: Lady of Gosport
* description: A lady who lived in Gosport and was once intimate with the author's former master. She intended to take the author away but was unsuccessful.
* knows -> Equiano
* knows -> FormerMaster

# FormerMaster [Person]
* name: Former Master
* description: The author's previous master, who sent him to be sold in Montserrat.
* owns -> Equiano
* knows -> LadyOfGosport

# CaptainThomasFarmer [Person]
* name: Captain Thomas Farmer
* jobTitle: Captain
* description: An Englishman who commanded a Bermudas sloop owned by Mr. King. He gained his master money by carrying passengers.
* employedBy -> RobertKing
* knows -> Equiano

# MrDubury [Person]
* name: Mr. Dubury
* description: A gentleman in Montserrat known for treating his slaves well.
* memberOf -> Montserrat

# SirPhilipGibbes [Person]
* name: Sir Philip Gibbes
* jobTitle: Baronet
* description: A native of Barbadoes with estates there, known for his humane treatment of slaves and for writing a treatise on their usage.
* memberOf -> Barbadoes

# MrJamesTobin [Person]
* name: Mr. James Tobin
* jobTitle: Labourer
* description: A zealous labourer in the vineyard of slavery who gave an account of a French planter.

# FrenchPlanter [Person]
* name: French Planter
* description: A planter in Martinico who had mulattoes working in his fields, who were the produce of his own loins.
* memberOf -> Martinico

# EmanuelSankey [Person]
* name: Emanuel Sankey
* description: A negro man in Montserrat who tried to escape by concealing himself on a London ship but was returned to his master.
* memberOf -> Montserrat

# Governor [Person]
* name: Governor
* description: The governor of the island who seized a boat from a negro-man and later died in poverty in the King's Bench in England.
* memberOf -> Montserrat

# DoctorPerkins [Person]
* name: Doctor Perkins
* description: A doctor who nearly murdered the author in Savannah.

# Montserrat [Place]
* name: Montserrat
* description: An island in the West Indies where the author was sold to Mr. King.

# Philadelphia [Place]
* name: Philadelphia
* description: A city in America where Mr. King lived and was connected with a mercantile house.

# Barbadoes [Place]
* name: Barbadoes
* description: An island in the West Indies known for having slaves meet with the best treatment, though still requiring recruits.

# Martinico [Place]
* name: Martinico
* description: An island in the West Indies.

# StEustatia [Place]
* name: St. Eustatia
* description: A Dutch island in the West Indies.

# StKitts [Place]
* name: St. Kitt's
* description: An island in the West Indies where slaves were commonly branded.

# Plymouth [Place]
* name: Plymouth
* description: A town in Montserrat.

# BrimstoneHill [Place]
* name: Brimstone-Hill
* description: A high and steep mountain in Montserrat known for its brimstone flakes and boiling ponds.

# Bermuda [Place]
* name: Bermuda
* description: A location associated with a sloop commanded by Captain Thomas Farmer.

# SantaCruz [Place]
* name: Santa Cruz
* description: An island in the West Indies.

# Guadaloupe [Place]
* name: Guadaloupe
* description: A French island in the West Indies.

# Grenada [Place]
* name: Grenada
* description: A French island in the West Indies.

# Savannah [Place]
* name: Savannah
* description: A location in America where the author was nearly murdered by Doctor Perkins.

# London [Place]
* name: London
* description: A city in England.

# Portsmouth [Place]
* name: Portsmouth
* description: A location in England where the ship waited for the West India convoy.

# Deptford [Place]
* name: Deptford
* description: A location in England where the author arrived.

# Gosport [Place]
* name: Gosport
* description: A location in England where the lady lived.

# WestIndies [Place]
* name: West Indies
* description: A region in the Caribbean where the author was enslaved.

# England [Place]
* name: England
* description: A country in Europe.

# America [Place]
* name: America
* description: A continent where the author traded.

# PhiladelphiaMercantileHouse [Organization]
* name: Philadelphia Mercantile House
* description: A great mercantile house in Philadelphia with which Mr. King was connected.