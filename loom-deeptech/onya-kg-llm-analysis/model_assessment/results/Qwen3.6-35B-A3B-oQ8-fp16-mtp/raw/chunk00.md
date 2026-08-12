# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# Olaudah [Person]
* name: Olaudah
* description: The author of the narrative, born in Eboe in 1745.
* parent -> Embrenche
* sibling -> Sister

# Embrenche [Person]
* name: Embrenche
* jobTitle: Chief or Elder
* description: A term importing the highest distinction, signifying a mark of grandeur. Olaudah's father.
* parent -> KingOfBenin
* child -> Olaudah
* child -> Brother

# KingOfBenin [Person]
* name: KingOfBenin
* jobTitle: King
* description: The ruler of the kingdom of Benin.
* subject -> Embrenche

# Sister [Person]
* name: Sister
* description: Olaudah's sister, the only daughter of his parents.
* sibling -> Olaudah

# Brother [Person]
* name: Brother
* description: One of Olaudah's brothers who received the Embrenche mark.
* sibling -> Olaudah

# DrGill [Person]
* name: Dr. Gill
* jobTitle: Author
* description: Author of a commentary on Genesis who deduces the pedigree of Africans from Afer and Afra.
* opinion -> AfricanOrigin

# DrJohnClarke [Person]
* name: Dr. John Clarke
* jobTitle: Dean of Sarum
* description: Author of 'Truth of the Christian Religion' who ascribes African origin to the Israelites.
* opinion -> AfricanOrigin

# MrTClarkson [Person]
* name: Mr. T. Clarkson
* jobTitle: Author
* description: Author of 'Essay on the Slavery and Commerce of the Human Species'.
* work -> SlaveryAndCommerce

# DrMitchel [Person]
* name: Dr. Mitchel
* jobTitle: Author
* description: Cited by Clarkson regarding the darkening of Spaniards in America.
* citedBy -> MrTClarkson

# CaptainDoran [Person]
* name: Capt. Doran
* jobTitle: Captain
* description: Captain of the Charming Sally.
* owns -> CharmingSally

# MrMansfield [Person]
* name: Mr. Mansfield
* jobTitle: Chief Mate
* description: Chief mate of the Charming Sally.
* memberOf -> CharmingSally

# Abraham [Person]
* name: Abraham
* jobTitle: Patriarch
* description: Patriarch of the Jews, ancestor of Afer and Afra according to Dr. Gill.
* spouse -> Keturah

# Keturah [Person]
* name: Keturah
* jobTitle: Concubine/Wife
* description: Wife and concubine of Abraham, mother of Afer and Afra.
* spouse -> Abraham
* child -> Afer
* child -> Afra

# Afer [Person]
* name: Afer
* jobTitle: Descendant
* description: Descendant of Abraham and Keturah.
* parent -> Abraham
* parent -> Keturah

# Afra [Person]
* name: Afra
* jobTitle: Descendant
* description: Descendant of Abraham and Keturah.
* parent -> Abraham
* parent -> Keturah

# CharmingSally [Organization]
* name: Charming Sally
* type: Ship
* description: A slave ship where the incident with the poisoned negro girl occurred.
* captain -> CaptainDoran

# KingdomOfBenin [Place]
* name: Kingdom of Benin
* type: Place
* description: A considerable kingdom in Guinea, extending along the coast about 170 miles.
* ruler -> KingOfBenin

# Eboe [Place]
* name: Eboe
* type: Place
* description: A remote and fertile province in the kingdom of Benin where Olaudah was born.
* partOf -> KingdomOfBenin

# Essaka [Place]
* name: Essaka
* type: Place
* description: A charming fruitful vale in Eboe where Olaudah was born.
* partOf -> Eboe

# Africa [Place]
* name: Africa
* type: Place
* description: The continent containing Guinea and the kingdom of Benin.

# Guinea [Place]
* name: Guinea
* type: Place
* description: Part of Africa known by that name, extending from the Senegal to Angola.
* partOf -> Africa

# Abyssinia [Place]
* name: Abyssinia
* type: Place
* description: An empire that terminates the kingdom of Benin to the interior.
* neighbor -> KingdomOfBenin

# London [Place]
* name: London
* type: Place
* description: A city where natives of Eboe are present.

# Barbadoes [Place]
* name: Barbadoes
* type: Place
* description: A location in the West Indies where the cargo was sold.

# WestIndies [Place]
* name: West Indies
* type: Place
* description: A region where slaves from Benin or Eboe are preferred by planters.

# Turkey [Place]
* name: Turkey
* type: Place
* description: A place with similar tobacco pipes to those used in Eboe.

# Virginia [Place]
* name: Virginia
* type: Place
* description: A location in America with native Indians who are dark coloured.

# SierraLeona [Place]
* name: Sierra Leona
* type: Place
* description: A river in Sierra Leona with a Portuguese settlement at Mitomba.

# Mitomba [Place]
* name: Mitomba
* type: Place
* description: A river in Sierra Leona where Portuguese settlers mixed with natives.

# Montserrat [Place]
* name: Montserrat
* type: Place
* description: A location in the West Indies where a poisoning incident occurred in 1763.

# Smyrna [Place]
* name: Smyrna
* type: Place
* description: A place where the author saw Greeks dance.

# England [Place]
* name: England
* type: Place
* description: A country to which the author brought earth resembling musk.

# LandOfPromise [Place]
* name: Land of Promise
* type: Place
* description: The land reached by the Jews, compared to the pastoral state of the author's countrymen.

# Genesis [Work]
* name: Genesis
* type: Book
* description: A biblical book referenced by Dr. Gill and the author.

# TruthOfTheChristianReligion [Work]
* name: Truth of the Christian Religion
* type: Book
* description: A book by Dr. John Clarke.

# SlaveryAndCommerce [Work]
* name: Essay on the Slavery and Commerce of the Human Species
* type: Book
* description: A book by Mr. T. Clarkson.

# AccountOfGuinea [Work]
* name: Account of Guinea
* type: Book
* description: A book by Benezet, referenced in footnotes.

# AccountOfAfrica [Work]
* name: Account of Africa
* type: Book
* description: A book by Benezet, referenced in footnotes.

# LeutMatthewsVoyage [Work]
* name: Leut. Matthew's Voyage
* type: Book
* description: A voyage referenced in footnotes.

# AfricanOrigin [Concept]
* name: African Origin
* description: The theory that Africans are descendants of Abraham via Keturah.
* supportedBy -> DrGill
* supportedBy -> DrJohnClarke