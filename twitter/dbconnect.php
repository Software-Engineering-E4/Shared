<?php

//ENTER YOUR DATABASE CONNECTION INFO BELOW:
  $hostname="ip-database.ccrihfbatmnt.eu-central-1.rds.amazonaws.com";
  $port = 3306;
  $database="ipdatabase";
  $username="admin";
  $password="6kT4Yi1S7AtqErWTxZyD";

//DO NOT EDIT BELOW THIS LINE
$link = mysqli_connect($hostname, $username, $password, $database, $port);
mysqli_select_db($link, $database) or die('abaCould not select datse');
?> 