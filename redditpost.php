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
    <link href="styles/post.css" rel="stylesheet">
    <script src="scripts/responsive.js" defer></script>
    <script src="scripts/darktheme.js" defer></script>
    <script src="scripts/keepingdarktheme.js" defer></script>
    <script src="scripts/chartcomm.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"> </script>
    <title>InfoMed | Reddit post</title>
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
            </ul>
        </div>
    </header>
</body>

<?php $idPost = $_GET['id']; ?>

<main class="main">
    <h2 class="platform_name reddit">Reddit post</h2>
    <div class="content">
        <section class="title_and_description reddit">
            <?php
                $stmt = $mysql->prepare('SELECT * FROM reddit_posts ORDER BY score');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
                    if($row['id']!=$idPost):
                        continue;
                    else:
            ?>
            <h3 class="title">
                <?php echo $row['title'] ?>
            </h3>
            <p class="description">
                <?php echo $row['selftext'] ?>
            </p>
        </section>
        <section class="stats_and_review reddit">
            <div class="date">
                <h3 class="stats_title">Date:</h3>
                <p class="description"><?php echo $row['created_utc'] ?></p>
            </div> 
            <div class="feelings">
                <div class="feeling">
                    <h3 class="stats_title">Positive:</h3>
                    <div class="progress-positive">
                        <div class="progress__fill__positive"></div>
                        <span class="progress__text__positive"></span>
                    </div>
                    <script type="text/javascript">
                        positive = '<?php echo $row['positive']; ?>';
                        positive_round = Math.round(positive);
                        document.querySelector(".progress__fill__positive").style.width = `${positive_round}%`;
                        document.querySelector(".progress__text__positive").textContent = `${positive_round}%`;
                    </script>
                </div>
                <div class="feeling">
                    <h3 class="stats_title">Neutral:</h3>
                    <div class="progress-neutral">
                        <div class="progress__fill__neutral"></div>
                        <span class="progress__text__neutral"></span>
                    </div>
                    <script type="text/javascript">
                        neutral = '<?php echo $row['neutral']; ?>';
                        neutral_round = Math.round(neutral);
                        document.querySelector(".progress__fill__neutral").style.width = `${neutral_round}%`;
                        document.querySelector(".progress__text__neutral").textContent = `${neutral_round}%`;
                    </script>
                </div>
                <div class="feeling">
                    <h3 class="stats_negative">Negative:</h3>
                    <div class="progress-negative">
                        <div class="progress__fill__negative"></div>
                        <span class="progress__text__negative"></span>
                    </div>
                    <script type="text/javascript">
                        negative = '<?php echo $row['negative']; ?>';
                        negative_round = Math.round(negative);
                        document.querySelector(".progress__fill__negative").style.width = `${negative_round}%`;
                        document.querySelector(".progress__text__negative").textContent = `${negative_round}%`;
                    </script>
                </div>
            </div>
        </section>
        </div>
        <div class="content_below">
            <section class="comments">
                <canvas id="myChart" style="width:100%;max-width:700px"></canvas>
            </section>
        <?php break; ?>
        <?php endif; ?>
        <?php endwhile; ?>
    </div>
</main>

<footer class="footer">
        <div class="footer_option first_option"><a class="menu_option" href="index.php#Categories">Categories</a></div>
        <div class="footer_option"><a class="menu_option" href="statistics.php">Statistics</a></div>
        <div class="footer_option"><a class="menu_option" href="about.php">About us</a></div>
        <div class="footer_option">© Copyright 2022 InfoMed</div>
    </footer>
</html>