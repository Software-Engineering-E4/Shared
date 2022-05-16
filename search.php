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
        <!-- Aici este functia pentru search (trebuie vazut de ce nu functioneaza) -->
        
        <?php echo $keyword=$_POST['keyword']; ?>

        <h2 class="titles" id="titles">Search responses</h2>
        <section class="Categories">
        
        <div class="twitter">
            <!-- De aici iau datele din twitter_posts pentru search-->
            <?php
                $sql = $mysql->query("SELECT * FROM twitter_posts where text LIKE '%$keyword%'");
                $stmt = $mysql->prepare($sql);
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()): 
            ?>

            <div class="twitter_post">
                <a class="post" id="<?php $row['id'] ?>" href="twitterpost.php?id=<?php echo $row['id'] ?>">
                    <p class="description"> <?php echo $row['text'] ?> </p>
                </a>
            </div>
            <?php endwhile; ?>
        </div>

        <div class="reddit">
            <!-- De aici iau datele din reddit_posts pentru search-->
            <?php
                $sql = $mysql->query("SELECT * FROM reddit_posts WHERE title LIKE '%$keyword%' OR seltext LIKE '%$keyword%'");
                $stmt = $mysql->prepare($sql);
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = mysqli_fetch_array($result)): 
            ?>

            <div class="reddit_post">
                <a class="post" id="<?php $row['id'] ?>" href="redditpost.php?id=<?php echo $row['id'] ?>">
                    <h3> <?php echo $row['title'] ?> </h3>
                    <p class="description"> <?php echo $row['selftext'] ?> </p>
                </a>
            </div>
            <?php endwhile; ?>
        </div>

        <div class="youtube">
            <!-- De aici iau datele din youtube_videos pentru search-->
            <?php
                $sql = $mysql->query("SELECT * FROM youtube_videos WHERE title LIKE '%$keyword%' OR description LIKE '%$keyword%'");
                $stmt = $mysql->prepare($sql);
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()): 
            ?>

            <div class="youtube_post">
                <a class="post" href="">
                    <h3> <?php echo $row['title'] ?> </h3>
                    <p class="description"> <?php echo $row['description'] ?> </p>
                </a>
            </div>
            <?php endwhile; ?>
        </div>
        </section>
    </main>

    <hr>

    <footer class="footer">
        Footer infos <br>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos dolores quam eaque inventore amet? Minima nisi
        sunt id illum provident architecto illo, laboriosam voluptatem incidunt necessitatibus recusandae exercitationem
        minus est.
    </footer>

</body>

</html>