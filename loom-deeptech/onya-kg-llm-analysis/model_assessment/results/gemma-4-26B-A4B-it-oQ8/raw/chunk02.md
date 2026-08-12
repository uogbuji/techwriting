# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GeneralWolfe [Person]
* name: General Wolfe
* jobTitle: General

# GeorgeBalfour [Person]
* name: Captain George Balfour

# Laforey [Person]
* name: Laforey
* jobTitle: Captain

# MonsConflans [Person]
* name: Mons. Conflans

# MonsLeClue [Person]
* name: Mons. Le Clue

# Boscawen [Person]
* name: Admiral Boscawen

# CharlesHardy [Person]
* name: Sir Charles Hardy

# Durell [Person]
* name: Durell

# JamesDoran [Person]
* name: Captain James Doran

# JohnMondle [Person]
* name: John Mondle
* jobTitle: Gunner

# DanielQueen [Person]
* name: Daniel Queen
* description: A man very well educated who was like a father to the author.

# MissGuerin [Person]
* name: Miss Guerin

# Dick [Person]
* name: Dick

# Author [Person]
* name: The author
* description: A black Christian who was baptized in St. Margaret's church.
* served -> Master
* knows -> Master
* knows -> DanielQueen
* knows -> MissGuerin
* knows -> GeneralWolfe
* knows -> GeorgeBalfour
* knows -> CaptainClark
* knows -> JohnMondle
* knows -> Dick

# Master [Person]
* name: My master
* description: The author's master who eventually sold him into slavery.
* owns -> Author
* sold -> Author
* treats -> Author

# CaptainClark [Person]
* name: Captain Clark

# GeneralCrawford [Person]
* name: General Crawford

# CommodoreKeppel [Person]
* name: Commodore Keppel

# CommodoreStanhope [Person]
* name: Commodore Stanhope

# CommodoreDennis [Person]
* name: Commodore Dennis

# Louisbourgh [Place]
* name: Louisbourgh

# CapeBreton [Place]
* name: Cape Breton

# NovaScotia [Place]
* name: Nova Scotia

# StGeorge [Place]
* name: St. George

# Halifax [Place]
* name: Halifax

# Gibraltar [Place]
* name: Gibraltar

# Barcelona [Place]
* name: Barcelona

# Toulon [Place]
* name: Toulon

# BelleIsle [Place]
* name: Belle-Isle

# London [Place]
* name: London

# Westminster [Place]
* name: Westminster

# Portsmouth [Place]
* name: Portsmouth

# Spithead [Place]
* name: Spithead

# Deptford [Place]
* name: Deptford

# Thames [Place]
* name: Thames

# WestIndies [Place]
* name: West Indies

# Namur [Organization]
* name: Namur

# Aetna [Organization]
* name: Ætna

# CharmingSally [Organization]
* name: Charming Sally

# PrincessAmelia [Organization]
* name: Princess Amelia

# RoyalWilliam [Organization]
* name: Royal William

# Somerset [Organization]
* name: Somerset

# Bienfaisant [Organization]
* name: Bienfaisant

# Ocean [Organization]
* name: Ocean

# LaModeste [Organization]
* name: La Modeste

# LeTemeraire [Organization]
* name: Le Temeraire

# Centaur [Organization]
* name: Centaur

# Redoubtable [Organization]
* name: Redoubtable

# Lynne [Organization]
* name: Lynne

# Jason [Organization]
* name: Jason

# Preston [Organization]
* name: Preston

# DanielQueen [Person]
* name: Daniel Queen
* teaches -> Author

# MissGuerin [Person]
* name: Miss Guerin
* teaches -> Author

# GeorgeBalfour [Person]
* name: Captain George Balfour
* knows -> Author

# JamesDoran [Person]
* name: Captain James Doran
* owns -> Author