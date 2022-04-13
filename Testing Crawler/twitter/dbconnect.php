<?php

//ENTER YOUR DATABASE CONNECTION INFO BELOW:
  $hostname="localhost";
  $database="twitter";
  $username="root";
  $password="";

//DO NOT EDIT BELOW THIS LINE
$link = mysqli_connect($hostname, $username, $password);
mysqli_select_db($link, $database) or die('Could not select database');
?> 