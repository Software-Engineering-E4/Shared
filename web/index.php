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
                    <a class="menu_option" href="#Categories">Categories</a>
                </li>
                <li class="about">
                    <a class="menu_option" href="about.html">About us</a>
                </li>
            </ul>
            <a href="https://www.info.uaic.ro" class="faculty"> <img src="images/logo-fii.png" alt="University logo"
                    class="faculty_logo">
            </a>

            <!-- responsive website -->
            <img src="./btn1.png" alt="" class="menu-btn">

        </nav>
        <!-- <div class="news">
            <p>Check out our latest post here!</p>
        </div>-->
    </header>

    <!-- script for responsive website -->
    <script>
        const menuBtn = document.querySelector('.menu-btn')
        const navlinks = document.querySelector('.container')
        menuBtn.addEventListener('click', () => {
            navlinks.classList.toggle('mobile-menu')
        })
    </script>

    <!-- AFISARE TITLU: echo "title: " . $row["title"] -->
    <!-- AFISARE SELFTEXT: echo "selftext: " . $row["selftext"] -->

    <main>
        <h2 class="titles">Popular works</h2>
        <section class="most_reviewed">
        
        <!-- De aici iau datele din reddit_posts -->
        <?php
            $stmt = $mysql->prepare('SELECT title, selftext FROM `reddit_posts` LIMIT 6');
            $stmt->execute();
            $result = $stmt->get_result();
            while ($row = $result->fetch_assoc()):
        ?>

        <div class="most_reviewed">
            <h3> <?php echo $row['title'] ?> </h3>
            <p class="description"> <?php echo $row['selftext'] ?> </p>
        </div>
        <?php endwhile; ?>

        </section>
        
        <h2 class="titles" id="Categories">Categories</h2>
        <section class="categories">

        <!-- De aici iau datele din twitter_posts -->
        <h2 class="twitter">Twitter</h2>
        <div class="twitter">
            <?php
                $stmt = $mysql->prepare('SELECT * FROM `twitter_posts` LIMIT 6');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>

            <div class="twitter_post">
                <h3>Title</h3>
                <p class="description"> <?php echo $row['text'] ?> </p>
            </div>
            <?php endwhile; ?>
        </div>
        
        <!-- De aici iau datele din reddit_posts -->
        <h2 class="reddit">Reddit</h2>
        <div class="reddit">
            <?php
                $stmt = $mysql->prepare('SELECT title, selftext FROM `reddit_posts` LIMIT 6');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>
        
            <div class="reddit_post">
                <h3> <?php echo $row['title'] ?> </h3>
                <p class="description"> <?php echo $row['selftext'] ?> </p>
            </div>
            <?php endwhile; ?>
        </div>
        
        <!-- De aici iau datele din youtube_videos -->
        <h2 class="youtube">YouTube</h2>
        <div class="youtube">
            <?php
                $stmt = $mysql->prepare('SELECT * FROM `youtube_videos` LIMIT 6');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>

            <div class="youtube_post">
                <h3> <?php echo $row['title'] ?> </h3>
                <p class="description"> <?php echo $row['description'] ?> </p>
            </div>
            <?php endwhile; ?>
        </div>

        </section>
    </main>

    <hr>

    <footer>
        Footer infos <br>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos dolores quam eaque inventore amet? Minima nisi
        sunt id illum provident architecto illo, laboriosam voluptatem incidunt necessitatibus recusandae exercitationem
        minus est.
    </footer>

</body>

</html>