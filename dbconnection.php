<?php
$mysql = new mysqli (
	'ip-database.ccrihfbatmnt.eu-central-1.rds.amazonaws.com', // locatia serverului
	'admin',       // numele de cont
	'6kT4Yi1S7AtqErWTxZyD',    // parola (atentie, in clar!)
	'ipdatabase'   // baza de date
	);

// verificam daca am reusit
if (mysqli_connect_errno()) {
	die ('Conexiunea a esuat...');
}
?>