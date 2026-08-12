# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The author and narrator of the narrative, formerly enslaved, later gained freedom.
* jobTitle: Sailor, Steward, Author

# GeneralWolfe [Person]
* name: General Wolfe
* description: A gallant general who was on board the author's ship.
* jobTitle: General

# CaptainGeorgeBalfour [Person]
* name: Captain George Balfour
* description: Captain of the Ætna fire-ship, who noticed and liked the author.
* jobTitle: Captain

# CaptainLaforey [Person]
* name: Captain Laforey
* description: A junior captain who served alongside Captain George Balfour.
* jobTitle: Captain

# AdmiralBoscawen [Person]
* name: Admiral Boscawen
* description: The admiral who commanded the fleet and sailed for England.
* jobTitle: Admiral

# RearAdmiralSirCharlesHardy [Person]
* name: Rear-admiral Sir Charles Hardy
* description: A rear-admiral left behind with ships after Admiral Boscawen sailed.
* jobTitle: Rear-Admiral

# RearAdmiralDurell [Person]
* name: Rear-admiral Durell
* description: A rear-admiral left behind with ships after Admiral Boscawen sailed.
* jobTitle: Rear-Admiral

# MonsConflans [Person]
* name: Mons. Conflans
* description: Commander of the French squadron encountered by the author's fleet.
* jobTitle: Commander

# MissGuerin [Person]
* name: Miss Guerin
* description: One of the Miss Guerins who treated the author with kindness, insisted on his baptism, and stood as godmother.
* jobTitle: Patroness

# MissGuerinEldest [Person]
* name: Eldest Miss Guerin
* description: The eldest Miss Guerin, with whom the author became a favourite, who insisted on his baptism.
* jobTitle: Patroness

# BishopOfSodorAndMan [Person]
* name: Bishop of Sodor and Man
* description: Author of the book 'Guide to the Indians' given to the author.
* jobTitle: Bishop

# Dick [Person]
* name: Dick
* description: The author's old companion who died while on the Preston.
* jobTitle: Companion

# JohnMondle [Person]
* name: John Mondle
* description: A gunner on the Ætna who had a religious experience and narrowly escaped death in a collision.
* jobTitle: Gunner

# CaptainClark [Person]
* name: Captain Clark
* description: Captain of the Lynne, which collided with the Ætna.
* jobTitle: Captain

# GeneralCrawford [Person]
* name: General Crawford
* description: A general taken prisoner during the landing at Belle-Isle.
* jobTitle: General

# CommodoreKeppel [Person]
* name: Commodore Keppel
* description: Commodore who commanded the fleet destined against Belle-Isle.
* jobTitle: Commodore

# DanielQueen [Person]
* name: Daniel Queen
* description: A man who messed with the author on the Ætna, taught him to shave and read, and was like a father to him.
* jobTitle: Captain's Clerk/Attendant

# CaptainJamesDoran [Person]
* name: Captain James Doran
* description: Captain of the Charming Sally, who bought the author from his master.
* jobTitle: Captain

# GustavusVassaMaster [Person]
* name: Gustavus Vassa's Master
* description: The person who owned the author, sold him to Captain Doran, and treated him with a mix of kindness and cruelty.
* jobTitle: Master

# MissGuerins [Organization]
* name: Miss Guerins
* description: The family of ladies who hosted the author, sent him to school, and insisted on his baptism.
* jobTitle: Family/Patrons

# Halifax [Place]
* name: Halifax
* description: A location in America with a commodious harbour called St. George.

# CapeBreton [Place]
* name: Cape Breton
* description: A location in Nova Scotia where the fleet arrived in 1758.

# Louisbourgh [Place]
* name: Louisbourgh
* description: A town in Cape Breton attacked by the English forces.

# StHelens [Place]
* name: St. Helen's
* description: A location where the fleet arrived at the close of 1758-9.

# Spithead [Place]
* name: Spithead
* description: A location where the fleet stayed for a short time before Portsmouth.

# Portsmouth [Place]
* name: Portsmouth
* description: A harbour where ships went to refit.

# London [Place]
* name: London
* description: A city the author visited with his master.

# Westminster [Place]
* name: Westminster
* description: Location of St. Margaret's church where the author was baptized.

# Gibraltar [Place]
* name: Gibraltar
* description: A Spanish sea-port where the fleet stopped in the Mediterranean.

# Barcelona [Place]
* name: Barcelona
* description: A Spanish sea-port known for silk manufactures.

# Toulon [Place]
* name: Toulon
* description: A location off which the fleet cruised to intercept French ships.

# CapeLogas [Place]
* name: Cape Logas
* description: A coast in Portugal where French ships ran ashore.

# BelleIsle [Place]
* name: Belle-Isle
* description: An island attacked by the English fleet.

# BasseRoad [Place]
* name: Basse-road
* description: A location where the fleet blocked up a French fleet.

# StSebastian [Place]
* name: St. Sebastian
* description: A location in Spain the ship was sent to.

# Bayonne [Place]
* name: Bayonne
* description: A location in France the ship was sent to as a cartel.

# Guernsey [Place]
* name: Guernsey
* description: A location the ship went to in September.

# Deptford [Place]
* name: Deptford
* description: A location on the Thames where the ship arrived to be paid off.

# GustavusVassa-GustavusVassaMaster [Relationship]
* name: Gustavus Vassa owned by and works for his Master
* owns: GustavusVassaMaster
* worksFor: GustavusVassaMaster

# GustavusVassa-GeneralWolfe [Relationship]
* name: Gustavus Vassa knows General Wolfe
* knows: GeneralWolfe

# GustavusVassa-CaptainGeorgeBalfour [Relationship]
* name: Gustavus Vassa knows Captain George Balfour
* knows: CaptainGeorgeBalfour

# CaptainGeorgeBalfour-CaptainLaforey [Relationship]
* name: Captain George Balfour is colleague of Captain Laforey
* colleague: CaptainLaforey

# GustavusVassa-AdmiralBoscawen [Relationship]
* name: Gustavus Vassa knows Admiral Boscawen
* knows: AdmiralBoscawen

# AdmiralBoscawen-RearAdmiralSirCharlesHardy [Relationship]
* name: Admiral Boscawen is colleague of Rear-admiral Sir Charles Hardy
* colleague: RearAdmiralSirCharlesHardy

# AdmiralBoscawen-RearAdmiralDurell [Relationship]
* name: Admiral Boscawen is colleague of Rear-admiral Durell
* colleague: RearAdmiralDurell

# GustavusVassa-MissGuerin [Relationship]
* name: Gustavus Vassa knows and is taught by Miss Guerin
* knows: MissGuerin
* teacherOf: MissGuerin

# GustavusVassa-MissGuerinEldest [Relationship]
* name: Gustavus Vassa knows Eldest Miss Guerin
* knows: MissGuerinEldest

# GustavusVassa-Dick [Relationship]
* name: Gustavus Vassa knows Dick
* knows: Dick

# GustavusVassa-JohnMondle [Relationship]
* name: Gustavus Vassa knows John Mondle
* knows: JohnMondle

# GustavusVassa-DanielQueen [Relationship]
* name: Gustavus Vassa knows Daniel Queen
* knows: DanielQueen

# GustavusVassa-CaptainJamesDoran [Relationship]
* name: Gustavus Vassa knows Captain James Doran
* knows: CaptainJamesDoran

# GustavusVassaMaster-CaptainJamesDoran [Relationship]
* name: Gustavus Vassa's Master owns/sells to Captain James Doran
* owns: CaptainJamesDoran

# GustavusVassa-CaptainClark [Relationship]
* name: Gustavus Vassa knows Captain Clark
* knows: CaptainClark

# GustavusVassa-GeneralCrawford [Relationship]
* name: Gustavus Vassa knows General Crawford
* knows: GeneralCrawford

# GustavusVassa-CommodoreKeppel [Relationship]
* name: Gustavus Vassa knows Commodore Keppel
* knows: CommodoreKeppel

# GustavusVassa-MissGuerins [Relationship]
* name: Gustavus Vassa is member of Miss Guerins
* memberOf: MissGuerins

# GustavusVassa-BishopOfSodorAndMan [Relationship]
* name: Gustavus Vassa knows Bishop of Sodor and Man
* knows: BishopOfSodorAndMan

# GustavusVassa-MonsConflans [Relationship]
* name: Gustavus Vassa knows Mons. Conflans
* knows: MonsConflans

# GustavusVassa-CaptainLaforey [Relationship]
* name: Gustavus Vassa knows Captain Laforey
* knows: CaptainLaforey

# GustavusVassa-RearAdmiralSirCharlesHardy [Relationship]
* name: Gustavus Vassa knows Rear-admiral Sir Charles Hardy
* knows: RearAdmiralSirCharlesHardy

# GustavusVassa-RearAdmiralDurell [Relationship]
* name: Gustavus Vassa knows Rear-admiral Durell
* knows: RearAdmiralDurell

# GustavusVassa-BasseRoad [Relationship]
* name: Gustavus Vassa knows Basse-road
* knows: BasseRoad

# GustavusVassa-StSebastian [Relationship]
* name: Gustavus Vassa knows St. Sebastian
* knows: StSebastian

# GustavusVassa-Bayonne [Relationship]
* name: Gustavus Vassa knows Bayonne
* knows: Bayonne

# GustavusVassa-Guernsey [Relationship]
* name: Gustavus Vassa knows Guernsey
* knows: Guernsey

# GustavusVassa-Deptford [Relationship]
* name: Gustavus Vassa knows Deptford
* knows: Deptford

# GustavusVassa-Halifax [Relationship]
* name: Gustavus Vassa knows Halifax
* knows: Halifax

# GustavusVassa-CapeBreton [Relationship]
* name: Gustavus Vassa knows Cape Breton
* knows: CapeBreton

# GustavusVassa-Louisbourgh [Relationship]
* name: Gustavus Vassa knows Louisbourgh
* knows: Louisbourgh

# GustavusVassa-StHelens [Relationship]
* name: Gustavus Vassa knows St. Helen's
* knows: StHelens

# GustavusVassa-Spithead [Relationship]
* name: Gustavus Vassa knows Spithead
* knows: Spithead

# GustavusVassa-Portsmouth [Relationship]
* name: Gustavus Vassa knows Portsmouth
* knows: Portsmouth

# GustavusVassa-London [Relationship]
* name: Gustavus Vassa knows London
* knows: London

# GustavusVassa-Westminster [Relationship]
* name: Gustavus Vassa knows Westminster
* knows: Westminster

# GustavusVassa-Gibraltar [Relationship]
* name: Gustavus Vassa knows Gibraltar
* knows: Gibraltar

# GustavusVassa-Barcelona [Relationship]
* name: Gustavus Vassa knows Barcelona
* knows: Barcelona

# GustavusVassa-Toulon [Relationship]
* name: Gustavus Vassa knows Toulon
* knows: Toulon

# GustavusVassa-CapeLogas [Relationship]
* name: Gustavus Vassa knows Cape Logas
* knows: CapeLogas

# GustavusVassa-BelleIsle [Relationship]
* name: Gustavus Vassa knows Belle-Isle
* knows: BelleIsle