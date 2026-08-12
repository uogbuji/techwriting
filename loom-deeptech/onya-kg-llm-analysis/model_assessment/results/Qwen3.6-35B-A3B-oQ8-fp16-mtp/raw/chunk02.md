# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GeneralWolfe [Person]
* name: General Wolfe
* jobTitle: General
* description: A gallant general who was on board the author's ship during the voyage to Cape Breton. He was highly esteemed and beloved by the men for his affability. He saved the author from a flogging.
* knows -> Equiano
* memberOf -> BritishMilitary

# CaptainGeorgeBalfour [Person]
* name: Captain George Balfour
* jobTitle: Captain
* description: Captain of the Ætna fire-ship. He commanded boats that attacked French men of war. He liked the author and asked for him, but the author's master refused to part with him.
* memberOf -> BritishNavy
* owns -> Aetna

# CaptainLaforey [Person]
* name: Laforey
* jobTitle: Captain
* description: A junior captain who commanded boats alongside Captain George Balfour during the attack on French ships in Louisbourgh harbour.
* memberOf -> BritishNavy

# AdmiralBoscawen [Person]
* name: Admiral Boscawen
* jobTitle: Admiral
* description: The admiral who sailed with part of the fleet for England after the taking of Louisbourgh. He commanded the fleet during the engagement with Mons. Le Clue.
* memberOf -> BritishNavy

# RearAdmiralSirCharlesHardy [Person]
* name: Sir Charles Hardy
* jobTitle: Rear-Admiral
* description: A rear-admiral left behind with some ships after Admiral Boscawen sailed for England.
* memberOf -> BritishNavy

# RearAdmiralDurell [Person]
* name: Durell
* jobTitle: Rear-Admiral
* description: A rear-admiral left behind with some ships after Admiral Boscawen sailed for England.
* memberOf -> BritishNavy

# MonsConflans [Person]
* name: Mons. Conflans
* jobTitle: Commander
* description: Commander of the French squadron that the author's fleet encountered and chased.
* memberOf -> FrenchNavy

# MissGuerin [Person]
* name: Miss Guerin
* jobTitle: Lady
* description: One of the Miss Guerins who treated the author with kindness, sent him to school, and stood as his godmother during his baptism.
* knows -> Equiano
* knows -> EquianosMaster

# MissGuerins [Person]
* name: Miss Guerins
* description: Two ladies who treated the author with kindness, sent him to school, and instructed him in religion.
* knows -> Equiano

# EquianosMaster [Person]
* name: Equiano's Master
* jobTitle: Master
* description: The author's owner, who superintended the landing at Louisbourgh, refused to let the Miss Guerins baptize the author initially, and later sold the author to Captain James Doran.
* owns -> Equiano
* memberOf -> BritishNavy

# CaptainJamesDoran [Person]
* name: Captain James Doran
* jobTitle: Captain
* description: Captain of the Charming Sally, who bought the author from his master.
* owns -> Equiano
* memberOf -> BritishNavy

# JohnMondle [Person]
* name: John Mondle
* jobTitle: Gunner
* description: A gunner on the Ætna who had a religious vision and vow to stop drinking, which allegedly saved him from death when the Lynne collided with the Ætna.
* memberOf -> BritishNavy

# CaptainClark [Person]
* name: Captain Clark
* jobTitle: Captain
* description: Captain of the Lynne, a forty-gun ship that collided with the Ætna.
* memberOf -> BritishNavy

# CommodoreKeppel [Person]
* name: Commodore Keppel
* jobTitle: Commodore
* description: Commander of the large fleet at Spithead destined against Belle-Isle.
* memberOf -> BritishNavy

# GeneralCrawford [Person]
* name: General Crawford
* jobTitle: General
* description: A general who was taken prisoner during the landing at Belle-Isle.
* memberOf -> BritishMilitary

# CommodoreStanhope [Person]
* name: Commodore Stanhope
* jobTitle: Commodore
* description: A commander who led ships to Basse-road and sent the author's ship to St. Sebastian.
* memberOf -> BritishNavy

# CommodoreDennis [Person]
* name: Commodore Dennis
* jobTitle: Commodore
* description: A commander who sent the author's ship as a cartel to Bayonne.
* memberOf -> BritishNavy

# LordHowe [Person]
* name: Lord Howe
* jobTitle: Commander
* description: One of the commanders while the fleet was at Basse-road.
* memberOf -> BritishNavy

# DanielQueen [Person]
* name: Daniel Queen
* jobTitle: Captain's Clerk
* description: A well-educated man who messed with the author on the Ætna, taught him to shave, dress hair, and read the Bible. He was like a father to the author.
* knows -> Equiano
* memberOf -> BritishNavy

# Halifax [Place]
* name: Halifax
* description: A location in America with a commodious harbour called St. George, where the fleet resupplied.
* locatedIn -> NovaScotia

# NovaScotia [Place]
* name: Nova Scotia
* description: A region where Cape Breton is located.

# CapeBreton [Place]
* name: Cape Breton
* description: A location in Nova Scotia where the fleet arrived in the summer of 1758 to land soldiers for the attack on Louisbourgh.

# Louisbourgh [Place]
* name: Louisbourgh
* description: A town in Cape Breton that was besieged and taken by the English. It had a harbour blocked by the English fleet.

# StHelens [Place]
* name: St. Helen's
* description: A location where the fleet arrived at the close of the year 1758-9. The Namur ran aground here.

# Spithead [Place]
* name: Spithead
* description: A location where the fleet stayed for a short time before going to Portsmouth.

# Portsmouth [Place]
* name: Portsmouth
* description: A harbour where ships went to refit. The admiral went to London from here.

# London [Place]
* name: London
* description: A city where the author went with his master, attended school, and was baptized.

# Westminster [Place]
* name: Westminster
* description: A district in London where St. Margaret's church is located.

# StMargaretsChurch [Place]
* name: St. Margaret's church
* description: A church in Westminster where the author was baptized in February 1759.

# Gibraltar [Place]
* name: Gibraltar
* description: A Spanish sea-port where the fleet arrived after sailing from the Land's End. The author went on shore there.

# Barcelona [Place]
* name: Barcelona
* description: A Spanish sea-port remarkable for its silk manufactures, where the ships were watered.

# Toulon [Place]
* name: Toulon
* description: A location off which the fleet cruised to intercept French men of war.

# CapeLogas [Place]
* name: Cape Logas
* description: A coast of Portugal where the French ships Ocean and Redoubtable ran ashore.

# Portugal [Place]
* name: Portugal
* description: A country on whose coast Cape Logas is located.

# BelleIsle [Place]
* name: Belle-Isle
* description: An island against which an expedition was made. The author participated in the landing and siege.

# BasseRoad [Place]
* name: Basse-road
* description: A location where the fleet blocked up a French fleet from June to February.

# StSebastian [Place]
* name: St. Sebastian
* description: A location in Spain to which the author's ship was sent by Commodore Stanhope.

# Spain [Place]
* name: Spain
* description: A country where St. Sebastian is located.

# Bayonne [Place]
* name: Bayonne
* description: A location in France to which the author's ship was sent as a cartel by Commodore Dennis.

# France [Place]
* name: France
* description: A country where Bayonne is located.

# Guernsey [Place]
* name: Guernsey
* description: A location where the author's ship went in September, where he saw his old hostess.

# Deptford [Place]
* name: Deptford
* description: A location on the Thames where the ship arrived on the 10th of December to be paid off.

# Thames [Place]
* name: Thames
* description: A river where the author was forcibly taken by his master and sold.

# Gravesend [Place]
* name: Gravesend
* description: A location below which the author's master sold him to Captain Doran.

# WestIndies [Place]
* name: West Indies
* description: A region to which the Charming Sally was going, and where the author was sold as a slave.

# Mediterranean [Place]
* name: Mediterranean
* description: A sea where the fleet sailed from Spithead.

# GulfOfLyons [Place]
* name: Gulf of Lyons
* description: A gulf in the Mediterranean where the author's ship was overtaken by a gale of wind.

# England [Place]
* name: England
* description: A country where the author spent time at sea and in London.

# IsleOfWight [Place]
* name: Isle of Wight
* description: An island where the Ætna was stationed at Cowes.

# Cowes [Place]
* name: Cowes
* description: A location in the Isle of Wight.

# Plymouth [Place]
* name: Plymouth
* description: A location where the author belonged to the Jason in 1758.

# Turkey [Place]
* name: Turkey
* description: A destination of the Preston, where the author's companion Dick had gone.

# Levant [Place]
* name: Levant
* description: A region from which the Preston came.

# Aetna [Place]
* name: Ætna
* description: A fire-ship commanded by Captain George Balfour and later by Equiano's master.
* memberOf -> BritishNavy

# Namur [Place]
* name: Namur
* description: A ship on which the author served during the siege of Louisbourgh and the engagement with Mons. Le Clue.
* memberOf -> BritishNavy

# CharmingSally [Place]
* name: Charming Sally
* description: A ship going to the West Indies, owned by Captain James Doran, to which the author was sold.
* memberOf -> MerchantFleet

# Lynne [Place]
* name: Lynne
* description: A forty-gun ship commanded by Captain Clark that collided with the Ætna.
* memberOf -> BritishNavy

# Jason [Place]
* name: Jason
* description: A ship of fifty-four guns at Plymouth where the author belonged in 1758.
* memberOf -> BritishNavy

# Culloden [Place]
* name: Culloden
* description: A ship sent by the admiral to attack French frigates.
* memberOf -> BritishNavy

# Conqueror [Place]
* name: Conqueror
* description: A ship sent by the admiral to attack French frigates.
* memberOf -> BritishNavy

# Ocean [Place]
* name: Ocean
* description: An eighty-four gun ship commanded by Mons. La Clue, which was engaged and eventually ran ashore at Cape Logas.
* memberOf -> FrenchNavy

# Redoubtable [Place]
* name: Redoubtable
* description: A large French ship that ran ashore at Cape Logas along with the Ocean.
* memberOf -> FrenchNavy

# Newark [Place]
* name: Newark
* description: A ship where the admiral went after leaving the damaged Namur.
* memberOf -> BritishNavy

# Swiftsure [Place]
* name: Swiftsure
* description: A ship commanded by Commodore Stanhope.
* memberOf -> BritishNavy

# Wasp [Place]
* name: Wasp
* description: A sloop sent to St. Sebastian with the author's ship.
* memberOf -> BritishNavy

# Nassau [Place]
* name: Nassau
* description: A ship that a French vessel came within a gun shot of at Basse-road.
* memberOf -> BritishNavy

# LaModeste [Place]
* name: La Modeste
* description: A French prize of sixty-four guns taken during the engagement with Mons. Le Clue.
* memberOf -> FrenchNavy

# LeTemeraire [Place]
* name: Le Temeraire
* description: A French prize of seventy-four guns taken during the engagement with Mons. Le Clue.
* memberOf -> FrenchNavy

# Centaur [Place]
* name: Centaur
* description: A French prize of seventy-four guns taken during the engagement with Mons. Le Clue.
* memberOf -> FrenchNavy

# Carnarvon [Place]
* name: Carnarvon
* description: An English East Indiaman, a prize taken by the French, which the author's fleet chased.
* memberOf -> MerchantFleet

# PrincessAmelia [Place]
* name: Princess Amelia
* description: A ship whose lieutenant was killed during the landing at Louisbourgh.
* memberOf -> BritishNavy

# Bienfaisant [Place]
* name: Bienfaisant
* description: A sixty-four gun French ship brought off by the English.
* memberOf -> FrenchNavy

# IndianKing [Person]
* name: Indian King
* jobTitle: King
* description: An Indian king who was killed in the engagement at Louisbourgh. His scalp was held by the author.
* memberOf -> IndigenousPeoples

# Dick [Person]
* name: Dick
* jobTitle: Companion
* description: The author's old companion who died while on the Preston in Turkey.
* knows -> Equiano

# BlackBoy [Person]
* name: Black Boy
* jobTitle: Boy
* description: A black boy about the author's size, son of a gentleman on the Isle of Wight, who showed benevolence to the author.
* knows -> Equiano

# BishopOfSodorAndMan [Person]
* name: Bishop of Sodor and Man
* jobTitle: Bishop
* description: The author of the book "Guide to the Indians" given to the author by the clergyman at his baptism.

# AdmiralBroderick [Person]
* name: Admiral Broderick
* jobTitle: Admiral
* description: An admiral who took command after the Namur was disabled.
* memberOf -> BritishNavy