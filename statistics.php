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
    <link href="styles/statistics.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <script src="scripts/keepingdarktheme.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" charset="utf-8"></script>
    <title>InfoMed | Statistics</title>
</head>

<body>
    <header class="site_header">
        <nav class="navig_line">
            <div class="left_container">
                <div class="site_name">
                    <a class="site_name" href="/index.php">InfoMed</a>
                </div>
                <form action="search.php" method="get">
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
  
    <!-- Functie pentru calcularea procentajului -->
    <?php
        function calPercentage($numAmount, $numTotal) {
            $count1 = $numAmount / $numTotal;
            $count2 = $count1 * 100;
            $count = number_format($count2, 0);
            return $count;
        }
    ?>

    <!-- De aici iau sentimentele din twitter_posts -->
    <?php
        $stmt = $mysql->prepare('SELECT sentiment FROM twitter_posts WHERE sentiment IS NOT NULL');
        $stmt->execute();
        $result = $stmt->get_result();
        $counterNeutralTwitter=0;
        $neutralTwitter='neutral';
        $counterPositiveTwitter=0;
        $positiveTwitter='positive';
        $counterNegativeTwitter=0;
        $negativeTwitter='negative';
        $counterAllSentimentsTwitter=0;
        while($row = $result->fetch_assoc()){
            $counterAllSentimentsTwitter++;
            if($row['sentiment']==$neutralTwitter){
                $counterNeutralTwitter++;
            }
            if($row['sentiment']==$positiveTwitter){
                $counterPositiveTwitter++;
            }
            if($row['sentiment']==$negativeTwitter){
                $counterNegativeTwitter++;
            }
        }

        $percentagePositiveTwitter = calPercentage($counterNeutralTwitter, $counterAllSentimentsTwitter);
        $percentageNeutralTwitter = calPercentage($counterPositiveTwitter, $counterAllSentimentsTwitter);
        $percentageNegativeTwitter = calPercentage($counterNegativeTwitter, $counterAllSentimentsTwitter);
    ?>

    <!-- De aici iau sentimentele din reddit_posts -->
    <?php
        $stmt = $mysql->prepare('SELECT sentiment FROM reddit_posts WHERE sentiment IS NOT NULL');
        $stmt->execute();
        $result = $stmt->get_result(); 
        $counterNeutralReddit=0;
        $neutralReddit='neutral';
        $counterPositiveReddit=0;
        $positiveReddit='positive';
        $counterNegativeReddit=0;
        $negativeReddit='negative';
        $counterAllSentimentsReddit=0;
        while($row = $result->fetch_assoc()){
            $counterAllSentimentsReddit++;
            if($row['sentiment']==$neutralReddit){
                $counterNeutralReddit++;
            }
            if($row['sentiment']==$positiveReddit){
                $counterPositiveReddit++;
            }
            if($row['sentiment']==$negativeReddit){
                $counterNegativeReddit++;
            }
        }
        
        $percentagePositiveReddit = calPercentage($counterNeutralReddit, $counterAllSentimentsReddit);
        $percentageNeutralReddit = calPercentage($counterPositiveReddit, $counterAllSentimentsReddit);
        $percentageNegativeReddit = calPercentage($counterNegativeReddit, $counterAllSentimentsReddit);
    ?>

    <!-- De aici iau sentimentele din youtube_videos -->
    <?php
        $stmt = $mysql->prepare('SELECT sentiment FROM youtube_videos WHERE sentiment IS NOT NULL');
        $stmt->execute();
        $result = $stmt->get_result(); 
        $counterNeutralYoutube=0;
        $neutralYoutube='neutral';
        $counterPositiveYoutube=0;
        $positiveYoutube='positive';
        $counterNegativeYoutube=0;
        $negativeYoutube='negative';
        $counterAllSentimentsYoutube=0;
        while($row = $result->fetch_assoc()){
            $counterAllSentimentsYoutube++;
            if($row['sentiment']==$neutralYoutube){
                $counterNeutralYoutube++;
            }
            if($row['sentiment']==$positiveYoutube){
                $counterPositiveYoutube++;
            }
            if($row['sentiment']==$negativeYoutube){
                $counterNegativeYoutube++;
            }
        }

        $percentagePositiveYoutube = calPercentage($counterNeutralYoutube, $counterAllSentimentsYoutube);
        $percentageNeutralYoutube = calPercentage($counterPositiveYoutube, $counterAllSentimentsYoutube);
        $percentageNegativeYoutube = calPercentage($counterNegativeYoutube, $counterAllSentimentsYoutube);
    ?>

    <main class="statistics">

    <h2 class="intro">Common words used</h2>
        <div class="photo">
            <img class="general" src="images/WordCloud.png">
        </div>

        <h2 class="twitter">Twitter</h2>
        <div class="statistics-twitter">
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
                            <div class="bar" data-percentage=<?php echo $percentageNegativeTwitter ?>><span>Negative</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentagePositiveTwitter ?>><span>Positive</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentageNeutralTwitter ?>><span>Neutral</span></div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="place_for_single_image">
            <img src="images/PieChartTwitterPosts.png" class="single_image">
        </div>

        <h2 class="reddit">Reddit</h2>
        <div class="statistics-reddit">

            <div class="reddit">
                <div class="chart" class="reddit">
                    <ul class="values">
                        <!--vertical-->
                        <li><span>100%</span></li>
                        <li><span>50%</span></li>
                        <li><span>0%</span></li>
                    </ul>
                    <ul class="bars">
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentageNegativeReddit ?>><span>Negative</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentagePositiveReddit ?>><span>Positive</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentageNeutralReddit ?>><span>Neutral</span></div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <!--image slider start-->
        <div class="place_for_slider">
            <div class="slider">
                <div class="slides">
                    <input type="radio" name="button" id="radio1Reddit">
                    <input type="radio" name="button" id="radio2Reddit">
                    <input type="radio" name="button" id="radio3Reddit">
                    <!--slide images start-->
                    <div class="slide first">
                        <img src="images/PieChartRedditPosts.png">
                    </div>
                    <div class="slide">
                        <img src="images/BarChartRedditPosts.png">
                    </div>
                    <div class="slide">
                        <img src="images/LineChartRedditPosts.png">
                    </div>
                    <!--slide images end-->
                </div>
                <!--navigation-->
                <div class="navigation">
                    <label for="radio1Reddit" class="button reddit"></label>
                    <label for="radio2Reddit" class="button reddit"></label>
                    <label for="radio3Reddit" class="button reddit"></label>
                </div>
            </div>
            <!--image slider end-->
        </div>


        <h2 class="youtube">Youtube</h2>
        <div class="statistics-youtube">
            <div class="youtube">
                <div class="chart">
                    <ul class="values">
                        <!--vertical-->
                        <li><span>100%</span></li>
                        <li><span>50%</span></li>
                        <li><span>0%</span></li>
                    </ul>
                    <ul class="bars" class="reddit">
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentageNegativeYoutube ?>><span>Negative</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentagePositiveYoutube ?>><span>Positive</span></div>
                        </li>
                        <li>
                            <div class="bar" data-percentage=<?php echo $percentageNeutralYoutube ?>><span>Neutral</span></div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="place_for_slider">
            <div class="slider">
                <div class="slides">
                    <input type="radio" name="button" id="radio1Youtube">
                    <input type="radio" name="button" id="radio2Youtube">
                    <input type="radio" name="button" id="radio3Youtube">
                    <div class="slide first">
                        <img src="images/PieChartYoutubeVideos.png">
                    </div>
                    <div class="slide">
                        <img src="images/BarChartYoutubeVideos.png">
                    </div>
                    <div class="slide">
                        <img src="images/LineChartYoutube.png">
                    </div>
                </div>
                <div class="navigation">
                    <label for="radio1Youtube" class="button youtube"></label>
                    <label for="radio2Youtube" class="button youtube"></label>
                    <label for="radio3Youtube" class="button youtube"></label>
                </div>
            </div>
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
    <footer class="footer">
        <div class="footer_option first_option"><a class="menu_option" href="index.php#Categories">Categories</a></div>
        <div class="footer_option"><a class="menu_option" href="statistics.php">Statistics</a></div>
        <div class="footer_option"><a class="menu_option" href="about.php">About us</a></div>
        <div class="footer_option">© Copyright 2022 InfoMed</div>
    </footer>
 </body>
  </html>