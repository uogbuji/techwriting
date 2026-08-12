# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The narrator, a native of Africa who became a free man, missionary candidate, and commissary for the black poor.

# CharlesIrving [Person]
* name: Charles Irving
* jobTitle: Doctor
* description: A doctor who owned Gustavus Vassa, granted him freedom, and later became his friend.
* owns -> GustavusVassa
* knows -> GustavusVassa

# Hughes [Person]
* name: Hughes
* jobTitle: Owner
* description: An owner of a sloop who attempted to re-enslave Gustavus Vassa.
* owns -> Sloop
* memberOf -> Crew

# Cox [Person]
* name: Mr. Cox
* jobTitle: Carpenter
* description: A carpenter on board who knew the doctor and advocated for Gustavus Vassa.
* knows -> CharlesIrving
* knows -> GustavusVassa

# CaptainJenning [Person]
* name: Captain Jenning
* jobTitle: Captain
* description: Captain of a sloop who initially promised to sail to Jamaica but instead forced Vassa to cut mahogany.

# JohnBaker [Person]
* name: John Baker
* jobTitle: Captain
* description: Captain of the sloop Indian Queen, an Englishman who promised Vassa wages but refused to pay.
* owns -> IndianQueen
* memberOf -> Crew

# Stoker [Person]
* name: Stoker
* jobTitle: Pilot
* description: A white pilot on the Indian Queen who was abused by Captain Baker.
* memberOf -> Crew

# CaptainDouglas [Person]
* name: Captain Douglas
* jobTitle: Captain
* description: Captain of the Squirrel man of war who protected Gustavus Vassa from Captain Baker.
* owns -> Squirrel

# JoeDiamond [Person]
* name: Joe Diamond
* jobTitle: Taylor
* description: A free negro taylor who was owed money by Mr. Cochran.

# MrCochran [Person]
* name: Mr. Cochran
* description: A man indebted to Joe Diamond.

# GovernorMacnamara [Person]
* name: Governor Macnamara
* jobTitle: Governor
* description: A governor who served as Vassa's employer and advocated for his missionary work.
* memberOf -> Crew
* knows -> GustavusVassa

# Robert [Person]
* name: Robert
* jobTitle: Lord Bishop of London
* description: The Bishop of London who declined to ordain Gustavus Vassa as a missionary.

# MattMacnamara [Person]
* name: Matt. Macnamara
* description: Governor Macnamara, who wrote a letter supporting Vassa's missionary application.

# ThomasWallace [Person]
* name: Thomas Wallace
* jobTitle: Doctor
* description: A doctor who resided in Africa and supported Vassa's missionary application.

# MartinHopkin [Person]
* name: Martin Hopkin
* jobTitle: Captain
* description: Captain of the ship London.

# JohnWillet [Person]
* name: John Willet
* jobTitle: Captain
* description: Captain of the American ship Harmony.

# JHinslow [Person]
* name: J. Hinslow
* description: Principal Officer and Commissioner of his Majesty's Navy.

# GeoMarsh [Person]
* name: Geo. Marsh
* description: Principal Officer and Commissioner of his Majesty's Navy.

# WPalmer [Person]
* name: W. Palmer
* description: Principal Officer and Commissioner of his Majesty's Navy.

# CaptainThompson [Person]
* name: Capt. Thompson
* jobTitle: Captain
* description: Captain of the Nautilus who convoyed the expedition to Sierra Leone.
* owns -> Nautilus

# Queen [Person]
* name: The Queen
* description: The Queen of England to whom Gustavus Vassa presented a petition.

# MusquitoAdmiral [Person]
* name: Musquito admiral
* jobTitle: Admiral
* description: An Indian chief of a district who helped Gustavus Vassa.

# NewYork [Place]
* name: New-York
* description: A city in America where the ship London arrived.

# Jamaica [Place]
* name: Jamaica
* description: An island where Gustavus Vassa arrived and sought wages.

# Kingston [Place]
* name: Kingston
* description: A location in Jamaica where Vassa sought magistrates.

# SierraLeone [Place]
* name: Sierra Leone
* description: A location in Africa where the expedition to the black poor was destined.

# London [Place]
* name: London
* description: A city in England where Vassa resided and presented petitions.

# Plymouth [Place]
* name: Plymouth
* description: A port in England where Vassa arrived.

# Exeter [Place]
* name: Exeter
* description: A city in England where Vassa stayed among pious friends.

# Philadelphia [Place]
* name: Philadelphia
* description: A city in America where Vassa arrived.

# MusquitoShore [Place]
* name: Musquito Shore
* description: A location where Vassa previously worked and managed an estate.

# Carthagena [Place]
* name: Carthagena
* description: A destination towards which a vessel was sailing.

# Wales [Place]
* name: Wales
* description: A region in Britain visited by Vassa.

# Shropshire [Place]
* name: Shropshire
* description: A county in Britain where Vassa visited a coal-pit.

# Devonshire [Place]
* name: Devonshire
* description: A county in Britain where Vassa served in the militia.

# Coxheath [Place]
* name: Coxheath
* description: A location where Vassa was encamped with the Devonshire militia.

# Portsmouth [Place]
* name: Portsmouth
* description: A location with king's stores where superfluous slops were to be sent.

# Senegambia [Place]
* name: Senegambia
* description: A province on the coast of Africa where Thomas Wallace resided.

# CapeCoastCastle [Place]
* name: Cape Coast Castle
* description: A location in Africa mentioned by Matt Macnamara.

# Africa [Place]
* name: Africa
* description: The continent of Vassa's origin and intended missionary destination.

# England [Place]
* name: England
* description: The country Vassa returned to.

# BritishLegislature [Organization]
* name: British legislature
* description: The legislative body deliberating on the redress of oppression in the West Indies.

# CommissionersOfHisMajestysNavy [Organization]
* name: Commissioners of his Majesty's Navy
* description: The body that appointed Vassa as commissary and later dismissed him.

# CommitteeForTheBlackPoor [Organization]
* name: Committee for the black poor
* description: A select committee of gentlemen in London that recommended Vassa for the Sierra Leone expedition.

# LordsCommissionersOfHisMajestysTreasury [Organization]
* name: Lords Commissioners of his Majesty's Treasury
* description: The body to whom Vassa presented a memorial regarding his dismissal.

# Quakers [Organization]
* name: Friends or Quakers
* description: A religious group in London who freed and eased the burdens of African brethren.

# Squirrel [Organization]
* name: Squirrel
* description: A man of war ship commanded by Captain Douglas.

# Nautilus [Organization]
* name: Nautilus
* description: A ship commanded by Captain Thompson.

# IndianQueen [Organization]
* name: Indian Queen
* description: A sloop commanded by John Baker.

# London [Organization]
* name: London
* description: A fine new ship commanded by Martin Hopkin.

# Harmony [Organization]
* name: Harmony
* description: An American ship commanded by John Willet.

# Vernon [Organization]
* name: Vernon
* description: A ship appointed to proceed to Africa with the black poor.