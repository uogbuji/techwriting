# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# AdmiralBoscawen [Person]

* description: "The admiral who commanded the fleet and sailed for England."
* jobTitle: Admiral
* name: "Admiral Boscawen"

# AdmiralBoscawen-RearAdmiralDurell [Relationship]

* colleague: RearAdmiralDurell
* name: "Admiral Boscawen is colleague of Rear-admiral Durell"

# AdmiralBoscawen-RearAdmiralSirCharlesHardy [Relationship]

* colleague: RearAdmiralSirCharlesHardy
* name: "Admiral Boscawen is colleague of Rear-admiral Sir Charles Hardy"

# Africa [Place]

* description: "A continent rich in vegetable and mineral productions, target for commercial intercourse and civilization."
* description: "The continent, specifically the region known as Guinea, extending from Senegal to Angola."
* name: Africa

# AnotherLady [Person]

* description: "A lady who succeeded the Lady in Gosport in the former master's good graces and instigated the master to treat the author cruelly."
* knows: FormerMaster
* knows: OlaudahEquiano
* name: "Another Lady"

# Barbadoes [Place]

* description: "An island in the West Indies."
* description: "An island in the West Indies where the author arrived and the cargo was sold."
* name: Barbadoes

# Barcelona [Place]

* description: "A Spanish sea-port known for silk manufactures."
* name: Barcelona

# BasseRoad [Place]

* description: "A location where the fleet blocked up a French fleet."
* name: Basse-road

# Bayonne [Place]

* description: "A location in France the ship was sent to as a cartel."
* name: Bayonne

# BelleIsle [Place]

* description: "An island attacked by the English fleet."
* name: Belle-Isle

# Benezet [Person]

* description: "Author of 'Account of Guinea' and 'Account of Africa'."
* name: Benezet

# Benin [Place]

* description: "A considerable kingdom in Guinea, situated nearly under the line."
* name: Benin

# BishopOfLondon [Person]

* description: "The Bishop to whom Vassa applied for ordination as a missionary."
* jobTitle: Bishop
* knows: GustavusVassa
* knows: MattMacnamara
* knows: ThomasWallace
* name: "Robert, Lord Bishop of London"

# BishopOfSodorAndMan [Person]

* description: "Author of the book 'Guide to the Indians' given to the author."
* jobTitle: Bishop
* name: "Bishop of Sodor and Man"

# BlackfriarsChurch [Organization]

* description: "A church in London where Equiano heard Mr. Romaine preach."
* name: "Blackfriars church"

# BritishLegislature [Organization]

* description: "The legislative body considering the inhuman traffic of slavery and designs worthy of royal patronation."
* name: "British Legislature"

# BritishSeaman [Person]

* description: "A seaman on board who prevented a depredator from striking the author."
* name: "British Seaman"

# BrotherOfEquiano [Person]

* description: "One of Olaudah Equiano's brothers, who received the Embrenche mark."
* name: BrotherOfEquiano
* parent -> Embrenche

# Cadiz [Place]

* description: "A port city in Spain."
* name: Cadiz

# CapeBreton [Place]

* description: "A location in Nova Scotia where the fleet arrived in 1758."
* name: "Cape Breton"

# CapeLogas [Place]

* description: "A coast in Portugal where French ships ran ashore."
* name: "Cape Logas"

# CaptJohnHamer [Person]

* colleague: GustavusVassa
* description: "Captain of the ship Andromache, with whom Gustavus Vassa traveled to London."
* jobTitle: Captain
* name: "Capt. John Hamer"

# CaptLinna [Person]

* description: "Captain of the Turkeyman Wester Hall."
* jobTitle: Captain
* name: "Capt. Linna"
* worksFor: GustavusVassa

# CaptOHara [Person]

* description: "A gentleman who treated Gustavus Vassa with kindness and recommended him to a hair-dresser."
* jobTitle: Captain
* knows: GustavusVassa
* name: "Capt. O'Hara"

# CaptPascal [Person]

* description: "Cousin of the Miss Guerins, former master of Gustavus Vassa, who treated him ill and withheld prize money."
* jobTitle: Captain
* knows: GustavusVassa
* knows: MissGuerins
* name: "Capt. Pascal"
* owns: GustavusVassa

# CaptThompson [Person]

* description: "Captain of the Nautilus who convoyed the expedition to Sierra Leone."
* jobTitle: Captain
* knows: GustavusVassa
* name: "Capt. Thompson"

# CaptWmRobertson [Person]

* colleague: GustavusVassa
* description: "Captain of the ship Grenada Planter."
* jobTitle: Captain
* name: "Capt. Wm. Robertson"
* worksFor: GustavusVassa

# Captain [Person]

* description: "Gustavus Vassa's captain on the vessel bound for the West Indies; later died at sea."
* description: "The narrator's friendly captain who protected him, lent him money, and advocated for his freedom."
* jobTitle: Captain
* name: Captain
* advocatesFor -> GustavusVassa
* colleague -> Mate
* colleague -> RobertKing
* employs -> GustavusVassa
* knows -> MrRead
* knows -> MrDixon
* lendsMoney -> GustavusVassa
* protects -> GustavusVassa
* worksFor -> RobertKing

# CaptainClark [Person]

* description: "Captain of the Lynne, which collided with the Ætna."
* jobTitle: Captain
* name: "Captain Clark"

# CaptainDavidMiller [Person]

* description: "Captain of the sloop Morning Star."
* employs: Equiano
* knows: Equiano
* name: "Captain David Miller"
* owns: MorningStar

# CaptainDavidMillereemploysEquiano [Relationship]

* name: "CaptainDavidMiller employs Equiano"
* object: Equiano
* predicate: employs
* subject: CaptainDavidMiller

# CaptainDavidMillerownsMorningStar [Relationship]

* name: "CaptainDavidMiller owns MorningStar"
* object: MorningStar
* predicate: owns
* subject: CaptainDavidMiller

# CaptainDavidWatt [Person]

* colleague: GustavusVassa
* description: "Captain of the ship Jamaica."
* jobTitle: Captain
* name: "Captain David Watt"
* worksFor: GustavusVassa

# CaptainDoran [Person]

* description: "The captain of the ship who sent the author to be sold in Montserrat."
* description: "Captain of the Charming Sally."
* jobTitle: Captain
* name: "Captain Doran"
* worksFor: MrKing
* colleague -> MrMansfield
* colleague -> OlaudahEquiano

# CaptainDouglas [Person]

* description: "Captain of the Squirrel man of war who protected Vassa from Captain Baker."
* jobTitle: Captain
* knows: GustavusVassa
* knows: CharlesIrving
* name: "Captain Douglas"

# CaptainGeorgeBalfour [Person]

* description: "Captain of the Ætna fire-ship, who noticed and liked the author."
* jobTitle: Captain
* name: "Captain George Balfour"

# CaptainGeorgeBalfour-CaptainLaforey [Relationship]

* colleague: CaptainLaforey
* name: "Captain George Balfour is colleague of Captain Laforey"

# CaptainJamesDoran [Person]

* description: "Captain of the Charming Sally, who bought the author from his master."
* jobTitle: Captain
* name: "Captain James Doran"

# CaptainJenning [Person]

* description: "Captain of a sloop who employed Vassa to work his passage to Jamaica."
* jobTitle: Captain
* knows: GustavusVassa
* name: "Captain Jenning"
* worksFor: GustavusVassa

# CaptainJohnHughes [Person]

* description: "Commander of the ship Anglicania, bound for Smyrna."
* jobTitle: Captain
* knows: JohnAnnis
* name: "Captain John Hughes"
* worksFor: GustavusVassa

# CaptainJohnWillet [Person]

* description: "Captain of the American ship Harmony."
* jobTitle: Captain
* name: "Captain John Willet"
* worksFor: GustavusVassa

# CaptainLaforey [Person]

* description: "A junior captain who served alongside Captain George Balfour."
* jobTitle: Captain
* name: "Captain Laforey"

# CaptainLutwidge [Person]

* colleague: GustavusVassa
* colleague: JohnConstantinePhipps
* description: "Captain of the sloop Carcass, which joined Phipps' expedition."
* jobTitle: Captain
* name: "Captain Lutwidge"

# CaptainPascal [Person]

* description: "A captain met by the author in Martinico."
* description: "The narrator's old master in England whom he hoped to surprise."
* name: "Captain Pascal"
* name: "Capt. Pascal"
* formerMasterOf -> GustavusVassa
* knows -> GustavusVassa

# CaptainPlasmyah [Person]

* description: "A friendly chief and neighbor of Equiano and the Doctor."
* knows: Equiano
* name: "Captain Plasmyah"

# CaptainRichardStrange [Person]

* description: "Captain of the ship Hope."
* employs: Equiano
* knows: Equiano
* name: "Capt. Richard Strange"
* owns: Hope

# CaptainRichardStrangeownsHope [Relationship]

* name: "CaptainRichardStrange owns Hope"
* object: Hope
* predicate: owns
* subject: CaptainRichardStrange

# CaptainThomasFarmer [Person]

* description: "An English captain who commanded a Bermudas sloop and employed the author as a sailor."
* name: "Captain Thomas Farmer"
* worksFor: OlaudahEquiano
* worksFor: MrKing

# CharlesIrving [Person]

* description: "A doctor who owned Gustavus Vassa, granted him freedom, and later became his friend and protector."
* employs: GustavusVassa
* jobTitle: Doctor
* knows: CaptainDouglas
* knows: "CaptainBaker (implied via context of Kingston magistrates, but primarily known through Vassa's interactions)"
* knows: GustavusVassa
* knows: Hughes
* knows: MrCox
* name: "Charles Irving"

# CharmingSally [Organization]

* description: "A slave ship captained by Captain Doran."
* name: "Charming Sally"
* memberOf -> CaptainDoran
* memberOf -> MrMansfield

# CommissionersOfHisMajestysNavy [Organization]

* description: "The government body that appointed Vassa as commissary for the Sierra Leone expedition."
* employs: GustavusVassa
* name: "Commissioners of His Majesty's Navy"

# CommodoreKeppel [Person]

* description: "Commodore who commanded the fleet destined against Belle-Isle."
* jobTitle: Commodore
* name: "Commodore Keppel"

# DanielQueen [Person]

* description: "A man who messed with the author on the Ætna, taught him to shave and read, and was like a father to him."
* jobTitle: "Captain's Clerk/Attendant"
* name: "Daniel Queen"

# Depredator [Person]

* description: "A man in St. Eustatia who bought fowls and pigs from the author and tried to take his money back."
* name: Depredator

# Deptford [Place]

* description: "A location on the Thames where the ship arrived to be paid off."
* name: Deptford

# Dick [Person]

* description: "The author's old companion who died while on the Preston."
* jobTitle: Companion
* name: Dick

# DoctorBrady [Person]

* description: "An eminent doctor in Savannah who treated the narrator's wounds."
* description: "An honest and worthy man who assisted Gustavus Vassa when he was threatened by the watch in Savannah."
* name: "Doctor Brady"
* knows -> GustavusVassa
* treats -> GustavusVassa

# DoctorIrving [Person]

* description: "A friend and employer who engaged Equiano for a plantation venture."
* description: "A person with whom Gustavus Vassa hired himself to learn to freshen sea water."
* employs: Equiano
* knows: Equiano
* name: "Doctor Irving"
* owns: MorningStar
* employs -> GustavusVassa

# DoctorIrvingemploysEquiano [Relationship]

* name: "DoctorIrving employs Equiano"
* object: Equiano
* predicate: employs
* subject: DoctorIrving

# DoctorIrvingownsMorningStar [Relationship]

* name: "DoctorIrving owns MorningStar"
* object: MorningStar
* predicate: owns
* subject: DoctorIrving

# DoctorPerkins [Person]

* description: "A severe and cruel man in Savannah who beat the narrator."
* description: "A person referenced by the watch in Savannah as an example of how they might treat Vassa."
* description: "A doctor who nearly murdered the author in Savannah."
* name: "Doctor Perkins"
* attacks -> GustavusVassa

# DrCharlesIrving [Person]

* description: "A gentleman celebrated for experiments in making sea water fresh, who employed Gustavus Vassa as a hairdresser and later on an expedition."
* jobTitle: Master
* knows: GustavusVassa
* name: "Dr. Charles Irving"
* worksFor: GustavusVassa

# DrGill [Person]

* description: "Author of a commentary on Genesis, who deduced the pedigree of Africans from Afer and Afra."
* name: "Dr. Gill"
* colleague -> DrJohnClarke

# DrJohnClarke [Person]

* description: "Author of 'Truth of the Christian Religion', who ascribed an African origin to the Jews."
* jobTitle: "Dean of Sarum"
* name: "Dr. John Clarke"
* colleague -> DrGill

# DrMitchel [Person]

* description: "Cited by Clarkson regarding the change in complexion of Spaniards in America."
* name: "Dr. Mitchel"
* colleague -> MrTClarkson

# DutchCreole [Person]

* description: "A sailor who assisted Gustavus Vassa in saving the crew after the shipwreck."
* name: "Dutch Creole"
* colleague -> GustavusVassa

# Eboe [Place]

* description: "A remote and fertile province in the kingdom of Benin, where Olaudah Equiano was born."
* name: Eboe

# EmanuelSankey [Person]

* description: "A negro man who tried to escape from bondage by hiding on a London ship."
* name: "Emanuel Sankey"

# Embrenche [Person]

* description: "A chief or elder in Eboe, holding the highest distinction, styled Embrenche."
* jobTitle: Chief/Elder
* name: Embrenche
* parent -> BrotherOfEquiano
* parent -> OlaudahEquiano

# England [Place]

* description: "A country in Europe."
* name: England

# Equiano [Person]

* description: "The author of the narrative, formerly enslaved, later a free man and Christian convert."
* name: Equiano

# EquianoknowsCaptainPlasmyah [Relationship]

* name: "Equiano knows CaptainPlasmyah"
* object: CaptainPlasmyah
* predicate: knows
* subject: Equiano

# EquianoknowsFatherVincent [Relationship]

* name: "Equiano knows FatherVincent"
* object: FatherVincent
* predicate: knows
* subject: Equiano

# EquianoknowsGeorge [Relationship]

* name: "Equiano knows George"
* object: George
* predicate: knows
* subject: Equiano

# EquianoknowsMrGS [Relationship]

* name: "Equiano knows MrGS"
* object: MrGS
* predicate: knows
* subject: Equiano

# EquianoknowsMrLd [Relationship]

* name: "Equiano knows MrLd"
* object: MrLd
* predicate: knows
* subject: Equiano

# EquianoknowsMrP [Relationship]

* name: "Equiano knows MrP"
* object: MrP
* predicate: knows
* subject: Equiano

# EquianoknowsMrRomaine [Relationship]

* name: "Equiano knows MrRomaine"
* object: MrRomaine
* predicate: knows
* subject: Equiano

# EquianoknowsMusquitoKing [Relationship]

* name: "Equiano knows MusquitoKing"
* object: MusquitoKing
* predicate: knows
* subject: Equiano

# EquianoworksForCaptainDavidMiller [Relationship]

* name: "Equiano worksFor CaptainDavidMiller"
* object: CaptainDavidMiller
* predicate: worksFor
* subject: Equiano

# EquianoworksForCaptainRichardStrange [Relationship]

* name: "Equiano worksFor CaptainRichardStrange"
* object: CaptainRichardStrange
* predicate: worksFor
* subject: Equiano

# EquianoworksForDoctorIrving [Relationship]

* name: "Equiano worksFor DoctorIrving"
* object: DoctorIrving
* predicate: worksFor
* subject: Equiano

# Essaka [Place]

* description: "A charming fruitful vale in Eboe where Olaudah Equiano was born."
* name: Essaka

# FatherVincent [Person]

* description: "A Catholic priest Equiano disputed with in Malaga."
* knows: Equiano
* name: "Father Vincent"

# FormerMaster [Person]

* description: "The author's previous master who sent him to be sold in Montserrat."
* name: "Former Master"
* owns: OlaudahEquiano

# FrenchPlanter [Person]

* description: "A planter in Martinico who had mulattoes working in the fields, who were his own children."
* name: "French Planter"

# GeneralCrawford [Person]

* description: "A general taken prisoner during the landing at Belle-Isle."
* jobTitle: General
* name: "General Crawford"

# GeneralWolfe [Person]

* description: "A gallant general who was on board the author's ship."
* jobTitle: General
* name: "General Wolfe"

# Gentleman [Person]

* description: "A gentleman who begged off a negro-man from receiving a hundred lashes."
* name: Gentleman

# GeoMarsh [Person]

* description: "Principal Officer and Commissioner of His Majesty's Navy."
* jobTitle: Commissioner
* knows: GustavusVassa
* name: "Geo. Marsh"

# George [Person]

* description: "The Musquito king's son, an Indian prince baptized in England."
* knows: Equiano
* name: George

# GeorgeWhitfield [Person]

* description: "A preacher whom the narrator heard in Philadelphia."
* name: "Rev. Mr. George Whitfield"
* preachesTo -> GustavusVassa

# Georgia [Place]

* description: "A place in America where the narrator traded and was attacked."
* name: Georgia
* locationOf -> GustavusVassa
* locationOf -> DoctorBrady
* locationOf -> DoctorPerkins

# Gibraltar [Place]

* description: "A Spanish sea-port where the fleet stopped in the Mediterranean."
* name: Gibraltar

# Gosport [Place]

* description: "A location where a lady lived who wanted to take the author out of the ship."
* name: Gosport

# Governor [Person]

* description: "The governor who seized a boat from a negro-man and later died in poverty."
* name: Governor

# GovernorMacnamara [Person]

* description: "Governor who employed Vassa and supported his mission to Africa."
* jobTitle: Governor
* knows: MattMacnamara
* knows: GustavusVassa
* knows: BishopOfLondon
* name: "Governor Macnamara"
* worksFor: GustavusVassa

# GranvilleSharp [Person]

* description: "A philanthropist who advised Gustavus Vassa on how to procure John Annis's freedom."
* jobTitle: Philanthropist
* knows: GustavusVassa
* name: "Granville Sharp, Esq."

# GreatBritain [Place]

* description: "A country with manufacturing interests equal or superior to landed interests; source of British manufactures."
* name: "Great Britain"

# Grenada [Place]

* description: "An island where the author traded."
* name: Grenada

# GrenvilleSharp [Person]

* description: "Esq; an approved friend, man of virtue, benefactor to mankind."
* knows: RobertKing
* knows: ThomasClarkson
* knows: JamesRamsay
* memberOf: BritishLegislature
* name: "Grenville Sharp"

# Guadaloupe [Place]

* description: "A French island where the author traded."
* name: Guadaloupe

# Guernsey [Place]

* description: "A location the ship went to in September."
* name: Guernsey

# GustavusVassa [Person]

* description: "The narrator and author of the narrative, formerly enslaved, later a free man, steward, and commissary."
* description: "The narrator, originally named Jacob or Michael, a slave from Africa who was sold multiple times and served in the Royal Navy."
* description: "The narrator, formerly a slave, who purchases his freedom and becomes a sailor."
* description: "The author of the narrative, a free negro who serves as a sailor and captain."
* description: "The author and narrator of the narrative, formerly enslaved, later gained freedom."
* description: "The narrator and author of the narrative, formerly a slave, later a free man, steward, and Christian convert."
* jobTitle: "Sailor, Trader"
* jobTitle: "Slave, Sailor, Soldier"
* jobTitle: "Sailor, Steward, Author"
* knows: CaptOHara
* knows: MrCochran
* knows: DrCharlesIrving
* knows: GovernorMacnamara
* knows: JohnAnnis
* knows: BishopOfLondon
* knows: GranvilleSharp
* knows: MattMacnamara
* knows: MrC
* knows: ThomasWallace
* knows: JHinslow
* knows: GeoMarsh
* knows: WPalmer
* knows: CaptThompson
* knows: TheQueen
* knows: TheFriendsOrQuakers
* knows: CharlesIrving
* knows: Hughes
* knows: MrCox
* knows: CaptainJenning
* knows: JohnBaker
* knows: Stoker
* knows: MissGuerins
* knows: CaptainDouglas
* knows: CaptPascal
* knows: JoeDiamond
* name: "Gustavus Vassa"
* worksFor: CharlesIrving
* worksFor: CaptainJenning
* worksFor: JohnBaker
* worksFor: CaptainDouglas
* worksFor: RobertKing
* worksFor: DrCharlesIrving
* worksFor: GovernorMacnamara
* worksFor: CaptPascal
* worksFor: MartinHopkin
* worksFor: CaptOHara
* worksFor: CaptainJohnWillet
* worksFor: CaptWmRobertson
* worksFor: CommissionersOfHisMajestysNavy
* worksFor: JohnJolly
* worksFor: CaptainDavidWatt
* worksFor: JohnConstantinePhipps
* worksFor: CaptainLutwidge
* worksFor: CaptainJohnHughes
* worksFor: CaptLinna
* colleague -> RichardBaker
* colleague -> TheMateInGuernsey
* knows -> TheGentlemanInFalmouth
* knows -> TheWhiteMen
* knows -> TheGentlemanInVirginia
* knows -> TheMateInGuernsey
* knows -> TheDaughterOfGentleman
* knows -> TheYoungLadDick
* knows -> TheBlackWoman
* knows -> TheElderlyBlackMan
* knows -> TheWifeOfMateInGuernsey
* knows -> TheCaptain
* knows -> TheDoctors
* knows -> TheLittleDaughterOfMateInGuernsey
* knows -> TheMate
* knows -> TheBoy
* knows -> MrGuerin
* knows -> TheGentleman
* knows -> TheFrenchBuiltFrigate
* knows -> TheSistersOfMrGuerin
* knows -> TheDaughter
* knows -> TheAfricanTrader
* knows -> TheWife
* knows -> TheOverseer
* knows -> TheSisters
* knows -> TheMariners
* knows -> TheBoyWhoFought
* knows -> TheDuke
* knows -> TheStrangers
* knows -> MrsDavis
* knows -> TheYoungManWhoLostEye
* knows -> TheAdmiral
* knows -> TheBuyers
* knows -> DoctorBrady
* knows -> TheCrew
* knows -> TheAdmiralCornish
* knows -> ThePlanters
* knows -> DoctorPerkins
* knows -> TheBlackPeople
* knows -> TheAdmiralByng
* knows -> TheOldSlaves
* knows -> Terrylegay
* knows -> CaptainPascal
* knows -> TheWhitePeople
* knows -> TheMerchant
* knows -> TheAfricans
* knows -> MrRead
* knows -> GeorgeWhitfield
* knows -> TheWidow
* knows -> TheBrothers
* knows -> Captain
* knows -> TheSon
* knows -> TheWomen
* knows -> RobertKing
* knows -> TheMaster
* knows -> TheCompanions
* knows -> JosephClipson
* knows -> TheCountrymen
* knows -> TheCrewMembers
* owns -> TheShipIndustriousBee
* owns -> TheShipRoebuck
* owns -> TheShipPreston
* owns -> TheShipRoyalGeorge
* owns -> TheShipNamur
* owns -> TheShipSavage
* worksFor -> RobertKing
* worksFor -> MichaelHenryPascal
* worksFor -> Captain

# GustavusVassa-AdmiralBoscawen [Relationship]

* knows: AdmiralBoscawen
* name: "Gustavus Vassa knows Admiral Boscawen"

# GustavusVassa-Barcelona [Relationship]

* knows: Barcelona
* name: "Gustavus Vassa knows Barcelona"

# GustavusVassa-BasseRoad [Relationship]

* knows: BasseRoad
* name: "Gustavus Vassa knows Basse-road"

# GustavusVassa-Bayonne [Relationship]

* knows: Bayonne
* name: "Gustavus Vassa knows Bayonne"

# GustavusVassa-BelleIsle [Relationship]

* knows: BelleIsle
* name: "Gustavus Vassa knows Belle-Isle"

# GustavusVassa-BishopOfSodorAndMan [Relationship]

* knows: BishopOfSodorAndMan
* name: "Gustavus Vassa knows Bishop of Sodor and Man"

# GustavusVassa-CapeBreton [Relationship]

* knows: CapeBreton
* name: "Gustavus Vassa knows Cape Breton"

# GustavusVassa-CapeLogas [Relationship]

* knows: CapeLogas
* name: "Gustavus Vassa knows Cape Logas"

# GustavusVassa-CaptainClark [Relationship]

* knows: CaptainClark
* name: "Gustavus Vassa knows Captain Clark"

# GustavusVassa-CaptainGeorgeBalfour [Relationship]

* knows: CaptainGeorgeBalfour
* name: "Gustavus Vassa knows Captain George Balfour"

# GustavusVassa-CaptainJamesDoran [Relationship]

* knows: CaptainJamesDoran
* name: "Gustavus Vassa knows Captain James Doran"

# GustavusVassa-CaptainLaforey [Relationship]

* knows: CaptainLaforey
* name: "Gustavus Vassa knows Captain Laforey"

# GustavusVassa-CommodoreKeppel [Relationship]

* knows: CommodoreKeppel
* name: "Gustavus Vassa knows Commodore Keppel"

# GustavusVassa-DanielQueen [Relationship]

* knows: DanielQueen
* name: "Gustavus Vassa knows Daniel Queen"

# GustavusVassa-Deptford [Relationship]

* knows: Deptford
* name: "Gustavus Vassa knows Deptford"

# GustavusVassa-Dick [Relationship]

* knows: Dick
* name: "Gustavus Vassa knows Dick"

# GustavusVassa-GeneralCrawford [Relationship]

* knows: GeneralCrawford
* name: "Gustavus Vassa knows General Crawford"

# GustavusVassa-GeneralWolfe [Relationship]

* knows: GeneralWolfe
* name: "Gustavus Vassa knows General Wolfe"

# GustavusVassa-Gibraltar [Relationship]

* knows: Gibraltar
* name: "Gustavus Vassa knows Gibraltar"

# GustavusVassa-Guernsey [Relationship]

* knows: Guernsey
* name: "Gustavus Vassa knows Guernsey"

# GustavusVassa-GustavusVassaMaster [Relationship]

* name: "Gustavus Vassa owned by and works for his Master"
* owns: GustavusVassaMaster
* worksFor: GustavusVassaMaster

# GustavusVassa-Halifax [Relationship]

* knows: Halifax
* name: "Gustavus Vassa knows Halifax"

# GustavusVassa-JohnMondle [Relationship]

* knows: JohnMondle
* name: "Gustavus Vassa knows John Mondle"

# GustavusVassa-London [Relationship]

* knows: London
* name: "Gustavus Vassa knows London"

# GustavusVassa-Louisbourgh [Relationship]

* knows: Louisbourgh
* name: "Gustavus Vassa knows Louisbourgh"

# GustavusVassa-MissGuerin [Relationship]

* knows: MissGuerin
* name: "Gustavus Vassa knows and is taught by Miss Guerin"
* teacherOf: MissGuerin

# GustavusVassa-MissGuerinEldest [Relationship]

* knows: MissGuerinEldest
* name: "Gustavus Vassa knows Eldest Miss Guerin"

# GustavusVassa-MissGuerins [Relationship]

* memberOf: MissGuerins
* name: "Gustavus Vassa is member of Miss Guerins"

# GustavusVassa-MonsConflans [Relationship]

* knows: MonsConflans
* name: "Gustavus Vassa knows Mons. Conflans"

# GustavusVassa-Portsmouth [Relationship]

* knows: Portsmouth
* name: "Gustavus Vassa knows Portsmouth"

# GustavusVassa-RearAdmiralDurell [Relationship]

* knows: RearAdmiralDurell
* name: "Gustavus Vassa knows Rear-admiral Durell"

# GustavusVassa-RearAdmiralSirCharlesHardy [Relationship]

* knows: RearAdmiralSirCharlesHardy
* name: "Gustavus Vassa knows Rear-admiral Sir Charles Hardy"

# GustavusVassa-Spithead [Relationship]

* knows: Spithead
* name: "Gustavus Vassa knows Spithead"

# GustavusVassa-StHelens [Relationship]

* knows: StHelens
* name: "Gustavus Vassa knows St. Helen's"

# GustavusVassa-StSebastian [Relationship]

* knows: StSebastian
* name: "Gustavus Vassa knows St. Sebastian"

# GustavusVassa-Toulon [Relationship]

* knows: Toulon
* name: "Gustavus Vassa knows Toulon"

# GustavusVassa-Westminster [Relationship]

* knows: Westminster
* name: "Gustavus Vassa knows Westminster"

# GustavusVassaMaster [Person]

* description: "The person who owned the author, sold him to Captain Doran, and treated him with a mix of kindness and cruelty."
* jobTitle: Master
* name: "Gustavus Vassa's Master"

# GustavusVassaMaster-CaptainJamesDoran [Relationship]

* name: "Gustavus Vassa's Master owns/sells to Captain James Doran"
* owns: CaptainJamesDoran

# Halifax [Place]

* description: "A location in America with a commodious harbour called St. George."
* name: Halifax

# HonCaptPhipps [Person]

* description: "Captain on the voyage to the North Pole with Gustavus Vassa and Doctor Irving."
* name: "Hon. Capt. Phipps"
* employs -> DoctorIrving
* employs -> GustavusVassa

# Hope [Place]

* description: "A ship bound from London to Cadiz."
* name: Hope
* type: Place

# Hughes [Person]

* description: "An owner of a sloop who attempted to re-enslave Gustavus Vassa."
* jobTitle: Owner
* knows: GustavusVassa
* knows: CharlesIrving
* name: Hughes

# JHinslow [Person]

* description: "Principal Officer and Commissioner of His Majesty's Navy."
* jobTitle: Commissioner
* knows: GustavusVassa
* name: "J. Hinslow"

# Jamaica [Place]

* description: "An island where Equiano and the Doctor purchased slaves and cultivated land."
* name: Jamaica

# JamesRamsay [Person]

* description: "Reverend; an approved friend, man of virtue, benefactor to mankind."
* knows: RobertKing
* knows: GrenvilleSharp
* knows: ThomasClarkson
* memberOf: BritishLegislature
* name: "James Ramsay"

# JoeDiamond [Person]

* description: "A free negro tailor who accompanied Vassa."
* jobTitle: Taylor
* knows: GustavusVassa
* name: "Joe Diamond"

# JohnAnnis [Person]

* description: "A black man kidnapped from the ship Anglicania, formerly lived with Mr. William Kirkpatrick."
* jobTitle: Cook
* knows: GustavusVassa
* name: "John Annis"
* ownedBy: MrWilliamKirkpatrick
* worksFor: GustavusVassa

# JohnBaker [Person]

* description: "Captain of the sloop Indian Queen who promised Vassa wages but refused to pay them."
* jobTitle: Captain
* knows: GustavusVassa
* name: "John Baker"
* worksFor: GustavusVassa

# JohnBunton [Person]

* description: "Captain of the sloop Speedwell bound for Martinico."
* name: "John Bunton"
* employs -> GustavusVassa

# JohnConstantinePhipps [Person]

* colleague: GustavusVassa
* description: "Commander of the expedition to the North Pole, later Lord Mulgrave."
* jobTitle: Commander
* name: "Honourable John Constantine Phipps"
* worksFor: GustavusVassa

# JohnJolly [Person]

* colleague: GustavusVassa
* description: "Master of the ship Delawar, described as neat, smart, and good-humoured."
* jobTitle: Master
* name: "John Jolly"
* worksFor: GustavusVassa

# JohnMondle [Person]

* description: "A gunner on the Ætna who had a religious experience and narrowly escaped death in a collision."
* jobTitle: Gunner
* name: "John Mondle"

# JosephClipson [Person]

* description: "A free young mulatto-man who was forcibly taken into slavery by a Bermudas captain."
* name: "Joseph Clipson"

# LadyInGosport [Person]

* description: "A lady who lived in Gosport and was once intimate with the author's former master."
* knows: FormerMaster
* knows: OlaudahEquiano
* name: "Lady in Gosport"

# LeutMatthew [Person]

* description: "Author of a Voyage cited in footnotes."
* name: "Leut. Matthew"

# Lieutenant [Person]

* description: "An officer who was in a boat with the author when Mr. Mondle searched the ship."
* name: Lieutenant

# London [Place]

* description: "A city where natives of Eboe were present."
* description: "A city in England, a frequent port of call."
* description: "A city in England where the author was taken and where he later saw Emanuel Sankey."
* description: "A city the author visited with his master."
* name: London

# Louisbourgh [Place]

* description: "A town in Cape Breton attacked by the English forces."
* name: Louisbourgh

# Malaga [Place]

* description: "A city in Spain with a fine cathedral."
* name: Malaga

# MartinHopkin [Person]

* description: "Captain of the ship London."
* jobTitle: Captain
* name: "Martin Hopkin"
* worksFor: GustavusVassa

# Martinico [Place]

* description: "An island where a French planter had mulattoes working."
* name: Martinico

# Mate [Person]

* description: "The sickly mate on the vessel who served under the Captain and worked alongside Gustavus Vassa."
* name: Mate
* colleague -> GustavusVassa
* worksFor -> Captain

# MattMacnamara [Person]

* description: "Governor who wrote a letter supporting Vassa's mission."
* jobTitle: Governor
* knows: GustavusVassa
* knows: BishopOfLondon
* name: "Matt Macnamara"

# MichaelHenryPascal


# MissGuerin [Person]

* description: "One of the Miss Guerins who treated the author with kindness, insisted on his baptism, and stood as godmother."
* jobTitle: Patroness
* name: "Miss Guerin"

# MissGuerinEldest [Person]

* description: "The eldest Miss Guerin, with whom the author became a favourite, who insisted on his baptism."
* jobTitle: Patroness
* name: "Eldest Miss Guerin"

# MissGuerins [Organization Person]

* description: "The family of ladies who hosted the author, sent him to school, and insisted on his baptism."
* description: "Kind ladies in Greenwich who were cousins to Capt. Pascal and helped Gustavus Vassa find employment."
* jobTitle: Ladies
* jobTitle: Family/Patrons
* knows: CaptPascal
* knows: GustavusVassa
* name: "Miss Guerins"

# MonsConflans [Person]

* description: "Commander of the French squadron encountered by the author's fleet."
* jobTitle: Commander
* name: "Mons. Conflans"

# Montserrat [Place]

* description: "An island in the West Indies where the narrator lived and was freed."
* description: "An island in the West Indies where the author was sold to Mr. King."
* name: Montserrat
* locationOf -> GustavusVassa
* locationOf -> Captain
* locationOf -> RobertKing

# MorningStar [Place]

* description: "A sloop owned by Doctor Irving, captained by David Miller."
* name: "Morning Star"

# Mosa [Person]

* description: "A black man and friend of Gustavus Vassa in Savannah."
* name: Mosa
* knows -> GustavusVassa

# MosquitoShore [Place]

* description: "A location where Equiano and the Doctor established a plantation."
* name: "Mosquito Shore"

# MotherOfEquiano [Person]

* description: "Olaudah Equiano's mother, who attended to his upbringing and made oblations at her own mother's tomb."
* name: MotherOfEquiano
* parent -> OlaudahEquiano

# MrC [Person]

* description: "An old sea-faring man and Christian who guided Gustavus Vassa in his religious conversion."
* jobTitle: "Silk Weaver"
* knows: GustavusVassa
* name: "Mr. C----"

# MrCochran [Person]

* description: "A man indebted to Joe Diamond."
* jobTitle: Debtor
* knows: JoeDiamond
* name: "Mr Cochran"

# MrCox [Person]

* description: "A carpenter on board the sloop who knew Dr. Irving and advocated for Vassa."
* jobTitle: Carpenter
* knows: GustavusVassa
* knows: CharlesIrving
* name: "Mr Cox"

# MrDixon [Person]

* description: "A gentleman who lodged with the Captain and helped hide Gustavus Vassa from Mr. Read."
* name: "Mr. Dixon"
* knows -> GustavusVassa
* knows -> Captain

# MrDubury [Person]

* description: "A gentleman in Montserrat known for humane treatment of slaves."
* name: "Mr. Dubury"

# MrGS [Person]

* description: "The governor of Tothil-fields Bridewell, a religious friend who advised Equiano."
* knows: Equiano
* name: "Mr. G.S."
* worksFor: TothilFieldsBridewell

# MrGSworksForTothilFieldsBridewell [Relationship]

* name: "MrGS worksFor TothilFieldsBridewell"
* object: TothilFieldsBridewell
* predicate: worksFor
* subject: MrGS

# MrGuerin


# MrJamesTobin [Person]

* description: "A zealous labourer in the vineyard of slavery who gave an account of a French planter."
* name: "Mr. James Tobin"

# MrKing [Organization Person]

* description: "The owner of the vessel and a benefactor/friend to Gustavus Vassa."
* description: "The mercantile house in Philadelphia with which Mr. Robert King was connected."
* memberOf: MrKing
* name: "Mr. King"
* employs -> WilliamPhillips
* knows -> GustavusVassa

# MrLd [Person]

* description: "A clerk in a chapel who served as Equiano's interpreter and friend regarding religious matters."
* knows: Equiano
* name: "Mr. L----d"
* worksFor: Chapel

# MrMIntosh [Person]

* description: "A justice of the peace to whom Gustavus Vassa complained about a non-paying customer."
* jobTitle: "Justice of the Peace"
* knows: GustavusVassa
* name: "Mr. M'Intosh"

# MrMansfield [Person]

* description: "Chief mate of the Charming Sally."
* jobTitle: "Chief Mate"
* name: "Mr Mansfield"
* colleague -> CaptainDoran
* colleague -> OlaudahEquiano

# MrMondle [Person]

* description: "An officer who believed the author was on the ship when he was actually in a boat."
* name: "Mr. Mondle"

# MrP [Person]

* description: "A preacher at Westminster chapel who delivered a sermon on Lam. iii. 39."
* knows: Equiano
* name: "Rev. Mr. P----"
* worksFor: WestminsterChapel

# MrPworksForWestminsterChapel [Relationship]

* name: "MrP worksFor WestminsterChapel"
* object: WestminsterChapel
* predicate: worksFor
* subject: MrP

# MrRead [Person]

* description: "A merchant of Savannah."
* description: "A spiteful man who owned a slave that struck Gustavus Vassa; attempted to have Vassa flogged."
* name: "Mr. Read"
* owns -> NegroSlave

# MrRobertKing [Person]

* description: "A Quaker and the first merchant in Montserrat, who bought the author."
* name: "Mr. Robert King"
* owns: OlaudahEquiano
* worksFor: OlaudahEquiano

# MrRomaine [Person]

* description: "A preacher known for his great knowledge in the scriptures."
* knows: Equiano
* name: "Reverend Mr. Romaine"
* worksFor: BlackfriarsChurch

# MrRomaineworksForBlackfriarsChurch [Relationship]

* name: "MrRomaine worksFor BlackfriarsChurch"
* object: BlackfriarsChurch
* predicate: worksFor
* subject: MrRomaine

# MrTClarkson [Person]

* description: "Author of 'Essay on the Slavery and Commerce of the Human Species'."
* jobTitle: Author
* name: "Mr. T. Clarkson"
* colleague -> DrMitchel

# MrWilliamKirkpatrick [Person]

* description: "A gentleman from St. Kitts who kidnapped John Annis."
* jobTitle: Gentleman
* knows: JohnAnnis
* name: "Mr. William Kirkpatrick"
* owns: JohnAnnis

# MrsDavis [Person]

* description: "A wise woman in Philadelphia who revealed secrets and foretold events."
* name: "Mrs. Davis"

# MusquitoKing [Person]

* description: "The king of the Musquito people."
* knows: George
* name: "Musquito king"

# NegroSlave [Person]

* description: "A slave owned by Mr. Read who struck Gustavus Vassa."
* name: "Negro Slave"

# OlaudahEquiano [Person]

* description: "The author of the narrative, born in Eboe in 1745, later kidnapped and enslaved."
* description: "The author of the narrative, a slave who was sold to Mr. King and later became a merchant."
* name: "Olaudah Equiano"
* colleague -> MrMansfield
* colleague -> CaptainDoran
* parent -> Embrenche
* parent -> MotherOfEquiano
* sibling -> SisterOfEquiano

# OldShipmates [Person]

* description: "The author's former shipmates who sent him oranges and tokens of regard."
* knows: OlaudahEquiano
* name: "Old Shipmates"

# Overseeer [Person]

* description: "A cruel overseer whom a negro man attempted to poison."
* name: Overseer

# Philadelphia [Place]

* description: "A town in America where the narrator traded and met Mrs. Davis."
* description: "A city in America where Mr. Robert King lived and was going soon."
* name: Philadelphia
* locationOf -> GeorgeWhitfield
* locationOf -> MrsDavis
* locationOf -> GustavusVassa

# Portsmouth [Place]

* description: "A location where the ship waited for the West India convoy."
* description: "A harbour where ships went to refit."
* name: Portsmouth

# RearAdmiralDurell [Person]

* description: "A rear-admiral left behind with ships after Admiral Boscawen sailed."
* jobTitle: Rear-Admiral
* name: "Rear-admiral Durell"

# RearAdmiralSirCharlesHardy [Person]

* description: "A rear-admiral left behind with ships after Admiral Boscawen sailed."
* jobTitle: Rear-Admiral
* name: "Rear-admiral Sir Charles Hardy"

# RevMrGregory [Person]

* description: "A gentleman who kept an academy and taught Gustavus Vassa arithmetic."
* jobTitle: Teacher
* name: "Rev. Mr. Gregory"
* teacherOf: GustavusVassa

# RichardBaker


# RobertKing [Person]

* description: "A merchant in Montserrat who owned Gustavus Vassa and granted him manumission."
* description: "Gustavus Vassa's former master who provided a certificate of good behavior."
* description: "The author of the narrative, who was unwilling and unable to adorn the plainness of truth."
* jobTitle: "Merchant, Master"
* jobTitle: Master
* knows: ThomasClarkson
* knows: JamesRamsay
* knows: GrenvilleSharp
* name: "Robert King"
* owns: GustavusVassa
* worksFor: GustavusVassa
* employs -> GustavusVassa
* grantsManumission -> GustavusVassa
* owns -> GustavusVassa

# Sailor [Person]

* description: "A sailor on board who took a guinea from the author promising to get him a boat."
* name: Sailor

# SantaCruz [Place]

* description: "An island where the author and Emanuel Sankey went to sell fruits."
* name: "Santa Cruz"

# Savannah [Place]

* description: "A location where the author was nearly murdered by Doctor Perkins."
* description: "A town in Georgia where the narrator was attacked by Doctor Perkins."
* name: Savannah
* locationOf -> MrRead
* locationOf -> DoctorBrady
* locationOf -> DoctorPerkins

# SirPhilipGibbes [Person]

* description: "A native of Barbadoes with estates there, who wrote a treatise on the usage of his slaves."
* name: "Sir Philip Gibbes"

# SisterOfEquiano [Person]

* description: "Olaudah Equiano's sister, the only daughter in his immediate family, kidnapped and separated from him."
* name: SisterOfEquiano
* sibling -> OlaudahEquiano

# Spain [Place]

* description: "A country in Europe."
* name: Spain

# Spithead [Place]

* description: "A location where the fleet stayed for a short time before Portsmouth."
* name: Spithead

# StEustatia [Place]

* description: "An island where a depredator bought goods from the author."
* description: "An island where the narrator discharged cargo and took in slaves."
* name: "St. Eustatia"
* locationOf -> GustavusVassa

# StHelens [Place]

* description: "A location where the fleet arrived at the close of 1758-9."
* name: "St. Helen's"

# StKitts [Place]

* description: "An island where slaves were commonly branded."
* name: "St. Kitt's"

# StSebastian [Place]

* description: "A location in Spain the ship was sent to."
* name: "St. Sebastian"

# Stoker [Person]

* description: "A white pilot on the Indian Queen who was abused by Captain Baker."
* jobTitle: Pilot
* knows: JohnBaker
* knows: GustavusVassa
* name: Stoker

# Terrylegay [Person]

* description: "The Register in Montserrat who drew up the narrator's manumission."
* name: Terrylegay
* registers -> GustavusVassa

# TheAdmiral


# TheAdmiralByng


# TheAdmiralCornish


# TheAfricanTrader


# TheAfricans


# TheBlackPeople


# TheBlackWoman


# TheBoy


# TheBoyWhoFought


# TheBrothers


# TheBuyers


# TheCaptain


# TheCompanions


# TheCountrymen


# TheCrew


# TheCrewMembers


# TheDaughter


# TheDaughterOfGentleman


# TheDoctors


# TheDuke


# TheElderlyBlackMan


# TheFrenchBuiltFrigate


# TheFriendsOrQuakers [Organization]

* description: "A religious group in London that Vassa thanked for their benevolence."
* knows: GustavusVassa
* name: "The Friends or Quakers"

# TheGentleman


# TheGentlemanInFalmouth


# TheGentlemanInVirginia


# TheLittleDaughterOfMateInGuernsey


# TheMariners


# TheMaster


# TheMate


# TheMateInGuernsey


# TheMerchant


# TheOldSlaves


# TheOverseer


# ThePlanters


# TheQueen [Person]

* description: "The British Queen to whom Vassa presented a petition."
* jobTitle: Queen
* knows: GustavusVassa
* name: "The Queen"

# TheShipIndustriousBee


# TheShipNamur


# TheShipPreston


# TheShipRoebuck


# TheShipRoyalGeorge


# TheShipSavage


# TheSisters


# TheSistersOfMrGuerin


# TheSon


# TheStrangers


# TheWhiteMen


# TheWhitePeople


# TheWidow


# TheWife


# TheWifeOfMateInGuernsey


# TheWomen


# TheYoungLadDick


# TheYoungManWhoLostEye


# ThomasClarkson [Person]

* description: "Reverend; an approved friend, man of virtue, benefactor to mankind."
* knows: GrenvilleSharp
* knows: JamesRamsay
* knows: RobertKing
* memberOf: BritishLegislature
* name: "Thomas Clarkson"

# ThomasWallace [Person]

* description: "A doctor who resided in Africa and supported Vassa's mission."
* jobTitle: Doctor
* knows: GustavusVassa
* knows: BishopOfLondon
* name: "Thomas Wallace"

# TothilFieldsBridewell [Organization]

* description: "A prison/governorship where Mr. G.S. served."
* name: "Tothil-fields Bridewell"

# Toulon [Place]

* description: "A location off which the fleet cruised to intercept French ships."
* name: Toulon

# WPalmer [Person]

* description: "Principal Officer and Commissioner of His Majesty's Navy."
* jobTitle: Commissioner
* knows: GustavusVassa
* name: "W. Palmer"

# WestIndies [Place]

* description: "The region where slaves were sold and where the Charming Sally operated."
* name: "West Indies"

# Westminster [Place]

* description: "Location of St. Margaret's church where the author was baptized."
* name: Westminster

# WestminsterChapel [Organization]

* description: "A chapel where Equiano attended services and was examined."
* name: "Westminster chapel"

# WhiteMan [Person]

* description: "A white man who bought a boat for a negro-man."
* name: "White Man"

# WilliamPhillips [Person]

* description: "A new captain appointed by Mr. King, an old acquaintance of Gustavus Vassa."
* name: "William Phillips"
* colleague -> GustavusVassa
* worksFor -> MrKing

