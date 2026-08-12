# @docheader

* @document: https://example.org/books/equiano-narrative
* @nodebase: https://example.org/books/equiano-narrative/
* @schema: https://schema.org/

# GustavusVassa [Person]
* name: Gustavus Vassa
* description: The narrator, formerly a slave, who purchases his freedom and becomes a sailor.
* jobTitle: Sailor, Trader

# RobertKing [Person]
* name: Robert King
* description: A merchant in Montserrat who owned Gustavus Vassa and granted him manumission.
* jobTitle: Merchant, Master

# Captain [Person]
* name: Captain
* description: The narrator's friendly captain who protected him, lent him money, and advocated for his freedom.
* jobTitle: Captain

# JosephClipson [Person]
* name: Joseph Clipson
* description: A free young mulatto-man who was forcibly taken into slavery by a Bermudas captain.

# MrsDavis [Person]
* name: Mrs. Davis
* description: A wise woman in Philadelphia who revealed secrets and foretold events.

# DoctorPerkins [Person]
* name: Doctor Perkins
* description: A severe and cruel man in Savannah who beat the narrator.

# DoctorBrady [Person]
* name: Doctor Brady
* description: An eminent doctor in Savannah who treated the narrator's wounds.

# Terrylegay [Person]
* name: Terrylegay
* description: The Register in Montserrat who drew up the narrator's manumission.

# MrRead [Person]
* name: Mr. Read
* description: A merchant of Savannah.

# CaptainPascal [Person]
* name: Capt. Pascal
* description: The narrator's old master in England whom he hoped to surprise.

# GeorgeWhitfield [Person]
* name: Rev. Mr. George Whitfield
* description: A preacher whom the narrator heard in Philadelphia.

# Montserrat [Place]
* name: Montserrat
* description: An island in the West Indies where the narrator lived and was freed.

# Philadelphia [Place]
* name: Philadelphia
* description: A town in America where the narrator traded and met Mrs. Davis.

# Georgia [Place]
* name: Georgia
* description: A place in America where the narrator traded and was attacked.

# StEustatia [Place]
* name: St. Eustatia
* description: An island where the narrator discharged cargo and took in slaves.

# Savannah [Place]
* name: Savannah
* description: A town in Georgia where the narrator was attacked by Doctor Perkins.

# RobertKing [Person]
* owns -> GustavusVassa
* employs -> GustavusVassa
* grantsManumission -> GustavusVassa

# GustavusVassa [Person]
* worksFor -> Captain
* worksFor -> RobertKing
* knows -> Captain
* knows -> RobertKing
* knows -> JosephClipson
* knows -> MrsDavis
* knows -> DoctorBrady
* knows -> DoctorPerkins
* knows -> Terrylegay
* knows -> MrRead
* knows -> CaptainPascal
* knows -> GeorgeWhitfield

# Captain [Person]
* worksFor -> RobertKing
* employs -> GustavusVassa
* protects -> GustavusVassa
* lendsMoney -> GustavusVassa
* advocatesFor -> GustavusVassa
* colleague -> RobertKing

# DoctorBrady [Person]
* treats -> GustavusVassa

# DoctorPerkins [Person]
* attacks -> GustavusVassa

# Terrylegay [Person]
* registers -> GustavusVassa

# CaptainPascal [Person]
* formerMasterOf -> GustavusVassa

# GeorgeWhitfield [Person]
* preachesTo -> GustavusVassa

# Montserrat [Place]
* locationOf -> RobertKing
* locationOf -> GustavusVassa
* locationOf -> Captain

# Philadelphia [Place]
* locationOf -> GustavusVassa
* locationOf -> MrsDavis
* locationOf -> GeorgeWhitfield

# Georgia [Place]
* locationOf -> GustavusVassa
* locationOf -> DoctorPerkins
* locationOf -> DoctorBrady

# StEustatia [Place]
* locationOf -> GustavusVassa

# Savannah [Place]
* locationOf -> DoctorPerkins
* locationOf -> DoctorBrady
* locationOf -> MrRead