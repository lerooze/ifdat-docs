Πίνακας Μεταβλητών Στοιχείων Αναφοράς ΠΜ (FND_DYNMC)
====================================================

Χρησιμοποιείται για την παροχή στοιχείων αναφοράς της ΠΜ (των ΠΜ) και
περιλαμβάνει μεταβλητές που οι τιμές τους δύναται να μεταβληθούν κατά
τη διάρκεια του κύκλου ζωής της κάθε ΠΜ.

ΔΙΑΣΤΑΣΕΙΣ
----------
Αναγνωριστικός Κωδικός ΠΜ (ID)
    Από τον πίνακα επιλέγεται ο αναγνωριστικός κωδικός ID της ΠΜ

Ισχύει από (VLD_FRM)
    Ημερομηνία από την οποία ισχύουν οι τιμές των παρεχόμενων μεταβλητών.

    Περαιτέρω διευκρινιστικές πληροφορίες δίδονται στην ενότητα :doc:`../../generic`.

    Το είδος της τιμής είναι :doc:`../../types/formats/date`.

Ισχύει έως (VLD_T)
    Ημερομηνία από την οποία ισχύουν οι τιμές των παρεχόμενων μεταβλητών.

    Περαιτέρω διευκρινιστικές πληροφορίες δίδονται στην ενότητα :doc:`../../generic`.

    Το είδος της τιμής είναι :doc:`../../types/formats/date`.


ΜΕΤΑΒΛΗΤΕΣ
----------

Ονομασία (NM)
    Επωνυμία/Ονομασία της ΠΜ

    Το είδος της τιμής είναι :doc:`../../types/formats/string128`

Ονομασία με Λατινικούς Χαρακτήρες (NM_LTN)
    Επωνυμία/Ονομασία του ΕΟ με λατινικούς χαρακτήρες

    Το είδος της τιμής είναι :doc:`../../types/formats/ascii128`

Σύντομη Ονομασία (NM_SHRT)
    Διακριτικό όνομα ή σύντομη ονομασία της ΠΜ.

    Συμπληρώνεται μόνο αν υπάρχει τέτοια ονομασία για την ΠΜ.

    Το είδος της τιμής είναι :doc:`../../types/formats/string64`

Οδός και Αριθμός (STRT)
    Οδός και αριθμός της διεύθυνσης της ΠΜ.

    Συμπληρώνεται μόνο για τις ΠΜ με νομική υπόσταση.

    Το είδος της τιμής είναι :doc:`../../types/formats/string64`

Οδός με Λατινικούς Χαρακτήρες (STRT_LTN)
    Οδός και αριθμός της διεύθυνσης της ΠΜ με λατινικούς χαρακτήρες

    Συμπληρώνεται μόνο για τις ΠΜ με νομική υπόσταση.

    Το είδος της τιμής είναι :doc:`../../types/formats/ascii64`

Πόλη (CTY)
    Πόλη/χωριό της διεύθυνσης της ΠΜ.

    Συμπληρώνεται μόνο για τις ΠΜ με νομική υπόσταση.

    Το είδος της τιμής είναι :doc:`../../types/formats/string32`

Πόλη με Λατινικούς Χαρακτήρες (CTY_LTN)
    Πόλη/χωριό της διεύθυνσης της ΠΜ με λατινικούς χαρακτήρες.

    Συμπληρώνεται μόνο για τις ΠΜ με νομική υπόσταση.

    Το είδος της τιμής είναι :doc:`../../types/formats/ascii32`

Ταχυδρομικός κώδικας (PSTL_CD)
    Ταχυδρομικός κώδικας της διεύθυνσης της ΠΜ.

    Συμπληρώνεται μόνο για τις ΠΜ με νομική υπόσταση.

    Το είδος της τιμής είναι :doc:`../../types/formats/string16`

Διαδικτυακή Διεύθυνση (URL)
    Διεύθυνση στο διαδίκτυο της ΠΜ.

    Συμπληρώνεται μόνο αν υπάρχει τέτοια διεύθυνση που παρέχει πληροφορίες της ΠΜ στο διαδίκτυο.

    Το είδος της τιμής είναι :doc:`../../types/formats/url`

Ηλεκτρονική Διεύθυνση (EMAIL)
    Ηλεκτρονική διεύθυνση αλληλογραφίας

    Συμπληρώνεται μόνο αν υπάρχει τέτοια διεύθυνση για απευθείας ηλεκτρονική επικοινωνία με την ΠΜ.

    Το είδος της τιμής είναι :doc:`../../types/formats/email`

ΠΜ Εισηγμένη σε Οργανωμένη Αγορά (IS_LSTD)
    Ένδειξη για το αν τουλάχιστον ένας συμμετοχικός τίτλος της ΠΜ διαπραγματεύεται σε οργανωμένη αγορά.

    Το είδος της τιμής είναι :doc:`../../types/formats/bool`

ΠΜ σε Κατάσταση Αδράνειας (IS_INCTV)
    Ένδειξη ότι η ΠΜ βρίσκετα σε κατάστασης αδράνειας.

    Το είδος της τιμής είναι :doc:`../../types/formats/bool`

ΠΜ σε Καθεστώς Ρευστοποίησης (IS_UNDR_LQDTN)
    Ένδειξη ότι η ΠΜ βρίσκετα σε καθεστώς ρευστοποίησης.

    Το είδος της τιμής είναι :doc:`../../types/formats/bool`

Καθεστώς Ελέγχου της ΠΜ (INSTTTNL_SCTR_CNTRL)
    Είδος θεσμικού ελέγχου που ασκούνε οι μετόχοι/μεριδιούχοι στον ΕΟ.
    
    Για την έννοια του θεσμικού ελέγχου δείτε το Κεφάλαιο 2 τους ΕΣΛ2010.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/org_instttnl_sctr_cntrl`

Διαχειρίστρια Εταιρεία ΕΟ (MNGD_BY)
    Αναγνωριστικός κωδικός της διαχειρίστριας εταιρείας
    
    Η μεταβλητή συμπληρώνεται μόνο για τους ΕΟ που λειτουργούν ως αμοιβαία κεφάλαια

    Το είδος της τιμής είναι :ref:`ORG <org>`.

ΠΜ που ανήκει σε άλλο ΕΟ τύπου "μανδύα" (UNDR_UMBRLL_BY)
    Ο αναγνωριστικός κωδικός του ΕΟ τύπου μανδύα (umbrella fund) στο οποίο ανήκει η ΠΜ
    
    Η μεταβλητή συμπληρώνεται μόνο για τις ΠΜ που είναι μέλη άλλων ΕΟ που έχουν τη μορφή του μανδύα (umbrell fund)

    Το είδος της τιμής είναι :ref:`ORG <org>`.

Μορφή (TYP)
    Μορφή της ΠΜ.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_typ`

Επενδυτική πολιτική (INVSTMNT_PLCY)
    Επενδυτική πολιτική της ΠΜ
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_invstmnt_plcy`

Δευτορογενή Μορφή (SBTYP)
    Δευτερογενή μορφή της ΠΜ.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_sbtyp`

Τρόπος Διανομής Μερίσματος (DSTRBTN_TYP)
    Μερισματική πολιτική της ΠΜ.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_dstrbtn_typ`

Είδος Μεριδιούχων (INVSTR_TYP)
    Είδος μετόχων/μεριδιούχων.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_invstr_typ`

Είδος Πράσινου ΕΟ (GRN_TYP)
    Πράσινη κατηγορία που ανήκει η ΠΜ.
    
    Η μεταβλητή συμπληρώνεται μόνο από "πράσινους" ΠΜ.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_grn_typ`

Επενδυτική Στρατηγική (STRTGY)
    Επενδυτική στρατηγική της ΠΜ.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_strtgy`

Γεωγραφικός Προσδιορισμός (GGPHCL_FCS)
    Γεωγραφικός προσδιορισμός της πλειοψηφίας των περιουσιακών στοιχείων της ΠΜ
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_ggrphcl_fcs`

Επενδυτικός Προσδιορισμός των Ομολογιακών ΠΜ (BND_FCS)
    Προσδιορισμός της πλειοψηφίας των επενδύσεων των Ομολογιακών ΠΜ.

    Τιμή συμπληρώνεται μόνο όταν η μεταβλητή *INVSTMNT_PLCY* έχει την τιμή *BON*.
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_bnd_fcs`

Επενδυτικός Προσδιορισμός των ΠΜ που επενδύουν σε Ακίνητη Περιουσία (RL_ESTT_TYP)
    Προσδιορισμός της πλειοψηφίας των επενδύσεων των ΠΜ που επενδύουν σε ακίνητη περιουσία.

    Τιμή συμπληρώνεται μόνο όταν η μεταβλητή *INVSTMNT_PLCY* έχει την *RES*
    
    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/fnd_rl_estt_typ`

Ένδειξη επενδύσεων της ΠΜ σε άλλους ΕΟ (IS_FOF)
    Ένδειξη περί επενδύσεων της ΠΜ κυρίως σε άλλους ΕΟ

    Το είδος της τιμής είναι :doc:`../../types/formats/bool`

Ένδειξη περί διαπραγματεύσιμης ΠΜ (IS_ETF)
    Ένδειξη ότι η ΠΜ αποτελεί διαπραγματεύσιμο αμοιβαίο κεφάλαιο. 

    Για περισσότερες πληροφορίες δείτε την ΕΚΤ/2014/5 κατευθυντήρια γραμμή

    Το είδος της τιμής είναι :doc:`../../types/formats/bool`

Ένδειξη περί Ιδιωτικού Επενδυτικού Κεφαλαίου (IS_PEF)
    Ένδειξη ότι η ΠΜ αποτελεί έχει τη μορφή ιδιωτικού επενδυτικού κεφαλαίου. 

    Για περισσότερες πληροφορίες δείτε την ΕΚΤ/2014/5 κατευθυντήρια γραμμή

    Το είδος της τιμής είναι :doc:`../../types/formats/bool`

.. _fscurrency:

Νόμισμα Αποτίμησης της ΠΜ (VLTN_CRRNCY)
    Νόμισμα βάση του οποίου γίνεται η απότιμηση της ΠΜ.

    Η τιμή επιλέγεται από τη λίστα τιμών :doc:`../../types/codelists/gen_crrncy`