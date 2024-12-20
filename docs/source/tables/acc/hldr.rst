
Πίνακας Α11: Διακρατήσεις Μετοχών/Μεριδίων Eκδοθέντων από τον ΕΟ (HLDR)
=======================================================================
Χρησιμοποιείται για την καταγραφή των μετόχων/μεριδιούχων του ΕΟ.

Προϋπόθεση συμπλήρωσης των στοιχείων του πίνακα είναι να έχουν συμπληρωθεί οι
πίνακες **REF:SELF_SHR** και **REF:SELF_SHR_DYNMC** που περιλαμβάνουν
πληροφοριακά στοιχεία των συμμετοχικών τίτλων που έχει εκδώσει ο ΕΟ αλλά και ο
πίνακας **REF:CNTRPRTY** που περιλαμβάνει πληροφοριακά στοιχεία των
μετόχων/μεριδιούχων. 

Ακολουθεί περιγραφή των μεταβλητών του πίνακα:

ΔΙΑΣΤΑΣΕΙΣ
----------

Αναγνωριστικός κωδικός μετοχής/μεριδίου εκδοθέντος από τον ΕΟ(IID)
    Ο αναγνωριστικός κωδικός :ref:`SHR <shr>` μετοχής/μεριδίου του ΕΟ.

Αναγνωριστικός κωδικός μετόχου/μεριδιούχου (ID)
    Ο αναγνωριστικός κωδικός :ref:`ORG <org>` του κατόχου.  Συμπληρώνεται και ο
    πίνακας REF.CNTRPRTY στην πρώτη αναγγελία του αναγνωριστικού κωδικού.

Ημερομηνία (DT)
    Ημερομηνία που ισχύουν η τιμή της μεταβλητής QNTTY.

    Περαιτέρω διευκρινιστικές πληροφορίες δίδονται στην ενότητα :doc:`../../generic`.

    Το είδος της τιμής είναι :doc:`../../types/formats/datetime`.


Συχνότητα υποβολής στοιχείων ΕΟ (FRQNCY)
    Σε συνδυασμό με τη διάσταση DT ορίζει τη χρονική περίοδο που ισχύουν οι τιμές των μεταβλητών SBSCRPTNS και RDMPTNS.

    Περισσότερες πληροφορίες στις :doc:`../../../generic`.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/gen_frqncy`


ΜΕΤΑΒΛΗΤΕΣ
----------

Ποσότητα (QNTTY)
    Αριθμός μονάδων (μετοχών/μεριδίων)·

    Το είδος της τιμής είναι :doc:`../../types/formats/nonnegativefloat`.

Συμμετοχές (SBSCRPTNS)
    Συμμετοχές σε νέα μερίδια ή σε αυξήσεις μετοχικού κεφαλαίου.  
    
    Στο ποσό δεν περιλαμβάνονται οι προμήθειες συμμετοχής (διάθεσης).

    Συμμετοχές σε συνάλλαγμα μετατρέπονται σε Ευρώ με βάση τις :xref:`exr`
    την ημέρα της συμμετοχής.

    Το είδος της τιμής είναι :doc:`../../types/formats/nonnegativefloat`.

Εξαγορές (RDMPTNS)
    Εξαγορές μεριδίων ή μείωση μετοχικού κεφαλαίου.  
    
    Από το ποσό δεν αφαιρούνται οι προμήθειες εξαγοράς.

    Εξαγορές σε συνάλλαγμα μετατρέπονται σε Ευρώ με βάση τις :xref:`exr`
    την ημέρα της συμμετοχής.

    Το είδος της τιμής είναι :doc:`../../types/formats/nonnegativefloat`.
