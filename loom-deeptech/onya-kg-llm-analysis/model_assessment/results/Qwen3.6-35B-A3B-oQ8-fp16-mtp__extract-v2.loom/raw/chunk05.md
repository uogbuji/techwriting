# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The author of the narrative, a free negro who serves as a sailor and captain.

# MrRead [Person]
* name: Mr. Read
* description: A spiteful man who owned a slave that struck Gustavus Vassa; attempted to have Vassa flogged.
* owns -> NegroSlave

# NegroSlave [Person]
* name: Negro Slave
* description: A slave owned by Mr. Read who struck Gustavus Vassa.

# Captain [Person]
* name: Captain
* description: Gustavus Vassa's captain on the vessel bound for the West Indies; later died at sea.
* employs -> GustavusVassa
* colleague -> Mate
* knows -> MrRead
* knows -> MrDixon

# Mate [Person]
* name: Mate
* description: The sickly mate on the vessel who served under the Captain and worked alongside Gustavus Vassa.
* worksFor -> Captain
* colleague -> GustavusVassa

# MrDixon [Person]
* name: Mr. Dixon
* description: A gentleman who lodged with the Captain and helped hide Gustavus Vassa from Mr. Read.
* knows -> Captain
* knows -> GustavusVassa

# WilliamPhillips [Person]
* name: William Phillips
* description: A new captain appointed by Mr. King, an old acquaintance of Gustavus Vassa.
* worksFor -> MrKing
* colleague -> GustavusVassa

# MrKing [Person]
* name: Mr. King
* description: The owner of the vessel and a benefactor/friend to Gustavus Vassa.
* employs -> WilliamPhillips
* knows -> GustavusVassa

# DoctorBrady [Person]
* name: Doctor Brady
* description: An honest and worthy man who assisted Gustavus Vassa when he was threatened by the watch in Savannah.
* knows -> GustavusVassa

# Mosa [Person]
* name: Mosa
* description: A black man and friend of Gustavus Vassa in Savannah.
* knows -> GustavusVassa

# DoctorPerkins [Person]
* name: Doctor Perkins
* description: A person referenced by the watch in Savannah as an example of how they might treat Vassa.

# JohnBunton [Person]
* name: John Bunton
* description: Captain of the sloop Speedwell bound for Martinico.
* employs -> GustavusVassa

# DutchCreole [Person]
* name: Dutch Creole
* description: A sailor who assisted Gustavus Vassa in saving the crew after the shipwreck.
* colleague -> GustavusVassa

# CaptainPascal [Person]
* name: Captain Pascal
* description: A captain met by the author in Martinico.
* knows -> GustavusVassa

# DoctorIrving [Person]
* name: Doctor Irving
* description: A person with whom Gustavus Vassa hired himself to learn to freshen sea water.
* employs -> GustavusVassa

# HonCaptPhipps [Person]
* name: Hon. Capt. Phipps
* description: Captain on the voyage to the North Pole with Gustavus Vassa and Doctor Irving.
* employs -> GustavusVassa
* employs -> DoctorIrving