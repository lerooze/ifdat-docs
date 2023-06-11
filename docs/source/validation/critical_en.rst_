Critical Errors
===============


This section describes the critical errors that can occur while an authorized user submits data on behalf of a RA.  If a critical error occurs the respective file is not furthered processed and is not loaded into the system database. 

no_header
    A file or a list of incoming files that have no headers.

corrupt_excel
    A list of incoming files that have an **.xlsx** extension but are corrupt 

not_supported_domain
    A list of incoming files that refer to a not supported data domain

corrupt_json
    A list of incoming files that have a **.json** extension but are corrupt 

submitter_inconsistency
    For files that have an inconsistency between the submitter from the filename and the source_person from the header of the file the following attributes are provided:
    * filename: the name of the file.
    * from_filename: the submitter identifier parsed from the filename.
    * from_object: the submitter(source_person) identifier parsed from the header in the file contents.

unauthorized_submitter
    For files that contain data on a domain that the submitter is not authorized to submit data the following attributes are provided:
    * filename: the name of the file
    * domain: the domain of the data

schema_errors
    A list of errors that occurs when the incoming json file is validated against its corresponding schema.  If data is transmitted via the excel channel the incoming excel formatted data are converted by a built-in method into json formatted data and this json data are validated against the corresponding schema.  In :doc:`Schema Error<schema_error>` the error attributes are described. 
