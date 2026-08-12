# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# OlaudahEquiano [Person]
* name: Olaudah Equiano
* description: The author of the narrative, born in Eboe in 1745, later kidnapped and enslaved.
* parent -> Embrenche
* parent -> MotherOfEquiano
* sibling -> SisterOfEquiano
* colleague -> CaptainDoran
* colleague -> MrMansfield

# Embrenche [Person]
* name: Embrenche
* jobTitle: Chief/Elder
* description: A chief or elder in Eboe, holding the highest distinction, styled Embrenche.
* parent -> OlaudahEquiano
* parent -> BrotherOfEquiano

# MotherOfEquiano [Person]
* name: MotherOfEquiano
* description: Olaudah Equiano's mother, who attended to his upbringing and made oblations at her own mother's tomb.
* parent -> OlaudahEquiano

# SisterOfEquiano [Person]
* name: SisterOfEquiano
* description: Olaudah Equiano's sister, the only daughter in his immediate family, kidnapped and separated from him.
* sibling -> OlaudahEquiano

# BrotherOfEquiano [Person]
* name: BrotherOfEquiano
* description: One of Olaudah Equiano's brothers, who received the Embrenche mark.
* parent -> Embrenche

# CaptainDoran [Person]
* name: Captain Doran
* jobTitle: Captain
* description: Captain of the Charming Sally.
* colleague -> OlaudahEquiano
* colleague -> MrMansfield

# MrMansfield [Person]
* name: Mr Mansfield
* jobTitle: Chief Mate
* description: Chief mate of the Charming Sally.
* colleague -> OlaudahEquiano
* colleague -> CaptainDoran

# DrGill [Person]
* name: Dr. Gill
* description: Author of a commentary on Genesis, who deduced the pedigree of Africans from Afer and Afra.
* colleague -> DrJohnClarke

# DrJohnClarke [Person]
* name: Dr. John Clarke
* jobTitle: Dean of Sarum
* description: Author of 'Truth of the Christian Religion', who ascribed an African origin to the Jews.
* colleague -> DrGill

# MrTClarkson [Person]
* name: Mr. T. Clarkson
* jobTitle: Author
* description: Author of 'Essay on the Slavery and Commerce of the Human Species'.
* colleague -> DrMitchel

# DrMitchel [Person]
* name: Dr. Mitchel
* description: Cited by Clarkson regarding the change in complexion of Spaniards in America.
* colleague -> MrTClarkson

# Benezet [Person]
* name: Benezet
* description: Author of 'Account of Guinea' and 'Account of Africa'.

# LeutMatthew [Person]
* name: Leut. Matthew
* description: Author of a Voyage cited in footnotes.

# Eboe [Place]
* name: Eboe
* description: A remote and fertile province in the kingdom of Benin, where Olaudah Equiano was born.

# Essaka [Place]
* name: Essaka
* description: A charming fruitful vale in Eboe where Olaudah Equiano was born.

# Benin [Place]
* name: Benin
* description: A considerable kingdom in Guinea, situated nearly under the line.

# Africa [Place]
* name: Africa
* description: The continent, specifically the region known as Guinea, extending from Senegal to Angola.

# London [Place]
* name: London
* description: A city where natives of Eboe were present.

# Barbadoes [Place]
* name: Barbadoes
* description: An island in the West Indies where the author arrived and the cargo was sold.

# WestIndies [Place]
* name: West Indies
* description: The region where slaves were sold and where the Charming Sally operated.

# CharmingSally [Organization]
* name: Charming Sally
* description: A slave ship captained by Captain Doran.
* memberOf -> CaptainDoran
* memberOf -> MrMansfield