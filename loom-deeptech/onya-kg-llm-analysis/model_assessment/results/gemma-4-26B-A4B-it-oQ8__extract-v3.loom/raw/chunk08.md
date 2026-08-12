# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: A native of Africa, a former servant to Dr. Irving, and a commissary for the black poor going to Sierra Leone.

# CharlesIrving [Person]
* name: Charles Irving
* jobTitle: Doctor
* description: A doctor on the Musquito shore who employed Gustavus Vassa.
* colleague -> GustavusVassa

# Hughes [Person]
* name: Hughes
* description: An owner of a sloop and a schooner.

# Cox [Person]
* name: Mr. Cox
* jobTitle: Carpenter
* description: A man on board a vessel who knew Dr. Irving and Gustavus Vassa.
* knows -> CharlesIrving
* knows -> GustavusVassa

# CaptainJenning [Person]
* name: Captain Jenning
* description: A captain of a sloop.

# JohnBaker [Person]
* name: John Baker
* jobTitle: Captain
* description: An Englishman and captain of the Indian Queen.

# Stoker [Person]
* name: Stoker
* jobTitle: White pilot
* description: A pilot on the Indian Queen.

# JoeDiamond [Person]
* name: Joe Diamond
* jobTitle: Taylor
* description: A free negro taylor.

# GovernorMacnamara [Person]
* name: Governor Macnamara
* jobTitle: Governor
* description: A governor who served on the coast of Africa.

# RobertLordBishopOfLondon [Person]
* name: Robert, Lord Bishop of London
* jobTitle: Bishop of London
* description: The Bishop to whom Gustavus Vassa applied for ordination.

# ThomasWallace [Person]
* name: Thomas Wallace
* description: A man who resided in Senegambia and supported the African mission.

# MartinHopkin [Person]
* name: Martin Hopkin
* jobTitle: Captain
* description: Captain of the ship London.

# CaptainDouglas [Person]
* name: Captain Douglas
* jobTitle: Captain
* description: Captain of the Squirrel man of war.

# MusquitoShore [Place]
* name: Musquito Shore

# Jamaica [Place]
* name: Jamaica

# Carthagena [Place]
* name: Carthagena

# London [Place]
* name: London

# Philadelphia [Place]
* name: Philadelphia

# SierraLeone [Place]
* name: Sierra Leone

# England [Place]
* name: England

# NewYork [Place]
* name: New-York

# Plymouth [Place]
* name: Plymouth

# Exeter [Place]
* name: Exeter

# Wales [Place]
* name: Wales

# Shropshire [Place]
* name: Shropshire

# HisMajestysNavy [Organization]
* name: His Majesty's Navy