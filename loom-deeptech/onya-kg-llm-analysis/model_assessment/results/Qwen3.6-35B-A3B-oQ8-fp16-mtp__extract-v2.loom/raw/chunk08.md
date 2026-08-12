# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The narrator and author of the narrative, formerly enslaved, later a free man, steward, and commissary.
* worksFor: CharlesIrving
* worksFor: CaptainJenning
* worksFor: JohnBaker
* worksFor: CaptainDouglas
* worksFor: GovernorMacnamara
* worksFor: MartinHopkin
* worksFor: CaptainJohnWillet
* worksFor: CommissionersOfHisMajestysNavy
* knows: CharlesIrving
* knows: Hughes
* knows: MrCox
* knows: CaptainJenning
* knows: JohnBaker
* knows: Stoker
* knows: CaptainDouglas
* knows: JoeDiamond
* knows: MrCochran
* knows: GovernorMacnamara
* knows: BishopOfLondon
* knows: MattMacnamara
* knows: ThomasWallace
* knows: JHinslow
* knows: GeoMarsh
* knows: WPalmer
* knows: CaptThompson
* knows: TheQueen
* knows: TheFriendsOrQuakers

# CharlesIrving [Person]
* name: Charles Irving
* jobTitle: Doctor
* description: A doctor who owned Gustavus Vassa, granted him freedom, and later became his friend and protector.
* employs: GustavusVassa
* knows: GustavusVassa
* knows: Hughes
* knows: MrCox
* knows: CaptainDouglas
* knows: CaptainBaker (implied via context of Kingston magistrates, but primarily known through Vassa's interactions)

# Hughes [Person]
* name: Hughes
* jobTitle: Owner
* description: An owner of a sloop who attempted to re-enslave Gustavus Vassa.
* knows: GustavusVassa
* knows: CharlesIrving

# MrCox [Person]
* name: Mr Cox
* jobTitle: Carpenter
* description: A carpenter on board the sloop who knew Dr. Irving and advocated for Vassa.
* knows: GustavusVassa
* knows: CharlesIrving

# CaptainJenning [Person]
* name: Captain Jenning
* jobTitle: Captain
* description: Captain of a sloop who employed Vassa to work his passage to Jamaica.
* worksFor: GustavusVassa
* knows: GustavusVassa

# JohnBaker [Person]
* name: John Baker
* jobTitle: Captain
* description: Captain of the sloop Indian Queen who promised Vassa wages but refused to pay them.
* worksFor: GustavusVassa
* knows: GustavusVassa

# Stoker [Person]
* name: Stoker
* jobTitle: Pilot
* description: A white pilot on the Indian Queen who was abused by Captain Baker.
* knows: JohnBaker
* knows: GustavusVassa

# CaptainDouglas [Person]
* name: Captain Douglas
* jobTitle: Captain
* description: Captain of the Squirrel man of war who protected Vassa from Captain Baker.
* knows: GustavusVassa
* knows: CharlesIrving

# JoeDiamond [Person]
* name: Joe Diamond
* jobTitle: Taylor
* description: A free negro tailor who accompanied Vassa.
* knows: GustavusVassa

# MrCochran [Person]
* name: Mr Cochran
* jobTitle: Debtor
* description: A man indebted to Joe Diamond.
* knows: JoeDiamond

# GovernorMacnamara [Person]
* name: Governor Macnamara
* jobTitle: Governor
* description: Governor who employed Vassa and supported his mission to Africa.
* worksFor: GustavusVassa
* knows: GustavusVassa
* knows: BishopOfLondon
* knows: MattMacnamara

# BishopOfLondon [Person]
* name: Robert, Lord Bishop of London
* jobTitle: Bishop
* description: The Bishop to whom Vassa applied for ordination as a missionary.
* knows: GustavusVassa
* knows: MattMacnamara
* knows: ThomasWallace

# MattMacnamara [Person]
* name: Matt Macnamara
* jobTitle: Governor
* description: Governor who wrote a letter supporting Vassa's mission.
* knows: GustavusVassa
* knows: BishopOfLondon

# ThomasWallace [Person]
* name: Thomas Wallace
* jobTitle: Doctor
* description: A doctor who resided in Africa and supported Vassa's mission.
* knows: GustavusVassa
* knows: BishopOfLondon

# JHinslow [Person]
* name: J. Hinslow
* jobTitle: Commissioner
* description: Principal Officer and Commissioner of His Majesty's Navy.
* knows: GustavusVassa

# GeoMarsh [Person]
* name: Geo. Marsh
* jobTitle: Commissioner
* description: Principal Officer and Commissioner of His Majesty's Navy.
* knows: GustavusVassa

# WPalmer [Person]
* name: W. Palmer
* jobTitle: Commissioner
* description: Principal Officer and Commissioner of His Majesty's Navy.
* knows: GustavusVassa

# CaptThompson [Person]
* name: Capt. Thompson
* jobTitle: Captain
* description: Captain of the Nautilus who convoyed the expedition to Sierra Leone.
* knows: GustavusVassa

# TheQueen [Person]
* name: The Queen
* jobTitle: Queen
* description: The British Queen to whom Vassa presented a petition.
* knows: GustavusVassa

# MartinHopkin [Person]
* name: Martin Hopkin
* jobTitle: Captain
* description: Captain of the ship London.
* worksFor: GustavusVassa

# CaptainJohnWillet [Person]
* name: Captain John Willet
* jobTitle: Captain
* description: Captain of the American ship Harmony.
* worksFor: GustavusVassa

# CommissionersOfHisMajestysNavy [Organization]
* name: Commissioners of His Majesty's Navy
* description: The government body that appointed Vassa as commissary for the Sierra Leone expedition.
* employs: GustavusVassa

# TheFriendsOrQuakers [Organization]
* name: The Friends or Quakers
* description: A religious group in London that Vassa thanked for their benevolence.
* knows: GustavusVassa