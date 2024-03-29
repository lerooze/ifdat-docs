Πίνακας Στοιχείων Αναφοράς Καταθετικών Λογαριασμών των ΠΜ (DPST)
================================================================

Χρησιμοποιείται για την παροχή στοιχείων αναφοράς των καταθετικών
λογαριασμών που κατέχει η ΠΜ.  Η κάθε μεταβλητή του πίνακα λαμβάνει έως και μία
τιμή κατά τη διάρκεια του κύκλου ζωής της κατάθεσης.  Αν προκύψει ανάγκη
αλλαγής της τιμής μίας μεταβλητής θα πρέπει να δημιουργείται νέα κατάθεση και
όχι να αλλάζει η τιμή της μεταβλητής.  Αλλαγές σε τιμές μεταβλητών επιτρέπονται
μόνο στην περίπτωση διορθώσεων.


ΔΙΑΣΤΑΣΕΙΣ
----------

Αναγνωριστικός Κωδικός Χρεογράφου (ID)
    Ο αναγνωριστικός κωδικός :ref:`DEP <dep>` της κατάθεσης.


ΜΕΤΑΒΛΗΤΕΣ
----------
Ημερομηνία Έκδοσης (DT_BRTH)
    Ημερομηνία έκδοσης/ενεργοποίησης/αρχικοποίησης του καταθετικού λογαριασμού.

    Το είδος της τιμής είναι :doc:`../../types/formats/date`.

.. _oidepclose:

Ημερομηνία Λήξης (DT_CLS)
    Ημερομηνία λύσης του καταθετικού λογαριασμού.

    Συμπληρώνεται μόνο όταν οι όροι του καταθετικού λογαριασμού καθορίζουν τέτοια ημερομηνία.  Δεν συμπληρώνεται για καταθέσεις όψεως ή καταθέσεις με προειδοποίηση.

    Το είδος της τιμής είναι :doc:`../../types/formats/date`.

Είδος (TYP)
    Είδος κατάθεσης (όψεως, προθεσμίας, με προειδοποίηση).

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/dep_typ`


Χρόνος Προειδοποίησης (NTC)
    Χρόνος προειδοποίησης.
    
    Συμπληρώνεται μόνο για καταθέσεις με προειδοποίηση.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/dep_ntc`

.. _depcurrency:

Νόμισμα Συναλλαγής (CRRNCY)
    Το νόμισμα που χρησιμοποιείται για τη διενέργεια συναλλαγών στον καταθετικό λογαριασμό.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`


Χρεώστης (DBTR)
    Αναγνωριστικός κωδικός :ref:`ORG <org>` του πιστωτικού ιδρύματος που έχει δημιουργηθεί ο καταθετικός λογαριασμός.
    
    Σε περίπτωση εσωτερικού αναγνωριστικού κωδικού θα πρέπει να συμπληρώνεται και ο πίνακας REF.CNTRPTY.


Πιστωτής (CRDTR)
    Αναγνωριστικός κωδικός :ref:`ORG <org>` της ΠΜ που έχει δημιουργήσει τον καταθετικό λογαριασμό.

Ταυτόσημο με (ALS_OF)
    Χρησιμοποιείται για την συσχέτιση εσωτερικών αναγνωριστικών κωδικών.

    Συμπληρώνεται μόνο σε περίπτωση αλλαγής της ΜΠΣ ή σε περίπτωση εταιρικής πράξης όπου η ΜΠΣ διαφέρει.

    Το είδος της τιμής είναι :ref:`DEP <dep>`
