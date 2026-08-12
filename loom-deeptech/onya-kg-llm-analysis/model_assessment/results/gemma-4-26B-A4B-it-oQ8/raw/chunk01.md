# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: Also known as Jacob or Michael; a former slave who served as a companion to various masters and traveled extensively.

# Tinmah [Place]
* name: Tinmah

# Merchant [Person]
* name: Merchant
* description: A merchant in Tinmah who sold Gustavus Vassa.

# WealthyWidow [Person]
* name: Wealthy widow
* description: A neighbour of the merchant in Tinmah who bought Gustavus Vassa.

# WidowSon [Person]
* name: Only son
* description: The son of the wealthy widow in Tinmah.

# MrCampbell [Person]
* name: Mr. Campbell
* description: A master in Virginia.

# MichaelHenryPascal [Person]
* name: Michael Henry Pascal
* jobTitle: Lieutenant in the royal navy
* description: Captain of the Industrious Bee who purchased Gustavus Vassa.

# RichardBaker [Person]
* name: Richard Baker
* description: A young lad and constant companion and instructor to Gustavus Vassa.

# Falmouth [Place]
* name: Falmouth

# NicholasDoberry [Person]
* name: Nicholas Doberry
* description: A merchant in Guernsey.

# Mary [Person]
* name: Mary
* description: The daughter of a mate in Guernsey.

# Roebuck [Place]
* name: Roebuck

# AdmiralBoscawen [Person]
* name: Admiral Boscawen

# Savage [Place]
* name: Savage

# Deal [Place]
* name: Deal

# MrGuerin [Person]
* name: Mr. Guerin
* description: A relation of Gustavus Vassa's master in London.

# StGeorgesHospital [Place]
* name: St. George's Hospital

# Preston [Place]
* name: Preston

# RoyalGeorge [Place]
* name: Royal George

# Namur [Place]
* name: Namur

# AdmiralCornish [Person]
* name: Admiral Cornish

# Lenox [Place]
* name: Lenox

# America [Place]
* name: America

# England [Place]
* name: England

# Guernsey [Place]
* name: Guernsey

# London [Place]
* name: London

# Virginia [Place]
* name: Virginia

# Barbadoes [Place]
* name: Barbadoes

# BridgeTown [Place]
* name: Bridge Town

# GustavusVassaboughtByMerchant [Relationship]
* name: GustavusVassa boughtBy Merchant
* GustavusVassa -> Merchant

# GustavusVassaboughtByWidowSon [Relationship]
* name: GustavusVassa boughtBy WidowSon
* GustavusVassa -> WidowSon

# GustavusVassaboughtByMichaelHenryPascal [Relationship]
* name: GustavusVassa boughtBy MichaelHenryPascal
* GustavusVassa -> MichaelHenryPascal

# GustavusVassafriendOfRichardBaker [Relationship]
* name: GustavusVassa friendOf RichardBaker
* GustavusVassa -> RichardBaker

# GustavusVassaservedByRichardBaker [Relationship]
* name: GustavusVassa servedBy RichardBaker
* RichardBaker -> GustavusVassa

# GustavusVassaservedByMary [Relationship]
* name: GustavusVassa servedBy Mary
* Mary -> GustavusVassa

# GustavusVassaservedByMrGuerin [Relationship]
* name: GustavusVassa servedBy MrGuerin
* MrGuerin -> GustavusVassa