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
    <link href="styles/statistics.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" charset="utf-8"></script>
    <title>Site name</title>
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
        <div class="statistics">
            <h2 class="twitter">Twitter</h2>
            <div class="twitter">
                <div class="chart">
                    <ul class="values">
                        <!--vertical-->
                        <li><span>100%</span></li>
                        <li><span>50%</span></li>
                        <li><span>0%</span></li>
                    </ul>
                    <ul class="bars">
                        <li>
                            <div class="bar" data-percentage="70"><span>Negative</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage="20"><span>Positive</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage="30"><span>Neutral</span></div>
                        </li>
                    </ul>
                </div>
            </div>

            <h2 class="reddit">Reddit</h2>
            <div class="reddit">

            </div>
            <h2 class="youtube">Youtube</h2>
            <div class="youtube">

            </div>
            <!--script desenare bare-->
            <script type="text/javascript">
                $(function () {
                    $('.bars li .bar').each(function (key, bar) {
                        var percentage = $(this).data('percentage');
                        $(this).animate({
                            'height': percentage + '%'
                        }, 1000);
                    });
                });
            </script>
        </div>
    </main>
    </html>