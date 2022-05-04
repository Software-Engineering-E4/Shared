<?php

function fetchRedditPosts ($mysql) {
    
    $stmt = $mysql->prepare('SELECT title, SUBSTRING_INDEX(selftext, ".", 2), score FROM `reddit_posts` ORDER BY score DESC LIMIT 2');
    $stmt->execute();
    $result = $stmt->get_result();
    return $result;  
}
?>