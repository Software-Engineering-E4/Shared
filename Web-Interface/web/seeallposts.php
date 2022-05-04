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
    <title>All posts</title>
</head>

<body>
    <header class="site_header">
        <nav class="navig_line">
            <div class="left_container">
                <div class="site_name">
                    <a class="site_name" href="/homepage.html">Site name</a>
                </div>
                <form action="/homepage.html" method="get">
                    <div class="search_bar">
                        <input type="search" id="search" name="search" placeholder=" Search...">
                    </div>
                </form>
            </div>
            <ul class="right_container">
                <li class="latest">
                    <a class="menu_option" href="homepage.html"> Latest </a>
                </li>
                <li class="categories">
                    <a class="menu_option" href="homepage.html#Categories">Categories</a>
                </li>
                <li class="statistics">
                    <a class="menu_option" href="statistics.html">Statistics</a>
                </li>
                <li class="about">
                    <a class="menu_option" href="about.html">About us</a>
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

        <?php if ("platform_name" == 'Reddit'): ?>
            <div class="reddit">
                <?php
                    $stmt = $mysql->prepare('SELECT title, selftext FROM `reddit_posts`');
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while ($row = $result->fetch_assoc()):
                ?>

                <div class="reddit_post">
                    <a class="post" href="post.php">
                        <h3> <?php echo $row['title'] ?> </h3>
                        <p class="description"> <?php echo $row['selftext'] ?> </p>
                    </a>
                </div>
                <?php endwhile; ?>     
            </div>
        <?php endif; ?>
        
        <?php if ("platform_name" == 'Youtube'): ?>
            <div class="youtube">
                <?php
                    $stmt = $mysql->prepare('SELECT title, description FROM `youtube_videos`');
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while ($row = $result->fetch_assoc()):
                ?>

                <div class="youtube_post">
                    <a class="post" href="post.php">
                        <h3> <?php echo $row['title'] ?> </h3>
                        <p class="description"> <?php echo $row['description'] ?> </p>
                    </a>
                </div>
                <?php endwhile; ?>   
            </div>
        <?php endif; ?>
        
        <?php if ("platform_name" == 'Twitter'): ?>
        <div class="twitter">
            <?php
                $stmt = $mysql->prepare('SELECT text FROM `twitter_posts`');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>

            <div class="twitter_post">
                <a class="post" href="post.php">
                    <p class="description"> <?php echo $row['text'] ?> </p>
                </a>
            </div>
            <?php endwhile; ?>   
        </div>
        <?php endif; ?>

    </main>
</body>

</html>