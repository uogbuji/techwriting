# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GrenvilleSharp [Person]
* name: Grenville Sharp
* description: Esq; an approved friend, man of virtue, benefactor to mankind.
* memberOf: BritishLegislature
* knows: ThomasClarkson
* knows: JamesRamsay
* knows: RobertKing

# ThomasClarkson [Person]
* name: Thomas Clarkson
* description: Reverend; an approved friend, man of virtue, benefactor to mankind.
* memberOf: BritishLegislature
* knows: GrenvilleSharp
* knows: JamesRamsay
* knows: RobertKing

# JamesRamsay [Person]
* name: James Ramsay
* description: Reverend; an approved friend, man of virtue, benefactor to mankind.
* memberOf: BritishLegislature
* knows: GrenvilleSharp
* knows: ThomasClarkson
* knows: RobertKing

# BritishLegislature [Organization]
* name: British Legislature
* description: The legislative body considering the inhuman traffic of slavery and designs worthy of royal patronation.

# GreatBritain [Place]
* name: Great Britain
* description: A country with manufacturing interests equal or superior to landed interests; source of British manufactures.

# Africa [Place]
* name: Africa
* description: A continent rich in vegetable and mineral productions, target for commercial intercourse and civilization.

# RobertKing [Person]
* name: Robert King
* description: The author of the narrative, who was unwilling and unable to adorn the plainness of truth.
* knows: GrenvilleSharp
* knows: ThomasClarkson
* knows: JamesRamsay