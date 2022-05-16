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
    <script src="scripts/keepingdarktheme.js" defer></script>
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
                <form action="/search.php" method="post">
                    <div class="search_bar">
                        <input type="search" id="search" name="search" placeholder=" Search...">
                    </div>
                </form>
            </div>
            <ul class="right_container">
                <li class="latest">
                    <a class="menu_option" href="index.php"> Home </a>
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
            <div class="change_theme" id="change_theme">
                <img src="images/sun.svg" class="sun">
                <img src="images/moon.svg" class="moon">
            </div>
            <a href="https://www.info.uaic.ro" class="faculty" target="_blank"> <img src="images/logo-fii.png"
                    alt="University logo" class="faculty_logo">
            </a>

            <!-- responsive website -->
            <div class="phone-buttons">
                <img src="images/search.png" class="search-btn">
                <img src="images/menu.png" class="menu-btn">
            </div>
        </nav>
        <div class="phone options">
            <ul class="phone container">
                <li class="phone_list_element">
                    <a class="phone menu_option" href="index.php">Home</a>
                </li>
                <li class="phone_list_element">
                    <a class="phone menu_option" href="index.php#Categories">Categories</a>
                </li>
                <li class="phone_list_element">
                    <a class="phone menu_option" href="statistics.php">Statistics</a>
                </li>
                <li class="phone_list_element">
                    <a class="phone menu_option" href="about.php">About us</a>
                </li>
            </ul>
        </div>
    </header>

    <main>
        <h2 class="platform_name" id="platform_name"></h2>
        
        <?php
        $queries = array();
        parse_str($_SERVER['QUERY_STRING'], $queries);
        $platformName =  $queries['platformName'];

        if ($platformName == 'Twitter'): ?>
        <div class="twitter" id="twitter_see_all">
            <?php
                $stmt = $mysql->prepare('SELECT SUBSTRING(text, 1, 250), retweets, id FROM twitter_posts GROUP BY text ORDER BY retweets DESC');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>
                <div class="twitter_post">
                    <a class="post" id="<?php $row['id'] ?>" href="twitterpost.php?id=<?php echo $row['id'] ?>">
                        <p class="description"> <?php echo $row['SUBSTRING(text, 1, 250)'] ?> </p>
                    </a>
            </div>
            <?php endwhile; ?>
        </div>
        <?php endif; ?>

        <?php
        $queries = array();
        parse_str($_SERVER['QUERY_STRING'], $queries);
        $platformName =  $queries['platformName'];

        if ($platformName == 'Reddit'): ?>
            <div class="reddit" id="reddit_see_all">
                <?php
                    $stmt = $mysql->prepare('SELECT title,SUBSTRING(selftext, 1, 250), score, id FROM reddit_posts WHERE selftext IS NOT NULL ORDER BY score DESC');
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while ($row = $result->fetch_assoc()):
                ?>

                <div class="reddit_post">
                    <a class="post" id="<?php $row['id'] ?>" href="redditpost.php?id=<?php echo $row['id'] ?>">
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
                    $stmt = $mysql->prepare('SELECT title, SUBSTRING(description, 1, 250), score FROM youtube_videos ORDER BY score DESC');
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while ($row = $result->fetch_assoc()):
                ?>

                <div class="youtube_post">
                    <a class="post" href="">
                        <h3> <?php echo $row['title'] ?> </h3>
                        <p class="description"> <?php echo $row['SUBSTRING(description, 1, 250)'] ?> </p>
                    </a>
                </div>
                <?php endwhile; ?>
            </div>
        <?php endif; ?>

    </main>

    <footer class="footer">
        Footer infos <br>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos dolores quam eaque inventore amet? Minima nisi
        sunt id illum provident architecto illo, laboriosam voluptatem incidunt necessitatibus recusandae exercitationem
        minus est.
    </footer>
</body>

</html>