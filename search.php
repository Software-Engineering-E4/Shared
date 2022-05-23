<?php
    require "dbconnection.php";
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="images/favicon.ico" />
    <link href="styles/general.css" rel="stylesheet">
    <link href="styles/homepage.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <script src="scripts/keepingdarktheme.js" defer></script>
    <script src="scripts/homepage.js" defer></script>
    <title>InfoMed</title>
</head>

<body>
    <header class="site_header">
        <nav class="navig_line">
            <div class="left_container">
                <div class="site_name">
                    <a class="site_name" href="/index.php">InfoMed</a>
                </div>
                <form action="/search.php" method="POST">
                    <div class="search_bar">
                        <input type="search" id="search" name="keyword" placeholder=" Search...">
                    </div>
                </form>
            </div>

            <ul class="right_container">
                <li class="home">
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

            <a href="https://www.info.uaic.ro" class="faculty"> <img src="images/logo-fii.png" alt="University logo"
                    class="faculty_logo">
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
        
        <?php $keyword = mysqli_real_escape_string($mysql, $_POST['keyword']); ?>

        <h2 class="titles" id="titles">Search responses</h2>
        <section class="Categories">
        
        <h2 class="twitter">Twitter</h2>
        <div class="twitter">
            <!-- De aici iau datele din twitter_posts pentru search-->
            <?php
              $q = "SELECT id,SUBSTRING(text, 1, 250) FROM twitter_posts where text LIKE '%$keyword%' GROUP BY text ORDER BY retweets DESC";
              $result = mysqli_query($mysql, $q);
              $rows = mysqli_num_rows($result);
              if($rows > 0) :
               while ($row = mysqli_fetch_assoc($result)): 
            ?>
            <div class="twitter_post">
                <a class="post" id="<?php $row['id'] ?>" href="twitterpost.php?id=<?php echo $row['id'] ?>">
                    <p class="description"> <?php echo $row['SUBSTRING(text, 1, 250)'] ?> </p>
                </a>
            </div>
            <?php
         endwhile;
        endif;
          ?>
        </div>

        <h2 class="reddit">Reddit</h2>
        <div class="reddit">
            <!-- De aici iau datele din reddit_posts pentru search-->
            <?php
                $q = "SELECT id,title,SUBSTRING(selftext, 1, 250) FROM reddit_posts where selftext LIKE '%$keyword%' OR title  LIKE '%$keyword%' and selftext IS NOT NULL ORDER BY score DESC";
                $result = mysqli_query($mysql, $q);
                $rows = mysqli_num_rows($result);
                if($rows > 0) :
                 while ($row = mysqli_fetch_assoc($result)): 
            ?>

            <div class="reddit_post">
                <a class="post" id="<?php $row['id'] ?>" href="redditpost.php?id=<?php echo $row['id'] ?>">
                    <h3 class="title"> <?php echo $row['title'] ?> </h3>
                    <p class="description"> <?php echo $row['SUBSTRING(selftext, 1, 250)'] ?> </p>
                </a>
            </div>
            <?php endwhile;
            endif; ?>
        </div>

        <h2 class="youtube">YouTube</h2>
        <div class="youtube">
            <!-- De aici iau datele din youtube_videos pentru search-->
            <?php
                $q = "SELECT title,link,thumbnail FROM youtube_videos where description LIKE '%$keyword%' OR title  LIKE '%$keyword%' ORDER BY score DESC";
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
            <?php endwhile; 
            endif;?>
        </div>
        </section>
    </main>
    <footer class="footer">
        <div class="footer_option first_option"><a class="menu_option" href="index.php#Categories">Categories</a></div>
        <div class="footer_option"><a class="menu_option" href="statistics.php">Statistics</a></div>
        <div class="footer_option"><a class="menu_option" href="about.php">About us</a></div>
        <div class="footer_option">© Copyright 2022 InfoMed</div>
    </footer>

</body>

</html>