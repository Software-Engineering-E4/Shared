<?php
require "vendor/autoload.php";
require "dbconnect.php";
require "helper.php";

use Abraham\TwitterOAuth\TwitterOAuth;

use Noweh\TwitterApi\Client;

$settings = [
    'account_id' => ,
    'consumer_key' => '',
    'consumer_secret' => '',
    'bearer_token' => '',
    'access_token' => '',
    'access_token_secret' => ''
];

$client = new Client($settings);

$result = $client->tweetSearch()
    ->showMetrics()
//    ->onlyWithMedias()
/*    ->addFilterOnUsernamesFrom([
        'twitterdev',
        'Noweh95'
    ], \Noweh\TwitterApi\Enum\Operators::or)*/
    ->addFilterOnKeywordOrPhrase([
        'prostate cancer'
//        'colorectal cancer'
    ], \Noweh\TwitterApi\Enum\Operators::or)
    ->addFilterOnLocales(['en'])
    ->addMaxResults(100)
//    ->addStartTime('2022-04-01')
//	  ->addEndTime('2022-04-02')
//    ->showUserDetails()
    ->performRequest()
;

InsertJsonIntoDB($result);
/*
echo "<pre>";
print_r($result);
echo "</pre>";
*/
?>