# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# Olaudah [Person]
* name: Olaudah
* description: An Eboe man who was kidnapped and later became a slave.

# OlaudahsMother [Person]
* name: Olaudah's Mother
* description: A woman from Eboe who was very fond of her son.

# OlaudahsFather [Person]
* name: Olaudah's Father
* jobTitle: Embrenche
* description: An elder or chief in Eboe.

# OlaudahsSister [Person]
* name: Olaudah's Sister
* description: The only daughter in Olaudah's family.

# Chieftain [Person]
* name: Chieftain
* jobTitle: Smith
* description: A man who bought Olaudah and treated him well.

# ChieftainsFirstWife [Person]
* name: Chieftain's First Wife
* description: The first wife of the chieftain who comforted Olaudah.

# ChieftainsDaughter [Person]
* name: Chieftain's Daughter
* description: The only daughter of the chieftain and his first wife.

# Eboe [Place]
* name: Eboe

# Essaka [Place]
* name: Essaka

# Guinea [Place]
* name: Guinea

# Africa [Place]
* name: Africa

# Benin [Place]
* name: Benin

# Abyssinia [Place]
* name: Abyssinia

# Senegal [Place]
* name: Senegal

# Angola [Place]
* name: Angola

# London [Place]
* name: London

# WestIndies [Place]
* name: West Indies

# Barbados [Place]
* name: Barbados

# Mitomba [Place]
* name: Mitomba

# SierraLeona [Place]
* name: Sierra Leona

# America [Place]
* name: America

# Virginia [Place]
* name: Virginia

# DrGill [Person]
* name: Dr. Gill

# DrJohnClarke [Person]
* name: Dr. John Clarke

# MrTClarkson [Person]
* name: Mr. T. Clarkson

# DrMitchel [Person]
* name: Dr. Mitchel

# Benezet [Person]
* name: Benezet

# OlaudahsFather-Olaudah [Relationship]
* parent -> Olaudah

# OlaudahsFather-OlaudahsSister [Relationship]
* parent -> OlaudahsSister

# OlaudahsFather-Olaudah [Relationship]
* parent -> Olaudah

# OlaudahsMother-Olaudah [Relationship]
* parent -> Olaudah

# OlaudahsMother-OlaudahsSister [Relationship]
* parent -> OlaudahsSister

# OlaudahsMother-Olaudah [Relationship]
* knows -> Olaudah

# Chieftain-ChieftainsFirstWife [Relationship]
* knows -> ChieftainsFirstWife

# Chieftain-ChieftainsDaughter [Relationship]
* parent -> ChieftainsDaughter

# ChieftainsFirstWife-ChieftainsDaughter [Relationship]
* parent -> ChieftainsDaughter

# Olaudah-OlaudahsSister [Relationship]
* knows -> OlaudahsSister

# Olaudah-OlaudahsMother [Relationship]
* knows -> OlaudahsMother

# Olaudah-OlaudahsFather [Relationship]
* knows -> OlaudahsFather

# Olaudah-OlaudahsSister [Relationship]
* knows -> OlaudahsSister