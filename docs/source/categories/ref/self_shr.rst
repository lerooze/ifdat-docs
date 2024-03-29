Στοιχεία Αναφοράς Συμμετοχικών Τίτλων Εκδοθέντοι από τις ΠΜ (SELF_SHR)
======================================================================

Χρησιμοποιείται για την παροχή στοιχείων αναφοράς του συμμετοχικού τίτλου
(των συμμετοχικών τίτλων) της ΠΜ (των ΠΜ) και περιλαμβάνει μεταβλητές που
μπορούν να λάβουν έως και μία ξεχωριστή τιμή κατά τη διάρκεια του κύκλου ζωής
του κάθε συμμετοχικού τίτλου.

ΔΙΑΣΤΑΣH
--------
Αναγνωριστικός Κωδικός Συμμετοχικού Τίτλου (ID)
    Ο αναγνωριστικός κωδικός :ref:`SHR <shr>` του συμμετοχικού τίτλου που έχει εκδοθεί από την ΠΜ.

ΜΕΤΑΒΛΗΤΕΣ
----------

Ημερομηνία Έκδοσης (DT_BRTH)
    Ημερομηνία έκδοσης/ενεργοποίησης/αρχικοποίησης

    Το είδος της τιμής είναι :doc:`../../types/formats/date`.

.. _sishareclose:

Ημερομηνία Λήξης (DT_CLS)
    Ημερομηνία λήξης/ολικής ρευστοποίησης 

    Συμπληρώνεται μόνο στην περίπτωση λήξης/ρευστοποίησης.

    Το είδος της τιμής είναι :doc:`../../types/formats/date`.

.. _sishrcurrency:

Νόμισμα Έκδοσης (CRRNCY)
    Το νόμισμα έκδοσης του συμμετοχικού τίτλου.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`

Αγορά Διαπραγμάτευσης (MRKT)
    Η χρηματιστηριακή αγορά διαπραγμάτευσης

    Για περισσότερες πληροφορίες δείτε το πρότυπο ISO-10383

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/gen_mrkt`

Αναδιάρθρωση σε (RSTRCTRD_T)
    Συμπληρώνεται ο αναγνωριστικός κωδικός του νέου συμμετοχικού τίτλου καθώς και η sishareclose_ με την ημερομηνία αναδιάρθρωσης.

    Συμπληρώνεται μόνο σε περίπτωση αναδιάρθρωσης σε νέο συμμετοχικό τίτλο.

    Το είδος της τιμής είναι :ref:`SHR <shr>`


Ταυτόσημο με (ALS_OF)
    Χρησιμοποιείται για την συσχέτιση εσωτερικών αναγνωριστικών κωδικών.

    Συμπληρώνεται μόνο σε περίπτωση αλλαγής της ΜΠΣ ή σε περίπτωση εταιρικής πράξης.

    Το είδος της τιμής είναι :ref:`SHR <shr>`
