<?php

use Noweh\TwitterApi\Client;

use Abraham\TwitterOAuth\TwitterOAuth;

Class Helper {
    private $settings = [
        'account_id' => 2244994945,
        'consumer_key' => 'cCYOTLx09q198b9ucpoeub9LT',
        'consumer_secret' => 'HSk5dpgzAx5tBNH27ybCga4xJrFEv1BKvVLMNrV02TciIiluc4',
        'bearer_token' => 'AAAAAAAAAAAAAAAAAAAAABs6bgEAAAAABdp3e1xIUmO95Wau0WH3YlpLzwQ%3D6GkZgDUgv2CIvujqyhhMhVLTqQ1UbkngHitOYOMGIWImUgPwjs',
        'access_token' => '1515303940048441346-RoWMP3SbVwsJMDvaWjMghj7d86brdX',
        'access_token_secret' => 'Jgt2QW698TRNXh4fgDkQxIungg9v0hcdakYSQju6sMqTZ'
    ];
    
    function InsertJsonIntoDB(object $object) {
        global $link;
    
        if (!($object == null)) {
            return;
        }
    
        //Original object has two attributes but we're not interested in 'metadata'.
        $object = $object->data;
    
        // processing the array of objects
    //    foreach ($object as $tweets) {
            foreach ($object as $tweet) {
    
                    $tweet_id = $tweet->id;
                    $retweet_count = $tweet->public_metrics->retweet_count;
                    $like_count = $tweet->public_metrics->like_count;
                    $text = $tweet->text;
        
                        // preparing statement for insert query
                        $st = mysqli_prepare($link, 'INSERT IGNORE INTO twitter_posts(id, likes, retweets, text) VALUES (?, ?, ?, ?)');
                    
                        // bind variables to insert query params
                        mysqli_stmt_bind_param($st, 'ddds', $tweet_id, $like_count, $retweet_count, $text);
                    
                        // executing insert query
                        mysqli_stmt_execute($st);
            }
    //    }
    }
    
    
    function getData(string $searchPhrase) {
    
        $client = new Client($this->settings);
        
        $result = $client->tweetSearch()
            ->showMetrics()
        //    ->onlyWithMedias()
        /*    ->addFilterOnUsernamesFrom([
                'twitterdev',
                'Noweh95'
            ], \Noweh\TwitterApi\Enum\Operators::or)*/
            ->addFilterOnKeywordOrPhrase([
        //        'prostate cancer'
        //        'colorectal cancer'
                  $searchPhrase
            ], \Noweh\TwitterApi\Enum\Operators::or)
        //    ->addFilterOnLocales(['en'])
            ->addMaxResults(100)
        //    ->addStartTime('2022-04-01')
        //	  ->addEndTime('2022-04-02')
        //    ->showUserDetails()
            ->performRequest()
        ;
    
        return $result;
    }    
}

?>
