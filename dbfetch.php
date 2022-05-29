
<?php
    require "dbconnection.php";

    function fetch_twitter_items($currentLimit, $limit) {
        global $mysql;
        $query = 'SELECT SUBSTRING(text, 1, 250), retweets, id FROM twitter_posts GROUP BY text ORDER BY likes DESC LIMIT '. $currentLimit .',' .$limit.' ';
        $stmt = $mysql->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();
        return $result;
    }
    function display_twitter_items($currentLimit) {
        $result = fetch_twitter_items($currentLimit, 12);
        while ($row = $result->fetch_assoc()) {
            echo '<div class="twitter_post">';
            echo '    <a class="post" id="'.$row['id'].'" href="twitterpost.php?id='.$row['id'].'">';
            echo '        <h3> </h3>';
            echo '        <p class="description">'.$row['SUBSTRING(text, 1, 250)'] . '...' . '</p>';
            echo '    </a>';
            echo '</div>';
        }
    }

    function fetch_reddit_items($currentLimit, $limit) {
        global $mysql;
        $query = 'SELECT title, SUBSTRING(selftext, 1, 250), score, id FROM reddit_posts WHERE selftext IS NOT NULL ORDER BY score DESC LIMIT '. $currentLimit .',' .$limit.' ';
        $stmt = $mysql->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result;
    }
    function display_reddit_items($currentLimit) {
        $result = fetch_reddit_items($currentLimit, 12);
        while ($row = $result->fetch_assoc()) {
            echo '<div class="reddit_post">';
            echo '    <a class="post" id="<'.$row['id'].'" href="redditpost.php?id='.$row['id'].'">';
            echo '        <h3>'.$row['title'].' </h3>';
            echo '        <p class="description">'.$row['SUBSTRING(selftext, 1, 250)'] . '...' . '</p>';
            echo '    </a>';
            echo '</div>';
        }
    }

    function fetch_youtube_items($currentLimit, $limit) {
        global $mysql;
        $query = 'SELECT title, link, thumbnail, score FROM youtube_videos WHERE description IS NOT NULL ORDER BY score DESC LIMIT '. $currentLimit .',' .$limit.' ';
        $stmt = $mysql->prepare($query);
        $stmt->execute();
        $result = $stmt->get_result();

        return $result;
    }
    function display_youtube_items($currentLimit) {
        $result = fetch_youtube_items($currentLimit, 12);
        while ($row = $result->fetch_assoc()) {
            echo '<div class="youtube_post">';
            echo '	<a class="post" href="'.$row['link'].'" target="_blank">';
            echo '		<h3> '.$row['title'].' </h3>';
            echo '		<div class="for_image">';
            echo '			<img class="youtube_image" src="'.$row['thumbnail'].'">';
            echo '		</div>';
            echo '	</a>';
            echo '</div>';
        }
    }

    if(array_key_exists('seemoretwitter', $_GET)) {
        $currentLimit = (int)$_GET['seemoretwitter'];
        display_twitter_items($currentLimit); 
    } else if(array_key_exists('seemorereddit', $_GET)) {
        $currentLimit = (int)$_GET['seemorereddit'];
        display_reddit_items($currentLimit); 
    } else if(array_key_exists('seemoreyoutube', $_GET)) {
        $currentLimit = (int)$_GET['seemoreyoutube'];
        display_youtube_items($currentLimit); 
    }
    
?>