<?php

function fetchYoutubeVideos ($mysql) {
    
    $stmt = $mysql->prepare('SELECT title, SUBSTRING_INDEX(description, ".", 2), likes FROM `youtube_videos` ORDER BY likes LIMIT 2');
    $stmt->execute();
    $result = $stmt->get_result();
    return $result;  
}
?>
