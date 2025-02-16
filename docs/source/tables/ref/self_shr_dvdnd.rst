
Πίνακας B11: Μερίσματα Μετοχών/Μεριδίων Εκδοθέντων από τον ΕΟ (SELF_SHR_DVDND)
==============================================================================

Χρησιμοποιείται για στοιχεία μερισμάτων (dividends) ιδίων μετοχών/μεριδίων των ΕΟ.

Ακολουθεί περιγραφή των μεταβλητών του πίνακα:

ΔΙΑΣΤΑΣΕΙΣ
----------
Αναγνωριστικός κωδικός μετοχής/μεριδίου (ID)
    Ο αναγνωριστικός κωδικός :ref:`SHR <shr>` της ιδίας μετοχής/μεριδίου.

Ημερομηνία καταγραφής (DT)
    Ημερομηνία καταγραφής που ο ΕΟ ελέγχει τα βιβλία του για να εντοπίσει τους
    κατόχους της ιδίας μετοχής/μεριδίου.
    
    Ένας κάτοχος πρέπει να είναι δηλωμένος τη συγκεκριμένη ημερομηνία για να
    είναι δικαιούχος του μερίσματος.

    Το είδος της τιμής είναι :doc:`../../types/formats/datetime`.

ΜΕΤΑΒΛΗΤΕΣ
----------

Επόμενη ημερομηνία (EX_DT)
    Ημερομηνία από την οποία το μέρισμα δεν οφείλεται σε νέους κατόχους των
    μετοχών/μεριδίων (ΕΧ DATE)

    Το είδος της τιμής είναι :doc:`../../types/formats/datetime`.

Ημερομηνία αναγγελίας (DCLRTN_DT)
    Ημερομηνία αναγγελίας του μερίσματος.

    Το είδος της τιμής είναι :doc:`../../types/formats/datetime`.

Ημερομηνία πληρωμής (PMNT_DT)
    Ημερομηνία πληρωμής του μερίσματος.

    Το είδος της τιμής είναι :doc:`../../types/formats/datetime`.


Συχνότητα διανομής μερίσματος (FRQNCY)
    Συχνότητα υποβολής στοιχείων ΕΟ διανομής μερίσματος.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/dvdnd_cstm_frqncy`.

Είδος (TYP)
    Είδος μερίσματος.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/dvdnd_typ`.

.. _currency_div:

Νόμισμα (CRRNCY)
    Το νόμισμα διανομής του μερίσματος.

    Συμπληρώνεται τιμή στη περίπτωση που το μέρισμα πληρώνεται σε νόμισμα.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`.

Ποσό (AMNT)
    Ποσό μερίσματος.
    
    Το είδος της τιμής είναι :doc:`../../types/formats/positivefloat`.
