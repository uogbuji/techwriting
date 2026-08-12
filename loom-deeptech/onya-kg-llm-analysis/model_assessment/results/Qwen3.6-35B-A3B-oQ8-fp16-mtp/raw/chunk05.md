# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# MrRead [Person]
* name: Mr. Read
* description: A man who desired the author to be flogged for beating his slave; later refused to pursue the author after intervention by the captain.
* owns -> NegroSlave
* knows -> Captain

# NegroSlave [Person]
* name: negro slave
* description: A slave belonging to Mr. Read who struck the author.
* ownedBy -> MrRead

# Captain [Person]
* name: Captain
* description: The author's captain who protected him from Mr. Read and later died at sea.
* employs -> Author
* memberOf -> Vessel
* knows -> MrRead
* knows -> MrDixon
* knows -> Author
* parent -> Author

# Author [Person]
* name: Author
* description: The narrator, a free negro who served as captain and mate on various vessels.
* employedBy -> Captain
* employedBy -> WilliamPhillips
* employedBy -> CaptainJohnBunton
* knows -> MrKing
* knows -> DoctorBrady
* knows -> Mosa
* knows -> CaptainPascal
* knows -> DoctorIrving
* knows -> HonCaptPhipps

# MrDixon [Person]
* name: Mr. Dixon
* description: A gentleman with whom the captain lodged; helped hide the author from Mr. Read.
* knows -> Captain
* knows -> Author

# CaptainPascal [Person]
* name: Capt. Pascal
* description: A captain met by the author in Montserrat.
* knows -> Author

# DoctorIrving [Person]
* name: Doctor Irving
* description: A doctor with whom the author hired himself to learn to freshen sea water.
* employs -> Author
* knows -> Author

# HonCaptPhipps [Person]
* name: Hon. Capt. Phipps
* description: A captain on a voyage to the North Pole with the author and Doctor Irving.
* employs -> Author
* employs -> DoctorIrving
* knows -> Author
* knows -> DoctorIrving

# MrKing [Person]
* name: Mr. King
* description: The author's old master and benefactor, owner of the vessel Nancy.
* owns -> Vessel
* employs -> Author
* knows -> Author

# WilliamPhillips [Person]
* name: William Phillips
* description: A new captain appointed by Mr. King, an old acquaintance of the author.
* employs -> Author
* knows -> Author

# CaptainJohnBunton [Person]
* name: Captain John Bunton
* description: Captain of the sloop Speedwell, bound for Martinico.
* employs -> Author
* owns -> Speedwell

# DoctorBrady [Person]
* name: Doctor Brady
* description: An honest and worthy man who assisted the author in Savannah.
* knows -> Author

# Mosa [Person]
* name: Mosa
* description: A black man and friend of the author in Savannah.
* knows -> Author

# Speedwell [Organization]
* name: Speedwell
* description: A sloop belonging to Grenada, bound for Martinico.
* ownedBy -> CaptainJohnBunton

# Vessel [Organization]
* name: Vessel
* description: The vessel owned by Mr. King and captained by the Captain and later William Phillips.
* ownedBy -> MrKing
* employedBy -> Captain
* employedBy -> WilliamPhillips

# Georgia [Place]
* name: Georgia
* description: A location the author traveled to and from, including Savannah.
* contains -> Savannah

# Savannah [Place]
* name: Savannah
* description: A town in Georgia where the author stayed and faced legal issues.
* locatedIn -> Georgia

# Montserrat [Place]
* name: Montserrat
* description: An island where the author bid farewell to Mr. King and sailed for England.
* contains -> Plymouth

# Plymouth [Place]
* name: Plymouth
* description: A town in Montserrat opposite Mr. King's house.
* locatedIn -> Montserrat

# Martinico [Place]
* name: Martinico
* description: A French island the author sailed to from Georgia.

# NewProvidence [Place]
* name: New Providence
* description: An island in the Bahamas where the author and crew sought refuge after shipwreck.

# StEustatia [Place]
* name: St. Eustatia
* description: An island the author visited on his way to St. Kitts.

# StKitts [Place]
* name: St. Kitts
* description: An island where the author arrived in Basseterre.

# England [Place]
* name: England
* description: The author's intended final destination.

# Jamaica [Place]
* name: Jamaica
* description: A destination the author refused to sail to.

# Turkey [Place]
* name: Turkey
* description: A location of a voyage taken by the author.

# Portugal [Place]
* name: Portugal
* description: A location of a voyage taken by the author.

# Grenada [Place]
* name: Grenada
* description: An island from which the Speedwell belonged.

# NorthPole [Place]
* name: North Pole
* description: The destination of a voyage with Hon. Capt. Phipps.