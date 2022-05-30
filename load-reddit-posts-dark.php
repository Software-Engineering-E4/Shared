<?php
    require "dbconnection.php";
    
    $redditNewPostsCount = $_POST['redditNewPostsCount'];
    $keyword = $_POST['sendKeyword'];
    $q = "SELECT id,title,SUBSTRING(selftext, 1, 250)
        FROM reddit_posts where selftext LIKE '%$keyword%' OR title  LIKE '%$keyword%' and selftext IS NOT NULL
        ORDER BY score DESC LIMIT $redditNewPostsCount";
    $result = mysqli_query($mysql, $q);
    $rows = mysqli_num_rows($result);
    if($rows > 0) :
        while ($row = mysqli_fetch_assoc($result)): 
?>

<div class="reddit_post dark-theme-grey">
    <a class="post" id="<?php $row['id'] ?>" href="redditpost.php?id=<?php echo $row['id'] ?>">
        <h3 class="title dark-theme-light-grey"> <?php echo $row['title'] ?> </h3>
        <p class="description dark-theme-light-grey"> <?php echo $row['SUBSTRING(selftext, 1, 250)'] ?> </p>
    </a>
</div>
<?php endwhile; endif; ?>
