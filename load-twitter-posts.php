<?php
    require "dbconnection.php";

    $twitterNewPostsCount = $_POST['twitterNewPostsCount'];
    $keyword = $_POST['sendKeyword'];
    $q = "SELECT id, SUBSTRING(text, 1, 250) 
    FROM twitter_posts where text LIKE '%$keyword%' GROUP BY text
    ORDER BY retweets DESC LIMIT $twitterNewPostsCount";
    $result = mysqli_query($mysql, $q);
    $rows = mysqli_num_rows($result);
    if($rows > 0) :
        while ($row = mysqli_fetch_assoc($result)): 
?>

<div class="twitter_post" id="twitter_post">
    <a class="post" id="<?php $row['id'] ?>" href="twitterpost.php?id=<?php echo $row['id'] ?>">
        <p class="description"> <?php echo $row['SUBSTRING(text, 1, 250)'] . '...' ?> </p>
    </a>
</div>
<?php endwhile; ?>
<?php endif; ?>