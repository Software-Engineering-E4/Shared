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
    <link href="styles/post.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <title>Twitter post</title>
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
                    <a class="menu_option" href="/index.php#Categories">Categories</a>
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
</body>

<main>
    <h2 class="platform_title">Twitter post</h2>
    <div class="content">
        <section class="title_and_description">
            <h3 class="title">
                Title of post
            </h3>
            <p class="description">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio similique explicabo doloremque iure
                eveniet
                incidunt adipisci, doloribus sit vel eligendi at architecto quod necessitatibus voluptatem magni sint
                non
                aut voluptate.
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid tempore assumenda praesentium. Officiis
                nemo ut possimus debitis numquam corporis delectus dolores quam illum, necessitatibus repellendus,
                fugiat, ipsum eum ad error?
            </p>
        </section>
        <section class="stats_and_review">
            <div class="date">
                <h3 class="stats_title">Date:</h3>
                <p class="description">posted date</p>
            </div>
            <div class="feelings">
                <h3 class="stats_title">Overall feeling:</h3>
                <p class="description">Lorem ipsum dolor sit amet</p>
            </div>
            <div class=" review">
                <h3 class="stats_title">Leave a review here:</h3>
                <p class="description">To be done...</p>
            </div>
        </section>
    </div>
</main>

</html>