# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The narrator and author of the narrative, formerly a slave, later a free man, steward, and Christian convert.
* worksFor: RobertKing
* worksFor: CaptPascal
* worksFor: CaptOHara
* worksFor: DrCharlesIrving
* worksFor: JohnJolly
* worksFor: CaptWmRobertson
* worksFor: CaptainDavidWatt
* worksFor: JohnConstantinePhipps
* worksFor: CaptainLutwidge
* worksFor: CaptainJohnHughes
* worksFor: CaptLinna
* knows: MissGuerins
* knows: CaptPascal
* knows: CaptOHara
* knows: DrCharlesIrving
* knows: JohnAnnis
* knows: GranvilleSharp
* knows: MrC

# RobertKing [Person]
* name: Robert King
* jobTitle: Master
* description: Gustavus Vassa's former master who provided a certificate of good behavior.
* owns: GustavusVassa
* worksFor: GustavusVassa

# CaptJohnHamer [Person]
* name: Capt. John Hamer
* jobTitle: Captain
* description: Captain of the ship Andromache, with whom Gustavus Vassa traveled to London.
* colleague: GustavusVassa

# MissGuerins [Person]
* name: Miss Guerins
* jobTitle: Ladies
* description: Kind ladies in Greenwich who were cousins to Capt. Pascal and helped Gustavus Vassa find employment.
* knows: GustavusVassa
* knows: CaptPascal

# CaptPascal [Person]
* name: Capt. Pascal
* jobTitle: Captain
* description: Cousin of the Miss Guerins, former master of Gustavus Vassa, who treated him ill and withheld prize money.
* owns: GustavusVassa
* knows: GustavusVassa
* knows: MissGuerins

# CaptOHara [Person]
* name: Capt. O'Hara
* jobTitle: Captain
* description: A gentleman who treated Gustavus Vassa with kindness and recommended him to a hair-dresser.
* knows: GustavusVassa

# RevMrGregory [Person]
* name: Rev. Mr. Gregory
* jobTitle: Teacher
* description: A gentleman who kept an academy and taught Gustavus Vassa arithmetic.
* teacherOf: GustavusVassa

# DrCharlesIrving [Person]
* name: Dr. Charles Irving
* jobTitle: Master
* description: A gentleman celebrated for experiments in making sea water fresh, who employed Gustavus Vassa as a hairdresser and later on an expedition.
* worksFor: GustavusVassa
* knows: GustavusVassa

# JohnJolly [Person]
* name: John Jolly
* jobTitle: Master
* description: Master of the ship Delawar, described as neat, smart, and good-humoured.
* worksFor: GustavusVassa
* colleague: GustavusVassa

# CaptWmRobertson [Person]
* name: Capt. Wm. Robertson
* jobTitle: Captain
* description: Captain of the ship Grenada Planter.
* worksFor: GustavusVassa
* colleague: GustavusVassa

# MrMIntosh [Person]
* name: Mr. M'Intosh
* jobTitle: Justice of the Peace
* description: A justice of the peace to whom Gustavus Vassa complained about a non-paying customer.
* knows: GustavusVassa

# CaptainDavidWatt [Person]
* name: Captain David Watt
* jobTitle: Captain
* description: Captain of the ship Jamaica.
* worksFor: GustavusVassa
* colleague: GustavusVassa

# JohnConstantinePhipps [Person]
* name: Honourable John Constantine Phipps
* jobTitle: Commander
* description: Commander of the expedition to the North Pole, later Lord Mulgrave.
* worksFor: GustavusVassa
* colleague: GustavusVassa

# CaptainLutwidge [Person]
* name: Captain Lutwidge
* jobTitle: Captain
* description: Captain of the sloop Carcass, which joined Phipps' expedition.
* colleague: GustavusVassa
* colleague: JohnConstantinePhipps

# CaptainJohnHughes [Person]
* name: Captain John Hughes
* jobTitle: Captain
* description: Commander of the ship Anglicania, bound for Smyrna.
* worksFor: GustavusVassa
* knows: JohnAnnis

# JohnAnnis [Person]
* name: John Annis
* jobTitle: Cook
* description: A black man kidnapped from the ship Anglicania, formerly lived with Mr. William Kirkpatrick.
* worksFor: GustavusVassa
* knows: GustavusVassa
* ownedBy: MrWilliamKirkpatrick

# MrWilliamKirkpatrick [Person]
* name: Mr. William Kirkpatrick
* jobTitle: Gentleman
* description: A gentleman from St. Kitts who kidnapped John Annis.
* owns: JohnAnnis
* knows: JohnAnnis

# GranvilleSharp [Person]
* name: Granville Sharp, Esq.
* jobTitle: Philanthropist
* description: A philanthropist who advised Gustavus Vassa on how to procure John Annis's freedom.
* knows: GustavusVassa

# CaptLinna [Person]
* name: Capt. Linna
* jobTitle: Captain
* description: Captain of the Turkeyman Wester Hall.
* worksFor: GustavusVassa

# MrC [Person]
* name: Mr. C----
* jobTitle: Silk Weaver
* description: An old sea-faring man and Christian who guided Gustavus Vassa in his religious conversion.
* knows: GustavusVassa