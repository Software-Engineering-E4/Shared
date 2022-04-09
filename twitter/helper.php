<?php

function InsertJsonIntoDB(object $object) {
    global $link;

    //Original object has two attributes but we're not interested in 'metadata'.
    $object = $object->data;

    // processing the array of objects
//    foreach ($object as $tweets) {
        foreach ($object as $tweet) {

                $tweet_id = $tweet->id;
                $retweet_count = $tweet->public_metrics->retweet_count;
                $reply_count = $tweet->public_metrics->reply_count;
                $like_count = $tweet->public_metrics->like_count;
                $quote_count = $tweet->public_metrics->quote_count;
                $text = $tweet->text;
    
                    // preparing statement for insert query
                    $st = mysqli_prepare($link, 'INSERT INTO tweets(tweet_id, retweet_count, reply_count, like_count, quote_count, text) VALUES (?, ?, ?, ?, ?, ?)');
                
                    // bind variables to insert query params
                    mysqli_stmt_bind_param($st, 'ddddds', $tweet_id, $retweet_count, $reply_count, $like_count, $quote_count, $text);
                
                    // executing insert query
                    mysqli_stmt_execute($st);
        }
//    }
}
?>