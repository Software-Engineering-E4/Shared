<?php
    require "dbconnection.php";
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="styles/general.css" rel="stylesheet">
    <link href="styles/seeallposts.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <script src="scripts/seeallposts.js" defer></script>
    <script src="scripts/homepage.js" defer></script>
    <title>All posts</title>
</head>

<body>
    <header class="site_header">
        <nav class="navig_line">
            <div class="left_container">
                <div class="site_name">
                    <a class="site_name" href="/index.php">Site name</a>
                </div>
                <form action="/index.php" method="get">
                    <div class="search_bar">
                        <input type="search" id="search" name="search" placeholder=" Search...">
                    </div>
                </form>
            </div>
            <ul class="right_container">
                <li class="latest">
                    <a class="menu_option" href="latest.php"> Latest </a>
                </li>
                <li class="categories">
                    <a class="menu_option" href="index.php#Categories">Categories</a>
                </li>
                <li class="statistics">
                    <a class="menu_option" href="statistics.php">Statistics</a>
                </li>
                <li class="about">
                    <a class="menu_option" href="about.php">About us</a>
                </li>
            </ul>
            <div class="change_theme">
                <input type="checkbox" class="checkbox" id="checkbox">
                <label class="label_for_checkbox" for="checkbox">
                    <i class="fas fa-moon"></i>
                    <i class="fas fa-sun"></i>
                </label>
            </div>
            <a href="https://www.info.uaic.ro" class="faculty" target="_blank"> <img src="images/logo-fii.png"
                    alt="University logo" class="faculty_logo">
            </a>

            <!-- responsive website -->
            <img src="images/btn1.png" alt="" class="menu-btn">
            <img src="images/search.png" alt="" class="search-btn">

        </nav>
    </header>

    <main>
        <h2 class="platform_name" id="platform_name"></h2>
        <?php
        $queries = array();
        parse_str($_SERVER['QUERY_STRING'], $queries);
        $platformName =  $queries['platformName'];

        if ($platformName == 'Reddit'): ?>
            <div class="reddit" id="reddit_see_all">
                <?php
                    $stmt = $mysql->prepare('SELECT title,SUBSTRING(selftext, 1, 250), score FROM `reddit_posts` ORDER BY score DESC');
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while ($row = $result->fetch_assoc()):
                ?>
                <div class="reddit_post">
                    <a class="post" href="post.php">
                        <h3> <?php echo $row['title'] ?> </h3>
                        <p class="description"> <?php echo $row['SUBSTRING(selftext, 1, 250)'] ?> </p>
                    </a>
                </div>
                <?php endwhile; ?>     
            </div>
        <?php endif; ?>
        
        <?php
        $queries = array();
        parse_str($_SERVER['QUERY_STRING'], $queries);
        $platformName =  $queries['platformName'];

        if ($platformName == 'Youtube'): ?>
            <div class="youtube" id="youtube_see_all">
                <?php
                    $stmt = $mysql->prepare('SELECT title,SUBSTRING(description, 1, 250), likes FROM `youtube_videos` ORDER BY likes DESC');
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while ($row = $result->fetch_assoc()):
                ?>

                <div class="youtube_post">
                    <a class="post" href="post.php">
                        <h3> <?php echo $row['title'] ?> </h3>
                        <p class="description"> <?php echo $row['SUBSTRING(description, 1, 250)'] ?> </p>
                    </a>
                </div>
                <?php endwhile; ?>
            </div>
        <?php endif; ?>
        
        <?php
        $queries = array();
        parse_str($_SERVER['QUERY_STRING'], $queries);
        $platformName =  $queries['platformName'];

        if ($platformName == 'Twitter'): ?>
        <div class="twitter" id="twitter_see_all">
            <?php
                $stmt = $mysql->prepare('SELECT SUBSTRING(text, 1, 250), retweets FROM `twitter_posts` ORDER BY retweets DESC');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>
                <div class="twitter_post">
                    <a class="post" href="post.php">
                        <p class="description"> <?php echo $row['SUBSTRING(text, 1, 250)'] ?> </p>
                    </a>
            </div>
            <?php endwhile; ?>
        </div>
        <?php endif; ?>

    </main>
</body>

</html>