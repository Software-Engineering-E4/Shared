<?php
    require "dbconnection.php";
    
    $youtubeNewPostsCount = $_POST['youtubeNewPostsCount'];
    $keyword = $_POST['sendKeyword'];
    $q = "SELECT title, link, thumbnail 
    FROM youtube_videos where description LIKE '%$keyword%' OR title  LIKE '%$keyword%' 
    ORDER BY score DESC LIMIT $youtubeNewPostsCount";
    $result = mysqli_query($mysql, $q);
    $rows = mysqli_num_rows($result);
    if($rows > 0) :
        while ($row = mysqli_fetch_assoc($result)): 
?>
        <div class="youtube_post">
        <a class="post" href="<?php echo $row['link'] ?>" target="_blank">
            <h3 class="title"> <?php echo $row['title'] ?> </h3>
            <div class="for_image">
                <img class="youtube_image" src="<?php echo $row['thumbnail'] ?>">
            </div>
        </a>
    </div>
<?php endwhile; endif; ?>