<?php
require "vendor/autoload.php";
require "dbconnect.php";
require "helper.php";

class Api {
    private $phrases = array("prostate cancer", "colorectal cancer", "prostate cancer treatment", "prostate cancer survival rate", "prostate cancer diagnosis", "prostate cancer screening", "prostate cancer staging", "prostate cancer metastasis");
    private $helper = new Helper();


    function Run() {
        foreach ($this->phrases as $phrase) {
            $data = $helper->getData($phrase);

            if ($data == null) {
                return false;
            }

            $this->helper->InsertJsonIntoDB($data);
        }

        return true;
    }
}
?>