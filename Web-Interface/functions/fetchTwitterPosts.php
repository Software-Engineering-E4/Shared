<?php

function fetchTwitterPosts ($mysql) {
    
    $stmt = $mysql->prepare('SELECT SUBSTRING_INDEX(text, ".", 2), retweets FROM `twitter_posts` ORDER BY retweets DESC LIMIT 2');
    $stmt->execute();
    $result = $stmt->get_result();
    return $result;  
}
?>