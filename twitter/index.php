<?php
require "vendor/autoload.php";
require "dbconnect.php";
require "helper.php";

    $phrases = array("prostate cancer", "colorectal cancer", "prostate cancer treatment", "prostate cancer survival rate", "prostate cancer diagnosis", "prostate cancer screening", "prostate cancer staging", "prostate cancer metastasis");

    foreach ($phrases as $phrase) {
        $data = getData($phrase);
        InsertJsonIntoDB($data);
    }
?>