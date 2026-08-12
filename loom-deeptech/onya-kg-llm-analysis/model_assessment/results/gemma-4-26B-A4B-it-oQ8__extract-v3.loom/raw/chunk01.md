# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: Also known as Jacob or Michael; a person who experienced slavery and traveled extensively.

# Tinmah [Place]
* name: Tinmah

# MerchantOfTinmah [Person]
* name: Merchant of Tinmah
* description: A merchant who lived in Tinmah and sold Gustavus Vassa.

# WealthyWidow [Person]
* name: Wealthy Widow
* description: A neighbour of the merchant in Tinmah who bought Gustavus Vassa.

# YoungGentleman [Person]
* name: Young Gentleman
* description: The only son of the wealthy widow.
* parent -> WealthyWidow

# MrCampbell [Person]
* name: Mr. Campbell
* description: A master in Virginia.

# MichaelHenryPascal [Person]
* name: Michael Henry Pascal
* jobTitle: Lieutenant in the Royal Navy
* description: Captain of the Industrious Bee who purchased Gustavus Vassa.

# RichardBaker [Person]
* name: Richard Baker
* description: A young lad and constant companion and instructor to Gustavus Vassa.
* colleague -> GustavusVassa

# NicholasDoberry [Person]
* name: Nicholas Doberry
* description: A merchant in Guernsey.

# Mary [Person]
* name: Mary
* description: The daughter of a mate in Guernsey.

# MateOfPascal [Person]
* name: Mate of Pascal
* description: A mate of Michael Henry Pascal who cared for Gustavus Vassa in Guernsey.
* colleague -> MichaelHenryPascal

# AdmiralBoscawen [Person]
* name: Admiral Boscawen
* description: Commander of an expedition against Louisbourg.

# AdmiralCornish [Person]
* name: Admiral Cornish
* description: Commander of a fleet destined for the East Indies.

# AdmiralByng [Person]
* name: Admiral Byng
* description: An admiral involved in a trial at Portsmouth.

# MrGuerin [Person]
* name: Mr. Guerin
* description: A relation of Mr. Pascal in London.
* colleague -> MichaelHenryPascal

# Barbadoes [Place]
* name: Barbadoes

# Falmouth [Place]
* name: Falmouth

# Guernsey [Place]
* name: Guernsey

# London [Place]
* name: London

# Virginia [Place]
* name: Virginia