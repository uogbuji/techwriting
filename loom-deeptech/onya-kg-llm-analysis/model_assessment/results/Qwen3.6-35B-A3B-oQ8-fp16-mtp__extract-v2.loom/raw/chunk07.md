# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# Equiano [Person]
* name: Equiano
* description: The author of the narrative, formerly enslaved, later a free man and Christian convert.

# MrLd [Person]
* name: Mr. L----d
* description: A clerk in a chapel who served as Equiano's interpreter and friend regarding religious matters.
* worksFor: Chapel
* knows: Equiano

# MrP [Person]
* name: Rev. Mr. P----
* description: A preacher at Westminster chapel who delivered a sermon on Lam. iii. 39.
* worksFor: WestminsterChapel
* knows: Equiano

# CaptainRichardStrange [Person]
* name: Capt. Richard Strange
* description: Captain of the ship Hope.
* owns: Hope
* employs: Equiano
* knows: Equiano

# MrGS [Person]
* name: Mr. G.S.
* description: The governor of Tothil-fields Bridewell, a religious friend who advised Equiano.
* worksFor: TothilFieldsBridewell
* knows: Equiano

# MrRomaine [Person]
* name: Reverend Mr. Romaine
* description: A preacher known for his great knowledge in the scriptures.
* worksFor: BlackfriarsChurch
* knows: Equiano

# DoctorIrving [Person]
* name: Doctor Irving
* description: A friend and employer who engaged Equiano for a plantation venture.
* owns: MorningStar
* employs: Equiano
* knows: Equiano

# CaptainDavidMiller [Person]
* name: Captain David Miller
* description: Captain of the sloop Morning Star.
* owns: MorningStar
* employs: Equiano
* knows: Equiano

# George [Person]
* name: George
* description: The Musquito king's son, an Indian prince baptized in England.
* knows: Equiano

# FatherVincent [Person]
* name: Father Vincent
* description: A Catholic priest Equiano disputed with in Malaga.
* knows: Equiano

# CaptainPlasmyah [Person]
* name: Captain Plasmyah
* description: A friendly chief and neighbor of Equiano and the Doctor.
* knows: Equiano

# MusquitoKing [Person]
* name: Musquito king
* description: The king of the Musquito people.
* knows: George

# Hope [Place]
* name: Hope
* description: A ship bound from London to Cadiz.
* type: Place

# WestminsterChapel [Organization]
* name: Westminster chapel
* description: A chapel where Equiano attended services and was examined.

# TothilFieldsBridewell [Organization]
* name: Tothil-fields Bridewell
* description: A prison/governorship where Mr. G.S. served.

# BlackfriarsChurch [Organization]
* name: Blackfriars church
* description: A church in London where Equiano heard Mr. Romaine preach.

# Cadiz [Place]
* name: Cadiz
* description: A port city in Spain.

# Malaga [Place]
* name: Malaga
* description: A city in Spain with a fine cathedral.

# Jamaica [Place]
* name: Jamaica
* description: An island where Equiano and the Doctor purchased slaves and cultivated land.

# MosquitoShore [Place]
* name: Mosquito Shore
* description: A location where Equiano and the Doctor established a plantation.

# London [Place]
* name: London
* description: A city in England, a frequent port of call.

# Spain [Place]
* name: Spain
* description: A country in Europe.

# England [Place]
* name: England
* description: A country in Europe.

# MorningStar [Place]
* name: Morning Star
* description: A sloop owned by Doctor Irving, captained by David Miller.

# EquianoknowsMrLd [Relationship]
* name: Equiano knows MrLd
* subject: Equiano
* predicate: knows
* object: MrLd

# EquianoknowsMrP [Relationship]
* name: Equiano knows MrP
* subject: Equiano
* predicate: knows
* object: MrP

# EquianoworksForCaptainRichardStrange [Relationship]
* name: Equiano worksFor CaptainRichardStrange
* subject: Equiano
* predicate: worksFor
* object: CaptainRichardStrange

# EquianoknowsMrGS [Relationship]
* name: Equiano knows MrGS
* subject: Equiano
* predicate: knows
* object: MrGS

# EquianoknowsMrRomaine [Relationship]
* name: Equiano knows MrRomaine
* subject: Equiano
* predicate: knows
* object: MrRomaine

# EquianoworksForDoctorIrving [Relationship]
* name: Equiano worksFor DoctorIrving
* subject: Equiano
* predicate: worksFor
* object: DoctorIrving

# EquianoworksForCaptainDavidMiller [Relationship]
* name: Equiano worksFor CaptainDavidMiller
* subject: Equiano
* predicate: worksFor
* object: CaptainDavidMiller

# EquianoknowsGeorge [Relationship]
* name: Equiano knows George
* subject: Equiano
* predicate: knows
* object: George

# EquianoknowsFatherVincent [Relationship]
* name: Equiano knows FatherVincent
* subject: Equiano
* predicate: knows
* object: FatherVincent

# EquianoknowsCaptainPlasmyah [Relationship]
* name: Equiano knows CaptainPlasmyah
* subject: Equiano
* predicate: knows
* object: CaptainPlasmyah

# EquianoknowsMusquitoKing [Relationship]
* name: Equiano knows MusquitoKing
* subject: Equiano
* predicate: knows
* object: MusquitoKing

# CaptainRichardStrangeownsHope [Relationship]
* name: CaptainRichardStrange owns Hope
* subject: CaptainRichardStrange
* predicate: owns
* object: Hope

# DoctorIrvingownsMorningStar [Relationship]
* name: DoctorIrving owns MorningStar
* subject: DoctorIrving
* predicate: owns
* object: MorningStar

# CaptainDavidMillerownsMorningStar [Relationship]
* name: CaptainDavidMiller owns MorningStar
* subject: CaptainDavidMiller
* predicate: owns
* object: MorningStar

# DoctorIrvingemploysEquiano [Relationship]
* name: DoctorIrving employs Equiano
* subject: DoctorIrving
* predicate: employs
* object: Equiano

# CaptainDavidMillereemploysEquiano [Relationship]
* name: CaptainDavidMiller employs Equiano
* subject: CaptainDavidMiller
* predicate: employs
* object: Equiano

# MrGSworksForTothilFieldsBridewell [Relationship]
* name: MrGS worksFor TothilFieldsBridewell
* subject: MrGS
* predicate: worksFor
* object: TothilFieldsBridewell

# MrPworksForWestminsterChapel [Relationship]
* name: MrP worksFor WestminsterChapel
* subject: MrP
* predicate: worksFor
* object: WestminsterChapel

# MrRomaineworksForBlackfriarsChurch [Relationship]
* name: MrRomaine worksFor BlackfriarsChurch
* subject: MrRomaine
* predicate: worksFor
* object: BlackfriarsChurch