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
    <link href="styles/homepage.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <script src="scripts/keepingdarktheme.js" defer></script>
    <script src="scripts/homepage.js" defer></script>
    <title>Site name</title>
</head>

<body>
    <header class="site_header">
        <nav class="navig_line">
            <div class="left_container">
                <div class="site_name">
                    <a class="site_name" href="/index.php">Site name</a>
                </div>
                <form action="/search.php" method="POST">
                    <div class="search_bar">
                        <input type="search" id="search" name="search" placeholder=" Search...">
                    </div>
                </form>
            </div>

            <ul class="right_container">
                <li class="latest">
                    <a class="menu_option" href="index.php"> Latest </a>
                </li>
                <li class="categories">
                    <a class="menu_option" href="#Categories">Categories</a>
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
            <img src="images/btn1.png" alt="" class="menu-btn">
            <img src="images/search.png" alt="" class="search-btn">

        </nav>
    </header>
    
    <main>
        <h2 class="titles" id="titles">Popular works</h2>
        <section class="most_reviewed">
        
        <!-- De aici iau datele din reddit_posts -->
        <?php
            $stmt = $mysql->prepare('SELECT title, SUBSTRING(selftext, 1, 250), score, id FROM reddit_posts WHERE selftext IS NOT NULL ORDER BY score DESC LIMIT 2');
            $stmt->execute();
            $result = $stmt->get_result();
            while ($row = $result->fetch_assoc()):
        ?>

        <div class="most_reviewed_post">
            <a class="post" id="<?php $row['id'] ?>" href="redditpost.php?id=<?php echo $row['id'] ?>">
                <h3> <?php echo $row['title'] ?> </h3>
                <p class="description"> <?php echo $row['SUBSTRING(selftext, 1, 250)'] ?> </p>
            </a>
        </div>
        <?php endwhile; ?>
        
        <!-- De aici iau datele din twitter_posts -->
        <?php
            $stmt = $mysql->prepare('SELECT SUBSTRING(text, 1, 250), retweets, id FROM twitter_posts GROUP BY text ORDER BY retweets DESC LIMIT 2');
            $stmt->execute();
            $result = $stmt->get_result();
            while ($row = $result->fetch_assoc()):
        ?>

        <div class="most_reviewed_post">
            <a class="post" id="<?php $row['id'] ?>" href="twitterpost.php?id=<?php echo $row['id'] ?>">
                <p class="description"> <?php echo $row['SUBSTRING(text, 1, 250)'] ?> </p>
            </a>
        </div>
        <?php endwhile; ?>
        
        <!-- De aici iau datele din youtube_videos -->
        <?php
            $stmt = $mysql->prepare('SELECT title, SUBSTRING(description, 1, 250), score FROM youtube_videos ORDER BY score LIMIT 2');
            $stmt->execute();
            $result = $stmt->get_result();
            while ($row = $result->fetch_assoc()):
        ?>

        <div class="most_reviewed_post">
            <a class="post" href="post.php">
                <h3> <?php echo $row['title'] ?> </h3>
                <p class="description"> <?php echo $row['SUBSTRING(description, 1, 250)'] ?> </p>
            </a>
        </div>
        <?php endwhile; ?>

        </section>
        
        <h2 class="titles" id="Categories">Categories</h2>
        <section class="Categories">

        <!-- De aici iau datele din twitter_posts -->
        <h2 class="twitter">Twitter</h2>
        <div class="twitter">
            <?php
                $stmt = $mysql->prepare('SELECT SUBSTRING(text, 1, 250), retweets, id FROM twitter_posts GROUP BY text ORDER BY retweets DESC LIMIT 6');
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

            <div class="see_all">
                <a class="twitter_see_all" href="/seeallposts.php?platformName=Twitter" id="twitter_see_all">See all</a>
            </div>
        </div>
        
        <!-- De aici iau datele din reddit_posts -->
        <h2 class="reddit">Reddit</h2>
        <div class="reddit">
            <?php
                $stmt = $mysql->prepare('SELECT title, SUBSTRING(selftext, 1, 250), score, id FROM reddit_posts WHERE selftext IS NOT NULL ORDER BY score DESC LIMIT 6');
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

            <div class="see_all">
                <a class="reddit_see_all" href="/seeallposts.php?platformName=Reddit" id="reddit_see_all">See all</a>
            </div>
        </div>
        
        <!-- De aici iau datele din youtube_videos -->
        <h2 class="youtube">YouTube</h2>
        <div class="youtube">
            <?php
                $stmt = $mysql->prepare('SELECT title, SUBSTRING(description, 1, 250), score FROM youtube_videos ORDER BY score LIMIT 6');
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

           

            <div class="see_all">
                <a class="youtube_see_all" href="/seeallposts.php?platformName=Youtube" id="youtube_see_all">See all</a>
            </div>
        </div>

        </section>
    </main>

    <footer class="footer">
        Footer infos <br>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos dolores quam eaque inventore amet? Minima nisi
        sunt id illum provident architecto illo, laboriosam voluptatem incidunt necessitatibus recusandae exercitationem
        minus est.
    </footer>

</body>

</html>