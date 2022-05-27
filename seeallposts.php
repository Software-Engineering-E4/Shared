<?php
    require "dbconnection.php";
    $queries = array();
    parse_str($_SERVER['QUERY_STRING'], $queries);
    $platformName =  $queries['platformName'];
    $content_selector_platform = "#content_see_all";
?>
<!DOCTYPE html>
<html lang="en">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="images/favicon.ico" />
    <link href="styles/general.css" rel="stylesheet">
    <link href="styles/seeallposts.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <script src="scripts/keepingdarktheme.js" defer></script>
    <script src="scripts/seeallposts.js" defer></script>
    <script src="scripts/homepage.js" defer></script>
    <title>InfoMed | All posts</title>

    <script type="text/javascript">
        $(document).ready(function() {
            currentLimit = 12;
            $("#bseemoreitems").click(function() {                
                $.ajax({    
                    type: "GET",
                    url: "dbfetch.php",
                    <?php
                        if ($platformName == 'Twitter') {
                            global $content_selector_platform;
                            $content_selector_platform = "#twitter_see_all";
                            echo 'data: {seemoretwitter: currentLimit},';
                        } else if ($platformName == 'Reddit') {
                            global $content_selector_platform;
                            $content_selector_platform = "#reddit_see_all";
                            echo 'data: {seemorereddit: currentLimit},';
                        } else if ($platformName == 'Youtube') {
                            global $content_selector_platform;
                            $content_selector_platform = "#youtube_see_all";
                            echo 'data: {seemoreyoutube: currentLimit},';
                        }
                    ?>
                    dataType: "html",                   
                    success: function(response){
                        <?php
                            echo '$("'.$content_selector_platform.'").append(response);'
                        ?>          
                        currentLimit = currentLimit + 12;
                        
                    }
                });
            });
        });
    </script>
</head>

<body>
    <header class="site_header">
        <nav class="navig_line">
            <div class="left_container">
                <div class="site_name">
                    <a class="site_name" href="/index.php">InfoMed</a>
                </div>
                <form action="/search.php" method="post">
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
                <li class="phone_list_element change_theme">
                    <div class="phone change_theme" id="phone_change_theme">
                        <img src="images/sun.svg" class="phone_sun">
                        <img src="images/moon.svg" class="phone_moon">
                    </div>
                </li>
            </ul>
        </div>
    </header>

    <main>
        <h2 class="platform_name" id="platform_name"></h2>
        
        <?php
            require "dbfetch.php";
            if ($platformName == 'Twitter') {
                echo '<div class="twitter" id="twitter_see_all">';
                display_twitter_items(0);
                echo '</div>';
            } else if ($platformName == 'Reddit') {
                echo '<div class="reddit" id="reddit_see_all">';
                display_reddit_items(0);
                echo '</div>';
            } else if ($platformName == 'Youtube') {
                echo '<div class="youtube" id="youtube_see_all">';
                display_youtube_items(0);
                echo '</div>';
            }
        ?>

        </br>
        <!-- See more button -->
        <div class="see_all">
            <p class="bseemoreitems" id="bseemoreitems"> See more </p>
        </div>

    </main>
    <footer class="footer">
        <div class="footer_option first_option"><a class="menu_option" href="index.php#Categories">Categories</a></div>
        <div class="footer_option"><a class="menu_option" href="statistics.php">Statistics</a></div>
        <div class="footer_option"><a class="menu_option" href="about.php">About us</a></div>
        <div class="footer_option">© Copyright 2022 InfoMed</div>
    </footer>
</body>

</html>